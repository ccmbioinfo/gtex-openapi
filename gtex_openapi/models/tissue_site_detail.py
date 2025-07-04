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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gtex_openapi.models.dataset_id import DatasetId
from gtex_openapi.models.sex_based_summary import SexBasedSummary
from gtex_openapi.models.tissue_site_detail_id import TissueSiteDetailId
from gtex_openapi.models.tissue_site_ontology_id import TissueSiteOntologyId
from typing import Optional, Set
from typing_extensions import Self

class TissueSiteDetail(BaseModel):
    """
    The TissueSiteDetail is returned by the endpoints: `GET /tissueSiteDetail`. It provides the client with information about samples obtained from the detailed tissue site.
    """ # noqa: E501
    tissue_site_detail_id: TissueSiteDetailId = Field(alias="tissueSiteDetailId")
    color_hex: StrictStr = Field(alias="colorHex")
    color_rgb: StrictStr = Field(alias="colorRgb")
    dataset_id: DatasetId = Field(alias="datasetId")
    e_gene_count: Optional[StrictInt] = Field(default=None, alias="eGeneCount")
    expressed_gene_count: Optional[StrictInt] = Field(default=None, alias="expressedGeneCount")
    has_e_genes: StrictBool = Field(alias="hasEGenes")
    has_s_genes: StrictBool = Field(alias="hasSGenes")
    mapped_in_hubmap: StrictBool = Field(alias="mappedInHubmap")
    eqtl_sample_summary: SexBasedSummary = Field(alias="eqtlSampleSummary")
    rna_seq_sample_summary: SexBasedSummary = Field(alias="rnaSeqSampleSummary")
    s_gene_count: Optional[StrictInt] = Field(default=None, alias="sGeneCount")
    sampling_site: StrictStr = Field(alias="samplingSite")
    tissue_site: StrictStr = Field(alias="tissueSite")
    tissue_site_detail: StrictStr = Field(alias="tissueSiteDetail")
    tissue_site_detail_abbr: StrictStr = Field(alias="tissueSiteDetailAbbr")
    ontology_id: TissueSiteOntologyId = Field(alias="ontologyId")
    ontology_iri: StrictStr = Field(alias="ontologyIri")
    __properties: ClassVar[List[str]] = ["tissueSiteDetailId", "colorHex", "colorRgb", "datasetId", "eGeneCount", "expressedGeneCount", "hasEGenes", "hasSGenes", "mappedInHubmap", "eqtlSampleSummary", "rnaSeqSampleSummary", "sGeneCount", "samplingSite", "tissueSite", "tissueSiteDetail", "tissueSiteDetailAbbr", "ontologyId", "ontologyIri"]

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
        """Create an instance of TissueSiteDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of eqtl_sample_summary
        if self.eqtl_sample_summary:
            _dict['eqtlSampleSummary'] = self.eqtl_sample_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rna_seq_sample_summary
        if self.rna_seq_sample_summary:
            _dict['rnaSeqSampleSummary'] = self.rna_seq_sample_summary.to_dict()
        # set to None if e_gene_count (nullable) is None
        # and model_fields_set contains the field
        if self.e_gene_count is None and "e_gene_count" in self.model_fields_set:
            _dict['eGeneCount'] = None

        # set to None if expressed_gene_count (nullable) is None
        # and model_fields_set contains the field
        if self.expressed_gene_count is None and "expressed_gene_count" in self.model_fields_set:
            _dict['expressedGeneCount'] = None

        # set to None if s_gene_count (nullable) is None
        # and model_fields_set contains the field
        if self.s_gene_count is None and "s_gene_count" in self.model_fields_set:
            _dict['sGeneCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TissueSiteDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tissueSiteDetailId": obj.get("tissueSiteDetailId"),
            "colorHex": obj.get("colorHex"),
            "colorRgb": obj.get("colorRgb"),
            "datasetId": obj.get("datasetId"),
            "eGeneCount": obj.get("eGeneCount"),
            "expressedGeneCount": obj.get("expressedGeneCount"),
            "hasEGenes": obj.get("hasEGenes"),
            "hasSGenes": obj.get("hasSGenes"),
            "mappedInHubmap": obj.get("mappedInHubmap"),
            "eqtlSampleSummary": SexBasedSummary.from_dict(obj["eqtlSampleSummary"]) if obj.get("eqtlSampleSummary") is not None else None,
            "rnaSeqSampleSummary": SexBasedSummary.from_dict(obj["rnaSeqSampleSummary"]) if obj.get("rnaSeqSampleSummary") is not None else None,
            "sGeneCount": obj.get("sGeneCount"),
            "samplingSite": obj.get("samplingSite"),
            "tissueSite": obj.get("tissueSite"),
            "tissueSiteDetail": obj.get("tissueSiteDetail"),
            "tissueSiteDetailAbbr": obj.get("tissueSiteDetailAbbr"),
            "ontologyId": obj.get("ontologyId"),
            "ontologyIri": obj.get("ontologyIri")
        })
        return _obj


