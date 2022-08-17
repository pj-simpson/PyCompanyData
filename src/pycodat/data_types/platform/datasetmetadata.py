import typing

from pydantic import BaseModel

from .pagination import PaginatedResponse


class DataSetMetadata(BaseModel):
    id: str
    companyId: str
    connectionId: str
    dataType: str
    status: str
    errorMessage: str = None
    requested: str
    progress: int
    isCompleted: bool
    isErrored: bool


class DataSetMetaDataPaginatedResponse(PaginatedResponse):
    results: typing.List[DataSetMetadata] = []
