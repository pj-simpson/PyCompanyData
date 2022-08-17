import typing

from pydantic import BaseModel, Field


class LinkHref(BaseModel):
    href: str


class PaginationLinks(BaseModel):
    self: LinkHref
    current: LinkHref
    next: LinkHref = None
    previous: LinkHref = None


class PaginatedResponse(BaseModel):
    pageNumber: int = None
    pageSize: int = None
    totalResults: int = None
    links: PaginationLinks = Field(None, alias="_links")
