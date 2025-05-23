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
from enum import Enum
from typing_extensions import Self


class SDKAgentState(str, Enum):
    """
    SDKAgentState
    """

    """
    allowed enum values
    """
    WARMUP = 'warmup'
    LISTENING = 'listening'
    THINKING = 'thinking'
    SPEAKING = 'speaking'
    TIME_LIMIT_EXCEEDED = 'time_limit_exceeded'
    USAGE_LIMIT_EXCEEDED = 'usage_limit_exceeded'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SDKAgentState from a JSON string"""
        return cls(json.loads(json_str))


