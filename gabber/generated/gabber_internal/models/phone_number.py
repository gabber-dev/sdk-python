# coding: utf-8

"""
    Session API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gabber.generated.gabber_internal.models.phone_number_attachment import PhoneNumberAttachment
from gabber.generated.gabber_internal.models.phone_number_capabilities import PhoneNumberCapabilities
from gabber.generated.gabber_internal.models.phone_number_type import PhoneNumberType
from typing import Optional, Set
from typing_extensions import Self

class PhoneNumber(BaseModel):
    """
    PhoneNumber
    """ # noqa: E501
    type: PhoneNumberType
    number: StrictStr
    capabilities: PhoneNumberCapabilities
    twilio_account_sid: Optional[StrictStr] = None
    phone_connection: StrictStr
    attachment: Optional[PhoneNumberAttachment] = None
    __properties: ClassVar[List[str]] = ["type", "number", "capabilities", "twilio_account_sid", "phone_connection", "attachment"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PhoneNumber from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of capabilities
        if self.capabilities:
            _dict['capabilities'] = self.capabilities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attachment
        if self.attachment:
            _dict['attachment'] = self.attachment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhoneNumber from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "number": obj.get("number"),
            "capabilities": PhoneNumberCapabilities.from_dict(obj["capabilities"]) if obj.get("capabilities") is not None else None,
            "twilio_account_sid": obj.get("twilio_account_sid"),
            "phone_connection": obj.get("phone_connection"),
            "attachment": PhoneNumberAttachment.from_dict(obj["attachment"]) if obj.get("attachment") is not None else None
        })
        return _obj


