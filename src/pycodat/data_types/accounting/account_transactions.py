import datetime
from pydantic import BaseModel
import typing


class BankAccountRef(BaseModel):
    id: typing.Optional[str]
    name: typing.Optional[str]


class RecordRef(BaseModel):
    id: str
    dataType: typing.Optional[str]


class Line(BaseModel):
    description: str
    recordRef: RecordRef
    amount: int


class Metadata(BaseModel):
    isDeleted: bool


class AccountTransaction(BaseModel):
    id: typing.Optional[str]
    transactionId: typing.Optional[str]
    note: typing.Optional[str]
    bankAccountRef: BankAccountRef
    date: datetime.datetime
    status: str
    currency: typing.Optional[str]
    currencyRate: typing.Optional[int]
    lines: typing.Optional[typing.List[Line]]
    totalAmount: int
    modifiedDate: typing.Optional[datetime.datetime]
    sourceModifiedDate: typing.Optional[datetime.datetime]
    metadata: typing.Optional[Metadata]
