# coding: utf-8

"""
    Gentrace API

    These API routes are designed to ingest events from clients.  # noqa: E501

    The version of the OpenAPI document: ${npm_package_version}
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from inspect import getfullargspec
from typing import Optional

from pydantic import BaseModel, Field, StrictStr


class PipelineRunResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    pipeline_run_id: Optional[StrictStr] = Field(None, alias="pipelineRunId")
    __properties = ["pipelineRunId"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PipelineRunResponse:
        """Create an instance of PipelineRunResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PipelineRunResponse:
        """Create an instance of PipelineRunResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PipelineRunResponse.parse_obj(obj)

        _obj = PipelineRunResponse.parse_obj(
            {"pipeline_run_id": obj.get("pipelineRunId")}
        )
        return _obj
