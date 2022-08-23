import typing

from pydantic import BaseModel, Field


class LinkHref(BaseModel):
    href: typing.Optional[str] = None


class PaginationLinks(BaseModel):
    self: typing.Optional[LinkHref] = None
    current: typing.Optional[LinkHref] = None
    next: typing.Optional[LinkHref] = None
    previous: typing.Optional[LinkHref] = None


class PaginatedResponse(BaseModel):
    pageNumber: typing.Optional[int] = None
    pageSize: typing.Optional[int] = None
    totalResults: typing.Optional[int] = None
    links: PaginationLinks = Field(None, alias="_links")
