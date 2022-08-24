import datetime
from pycodat.data_types.accounting.account_transactions import (
    AccountTransaction,
    BankAccountRef,
    Line,
    Metadata,
    RecordRef,
)

import pytest

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
