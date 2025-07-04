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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gtex_openapi.models.app_models_responses_hardy_scale import AppModelsResponsesHardyScale
from gtex_openapi.models.donor_age_bracket import DonorAgeBracket
from gtex_openapi.models.sex import Sex
from typing import Optional, Set
from typing_extensions import Self

class HistologySample(BaseModel):
    """
    HistologySample
    """ # noqa: E501
    age_bracket: DonorAgeBracket = Field(alias="ageBracket")
    hardy_scale: AppModelsResponsesHardyScale = Field(alias="hardyScale")
    hide: StrictBool
    histology_image_id: StrictStr = Field(alias="histologyImageId")
    pathology_notes: Optional[StrictStr] = Field(default=None, alias="pathologyNotes")
    pathology_notes_categories: Dict[str, StrictBool] = Field(alias="pathologyNotesCategories")
    sample_id: Optional[StrictStr] = Field(default=None, alias="sampleId")
    sex: Sex
    subject_id: StrictStr = Field(alias="subjectId")
    tissue_sample_id: Optional[StrictStr] = Field(default=None, alias="tissueSampleId")
    tissue_site_detail: StrictStr = Field(alias="tissueSiteDetail")
    __properties: ClassVar[List[str]] = ["ageBracket", "hardyScale", "hide", "histologyImageId", "pathologyNotes", "pathologyNotesCategories", "sampleId", "sex", "subjectId", "tissueSampleId", "tissueSiteDetail"]

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
        """Create an instance of HistologySample from a JSON string"""
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
        # set to None if pathology_notes (nullable) is None
        # and model_fields_set contains the field
        if self.pathology_notes is None and "pathology_notes" in self.model_fields_set:
            _dict['pathologyNotes'] = None

        # set to None if sample_id (nullable) is None
        # and model_fields_set contains the field
        if self.sample_id is None and "sample_id" in self.model_fields_set:
            _dict['sampleId'] = None

        # set to None if tissue_sample_id (nullable) is None
        # and model_fields_set contains the field
        if self.tissue_sample_id is None and "tissue_sample_id" in self.model_fields_set:
            _dict['tissueSampleId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HistologySample from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ageBracket": obj.get("ageBracket"),
            "hardyScale": obj.get("hardyScale"),
            "hide": obj.get("hide"),
            "histologyImageId": obj.get("histologyImageId"),
            "pathologyNotes": obj.get("pathologyNotes"),
            "pathologyNotesCategories": obj.get("pathologyNotesCategories"),
            "sampleId": obj.get("sampleId"),
            "sex": obj.get("sex"),
            "subjectId": obj.get("subjectId"),
            "tissueSampleId": obj.get("tissueSampleId"),
            "tissueSiteDetail": obj.get("tissueSiteDetail")
        })
        return _obj


