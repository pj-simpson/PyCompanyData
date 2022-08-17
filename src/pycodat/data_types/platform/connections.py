import datetime
import typing

from pydantic import BaseModel

from pycodat.data_types.platform.pagination import PaginatedResponse


class DataConnectionError(BaseModel):
    statusCode: str
    erroredOnUtc: datetime.datetime
    statusText: str = None
    errorMessage: str = None


class DataConnection(BaseModel):
    id: str
    integrationId: str
    sourceId: str
    platformName: str
    linkUrl: str
    status: str
    created: datetime.datetime = None
    sourceType: str
    lastSync: datetime.datetime = None
    DataConnectionErrors: typing.List[DataConnectionError] = None


class DataConnectionPaginatedResponse(PaginatedResponse):
    results: typing.List[DataConnection] = []
