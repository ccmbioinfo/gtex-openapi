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


class IschemicTimeGroup(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    LESS_THAN_EQUAL__0 = '<= 0'
    ENUM_1_MINUS__300 = '1 - 300'
    ENUM_301_MINUS__600 = '301 - 600'
    ENUM_601_MINUS__900 = '601 - 900'
    ENUM_901_MINUS__1200 = '901 - 1200'
    ENUM_1201_MINUS__1500 = '1201 - 1500'
    GREATER_THAN__1500 = '> 1500'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IschemicTimeGroup from a JSON string"""
        return cls(json.loads(json_str))


