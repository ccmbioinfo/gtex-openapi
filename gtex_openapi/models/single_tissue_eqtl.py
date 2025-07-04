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
from typing import Any, ClassVar, Dict, List, Optional, Union
from gtex_openapi.models.chromosome import Chromosome
from typing import Optional, Set
from typing_extensions import Self

class SingleTissueEqtl(BaseModel):
    """
    SingleTissueEqtl
    """ # noqa: E501
    chromosome: Chromosome
    dataset_id: StrictStr = Field(alias="datasetId")
    gencode_id: StrictStr = Field(alias="gencodeId")
    gene_symbol: StrictStr = Field(alias="geneSymbol")
    gene_symbol_upper: StrictStr = Field(alias="geneSymbolUpper")
    nes: Union[StrictFloat, StrictInt]
    p_value: Union[StrictFloat, StrictInt] = Field(alias="pValue")
    pos: StrictInt
    snp_id: Optional[StrictStr] = Field(default=None, alias="snpId")
    tissue_site_detail_id: StrictStr = Field(alias="tissueSiteDetailId")
    variant_id: StrictStr = Field(alias="variantId")
    __properties: ClassVar[List[str]] = ["chromosome", "datasetId", "gencodeId", "geneSymbol", "geneSymbolUpper", "nes", "pValue", "pos", "snpId", "tissueSiteDetailId", "variantId"]

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
        """Create an instance of SingleTissueEqtl from a JSON string"""
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
        # set to None if snp_id (nullable) is None
        # and model_fields_set contains the field
        if self.snp_id is None and "snp_id" in self.model_fields_set:
            _dict['snpId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SingleTissueEqtl from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chromosome": obj.get("chromosome"),
            "datasetId": obj.get("datasetId"),
            "gencodeId": obj.get("gencodeId"),
            "geneSymbol": obj.get("geneSymbol"),
            "geneSymbolUpper": obj.get("geneSymbolUpper"),
            "nes": obj.get("nes"),
            "pValue": obj.get("pValue"),
            "pos": obj.get("pos"),
            "snpId": obj.get("snpId"),
            "tissueSiteDetailId": obj.get("tissueSiteDetailId"),
            "variantId": obj.get("variantId")
        })
        return _obj


