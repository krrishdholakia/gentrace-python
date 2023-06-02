# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from dataclasses import dataclass
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401
import urllib3
from urllib3._collections import HTTPHeaderDict

from gentrace import (
    api_client,
    exceptions,
    schemas,  # noqa: F401
)

# body param

class SchemaForRequestBodyApplicationJson(schemas.DictSchema):
    class MetaOapg:
        required = {
            "testResults",
            "setId",
            "source",
        }

        class properties:
            setId = schemas.UUIDSchema
            branch = schemas.StrSchema
            commit = schemas.StrSchema

            class testResults(schemas.ListSchema):
                class MetaOapg:
                    class items(schemas.DictSchema):
                        class MetaOapg:
                            required = {
                                "output",
                                "inputs",
                                "caseId",
                            }

                            class properties:
                                id = schemas.UUIDSchema
                                caseId = schemas.UUIDSchema
                                inputs = schemas.DictSchema
                                output = schemas.StrSchema
                                __annotations__ = {
                                    "id": id,
                                    "caseId": caseId,
                                    "inputs": inputs,
                                    "output": output,
                                }
                        output: MetaOapg.properties.output
                        inputs: MetaOapg.properties.inputs
                        caseId: MetaOapg.properties.caseId

                        @typing.overload
                        def __getitem__(
                            self, name: typing_extensions.Literal["id"]
                        ) -> MetaOapg.properties.id: ...
                        @typing.overload
                        def __getitem__(
                            self, name: typing_extensions.Literal["caseId"]
                        ) -> MetaOapg.properties.caseId: ...
                        @typing.overload
                        def __getitem__(
                            self, name: typing_extensions.Literal["inputs"]
                        ) -> MetaOapg.properties.inputs: ...
                        @typing.overload
                        def __getitem__(
                            self, name: typing_extensions.Literal["output"]
                        ) -> MetaOapg.properties.output: ...
                        @typing.overload
                        def __getitem__(
                            self, name: str
                        ) -> schemas.UnsetAnyTypeSchema: ...
                        def __getitem__(
                            self,
                            name: typing.Union[
                                typing_extensions.Literal[
                                    "id",
                                    "caseId",
                                    "inputs",
                                    "output",
                                ],
                                str,
                            ],
                        ):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        @typing.overload
                        def get_item_oapg(
                            self, name: typing_extensions.Literal["id"]
                        ) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                        @typing.overload
                        def get_item_oapg(
                            self, name: typing_extensions.Literal["caseId"]
                        ) -> MetaOapg.properties.caseId: ...
                        @typing.overload
                        def get_item_oapg(
                            self, name: typing_extensions.Literal["inputs"]
                        ) -> MetaOapg.properties.inputs: ...
                        @typing.overload
                        def get_item_oapg(
                            self, name: typing_extensions.Literal["output"]
                        ) -> MetaOapg.properties.output: ...
                        @typing.overload
                        def get_item_oapg(
                            self, name: str
                        ) -> typing.Union[
                            schemas.UnsetAnyTypeSchema, schemas.Unset
                        ]: ...
                        def get_item_oapg(
                            self,
                            name: typing.Union[
                                typing_extensions.Literal[
                                    "id",
                                    "caseId",
                                    "inputs",
                                    "output",
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
                            output: typing.Union[
                                MetaOapg.properties.output,
                                str,
                            ],
                            inputs: typing.Union[
                                MetaOapg.properties.inputs,
                                dict,
                                frozendict.frozendict,
                            ],
                            caseId: typing.Union[
                                MetaOapg.properties.caseId,
                                str,
                                uuid.UUID,
                            ],
                            id: typing.Union[
                                MetaOapg.properties.id, str, uuid.UUID, schemas.Unset
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
                                output=output,
                                inputs=inputs,
                                caseId=caseId,
                                id=id,
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
                ) -> "testResults":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "setId": setId,
                "branch": branch,
                "commit": commit,
                "testResults": testResults,
            }
    testResults: MetaOapg.properties.testResults
    setId: MetaOapg.properties.setId
    source: schemas.AnyTypeSchema

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["setId"]
    ) -> MetaOapg.properties.setId: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["branch"]
    ) -> MetaOapg.properties.branch: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["commit"]
    ) -> MetaOapg.properties.commit: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["testResults"]
    ) -> MetaOapg.properties.testResults: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "setId",
                "branch",
                "commit",
                "testResults",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["setId"]
    ) -> MetaOapg.properties.setId: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["branch"]
    ) -> typing.Union[MetaOapg.properties.branch, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["commit"]
    ) -> typing.Union[MetaOapg.properties.commit, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["testResults"]
    ) -> MetaOapg.properties.testResults: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "setId",
                "branch",
                "commit",
                "testResults",
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
        testResults: typing.Union[
            MetaOapg.properties.testResults,
            list,
            tuple,
        ],
        setId: typing.Union[
            MetaOapg.properties.setId,
            str,
            uuid.UUID,
        ],
        source: typing.Union[
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
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader,
        ],
        branch: typing.Union[
            MetaOapg.properties.branch, str, schemas.Unset
        ] = schemas.unset,
        commit: typing.Union[
            MetaOapg.properties.commit, str, schemas.Unset
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
    ) -> "SchemaForRequestBodyApplicationJson":
        return super().__new__(
            cls,
            *_args,
            testResults=testResults,
            setId=setId,
            source=source,
            branch=branch,
            commit=commit,
            _configuration=_configuration,
            **kwargs,
        )

request_body_any_type = api_client.RequestBody(
    content={
        "application/json": api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson
        ),
    },
    required=True,
)

class SchemaFor200ResponseBodyApplicationJson(schemas.DictSchema):
    class MetaOapg:
        required = {
            "runId",
        }

        class properties:
            runId = schemas.UUIDSchema
            __annotations__ = {
                "runId": runId,
            }
    runId: MetaOapg.properties.runId

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["runId"]
    ) -> MetaOapg.properties.runId: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["runId",], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["runId"]
    ) -> MetaOapg.properties.runId: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self, name: typing.Union[typing_extensions.Literal["runId",], str]
    ):
        return super().get_item_oapg(name)
    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        runId: typing.Union[
            MetaOapg.properties.runId,
            str,
            uuid.UUID,
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
    ) -> "SchemaFor200ResponseBodyApplicationJson":
        return super().__new__(
            cls,
            *_args,
            runId=runId,
            _configuration=_configuration,
            **kwargs,
        )

class SchemaFor200ResponseBodyApplicationJsonCharsetutf8(schemas.DictSchema):
    class MetaOapg:
        required = {
            "runId",
        }

        class properties:
            runId = schemas.UUIDSchema
            __annotations__ = {
                "runId": runId,
            }
    runId: MetaOapg.properties.runId

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["runId"]
    ) -> MetaOapg.properties.runId: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["runId",], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["runId"]
    ) -> MetaOapg.properties.runId: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self, name: typing.Union[typing_extensions.Literal["runId",], str]
    ):
        return super().get_item_oapg(name)
    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        runId: typing.Union[
            MetaOapg.properties.runId,
            str,
            uuid.UUID,
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
    ) -> "SchemaFor200ResponseBodyApplicationJsonCharsetutf8":
        return super().__new__(
            cls,
            *_args,
            runId=runId,
            _configuration=_configuration,
            **kwargs,
        )

@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyApplicationJsonCharsetutf8,
    ]
    headers: schemas.Unset = schemas.unset

_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        "application/json": api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson
        ),
        "application/json; charset=utf-8": api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonCharsetutf8
        ),
    },
)
_all_accept_content_types = (
    "application/json",
    "application/json; charset=utf-8",
)

class BaseApi(api_client.Api):
    @typing.overload
    def _test_run_post_oapg(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def _test_run_post_oapg(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def _test_run_post_oapg(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _test_run_post_oapg(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...
    def _test_run_post_oapg(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: str = "application/json",
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Create a new test run from test results
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add("Accept", accept_content_type)

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                "The required body parameter has an invalid value of: unset. Set a valid value instead"
            )
        _fields = None
        _body = None
        serialized_data = request_body_any_type.serialize(body, content_type)
        _headers.add("Content-Type", content_type)
        if "fields" in serialized_data:
            _fields = serialized_data["fields"]
        elif "body" in serialized_data:
            _body = serialized_data["body"]
        response = self.api_client.call_api(
            resource_path=used_path,
            method="post".upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(
                response=response
            )
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(
                    response, self.api_client.configuration
                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response
                )

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response,
            )

        return api_response

class TestRunPost(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def test_run_post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def test_run_post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def test_run_post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def test_run_post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...
    def test_run_post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: str = "application/json",
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._test_run_post_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )

class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...
    def post(
        self,
        body: typing.Union[
            SchemaForRequestBodyApplicationJson,
            dict,
            frozendict.frozendict,
        ],
        content_type: str = "application/json",
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._test_run_post_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )
