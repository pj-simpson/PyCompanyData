import datetime
import typing

from pydantic import BaseModel


class Address(BaseModel):
    type: typing.Optional[str]
    line1: typing.Optional[str]
    line2: typing.Optional[str]
    city: typing.Optional[str]
    region: typing.Optional[str]
    country: typing.Optional[str]
    postalCode: typing.Optional[str]


class Supplier(BaseModel):
    id: typing.Optional[str]
    supplierName: typing.Optional[str]
    contactName: typing.Optional[str]
    emailAddress: typing.Optional[str]
    phone: typing.Optional[str]
    addresses: typing.Optional[typing.List[Address]]
    registrationNumber: typing.Optional[str]
    taxNumber: typing.Optional[str]
    status: typing.Optional[str]
    modifiedDate: typing.Optional[datetime.datetime]
    sourceModifiedDate: typing.Optional[datetime.datetime]
    defaultCurrency: typing.Optional[str]
