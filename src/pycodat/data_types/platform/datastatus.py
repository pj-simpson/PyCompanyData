import datetime

from pydantic import BaseModel


class DataTypeStatus(BaseModel):
    dataType: str
    lastSuccessfulSync: datetime.datetime
    currentStatus: str
    latestSyncId: str
    latestSuccessfulSyncId: str


class DataStatus(BaseModel):
    chartOfAccounts: DataTypeStatus = None
    bills: DataTypeStatus = None
    billPayments: DataTypeStatus = None
    company: DataTypeStatus = None
    creditNotes: DataTypeStatus = None
    customers: DataTypeStatus = None
    invoices: DataTypeStatus = None
    journals: DataTypeStatus = None
    journalEntries: DataTypeStatus = None
    payments: DataTypeStatus = None
    suppliers: DataTypeStatus = None
    balanceSheet: DataTypeStatus = None
    profitAndLoss: DataTypeStatus = None
    taxRates: DataTypeStatus = None
    items: DataTypeStatus = None
    bankAccounts: DataTypeStatus = None
    bankTransactions: DataTypeStatus = None
    billCreditNotes: DataTypeStatus = None
    trackingCategories: DataTypeStatus = None
    cashFlowStatement: DataTypeStatus = None
    purchaseOrders: DataTypeStatus = None
    accountTransactions: DataTypeStatus = None
    transfers: DataTypeStatus = None
    directCosts: DataTypeStatus = None
    directIncomes: DataTypeStatus = None
    paymentMethods: DataTypeStatus = None
    salesOrders: DataTypeStatus = None
