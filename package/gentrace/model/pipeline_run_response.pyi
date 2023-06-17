# coding: utf-8

"""
    Gentrace API

    These API routes are designed to ingest events from clients.  # noqa: E501

    The version of the OpenAPI document: 0.7.0
    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401

from gentrace import schemas  # noqa: F401

class PipelineRunResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            pipelineRunId = schemas.UUIDSchema
            __annotations__ = {
                "pipelineRunId": pipelineRunId,
            }
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["pipelineRunId"]
    ) -> MetaOapg.properties.pipelineRunId: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self, name: typing.Union[typing_extensions.Literal["pipelineRunId",], str]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["pipelineRunId"]
    ) -> typing.Union[MetaOapg.properties.pipelineRunId, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self, name: typing.Union[typing_extensions.Literal["pipelineRunId",], str]
    ):
        return super().get_item_oapg(name)
    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        pipelineRunId: typing.Union[
            MetaOapg.properties.pipelineRunId, str, uuid.UUID, schemas.Unset
        ] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[
            schemas.AnyTypeSchema,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            None,
            list,
            tuple,
            bytes,
        ],
    ) -> "PipelineRunResponse":
        return super().__new__(
            cls,
            *_args,
            pipelineRunId=pipelineRunId,
            _configuration=_configuration,
            **kwargs,
        )
