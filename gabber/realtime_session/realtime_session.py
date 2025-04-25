import asyncio
from typing import cast
import logging
from gabber.api import create_api, api_types
from livekit import rtc
from abc import ABC, abstractmethod
import json


class RealtimeSessionHandler(ABC):
    @abstractmethod
    def connection_state_changed(self, state: api_types.SDKConnectionState):
        pass

    @abstractmethod
    def agent_state_changed(self, state: api_types.SDKAgentState):
        pass

    @abstractmethod
    def remaining_seconds_changed(self, seconds: int):
        pass

    @abstractmethod
    def agent_error(self, msg: str):
        pass

    @abstractmethod
    def messages_changed(self, messages: list[api_types.SDKSessionTranscription]):
        pass


class RealtimeSession:
    def __init__(self, *, handler: RealtimeSessionHandler):
        self._microphone = VirtualMicrophone(channels=1, sample_rate=48000)
        self._audio_stream = AudioFrameStream(channels=1, sample_rate=24000)
        self._room = rtc.Room()
        self._room.on("data_received", self._on_data_received)
        self._room.on(
            "participant_metadata_changed", self._on_participant_metadata_changed
        )
        self._room.on("track_subscribed", self._on_track_subscribed)
        self._audio_source = rtc.AudioSource(sample_rate=48000, num_channels=1)
        self._handler = handler
        self._messages: list[api_types.SDKSessionTranscription] = []
        self._agent_participant: rtc.RemoteParticipant | None = None
        self._agent_audio_track: rtc.RemoteAudioTrack | None = None
        self._agent_audio_task: asyncio.Task | None = None

    async def connect(self, *, opts: api_types.SDKConnectOptions):
        self._handler.connection_state_changed(api_types.SDKConnectionState.CONNECTED)
        connection_details: api_types.RealtimeSessionConnectionDetails
        if isinstance(opts.actual_instance, api_types.SDKConnectOptionsOneOf):
            connection_details = opts.actual_instance.connection_details
        elif isinstance(opts.actual_instance, api_types.SDKConnectOptionsOneOf1):
            connection_details = await self._connection_details_from_usage_token(
                usage_token=opts.actual_instance.token,
                config=opts.actual_instance.config,
            )
        else:
            raise ValueError("Invalid SDKConnectOptions type")

        try:
            await self._room.connect(
                url=connection_details.url,
                token=connection_details.token,
                options=rtc.RoomOptions(auto_subscribe=True),
            )
        except Exception as e:
            self._handler.connection_state_changed(
                api_types.SDKConnectionState.NOT_CONNECTED
            )
            logging.error(f"Failed to connect to room: {e}")
            self._handler.agent_error(str(e))

    async def disconnect(self):
        await self._room.disconnect()
        self._microphone._close()
        self._audio_stream._close()

    async def _connection_details_from_usage_token(
        self,
        *,
        usage_token: str,
        config: api_types.RealtimeSessionConfigCreate,
    ):
        api = create_api(usage_token=usage_token)
        request = api_types.StartRealtimeSessionRequest(
            config=config,
        )
        rts = await api.realtime.start_realtime_session(request)
        return rts.connection_details

    @property
    def microphone(self):
        return self._microphone

    @property
    def audio_stream(self):
        return self._audio_stream

    def _on_data_received(self, data: rtc.DataPacket):
        str_data = data.data.decode("utf-8")
        if data.topic == "message":
            t = api_types.SDKSessionTranscription.from_json(str_data)
            self._messages.append(t)
            self._handler.messages_changed(self._messages)
        elif data.topic == "error":
            err_dict = json.loads(str_data)
            self._handler.agent_error(err_dict["message"])

    def _on_participant_metadata_changed(
        self, participant: rtc.Participant, old_metadata: str, metadata: str
    ):
        print("NEIL got md", participant, metadata)
        if metadata == "":
            return
        json_md = json.loads(metadata)
        if "remaining_seconds" in json_md:
            self._handler.remaining_seconds_changed(json_md["remaining_seconds"])
        if "agent_state" in json_md:
            agent_state = json_md["agent_state"]
            self._handler.agent_state_changed(api_types.SDKAgentState(agent_state))

    def _on_track_subscribed(
        self,
        room: rtc.Room,
        participant: rtc.RemoteParticipant,
        publication: rtc.TrackPublication,
    ):
        if publication.kind != "audio":
            return

        if self._agent_participant is None:
            self._agent_participant = participant

        if not publication.track:
            logging.error(
                f"No track to subscribe to for participant {participant.identity}"
            )
            return

        self._agent_audio_track = cast(rtc.RemoteAudioTrack, publication.track)
        if self._agent_audio_task is not None:
            self._agent_audio_task.cancel()

        self._agent_audio_task = asyncio.create_task(self._process_audio())
        self._handler.connection_state_changed(api_types.SDKConnectionState.CONNECTED)

    async def send_chat(self, *, text: str):
        msg_data = {"text": text}
        await self._room.local_participant.publish_data(
            payload=json.dumps(msg_data).encode("utf-8")
        )

    async def _process_audio(self):
        if self._agent_audio_track is None:
            return

        stream = rtc.AudioStream(self._agent_audio_track)
        async for frame in stream:
            self._audio_stream._push_audio(frame=bytes(frame.frame.data))


class AudioFrameStream:
    def __init__(self, *, channels: int, sample_rate: int):
        self._channels = channels
        self._sample_rate = sample_rate
        self._output_queue = asyncio.Queue[bytes | None]()

    def _close(self):
        self._output_queue.put_nowait(None)

    def _push_audio(self, *, frame: bytes):
        self._output_queue.put_nowait(frame)

    def __aiter__(self):
        return self

    async def __anext__(self):
        frame = await self._output_queue.get()
        if frame is None:
            raise StopAsyncIteration
        return frame


class VirtualMicrophone:
    def __init__(self, *, channels: int, sample_rate: int):
        self._channels = channels
        self._sample_rate = sample_rate
        self._output_queue = asyncio.Queue[bytes | None]()

    def push_audio(self, audio: bytes):
        self._output_queue.put_nowait(audio)

    def _close(self):
        self._output_queue.put_nowait(None)

    def __aiter__(self):
        return self

    async def __anext__(self):
        frame = await self._output_queue.get()
        if frame is None:
            raise StopAsyncIteration
        return frame
