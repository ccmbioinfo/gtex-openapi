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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from gtex_openapi.models.dataset_id import DatasetId
from gtex_openapi.models.tissue_site_detail_id import TissueSiteDetailId
from gtex_openapi.models.tissue_site_ontology_id import TissueSiteOntologyId
from gtex_openapi.models.units import Units
from typing import Optional, Set
from typing_extensions import Self

class MedianJunctionExpression(BaseModel):
    """
    MedianJunctionExpression
    """ # noqa: E501
    median: Union[StrictFloat, StrictInt]
    junction_id: StrictStr = Field(alias="junctionId")
    tissue_site_detail_id: TissueSiteDetailId = Field(alias="tissueSiteDetailId")
    ontology_id: TissueSiteOntologyId = Field(alias="ontologyId")
    dataset_id: DatasetId = Field(alias="datasetId")
    gencode_id: StrictStr = Field(alias="gencodeId")
    gene_symbol: StrictStr = Field(alias="geneSymbol")
    unit: Units
    __properties: ClassVar[List[str]] = ["median", "junctionId", "tissueSiteDetailId", "ontologyId", "datasetId", "gencodeId", "geneSymbol", "unit"]

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
        """Create an instance of MedianJunctionExpression from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MedianJunctionExpression from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "median": obj.get("median"),
            "junctionId": obj.get("junctionId"),
            "tissueSiteDetailId": obj.get("tissueSiteDetailId"),
            "ontologyId": obj.get("ontologyId"),
            "datasetId": obj.get("datasetId"),
            "gencodeId": obj.get("gencodeId"),
            "geneSymbol": obj.get("geneSymbol"),
            "unit": obj.get("unit")
        })
        return _obj


