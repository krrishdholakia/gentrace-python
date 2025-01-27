# coding: utf-8

"""
    Gentrace API

    These API routes are designed to ingest events from clients.  # noqa: E501

    The version of the OpenAPI document: 0.11.0
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


class Pipeline(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "organizationId",
            "createdAt",
            "cases",
            "id",
            "slug",
            "labels",
            "updatedAt",
        }
        
        class properties:
            id = schemas.UUIDSchema
            createdAt = schemas.DateTimeSchema
            updatedAt = schemas.DateTimeSchema
            
            
            class cases(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TestCase']:
                        return TestCase
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TestCase'], typing.List['TestCase']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cases':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TestCase':
                    return super().__getitem__(i)
            
            
            class labels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'labels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            slug = schemas.StrSchema
            organizationId = schemas.StrSchema
            
            
            class archivedAt(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'archivedAt':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class displayName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'displayName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class branch(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'branch':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "cases": cases,
                "labels": labels,
                "slug": slug,
                "organizationId": organizationId,
                "archivedAt": archivedAt,
                "displayName": displayName,
                "branch": branch,
            }
    
    organizationId: MetaOapg.properties.organizationId
    createdAt: MetaOapg.properties.createdAt
    cases: MetaOapg.properties.cases
    id: MetaOapg.properties.id
    slug: MetaOapg.properties.slug
    labels: MetaOapg.properties.labels
    updatedAt: MetaOapg.properties.updatedAt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cases"]) -> MetaOapg.properties.cases: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationId"]) -> MetaOapg.properties.organizationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archivedAt"]) -> MetaOapg.properties.archivedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branch"]) -> MetaOapg.properties.branch: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "createdAt", "updatedAt", "cases", "labels", "slug", "organizationId", "archivedAt", "displayName", "branch", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cases"]) -> MetaOapg.properties.cases: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationId"]) -> MetaOapg.properties.organizationId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archivedAt"]) -> typing.Union[MetaOapg.properties.archivedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branch"]) -> typing.Union[MetaOapg.properties.branch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "createdAt", "updatedAt", "cases", "labels", "slug", "organizationId", "archivedAt", "displayName", "branch", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        organizationId: typing.Union[MetaOapg.properties.organizationId, str, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, datetime, ],
        cases: typing.Union[MetaOapg.properties.cases, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        slug: typing.Union[MetaOapg.properties.slug, str, ],
        labels: typing.Union[MetaOapg.properties.labels, list, tuple, ],
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, datetime, ],
        archivedAt: typing.Union[MetaOapg.properties.archivedAt, None, str, datetime, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, None, str, schemas.Unset] = schemas.unset,
        branch: typing.Union[MetaOapg.properties.branch, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Pipeline':
        return super().__new__(
            cls,
            *_args,
            organizationId=organizationId,
            createdAt=createdAt,
            cases=cases,
            id=id,
            slug=slug,
            labels=labels,
            updatedAt=updatedAt,
            archivedAt=archivedAt,
            displayName=displayName,
            branch=branch,
            _configuration=_configuration,
            **kwargs,
        )

from gentrace.model.test_case import TestCase
