import datetime
import typing

from pydantic import BaseModel

from pycodat.data_types.pagination import PaginatedResponse


class ValidDatatypeLink(BaseModel):
    property: typing.Optional[str]
    links: typing.Optional[typing.List[str]]


class Account(BaseModel):
    id: typing.Optional[str]
    nominalCode: typing.Optional[str]
    name: typing.Optional[str]
    description: typing.Optional[str]
    fullyQualifiedCategory: typing.Optional[str]
    fullyQualifiedName: typing.Optional[str]
    currency: typing.Optional[str]
    currentBalance: typing.Optional[int]
    type: str
    status: str
    isBankAccount: bool
    modifiedDate: typing.Optional[datetime.datetime]
    sourceModifiedDate: typing.Optional[datetime.datetime]
    validDatatypeLinks: typing.Optional[typing.List[ValidDatatypeLink]]


class AccountsPaginatedResponse(PaginatedResponse):
    results: typing.List[Account] = []
