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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class OpenAccessFolder(BaseModel):
    """
    Encapsulates the information about a single grouping of files on the downloads page. Folders include front-end artefacts such as Tabs, Releases, File Groups, e.t.c
    """ # noqa: E501
    name: StrictStr
    display_name: StrictStr = Field(alias="displayName")
    description: StrictStr
    order: StrictInt
    parent: StrictStr
    children: OpenAccessFolderChildren
    __properties: ClassVar[List[str]] = ["name", "displayName", "description", "order", "parent", "children"]

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
        """Create an instance of OpenAccessFolder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of children
        if self.children:
            _dict['children'] = self.children.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpenAccessFolder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "displayName": obj.get("displayName"),
            "description": obj.get("description"),
            "order": obj.get("order"),
            "parent": obj.get("parent"),
            "children": OpenAccessFolderChildren.from_dict(obj["children"]) if obj.get("children") is not None else None
        })
        return _obj

from gtex_openapi.models.open_access_folder_children import OpenAccessFolderChildren
# TODO: Rewrite to not use raise_errors
OpenAccessFolder.model_rebuild(raise_errors=False)

