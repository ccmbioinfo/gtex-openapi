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


class DonorAgeBracket(str, Enum):
    """
         The age bracket of the donor in 10 year increments     
    """

    """
    allowed enum values
    """
    ENUM_20_MINUS_29 = '20-29'
    ENUM_30_MINUS_39 = '30-39'
    ENUM_40_MINUS_49 = '40-49'
    ENUM_50_MINUS_59 = '50-59'
    ENUM_60_MINUS_69 = '60-69'
    ENUM_70_MINUS_79 = '70-79'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DonorAgeBracket from a JSON string"""
        return cls(json.loads(json_str))


