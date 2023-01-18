import typing

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = typing.TypeVar("T")


class LinkHref(BaseModel):
    href: typing.Optional[str] = None


class PaginationLinks(BaseModel):
    self: typing.Optional[LinkHref] = None
    current: typing.Optional[LinkHref] = None
    next: typing.Optional[LinkHref] = None
    previous: typing.Optional[LinkHref] = None


class PaginatedResponse(GenericModel, typing.Generic[T]):
    results: typing.List[T]
    pageNumber: typing.Optional[int] = None
    pageSize: typing.Optional[int] = None
    totalResults: typing.Optional[int] = None
    links: PaginationLinks = Field(None, alias="_links")