import typing

from pydantic import BaseModel, Field


class LinkHref(BaseModel):
    href: str


class PaginationLinks(BaseModel):
    self: LinkHref
    current: LinkHref
    next: typing.Optional[LinkHref] = None
    previous: typing.Optional[LinkHref] = None


class PaginatedResponse(BaseModel):
    pageNumber: typing.Optional[int] = None
    pageSize: typing.Optional[int] = None
    totalResults: typing.Optional[int] = None
    links: PaginationLinks = Field(None, alias="_links")
