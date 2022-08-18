import datetime
import typing

from pydantic import BaseModel

from pycodat.data_types.platform.pagination import PaginatedResponse


class DataConnectionError(BaseModel):
    statusCode: str
    erroredOnUtc: datetime.datetime
    statusText: typing.Optional[str] = None
    errorMessage: typing.Optional[str] = None


class DataConnection(BaseModel):
    id: str
    integrationId: str
    sourceId: str
    platformName: str
    linkUrl: str
    status: str
    created: typing.Optional[datetime.datetime] = None
    sourceType: str
    lastSync: typing.Optional[datetime.datetime] = None
    DataConnectionErrors: typing.Optional[typing.List[DataConnectionError]] = None


class DataConnectionPaginatedResponse(PaginatedResponse):
    results: typing.List[DataConnection] = []
