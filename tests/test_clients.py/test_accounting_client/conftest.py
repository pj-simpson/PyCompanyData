import datetime

import pytest

from pycodat.data_types.accounting.account_transactions import (
    AccountTransaction,
    AccountTransactionsPaginatedResponse,
    BankAccountRef,
    Line,
    Metadata,
    RecordRef,
)
from pycodat.data_types.accounting.accounts import Account, AccountsPaginatedResponse
from pycodat.data_types.pagination import LinkHref, PaginationLinks


@pytest.fixture
def accounts():
    def _accounts(*args, **kwargs):
        return AccountsPaginatedResponse(
            pageNumber=1,
            pageSize=100,
            totalResults=2,
            links=PaginationLinks(
                self=LinkHref(
                    href="/companies/a57d404d-30ec-45c2-b6a4-98d2877bb93e/data/accounts"
                ),
                current=LinkHref(
                    href="/companies/a57d404d-30ec-45c2-b6a4-98d2877bb93e/data/accounts"
                ),
                next=None,
                previous=None,
            ),
            results=[
                Account(
                    id="1b6266d1-1e44-46c5-8eb5-a8f98e03124e",
                    nominalCode="610",
                    name="Accounts Receivable",
                    description="Invoices the business has issued but has not yet collected payment on.",
                    fullyQualifiedCategory="Asset.Current",
                    fullyQualifiedName="Asset.Current.Accounts Receivable",
                    currency="GBP",
                    currentBalance=0,
                    type="Asset",
                    status="Active",
                    isBankAccount=False,
                    modifiedDate=datetime.datetime(
                        2022, 8, 15, 7, 49, 33, tzinfo=datetime.timezone.utc
                    ),
                    sourceModifiedDate=datetime.datetime(2021, 9, 22, 17, 28, 5),
                    validDatatypeLinks=[],
                ),
                Account(
                    id="76d5f23b-9623-4e3b-89cd-da57228764d3",
                    nominalCode="611",
                    name="Accounts Receivable",
                    description="A provision anticipating that a portion of accounts receivable will never be collected.",
                    fullyQualifiedCategory="Asset.Current",
                    fullyQualifiedName="Asset.Current.Accounts Receivable",
                    currency="GBP",
                    currentBalance=0,
                    type="Asset",
                    status="Active",
                    isBankAccount=False,
                    modifiedDate=datetime.datetime(
                        2022, 8, 15, 7, 49, 33, tzinfo=datetime.timezone.utc
                    ),
                    sourceModifiedDate=datetime.datetime(2021, 9, 4, 9, 49, 5),
                    validDatatypeLinks=[],
                ),
            ],
        )

    return _accounts


@pytest.fixture
def account():
    def _account(*args, **kwargs):
        return Account(
            id="1b6266d1-1e44-46c5-8eb5-a8f98e03124e",
            nominalCode="610",
            name="Accounts Receivable",
            description="Invoices the business has issued but has not yet collected payment on.",
            fullyQualifiedCategory="Asset.Current",
            fullyQualifiedName="Asset.Current.Accounts Receivable",
            currency="GBP",
            currentBalance=0,
            type="Asset",
            status="Active",
            isBankAccount=False,
            modifiedDate=datetime.datetime(
                2022, 8, 15, 7, 49, 33, tzinfo=datetime.timezone.utc
            ),
            sourceModifiedDate=datetime.datetime(2021, 9, 22, 17, 28, 5),
            validDatatypeLinks=[],
        )

    return _account


@pytest.fixture
def account_transactions():
    def _account_transactions(*args, **kwargs):
        return AccountTransactionsPaginatedResponse(
            pageNumber=1,
            pageSize=100,
            totalResults=170,
            links=PaginationLinks(
                self=LinkHref(
                    href="/companies/3582754a-2315-4209-967d-760e3914d116/connections/3582754a-2315-4209-967d-760e3914d116/data/accounttransactions"
                ),
                current=LinkHref(
                    href="/companies/3582754a-2315-4209-967d-760e3914d116/connections/3582754a-2315-4209-967d-760e3914d116/data/accounttransactions"
                ),
                next=LinkHref(
                    href="/companies/3582754a-2315-4209-967d-760e3914d116/connections/3582754a-2315-4209-967d-760e3914d116/data/accounttransactions?page=2&pageSize=100"
                ),
                previous=None,
            ),
            results=[
                AccountTransaction(
                    id="85",
                    transactionId="85",
                    note="Opening Balance from Bank",
                    bankAccountRef=BankAccountRef(id="57", name="Visa Credit Card"),
                    date=datetime.datetime(2019, 8, 21, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description="Opening Balance from Bank",
                            recordRef=RecordRef(id="PUR-85", dataType="directCosts"),
                            amount=-3831,
                        )
                    ],
                    totalAmount=-3831,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 21, 18, 13, 7, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="6",
                    transactionId="6",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2019, 12, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-6", dataType="directCosts"),
                            amount=-900,
                        )
                    ],
                    totalAmount=-900,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 9, 50, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="7",
                    transactionId="7",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2019, 12, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-7", dataType="directCosts"),
                            amount=-390,
                        )
                    ],
                    totalAmount=-390,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 10, 7, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="2",
                    transactionId="2",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2019, 12, 7, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-2", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 10, 20, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="3",
                    transactionId="3",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2019, 12, 9, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-3", dataType="directCosts"),
                            amount=-188,
                        )
                    ],
                    totalAmount=-188,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 10, 33, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="4",
                    transactionId="4",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2019, 12, 9, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-4", dataType="directCosts"),
                            amount=-63,
                        )
                    ],
                    totalAmount=-63,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 10, 47, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="21",
                    transactionId="21",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2019, 12, 14, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-21", dataType="directCosts"),
                            amount=-6000,
                        )
                    ],
                    totalAmount=-6000,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 11, 1, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="8",
                    transactionId="8",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 1, 7, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-8", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 11, 30, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="9",
                    transactionId="9",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 1, 7, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-9", dataType="directCosts"),
                            amount=-199,
                        )
                    ],
                    totalAmount=-199,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 11, 55, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="10",
                    transactionId="10",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 1, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-10", dataType="directCosts"),
                            amount=-61,
                        )
                    ],
                    totalAmount=-61,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 12, 10, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="11",
                    transactionId="11",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 1, 12, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-11", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 12, 25, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="135",
                    transactionId="135",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 1, 12, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-135", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 12, 45, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="158",
                    transactionId="158",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 2, 1, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=0,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="158", dataType="billPayments"),
                            amount=-7940,
                        )
                    ],
                    totalAmount=-7940,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 19, 36, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="159",
                    transactionId="159",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 2, 1, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=0,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="159", dataType="billPayments"),
                            amount=-742,
                        )
                    ],
                    totalAmount=-742,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 19, 49, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="33",
                    transactionId="33",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 2, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-33", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 13, 1, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="34",
                    transactionId="34",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 2, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-34", dataType="directCosts"),
                            amount=-224,
                        )
                    ],
                    totalAmount=-224,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 13, 18, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="35",
                    transactionId="35",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 2, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-35", dataType="directCosts"),
                            amount=-82,
                        )
                    ],
                    totalAmount=-82,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 13, 32, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="136",
                    transactionId="136",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 2, 11, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-136", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 13, 55, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="25",
                    transactionId="25",
                    note="",
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 2, 21, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description="",
                            recordRef=RecordRef(id="25", dataType="payments"),
                            amount=10800,
                        )
                    ],
                    totalAmount=10800,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 21, 16, 42, 8, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="31",
                    transactionId="31",
                    note="",
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 2, 21, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description="",
                            recordRef=RecordRef(id="31", dataType="payments"),
                            amount=15615,
                        )
                    ],
                    totalAmount=15615,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 21, 16, 50, 17, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="36",
                    transactionId="36",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 3, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-36", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 14, 11, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="37",
                    transactionId="37",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 3, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-37", dataType="directCosts"),
                            amount=-257,
                        )
                    ],
                    totalAmount=-257,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 14, 26, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="38",
                    transactionId="38",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 3, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-38", dataType="directCosts"),
                            amount=-106,
                        )
                    ],
                    totalAmount=-106,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 14, 46, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="88",
                    transactionId="88",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 3, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-88", dataType="directCosts"),
                            amount=-328,
                        )
                    ],
                    totalAmount=-328,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 15, 3, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="137",
                    transactionId="137",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 3, 13, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-137", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 16, 12, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="92",
                    transactionId="92",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 3, 13, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-92", dataType="directCosts"),
                            amount=-840,
                        )
                    ],
                    totalAmount=-840,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 15, 27, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="94",
                    transactionId="94",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 3, 13, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-94", dataType="directCosts"),
                            amount=-900,
                        )
                    ],
                    totalAmount=-900,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 15, 48, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="56",
                    transactionId="56",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 3, 18, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-56", dataType="directCosts"),
                            amount=-900,
                        )
                    ],
                    totalAmount=-900,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 16, 40, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="233",
                    transactionId="233",
                    note=None,
                    bankAccountRef=BankAccountRef(id="85", name="Credit Card"),
                    date=datetime.datetime(2020, 3, 31, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-233", dataType="directCosts"),
                            amount=-1,
                        )
                    ],
                    totalAmount=-1,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 2, 17, 16, 32, 15, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="39",
                    transactionId="39",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 4, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-39", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 16, 56, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="40",
                    transactionId="40",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 4, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-40", dataType="directCosts"),
                            amount=-305,
                        )
                    ],
                    totalAmount=-305,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 17, 11, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="41",
                    transactionId="41",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 4, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-41", dataType="directCosts"),
                            amount=-110,
                        )
                    ],
                    totalAmount=-110,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 17, 28, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="138",
                    transactionId="138",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 4, 13, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-138", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 17, 48, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="102",
                    transactionId="102",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 4, 18, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-102", dataType="directCosts"),
                            amount=-1470,
                        )
                    ],
                    totalAmount=-1470,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 18, 37, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="62",
                    transactionId="62",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 4, 18, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-62", dataType="directCosts"),
                            amount=-444,
                        )
                    ],
                    totalAmount=-444,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 18, 6, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="97",
                    transactionId="97",
                    note="",
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 4, 18, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description="",
                            recordRef=RecordRef(id="97", dataType="payments"),
                            amount=4423,
                        )
                    ],
                    totalAmount=4423,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 21, 18, 38, 30, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="98",
                    transactionId="98",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 4, 18, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-98", dataType="directCosts"),
                            amount=-766,
                        )
                    ],
                    totalAmount=-766,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 18, 22, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="66",
                    transactionId="66",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 5, 2, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-66", dataType="directCosts"),
                            amount=-1275,
                        )
                    ],
                    totalAmount=-1275,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 18, 54, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="68",
                    transactionId="68",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 5, 2, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-68", dataType="directCosts"),
                            amount=-1200,
                        )
                    ],
                    totalAmount=-1200,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 21, 29, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="42",
                    transactionId="42",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 5, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-42", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 21, 45, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="43",
                    transactionId="43",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 5, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-43", dataType="directCosts"),
                            amount=-332,
                        )
                    ],
                    totalAmount=-332,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 22, 1, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="44",
                    transactionId="44",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 5, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-44", dataType="directCosts"),
                            amount=-108,
                        )
                    ],
                    totalAmount=-108,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 22, 16, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="139",
                    transactionId="139",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 5, 11, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-139", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 22, 43, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="105",
                    transactionId="105",
                    note="",
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 5, 16, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description="",
                            recordRef=RecordRef(id="105", dataType="payments"),
                            amount=3970,
                        )
                    ],
                    totalAmount=3970,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 21, 18, 42, 8, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="71",
                    transactionId="71",
                    note="",
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 5, 26, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description="",
                            recordRef=RecordRef(id="71", dataType="payments"),
                            amount=9859,
                        )
                    ],
                    totalAmount=9859,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 21, 17, 33, 25, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="72",
                    transactionId="72",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 6, 2, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-72", dataType="directCosts"),
                            amount=-889,
                        )
                    ],
                    totalAmount=-889,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 22, 59, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="45",
                    transactionId="45",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 6, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-45", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 23, 22, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="46",
                    transactionId="46",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 6, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-46", dataType="directCosts"),
                            amount=-299,
                        )
                    ],
                    totalAmount=-299,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 23, 40, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="47",
                    transactionId="47",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 6, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-47", dataType="directCosts"),
                            amount=-98,
                        )
                    ],
                    totalAmount=-98,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 23, 58, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="76",
                    transactionId="76",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 6, 9, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-76", dataType="directCosts"),
                            amount=-4500,
                        )
                    ],
                    totalAmount=-4500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 24, 20, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="78",
                    transactionId="78",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 6, 9, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-78", dataType="directCosts"),
                            amount=-1200,
                        )
                    ],
                    totalAmount=-1200,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 24, 39, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="140",
                    transactionId="140",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 6, 11, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-140", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 25, 2, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="57",
                    transactionId="57",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 6, 16, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-57", dataType="directCosts"),
                            amount=-900,
                        )
                    ],
                    totalAmount=-900,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 25, 20, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="81",
                    transactionId="81",
                    note="",
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 6, 29, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description="",
                            recordRef=RecordRef(id="81", dataType="payments"),
                            amount=10859,
                        )
                    ],
                    totalAmount=10859,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 21, 17, 39, 46, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="48",
                    transactionId="48",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 7, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-48", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 25, 35, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="49",
                    transactionId="49",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 7, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-49", dataType="directCosts"),
                            amount=-269,
                        )
                    ],
                    totalAmount=-269,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 25, 49, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="50",
                    transactionId="50",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 7, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-50", dataType="directCosts"),
                            amount=-89,
                        )
                    ],
                    totalAmount=-89,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 26, 4, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="141",
                    transactionId="141",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 7, 11, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-141", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 26, 33, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="106",
                    transactionId="106",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 7, 21, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-106", dataType="directCosts"),
                            amount=-1642,
                        )
                    ],
                    totalAmount=-1642,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 27, 50, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="110",
                    transactionId="110",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 7, 31, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-110", dataType="directCosts"),
                            amount=-4500,
                        )
                    ],
                    totalAmount=-4500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 28, 11, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="51",
                    transactionId="51",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 8, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-51", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 28, 29, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="52",
                    transactionId="52",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 8, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-52", dataType="directCosts"),
                            amount=-253,
                        )
                    ],
                    totalAmount=-253,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 28, 48, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="53",
                    transactionId="53",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 8, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-53", dataType="directCosts"),
                            amount=-81,
                        )
                    ],
                    totalAmount=-81,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 29, 10, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="86",
                    transactionId="86",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 8, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-86", dataType="directCosts"),
                            amount=-1000,
                        )
                    ],
                    totalAmount=-1000,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 30, 23, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="87",
                    transactionId="87",
                    note=None,
                    bankAccountRef=BankAccountRef(id="57", name="Visa Credit Card"),
                    date=datetime.datetime(2020, 8, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-87", dataType="directCosts"),
                            amount=-245,
                        )
                    ],
                    totalAmount=-245,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 21, 20, 53, 39, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="134",
                    transactionId="134",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 8, 11, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-134", dataType="directCosts"),
                            amount=-1000,
                        )
                    ],
                    totalAmount=-1000,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 30, 48, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="142",
                    transactionId="142",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 8, 11, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-142", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 31, 7, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="113",
                    transactionId="113",
                    note="",
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 8, 20, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description="",
                            recordRef=RecordRef(id="113", dataType="payments"),
                            amount=9999,
                        )
                    ],
                    totalAmount=9999,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 21, 18, 48, 26, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="154",
                    transactionId="154",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 8, 31, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-154", dataType="directCosts"),
                            amount=-500,
                        )
                    ],
                    totalAmount=-500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 52, 42, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="115",
                    transactionId="115",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 9, 2, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-115", dataType="directCosts"),
                            amount=-2625,
                        )
                    ],
                    totalAmount=-2625,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 3, 25, 9, 19, 30, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="54",
                    transactionId="54",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 9, 5, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-54", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 56, 3, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="55",
                    transactionId="55",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 9, 5, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-55", dataType="directCosts"),
                            amount=-240,
                        )
                    ],
                    totalAmount=-240,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 56, 19, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="143",
                    transactionId="143",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 9, 10, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-143", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 57, 13, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="155",
                    transactionId="155",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 9, 15, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-155", dataType="directCosts"),
                            amount=-500,
                        )
                    ],
                    totalAmount=-500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 22, 0, 47, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="58",
                    transactionId="58",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 9, 15, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-58", dataType="directCosts"),
                            amount=-900,
                        )
                    ],
                    totalAmount=-900,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 9, 22, 21, 58, 28, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="118",
                    transactionId="118",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 9, 20, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-118", dataType="directCosts"),
                            amount=-15000,
                        )
                    ],
                    totalAmount=-15000,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 3, 25, 9, 19, 30, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="120",
                    transactionId="120",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 9, 20, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-120", dataType="directCosts"),
                            amount=-3000,
                        )
                    ],
                    totalAmount=-3000,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 3, 25, 9, 19, 30, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="122",
                    transactionId="122",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 9, 20, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-122", dataType="directCosts"),
                            amount=-900,
                        )
                    ],
                    totalAmount=-900,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 3, 25, 9, 19, 30, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="164",
                    transactionId="164",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 10, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-164", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 11, 15, 10, 10, 21, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="165",
                    transactionId="165",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 10, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-165", dataType="directCosts"),
                            amount=-255,
                        )
                    ],
                    totalAmount=-255,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 11, 15, 15, 9, 6, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="166",
                    transactionId="166",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 10, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-166", dataType="directCosts"),
                            amount=-85,
                        )
                    ],
                    totalAmount=-85,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 11, 15, 15, 10, 15, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="167",
                    transactionId="167",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 10, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-167", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 11, 15, 15, 10, 23, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="168",
                    transactionId="168",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 11, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-168", dataType="directCosts"),
                            amount=-1500,
                        )
                    ],
                    totalAmount=-1500,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 11, 15, 15, 10, 34, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="169",
                    transactionId="169",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 11, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-169", dataType="directCosts"),
                            amount=-240,
                        )
                    ],
                    totalAmount=-240,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 11, 15, 15, 10, 49, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="170",
                    transactionId="170",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 11, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-170", dataType="directCosts"),
                            amount=-92,
                        )
                    ],
                    totalAmount=-92,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 11, 15, 15, 11, 1, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="171",
                    transactionId="171",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 11, 6, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-171", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 11, 15, 15, 11, 6, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="172",
                    transactionId="172",
                    note="",
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 11, 11, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description="",
                            recordRef=RecordRef(id="172", dataType="payments"),
                            amount=7800,
                        )
                    ],
                    totalAmount=7800,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 11, 12, 10, 26, 29, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="178",
                    transactionId="178",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 12, 11, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-178", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 12, 12, 0, 26, 9, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="179",
                    transactionId="179",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2020, 12, 13, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-179", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2020, 12, 14, 0, 27, 45, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="191",
                    transactionId="191",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 8, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-191", dataType="directCosts"),
                            amount=-68,
                        )
                    ],
                    totalAmount=-68,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 18, 3, 30, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="183",
                    transactionId="183",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 9, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-183", dataType="directCosts"),
                            amount=-63,
                        )
                    ],
                    totalAmount=-63,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 17, 48, 4, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="192",
                    transactionId="192",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 9, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-192", dataType="directCosts"),
                            amount=-18,
                        )
                    ],
                    totalAmount=-18,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 18, 3, 32, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="184",
                    transactionId="184",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 10, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-184", dataType="directCosts"),
                            amount=-32,
                        )
                    ],
                    totalAmount=-32,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 17, 48, 5, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="185",
                    transactionId="185",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 12, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-185", dataType="directCosts"),
                            amount=-59,
                        )
                    ],
                    totalAmount=-59,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 17, 48, 6, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="186",
                    transactionId="186",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 12, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-186", dataType="directCosts"),
                            amount=-85,
                        )
                    ],
                    totalAmount=-85,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 17, 48, 7, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="193",
                    transactionId="193",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 12, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-193", dataType="directCosts"),
                            amount=-37,
                        )
                    ],
                    totalAmount=-37,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 18, 3, 33, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="182",
                    transactionId="182",
                    note=None,
                    bankAccountRef=BankAccountRef(id="81", name="Current"),
                    date=datetime.datetime(2021, 1, 13, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-182", dataType="directCosts"),
                            amount=-471,
                        )
                    ],
                    totalAmount=-471,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 13, 0, 33, 42, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="187",
                    transactionId="187",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 13, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-187", dataType="directCosts"),
                            amount=-95,
                        )
                    ],
                    totalAmount=-95,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 17, 48, 8, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="194",
                    transactionId="194",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 13, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-194", dataType="directCosts"),
                            amount=-68,
                        )
                    ],
                    totalAmount=-68,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 18, 3, 34, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
                AccountTransaction(
                    id="195",
                    transactionId="195",
                    note=None,
                    bankAccountRef=BankAccountRef(id="83", name="Divvy Card Account"),
                    date=datetime.datetime(2021, 1, 13, 0, 0),
                    status="Unknown",
                    currency="GBP",
                    currencyRate=1,
                    lines=[
                        Line(
                            description=None,
                            recordRef=RecordRef(id="PUR-195", dataType="directCosts"),
                            amount=-71,
                        )
                    ],
                    totalAmount=-71,
                    modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
                    sourceModifiedDate=datetime.datetime(
                        2021, 1, 14, 18, 3, 35, tzinfo=datetime.timezone.utc
                    ),
                    metadata=Metadata(isDeleted=False),
                ),
            ],
        )

    return _account_transactions


@pytest.fixture
def account_transaction():
    def _account_transaction(*args, **kwargs):
        return AccountTransaction(
            id="85",
            transactionId="85",
            note="Opening Balance from Bank",
            bankAccountRef=BankAccountRef(id="57", name="Visa Credit Card"),
            date=datetime.datetime(2019, 8, 21, 0, 0),
            status="Unknown",
            currency="GBP",
            currencyRate=1,
            lines=[
                Line(
                    description="Opening Balance from Bank",
                    recordRef=RecordRef(id="PUR-85", dataType="directCosts"),
                    amount=-3831,
                )
            ],
            totalAmount=-3831,
            modifiedDate=datetime.datetime(2022, 7, 15, 14, 19, 8),
            sourceModifiedDate=datetime.datetime(
                2020, 9, 21, 18, 13, 7, tzinfo=datetime.timezone.utc
            ),
            metadata=Metadata(isDeleted=False),
        )

    return _account_transaction
