import datetime
import typing

from pydantic import BaseModel


class DataTypeStatus(BaseModel):
    dataType: str
    lastSuccessfulSync: datetime.datetime
    currentStatus: str
    latestSyncId: str
    latestSuccessfulSyncId: str


class DataStatus(BaseModel):
    chartOfAccounts: typing.Optional[DataTypeStatus] = None
    bills: typing.Optional[DataTypeStatus] = None
    billPayments: typing.Optional[DataTypeStatus] = None
    company: typing.Optional[DataTypeStatus] = None
    creditNotes: typing.Optional[DataTypeStatus] = None
    customers: typing.Optional[DataTypeStatus] = None
    invoices: typing.Optional[DataTypeStatus] = None
    journals: typing.Optional[DataTypeStatus] = None
    journalEntries: typing.Optional[DataTypeStatus] = None
    payments: typing.Optional[DataTypeStatus] = None
    suppliers: typing.Optional[DataTypeStatus] = None
    balanceSheet: typing.Optional[DataTypeStatus] = None
    profitAndLoss: typing.Optional[DataTypeStatus] = None
    taxRates: typing.Optional[DataTypeStatus] = None
    items: typing.Optional[DataTypeStatus] = None
    bankAccounts: typing.Optional[DataTypeStatus] = None
    bankTransactions: typing.Optional[DataTypeStatus] = None
    billCreditNotes: typing.Optional[DataTypeStatus] = None
    trackingCategories: typing.Optional[DataTypeStatus] = None
    cashFlowStatement: typing.Optional[DataTypeStatus] = None
    purchaseOrders: typing.Optional[DataTypeStatus] = None
    accountTransactions: typing.Optional[DataTypeStatus] = None
    transfers: typing.Optional[DataTypeStatus] = None
    directCosts: typing.Optional[DataTypeStatus] = None
    directIncomes: typing.Optional[DataTypeStatus] = None
    paymentMethods: typing.Optional[DataTypeStatus] = None
    salesOrders: typing.Optional[DataTypeStatus] = None
