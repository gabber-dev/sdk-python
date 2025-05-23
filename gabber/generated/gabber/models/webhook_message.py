# coding: utf-8

"""
    Gabber API Reference

    The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from gabber.generated.gabber.models.webhook_message_realtime_session_message_committed import WebhookMessageRealtimeSessionMessageCommitted
from gabber.generated.gabber.models.webhook_message_realtime_session_state_changed import WebhookMessageRealtimeSessionStateChanged
from gabber.generated.gabber.models.webhook_message_realtime_session_time_limit_exceeded import WebhookMessageRealtimeSessionTimeLimitExceeded
from gabber.generated.gabber.models.webhook_message_tool_calls_finished import WebhookMessageToolCallsFinished
from gabber.generated.gabber.models.webhook_message_tool_calls_started import WebhookMessageToolCallsStarted
from gabber.generated.gabber.models.webhook_message_usage_tracked import WebhookMessageUsageTracked
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

WEBHOOKMESSAGE_ONE_OF_SCHEMAS = ["WebhookMessageRealtimeSessionMessageCommitted", "WebhookMessageRealtimeSessionStateChanged", "WebhookMessageRealtimeSessionTimeLimitExceeded", "WebhookMessageToolCallsFinished", "WebhookMessageToolCallsStarted", "WebhookMessageUsageTracked"]

class WebhookMessage(BaseModel):
    """
    WebhookMessage
    """
    # data type: WebhookMessageUsageTracked
    oneof_schema_1_validator: Optional[WebhookMessageUsageTracked] = None
    # data type: WebhookMessageRealtimeSessionStateChanged
    oneof_schema_2_validator: Optional[WebhookMessageRealtimeSessionStateChanged] = None
    # data type: WebhookMessageRealtimeSessionMessageCommitted
    oneof_schema_3_validator: Optional[WebhookMessageRealtimeSessionMessageCommitted] = None
    # data type: WebhookMessageToolCallsStarted
    oneof_schema_4_validator: Optional[WebhookMessageToolCallsStarted] = None
    # data type: WebhookMessageToolCallsFinished
    oneof_schema_5_validator: Optional[WebhookMessageToolCallsFinished] = None
    # data type: WebhookMessageRealtimeSessionTimeLimitExceeded
    oneof_schema_6_validator: Optional[WebhookMessageRealtimeSessionTimeLimitExceeded] = None
    actual_instance: Optional[Union[WebhookMessageRealtimeSessionMessageCommitted, WebhookMessageRealtimeSessionStateChanged, WebhookMessageRealtimeSessionTimeLimitExceeded, WebhookMessageToolCallsFinished, WebhookMessageToolCallsStarted, WebhookMessageUsageTracked]] = None
    one_of_schemas: Set[str] = { "WebhookMessageRealtimeSessionMessageCommitted", "WebhookMessageRealtimeSessionStateChanged", "WebhookMessageRealtimeSessionTimeLimitExceeded", "WebhookMessageToolCallsFinished", "WebhookMessageToolCallsStarted", "WebhookMessageUsageTracked" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = WebhookMessage.model_construct()
        error_messages = []
        match = 0
        # validate data type: WebhookMessageUsageTracked
        if not isinstance(v, WebhookMessageUsageTracked):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhookMessageUsageTracked`")
        else:
            match += 1
        # validate data type: WebhookMessageRealtimeSessionStateChanged
        if not isinstance(v, WebhookMessageRealtimeSessionStateChanged):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhookMessageRealtimeSessionStateChanged`")
        else:
            match += 1
        # validate data type: WebhookMessageRealtimeSessionMessageCommitted
        if not isinstance(v, WebhookMessageRealtimeSessionMessageCommitted):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhookMessageRealtimeSessionMessageCommitted`")
        else:
            match += 1
        # validate data type: WebhookMessageToolCallsStarted
        if not isinstance(v, WebhookMessageToolCallsStarted):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhookMessageToolCallsStarted`")
        else:
            match += 1
        # validate data type: WebhookMessageToolCallsFinished
        if not isinstance(v, WebhookMessageToolCallsFinished):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhookMessageToolCallsFinished`")
        else:
            match += 1
        # validate data type: WebhookMessageRealtimeSessionTimeLimitExceeded
        if not isinstance(v, WebhookMessageRealtimeSessionTimeLimitExceeded):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhookMessageRealtimeSessionTimeLimitExceeded`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in WebhookMessage with oneOf schemas: WebhookMessageRealtimeSessionMessageCommitted, WebhookMessageRealtimeSessionStateChanged, WebhookMessageRealtimeSessionTimeLimitExceeded, WebhookMessageToolCallsFinished, WebhookMessageToolCallsStarted, WebhookMessageUsageTracked. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in WebhookMessage with oneOf schemas: WebhookMessageRealtimeSessionMessageCommitted, WebhookMessageRealtimeSessionStateChanged, WebhookMessageRealtimeSessionTimeLimitExceeded, WebhookMessageToolCallsFinished, WebhookMessageToolCallsStarted, WebhookMessageUsageTracked. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into WebhookMessageUsageTracked
        try:
            instance.actual_instance = WebhookMessageUsageTracked.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WebhookMessageRealtimeSessionStateChanged
        try:
            instance.actual_instance = WebhookMessageRealtimeSessionStateChanged.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WebhookMessageRealtimeSessionMessageCommitted
        try:
            instance.actual_instance = WebhookMessageRealtimeSessionMessageCommitted.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WebhookMessageToolCallsStarted
        try:
            instance.actual_instance = WebhookMessageToolCallsStarted.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WebhookMessageToolCallsFinished
        try:
            instance.actual_instance = WebhookMessageToolCallsFinished.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WebhookMessageRealtimeSessionTimeLimitExceeded
        try:
            instance.actual_instance = WebhookMessageRealtimeSessionTimeLimitExceeded.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into WebhookMessage with oneOf schemas: WebhookMessageRealtimeSessionMessageCommitted, WebhookMessageRealtimeSessionStateChanged, WebhookMessageRealtimeSessionTimeLimitExceeded, WebhookMessageToolCallsFinished, WebhookMessageToolCallsStarted, WebhookMessageUsageTracked. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into WebhookMessage with oneOf schemas: WebhookMessageRealtimeSessionMessageCommitted, WebhookMessageRealtimeSessionStateChanged, WebhookMessageRealtimeSessionTimeLimitExceeded, WebhookMessageToolCallsFinished, WebhookMessageToolCallsStarted, WebhookMessageUsageTracked. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], WebhookMessageRealtimeSessionMessageCommitted, WebhookMessageRealtimeSessionStateChanged, WebhookMessageRealtimeSessionTimeLimitExceeded, WebhookMessageToolCallsFinished, WebhookMessageToolCallsStarted, WebhookMessageUsageTracked]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


