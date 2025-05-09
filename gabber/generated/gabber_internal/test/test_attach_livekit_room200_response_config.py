# coding: utf-8

"""
    Session API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber_internal.models.attach_livekit_room200_response_config import AttachLivekitRoom200ResponseConfig

class TestAttachLivekitRoom200ResponseConfig(unittest.TestCase):
    """AttachLivekitRoom200ResponseConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachLivekitRoom200ResponseConfig:
        """Test AttachLivekitRoom200ResponseConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachLivekitRoom200ResponseConfig`
        """
        model = AttachLivekitRoom200ResponseConfig()
        if include_optional:
            return AttachLivekitRoom200ResponseConfig(
                general = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_general.attachLivekitRoom_200_response_config_general(
                    time_limit_s = 56, 
                    save_messages = True, ),
                input = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_input.attachLivekitRoom_200_response_config_input(
                    interruptable = True, 
                    parallel_listening = True, ),
                generative = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative.attachLivekitRoom_200_response_config_generative(
                    llm = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_llm.attachLivekitRoom_200_response_config_generative_llm(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        name = '', 
                        project = '', 
                        type = '', 
                        compliance = True, 
                        description = '', ), 
                    voice_override = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override.attachLivekitRoom_200_response_config_generative_voice_override(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        name = '', 
                        language = '', 
                        service = '', 
                        model = '', 
                        voice = '', 
                        embeddings = [
                            1.337
                            ], 
                        cartesia_voice_id = '', 
                        elevenlabs_voice_id = '', 
                        project = '', 
                        human = '', 
                        preview_url = '', 
                        pricing = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override_pricing.attachLivekitRoom_200_response_config_generative_voice_override_pricing(
                            price_per_second = '', 
                            currency = '', 
                            product_name = '', ), 
                        tags = [
                            gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override_tags_inner.attachLivekitRoom_200_response_config_generative_voice_override_tags_inner(
                                name = '', 
                                human_name = '', )
                            ], 
                        _extra = { }, ), 
                    persona = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_persona.attachLivekitRoom_200_response_config_generative_persona(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        id = '', 
                        image_url = '', 
                        name = '', 
                        project = '', 
                        human = '', 
                        gender = 'male', 
                        voice = '', ), 
                    scenario = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_scenario.attachLivekitRoom_200_response_config_generative_scenario(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        name = '', 
                        project = '', 
                        prompt = '', 
                        human = '', ), 
                    context = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_context.attachLivekitRoom_200_response_config_generative_context(
                        id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        project = '', 
                        human = '', 
                        latest_messages = [
                            gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_context_latest_messages_inner.attachLivekitRoom_200_response_config_generative_context_latest_messages_inner(
                                id = '', 
                                speaking_ended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                speaking_started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                role = 'assistant', 
                                realtime_session = '', 
                                content = [
                                    null
                                    ], 
                                tool_calls = [
                                    gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_context_latest_messages_inner_tool_calls_inner.attachLivekitRoom_200_response_config_generative_context_latest_messages_inner_tool_calls_inner(
                                        id = '', 
                                        type = 'function', 
                                        function = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_context_latest_messages_inner_tool_calls_inner_function.attachLivekitRoom_200_response_config_generative_context_latest_messages_inner_tool_calls_inner_function(
                                            name = '', 
                                            arguments = { }, ), )
                                    ], )
                            ], ), 
                    tool_definitions = [
                        gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_tool_definitions_inner.attachLivekitRoom_200_response_config_generative_tool_definitions_inner(
                            id = '', 
                            name = '', 
                            description = '', 
                            parameters = [
                                gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_tool_definitions_inner_parameters_inner.attachLivekitRoom_200_response_config_generative_tool_definitions_inner_parameters_inner(
                                    name = '', 
                                    description = '', 
                                    type = 'string', 
                                    required = True, 
                                    default = '', )
                                ], 
                            call_settings = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_tool_definitions_inner_call_settings.attachLivekitRoom_200_response_config_generative_tool_definitions_inner_call_settings(
                                id = '', 
                                destination = null, ), )
                        ], 
                    _extra = { }, ),
                output = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_output.attachLivekitRoom_200_response_config_output(
                    stream_transcript = True, 
                    speech_synthesis_enabled = True, 
                    answer_message = '', )
            )
        else:
            return AttachLivekitRoom200ResponseConfig(
                general = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_general.attachLivekitRoom_200_response_config_general(
                    time_limit_s = 56, 
                    save_messages = True, ),
                input = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_input.attachLivekitRoom_200_response_config_input(
                    interruptable = True, 
                    parallel_listening = True, ),
                generative = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative.attachLivekitRoom_200_response_config_generative(
                    llm = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_llm.attachLivekitRoom_200_response_config_generative_llm(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        name = '', 
                        project = '', 
                        type = '', 
                        compliance = True, 
                        description = '', ), 
                    voice_override = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override.attachLivekitRoom_200_response_config_generative_voice_override(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        name = '', 
                        language = '', 
                        service = '', 
                        model = '', 
                        voice = '', 
                        embeddings = [
                            1.337
                            ], 
                        cartesia_voice_id = '', 
                        elevenlabs_voice_id = '', 
                        project = '', 
                        human = '', 
                        preview_url = '', 
                        pricing = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override_pricing.attachLivekitRoom_200_response_config_generative_voice_override_pricing(
                            price_per_second = '', 
                            currency = '', 
                            product_name = '', ), 
                        tags = [
                            gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override_tags_inner.attachLivekitRoom_200_response_config_generative_voice_override_tags_inner(
                                name = '', 
                                human_name = '', )
                            ], 
                        _extra = { }, ), 
                    persona = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_persona.attachLivekitRoom_200_response_config_generative_persona(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        id = '', 
                        image_url = '', 
                        name = '', 
                        project = '', 
                        human = '', 
                        gender = 'male', 
                        voice = '', ), 
                    scenario = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_scenario.attachLivekitRoom_200_response_config_generative_scenario(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        name = '', 
                        project = '', 
                        prompt = '', 
                        human = '', ), 
                    context = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_context.attachLivekitRoom_200_response_config_generative_context(
                        id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        project = '', 
                        human = '', 
                        latest_messages = [
                            gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_context_latest_messages_inner.attachLivekitRoom_200_response_config_generative_context_latest_messages_inner(
                                id = '', 
                                speaking_ended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                speaking_started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                role = 'assistant', 
                                realtime_session = '', 
                                content = [
                                    null
                                    ], 
                                tool_calls = [
                                    gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_context_latest_messages_inner_tool_calls_inner.attachLivekitRoom_200_response_config_generative_context_latest_messages_inner_tool_calls_inner(
                                        id = '', 
                                        type = 'function', 
                                        function = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_context_latest_messages_inner_tool_calls_inner_function.attachLivekitRoom_200_response_config_generative_context_latest_messages_inner_tool_calls_inner_function(
                                            name = '', 
                                            arguments = { }, ), )
                                    ], )
                            ], ), 
                    tool_definitions = [
                        gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_tool_definitions_inner.attachLivekitRoom_200_response_config_generative_tool_definitions_inner(
                            id = '', 
                            name = '', 
                            description = '', 
                            parameters = [
                                gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_tool_definitions_inner_parameters_inner.attachLivekitRoom_200_response_config_generative_tool_definitions_inner_parameters_inner(
                                    name = '', 
                                    description = '', 
                                    type = 'string', 
                                    required = True, 
                                    default = '', )
                                ], 
                            call_settings = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_tool_definitions_inner_call_settings.attachLivekitRoom_200_response_config_generative_tool_definitions_inner_call_settings(
                                id = '', 
                                destination = null, ), )
                        ], 
                    _extra = { }, ),
                output = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_output.attachLivekitRoom_200_response_config_output(
                    stream_transcript = True, 
                    speech_synthesis_enabled = True, 
                    answer_message = '', ),
        )
        """

    def testAttachLivekitRoom200ResponseConfig(self):
        """Test AttachLivekitRoom200ResponseConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
