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
from gentrace.model.test_run import TestRun

# Query params
RunIdSchema = schemas.UUIDSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'runId': typing.Union[RunIdSchema, str, uuid.UUID, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_run_id = api_client.QueryParameter(
    name="runId",
    style=api_client.ParameterStyle.FORM,
    schema=RunIdSchema,
    required=True,
    explode=True,
)


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def testRun() -> typing.Type['TestRun']:
                return TestRun
            
            
            class stats(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "total",
                        "failure",
                        "pending",
                        "done",
                    }
                    
                    class properties:
                        total = schemas.NumberSchema
                        pending = schemas.NumberSchema
                        failure = schemas.NumberSchema
                        done = schemas.NumberSchema
                        __annotations__ = {
                            "total": total,
                            "pending": pending,
                            "failure": failure,
                            "done": done,
                        }
                
                total: MetaOapg.properties.total
                failure: MetaOapg.properties.failure
                pending: MetaOapg.properties.pending
                done: MetaOapg.properties.done
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["pending"]) -> MetaOapg.properties.pending: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["failure"]) -> MetaOapg.properties.failure: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["done"]) -> MetaOapg.properties.done: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", "pending", "failure", "done", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["pending"]) -> MetaOapg.properties.pending: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["failure"]) -> MetaOapg.properties.failure: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["done"]) -> MetaOapg.properties.done: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", "pending", "failure", "done", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, ],
                    failure: typing.Union[MetaOapg.properties.failure, decimal.Decimal, int, float, ],
                    pending: typing.Union[MetaOapg.properties.pending, decimal.Decimal, int, float, ],
                    done: typing.Union[MetaOapg.properties.done, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'stats':
                    return super().__new__(
                        cls,
                        *_args,
                        total=total,
                        failure=failure,
                        pending=pending,
                        done=done,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "testRun": testRun,
                "stats": stats,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["testRun"]) -> 'TestRun': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stats"]) -> MetaOapg.properties.stats: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["testRun", "stats", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["testRun"]) -> typing.Union['TestRun', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stats"]) -> typing.Union[MetaOapg.properties.stats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["testRun", "stats", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        testRun: typing.Union['TestRun', schemas.Unset] = schemas.unset,
        stats: typing.Union[MetaOapg.properties.stats, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            testRun=testRun,
            stats=stats,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaFor200ResponseBodyApplicationJsonCharsetutf8(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def testRun() -> typing.Type['TestRun']:
                return TestRun
            
            
            class stats(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "total",
                        "failure",
                        "pending",
                        "done",
                    }
                    
                    class properties:
                        total = schemas.NumberSchema
                        pending = schemas.NumberSchema
                        failure = schemas.NumberSchema
                        done = schemas.NumberSchema
                        __annotations__ = {
                            "total": total,
                            "pending": pending,
                            "failure": failure,
                            "done": done,
                        }
                
                total: MetaOapg.properties.total
                failure: MetaOapg.properties.failure
                pending: MetaOapg.properties.pending
                done: MetaOapg.properties.done
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["pending"]) -> MetaOapg.properties.pending: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["failure"]) -> MetaOapg.properties.failure: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["done"]) -> MetaOapg.properties.done: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", "pending", "failure", "done", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["pending"]) -> MetaOapg.properties.pending: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["failure"]) -> MetaOapg.properties.failure: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["done"]) -> MetaOapg.properties.done: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", "pending", "failure", "done", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, ],
                    failure: typing.Union[MetaOapg.properties.failure, decimal.Decimal, int, float, ],
                    pending: typing.Union[MetaOapg.properties.pending, decimal.Decimal, int, float, ],
                    done: typing.Union[MetaOapg.properties.done, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'stats':
                    return super().__new__(
                        cls,
                        *_args,
                        total=total,
                        failure=failure,
                        pending=pending,
                        done=done,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "testRun": testRun,
                "stats": stats,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["testRun"]) -> 'TestRun': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stats"]) -> MetaOapg.properties.stats: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["testRun", "stats", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["testRun"]) -> typing.Union['TestRun', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stats"]) -> typing.Union[MetaOapg.properties.stats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["testRun", "stats", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        testRun: typing.Union['TestRun', schemas.Unset] = schemas.unset,
        stats: typing.Union[MetaOapg.properties.stats, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJsonCharsetutf8':
        return super().__new__(
            cls,
            *_args,
            testRun=testRun,
            stats=stats,
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
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonCharsetutf8),
    },
)
_all_accept_content_types = (
    'application/json',
    'application/json; charset=utf-8',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _test_run_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _test_run_get_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _test_run_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _test_run_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Get test run by ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_run_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class TestRunGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def test_run_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def test_run_get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def test_run_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def test_run_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._test_run_get_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._test_run_get_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


