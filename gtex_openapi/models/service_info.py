# coding: utf-8

"""
    GTEx Portal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gtex_openapi.models.organization import Organization
from typing import Optional, Set
from typing_extensions import Self

class ServiceInfo(BaseModel):
    """
    The `ServiceInfo` object provides a structured format for describing web services implementing GA4GH API specifications. RNA-get implements service info through the standard `/service-info` API endpoint
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    version: StrictStr
    organization: Organization
    description: Optional[StrictStr] = None
    contact_url: Optional[StrictStr] = Field(default=None, alias="contactUrl")
    documentation_url: Optional[StrictStr] = Field(default=None, alias="documentationUrl")
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    environment: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "name", "version", "organization", "description", "contactUrl", "documentationUrl", "createdAt", "updatedAt", "environment"]

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
        """Create an instance of ServiceInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "version": obj.get("version"),
            "organization": Organization.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "description": obj.get("description"),
            "contactUrl": obj.get("contactUrl"),
            "documentationUrl": obj.get("documentationUrl"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "environment": obj.get("environment")
        })
        return _obj


