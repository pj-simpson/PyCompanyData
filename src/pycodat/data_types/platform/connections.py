import datetime
import typing

from pydantic import BaseModel

from pycodat.data_types.pagination import PaginatedResponse


class DataConnectionError(BaseModel):
    statusCode: typing.Optional[str] = None
    erroredOnUtc: typing.Optional[datetime.datetime] = None
    statusText: typing.Optional[str] = None
    errorMessage: typing.Optional[str] = None


class DataConnection(BaseModel):
    id: str
    integrationId: str
    sourceId: str
    platformName: str
    linkUrl: str
    status: typing.Optional[str] = None
    created: typing.Optional[datetime.datetime] = None
    sourceType: typing.Optional[str] = None
    lastSync: typing.Optional[datetime.datetime] = None
    DataConnectionErrors: typing.Optional[typing.List[DataConnectionError]] = None


class DataConnectionPaginatedResponse(PaginatedResponse):
    results: typing.List[DataConnection] = []
