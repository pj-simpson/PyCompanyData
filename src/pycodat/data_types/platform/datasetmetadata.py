import typing

from pydantic import BaseModel

from ..pagination import PaginatedResponse


class DataSetMetadata(BaseModel):
    id: str
    companyId: str
    connectionId: str
    dataType: typing.Optional[str] = None
    status: str
    errorMessage: typing.Optional[str] = None
    requested: str
    completed: typing.Optional[str] = None
    progress: int
    isCompleted: bool
    isErrored: bool
    validationinformationUrl: typing.Optional[str] = None


class DataSetMetaDataPaginatedResponse(PaginatedResponse):
    results: typing.List[DataSetMetadata] = []
