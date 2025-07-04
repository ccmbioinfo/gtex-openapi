# coding: utf-8

"""
    GTEx Portal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class OriginalMaterialType(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    CELLS_COLON_CELL_LINE_COMMA__VIABLE = 'Cells:Cell Line, Viable'
    CELLS_COLON_GROWING = 'Cells:Growing'
    CELLS_COLON_PELLET_FROZEN = 'Cells:Pellet frozen'
    OTHER_COLON_TRIZOL_LYSATE = 'Other:Trizol Lysate'
    TISSUE_COLON_FIXED_TISSUE = 'Tissue:Fixed Tissue'
    TISSUE_COLON_FRESH_FROZEN_TISSUE = 'Tissue:Fresh Frozen Tissue'
    TISSUE_COLON_FRESH_SKIN_PUNCH = 'Tissue:Fresh Skin Punch'
    TISSUE_COLON_FRESH_TISSUE = 'Tissue:Fresh Tissue'
    TISSUE_COLON_FROZEN_TISSUE_SECTION = 'Tissue:Frozen Tissue Section'
    TISSUE_COLON_PA_XGENE_PRESERVED = 'Tissue:PAXgene Preserved'
    WHOLE_BLOOD_COLON_PA_XGENE_PRESERVED = 'Whole Blood:PAXgene Preserved'
    WHOLE_BLOOD_COLON_WHOLE_BLOOD = 'Whole Blood:Whole Blood'
    WHOLE_BLOOD_COLON_WHOLE_BLOOD_FRESH = 'Whole Blood:Whole Blood Fresh'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OriginalMaterialType from a JSON string"""
        return cls(json.loads(json_str))


