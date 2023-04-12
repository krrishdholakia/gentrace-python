# coding: utf-8

"""
    Gentrace API

    These API routes are designed to ingest events from clients.  # noqa: E501

    The version of the OpenAPI document: 0.4.0
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


class PipelineRunRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "stepRuns",
            "name",
        }

        class properties:
            name = schemas.StrSchema

            class stepRuns(schemas.ListSchema):
                class MetaOapg:
                    class items(schemas.DictSchema):
                        class MetaOapg:
                            class properties:
                                class provider(schemas.DictSchema):
                                    class MetaOapg:
                                        class properties:
                                            name = schemas.StrSchema
                                            invocation = schemas.StrSchema

                                            class modelParams(schemas.DictSchema):
                                                class MetaOapg:
                                                    additional_properties = (
                                                        schemas.AnyTypeSchema
                                                    )

                                                def __getitem__(
                                                    self, name: typing.Union[str,]
                                                ) -> MetaOapg.additional_properties:
                                                    # dict_instance[name] accessor
                                                    return super().__getitem__(name)

                                                def get_item_oapg(
                                                    self, name: typing.Union[str,]
                                                ) -> MetaOapg.additional_properties:
                                                    return super().get_item_oapg(name)

                                                def __new__(
                                                    cls,
                                                    *_args: typing.Union[
                                                        dict,
                                                        frozendict.frozendict,
                                                    ],
                                                    _configuration: typing.Optional[
                                                        schemas.Configuration
                                                    ] = None,
                                                    **kwargs: typing.Union[
                                                        MetaOapg.additional_properties,
                                                        dict,
                                                        frozendict.frozendict,
                                                        str,
                                                        date,
                                                        datetime,
                                                        uuid.UUID,
                                                        int,
                                                        float,
                                                        decimal.Decimal,
                                                        bool,
                                                        None,
                                                        list,
                                                        tuple,
                                                        bytes,
                                                        io.FileIO,
                                                        io.BufferedReader,
                                                    ],
                                                ) -> "modelParams":
                                                    return super().__new__(
                                                        cls,
                                                        *_args,
                                                        _configuration=_configuration,
                                                        **kwargs,
                                                    )

                                            class inputs(schemas.DictSchema):
                                                class MetaOapg:
                                                    additional_properties = (
                                                        schemas.AnyTypeSchema
                                                    )

                                                def __getitem__(
                                                    self, name: typing.Union[str,]
                                                ) -> MetaOapg.additional_properties:
                                                    # dict_instance[name] accessor
                                                    return super().__getitem__(name)

                                                def get_item_oapg(
                                                    self, name: typing.Union[str,]
                                                ) -> MetaOapg.additional_properties:
                                                    return super().get_item_oapg(name)

                                                def __new__(
                                                    cls,
                                                    *_args: typing.Union[
                                                        dict,
                                                        frozendict.frozendict,
                                                    ],
                                                    _configuration: typing.Optional[
                                                        schemas.Configuration
                                                    ] = None,
                                                    **kwargs: typing.Union[
                                                        MetaOapg.additional_properties,
                                                        dict,
                                                        frozendict.frozendict,
                                                        str,
                                                        date,
                                                        datetime,
                                                        uuid.UUID,
                                                        int,
                                                        float,
                                                        decimal.Decimal,
                                                        bool,
                                                        None,
                                                        list,
                                                        tuple,
                                                        bytes,
                                                        io.FileIO,
                                                        io.BufferedReader,
                                                    ],
                                                ) -> "inputs":
                                                    return super().__new__(
                                                        cls,
                                                        *_args,
                                                        _configuration=_configuration,
                                                        **kwargs,
                                                    )

                                            class outputs(schemas.DictSchema):
                                                class MetaOapg:
                                                    additional_properties = (
                                                        schemas.AnyTypeSchema
                                                    )

                                                def __getitem__(
                                                    self, name: typing.Union[str,]
                                                ) -> MetaOapg.additional_properties:
                                                    # dict_instance[name] accessor
                                                    return super().__getitem__(name)

                                                def get_item_oapg(
                                                    self, name: typing.Union[str,]
                                                ) -> MetaOapg.additional_properties:
                                                    return super().get_item_oapg(name)

                                                def __new__(
                                                    cls,
                                                    *_args: typing.Union[
                                                        dict,
                                                        frozendict.frozendict,
                                                    ],
                                                    _configuration: typing.Optional[
                                                        schemas.Configuration
                                                    ] = None,
                                                    **kwargs: typing.Union[
                                                        MetaOapg.additional_properties,
                                                        dict,
                                                        frozendict.frozendict,
                                                        str,
                                                        date,
                                                        datetime,
                                                        uuid.UUID,
                                                        int,
                                                        float,
                                                        decimal.Decimal,
                                                        bool,
                                                        None,
                                                        list,
                                                        tuple,
                                                        bytes,
                                                        io.FileIO,
                                                        io.BufferedReader,
                                                    ],
                                                ) -> "outputs":
                                                    return super().__new__(
                                                        cls,
                                                        *_args,
                                                        _configuration=_configuration,
                                                        **kwargs,
                                                    )

                                            __annotations__ = {
                                                "name": name,
                                                "invocation": invocation,
                                                "modelParams": modelParams,
                                                "inputs": inputs,
                                                "outputs": outputs,
                                            }

                                    @typing.overload
                                    def __getitem__(
                                        self, name: typing_extensions.Literal["name"]
                                    ) -> MetaOapg.properties.name:
                                        ...

                                    @typing.overload
                                    def __getitem__(
                                        self,
                                        name: typing_extensions.Literal["invocation"],
                                    ) -> MetaOapg.properties.invocation:
                                        ...

                                    @typing.overload
                                    def __getitem__(
                                        self,
                                        name: typing_extensions.Literal["modelParams"],
                                    ) -> MetaOapg.properties.modelParams:
                                        ...

                                    @typing.overload
                                    def __getitem__(
                                        self, name: typing_extensions.Literal["inputs"]
                                    ) -> MetaOapg.properties.inputs:
                                        ...

                                    @typing.overload
                                    def __getitem__(
                                        self, name: typing_extensions.Literal["outputs"]
                                    ) -> MetaOapg.properties.outputs:
                                        ...

                                    @typing.overload
                                    def __getitem__(
                                        self, name: str
                                    ) -> schemas.UnsetAnyTypeSchema:
                                        ...

                                    def __getitem__(
                                        self,
                                        name: typing.Union[
                                            typing_extensions.Literal[
                                                "name",
                                                "invocation",
                                                "modelParams",
                                                "inputs",
                                                "outputs",
                                            ],
                                            str,
                                        ],
                                    ):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)

                                    @typing.overload
                                    def get_item_oapg(
                                        self, name: typing_extensions.Literal["name"]
                                    ) -> typing.Union[
                                        MetaOapg.properties.name, schemas.Unset
                                    ]:
                                        ...

                                    @typing.overload
                                    def get_item_oapg(
                                        self,
                                        name: typing_extensions.Literal["invocation"],
                                    ) -> typing.Union[
                                        MetaOapg.properties.invocation, schemas.Unset
                                    ]:
                                        ...

                                    @typing.overload
                                    def get_item_oapg(
                                        self,
                                        name: typing_extensions.Literal["modelParams"],
                                    ) -> typing.Union[
                                        MetaOapg.properties.modelParams, schemas.Unset
                                    ]:
                                        ...

                                    @typing.overload
                                    def get_item_oapg(
                                        self, name: typing_extensions.Literal["inputs"]
                                    ) -> typing.Union[
                                        MetaOapg.properties.inputs, schemas.Unset
                                    ]:
                                        ...

                                    @typing.overload
                                    def get_item_oapg(
                                        self, name: typing_extensions.Literal["outputs"]
                                    ) -> typing.Union[
                                        MetaOapg.properties.outputs, schemas.Unset
                                    ]:
                                        ...

                                    @typing.overload
                                    def get_item_oapg(
                                        self, name: str
                                    ) -> typing.Union[
                                        schemas.UnsetAnyTypeSchema, schemas.Unset
                                    ]:
                                        ...

                                    def get_item_oapg(
                                        self,
                                        name: typing.Union[
                                            typing_extensions.Literal[
                                                "name",
                                                "invocation",
                                                "modelParams",
                                                "inputs",
                                                "outputs",
                                            ],
                                            str,
                                        ],
                                    ):
                                        return super().get_item_oapg(name)

                                    def __new__(
                                        cls,
                                        *_args: typing.Union[
                                            dict,
                                            frozendict.frozendict,
                                        ],
                                        name: typing.Union[
                                            MetaOapg.properties.name, str, schemas.Unset
                                        ] = schemas.unset,
                                        invocation: typing.Union[
                                            MetaOapg.properties.invocation,
                                            str,
                                            schemas.Unset,
                                        ] = schemas.unset,
                                        modelParams: typing.Union[
                                            MetaOapg.properties.modelParams,
                                            dict,
                                            frozendict.frozendict,
                                            schemas.Unset,
                                        ] = schemas.unset,
                                        inputs: typing.Union[
                                            MetaOapg.properties.inputs,
                                            dict,
                                            frozendict.frozendict,
                                            schemas.Unset,
                                        ] = schemas.unset,
                                        outputs: typing.Union[
                                            MetaOapg.properties.outputs,
                                            dict,
                                            frozendict.frozendict,
                                            schemas.Unset,
                                        ] = schemas.unset,
                                        _configuration: typing.Optional[
                                            schemas.Configuration
                                        ] = None,
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
                                    ) -> "provider":
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            name=name,
                                            invocation=invocation,
                                            modelParams=modelParams,
                                            inputs=inputs,
                                            outputs=outputs,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )

                                elapsedTime = schemas.IntSchema
                                startTime = schemas.DateTimeSchema
                                endTime = schemas.DateTimeSchema
                                __annotations__ = {
                                    "provider": provider,
                                    "elapsedTime": elapsedTime,
                                    "startTime": startTime,
                                    "endTime": endTime,
                                }

                        @typing.overload
                        def __getitem__(
                            self, name: typing_extensions.Literal["provider"]
                        ) -> MetaOapg.properties.provider:
                            ...

                        @typing.overload
                        def __getitem__(
                            self, name: typing_extensions.Literal["elapsedTime"]
                        ) -> MetaOapg.properties.elapsedTime:
                            ...

                        @typing.overload
                        def __getitem__(
                            self, name: typing_extensions.Literal["startTime"]
                        ) -> MetaOapg.properties.startTime:
                            ...

                        @typing.overload
                        def __getitem__(
                            self, name: typing_extensions.Literal["endTime"]
                        ) -> MetaOapg.properties.endTime:
                            ...

                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
                            ...

                        def __getitem__(
                            self,
                            name: typing.Union[
                                typing_extensions.Literal[
                                    "provider",
                                    "elapsedTime",
                                    "startTime",
                                    "endTime",
                                ],
                                str,
                            ],
                        ):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)

                        @typing.overload
                        def get_item_oapg(
                            self, name: typing_extensions.Literal["provider"]
                        ) -> typing.Union[MetaOapg.properties.provider, schemas.Unset]:
                            ...

                        @typing.overload
                        def get_item_oapg(
                            self, name: typing_extensions.Literal["elapsedTime"]
                        ) -> typing.Union[
                            MetaOapg.properties.elapsedTime, schemas.Unset
                        ]:
                            ...

                        @typing.overload
                        def get_item_oapg(
                            self, name: typing_extensions.Literal["startTime"]
                        ) -> typing.Union[MetaOapg.properties.startTime, schemas.Unset]:
                            ...

                        @typing.overload
                        def get_item_oapg(
                            self, name: typing_extensions.Literal["endTime"]
                        ) -> typing.Union[MetaOapg.properties.endTime, schemas.Unset]:
                            ...

                        @typing.overload
                        def get_item_oapg(
                            self, name: str
                        ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
                            ...

                        def get_item_oapg(
                            self,
                            name: typing.Union[
                                typing_extensions.Literal[
                                    "provider",
                                    "elapsedTime",
                                    "startTime",
                                    "endTime",
                                ],
                                str,
                            ],
                        ):
                            return super().get_item_oapg(name)

                        def __new__(
                            cls,
                            *_args: typing.Union[
                                dict,
                                frozendict.frozendict,
                            ],
                            provider: typing.Union[
                                MetaOapg.properties.provider,
                                dict,
                                frozendict.frozendict,
                                schemas.Unset,
                            ] = schemas.unset,
                            elapsedTime: typing.Union[
                                MetaOapg.properties.elapsedTime,
                                decimal.Decimal,
                                int,
                                schemas.Unset,
                            ] = schemas.unset,
                            startTime: typing.Union[
                                MetaOapg.properties.startTime,
                                str,
                                datetime,
                                schemas.Unset,
                            ] = schemas.unset,
                            endTime: typing.Union[
                                MetaOapg.properties.endTime,
                                str,
                                datetime,
                                schemas.Unset,
                            ] = schemas.unset,
                            _configuration: typing.Optional[
                                schemas.Configuration
                            ] = None,
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
                        ) -> "items":
                            return super().__new__(
                                cls,
                                *_args,
                                provider=provider,
                                elapsedTime=elapsedTime,
                                startTime=startTime,
                                endTime=endTime,
                                _configuration=_configuration,
                                **kwargs,
                            )

                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple[
                            typing.Union[
                                MetaOapg.items,
                                dict,
                                frozendict.frozendict,
                            ]
                        ],
                        typing.List[
                            typing.Union[
                                MetaOapg.items,
                                dict,
                                frozendict.frozendict,
                            ]
                        ],
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "stepRuns":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            __annotations__ = {
                "name": name,
                "stepRuns": stepRuns,
            }

    stepRuns: MetaOapg.properties.stepRuns
    name: MetaOapg.properties.name

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["stepRuns"]
    ) -> MetaOapg.properties.stepRuns:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "name",
                "stepRuns",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["stepRuns"]
    ) -> MetaOapg.properties.stepRuns:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "name",
                "stepRuns",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        stepRuns: typing.Union[
            MetaOapg.properties.stepRuns,
            list,
            tuple,
        ],
        name: typing.Union[
            MetaOapg.properties.name,
            str,
        ],
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
    ) -> "PipelineRunRequest":
        return super().__new__(
            cls,
            *_args,
            stepRuns=stepRuns,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )
