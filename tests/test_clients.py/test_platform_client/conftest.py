import datetime
import uuid

import pytest

from pycodat.data_types.platform.company import Company, CompanyPaginatedResponse
from pycodat.data_types.platform.connections import (
    DataConnection,
    DataConnectionError,
    DataConnectionPaginatedResponse,
)
from pycodat.data_types.platform.datasetmetadata import (
    DataSetMetadata,
    DataSetMetaDataPaginatedResponse,
)
from pycodat.data_types.platform.datastatus import DataStatus, DataTypeStatus
from pycodat.data_types.platform.exceptions import CodatException
from pycodat.data_types.pagination import LinkHref, PaginationLinks
from pycodat.data_types.platform.syncsettings import SyncSetting, SyncSettings
from pycodat.rest_adapter import RestAdapter


@pytest.fixture
def companies():
    def _companies(*args, **kwargs):
        return CompanyPaginatedResponse(
            pageNumber=1,
            pageSize=100,
            totalResults=661,
            links=PaginationLinks(
                self=LinkHref(href="/companies/"),
                current=LinkHref(href="/companies/"),
                next=LinkHref(href="/companies/?page=2&pageSize=100"),
                previous=None,
            ),
            results=[
                Company(
                    id="bd40f311-761a-41b0-b295-c295c8213e16",
                    name="__ Bug 6512 __",
                    platform="QuickBooks Online",
                    redirect="https://link.codat.io/company/bd40f311-761a-41b0-b295-c295c8213e16",
                    created=datetime.datetime(
                        2019, 10, 22, 9, 25, 39, tzinfo=datetime.timezone.utc
                    ),
                    lastSync="2020-09-02T07:41:29.41Z",
                    dataConnections=[
                        DataConnection(
                            id="a66445bb-2c98-441b-a26d-87b3389fcf08",
                            integrationId="adeb7fe9-4c64-4848-9e0d-175317876b6f",
                            sourceId="d3a7993f-8165-46ef-8c61-f3c06c3ef88a",
                            platformName="QuickBooks Online",
                            linkUrl="https://link-api.codat.io/companies/bd40f311-761a-41b0-b295-c295c8213e16/connections/a66445bb-2c98-441b-a26d-87b3389fcf08/start",
                            status="Deauthorized",
                            created=datetime.datetime(
                                2019, 10, 22, 9, 26, tzinfo=datetime.timezone.utc
                            ),
                            sourceType="Accounting",
                            lastSync=datetime.datetime(
                                2020,
                                9,
                                2,
                                7,
                                41,
                                29,
                                410041,
                                tzinfo=datetime.timezone.utc,
                            ),
                            DataConnectionErrors=None,
                        )
                    ],
                    createdByUserName=None,
                    key="",
                    env="",
                ),
                Company(
                    id="bb304911-b193-4a27-bab9-69ab70b1d2f1",
                    name="__ Bug 7027 __",
                    platform="Xero",
                    redirect="https://link.codat.io/company/bb304911-b193-4a27-bab9-69ab70b1d2f1",
                    created=None,
                    lastSync="2020-02-11T09:39:38.0833333Z",
                    dataConnections=[
                        DataConnection(
                            id="5e4c5583-1924-450a-9310-65ca22c115eb",
                            integrationId="0f20c943-12d0-4800-9f6c-d218f62d494c",
                            sourceId="8a156a5a-39cb-4f9d-856e-76ef9b9a9607",
                            platformName="Xero",
                            linkUrl="https://link-api.codat.io/companies/bb304911-b193-4a27-bab9-69ab70b1d2f1/connections/5e4c5583-1924-450a-9310-65ca22c115eb/start",
                            status="Deauthorized",
                            created=None,
                            sourceType="Accounting",
                            lastSync=datetime.datetime(
                                2020,
                                2,
                                11,
                                9,
                                39,
                                37,
                                839172,
                                tzinfo=datetime.timezone.utc,
                            ),
                            DataConnectionErrors=None,
                        )
                    ],
                    createdByUserName=None,
                    key="",
                    env="",
                ),
            ],
        )

    return _companies


@pytest.fixture
def company():
    def _company(*args, **kwargs):
        return Company(
            id="14ae05f4-0b45-40f2-9da0-f45148b66219",
            name="Sandbox 2",
            platform="Sandbox",
            redirect="https://link-uat.codat.io/company/14ae05f4-0b45-40f2-9da0-f45148b66219",
            dataConnections=[
                DataConnection(
                    id="a8b32eac-0370-4e4b-bbb7-75ed0b3ce1aa",
                    integrationId="fbcbc488-be85-43fa-92dd-959047fc7765",
                    sourceId="0bd6e161-5534-408a-b945-ff21f2fcf4215",
                    platformName="Sandbox",
                    linkUrl="https://link-api-uat.codat.io/companies/8236e5a1-8876-47d6-8aa9-3558a0cf55d8/connections/905f4e47-bfd6-4cf9-a83d-d98cfb8ad83f/start",
                    status="Linked",
                    created="2022-07-19T15:19:15Z",
                    sourceType="Accounting",
                    lastSync="2022-07-19T15:19:15Z",
                    DataConnectionErrors=[
                        DataConnectionError(
                            statusCode="401",
                            statusText="An Error",
                            errorMessage="An Error 2",
                            erroredOnUtc="2022-08-13T09:03:23.533Z",
                        )
                    ],
                )
            ],
            created="2022-07-19T15:18:48Z",
            lastSync="2022-08-13T09:03:23.533Z",
            createdByUserName="Peter Simpson",
        )

    return _company


@pytest.fixture
def connections():
    def _connections(*args, **kwargs):
        return DataConnectionPaginatedResponse(
            results=[
                DataConnection(
                    id="a66445bb-2c98-441b-a26d-87b3389fcf08",
                    integrationId="adeb7fe9-4c64-4848-9e0d-175317876b6f",
                    sourceId="d3a7993f-8165-46ef-8c61-f3c06c3ef88a",
                    platformName="QuickBooks Online",
                    linkUrl="https://link-api.codat.io/companies/bd40f311-761a-41b0-b295-c295c8213e16/connections/a66445bb-2c98-441b-a26d-87b3389fcf08/start",
                    status="Deauthorized",
                    created=datetime.datetime(
                        2019, 10, 22, 9, 26, tzinfo=datetime.timezone.utc
                    ),
                    sourceType="Accounting",
                    lastSync=datetime.datetime(
                        2020, 9, 2, 7, 41, 29, 410041, tzinfo=datetime.timezone.utc
                    ),
                    DataConnectionErrors=None,
                )
            ],
            pageNumber=1,
            pageSize=100,
            totalResults=1,
        )

    return _connections


@pytest.fixture
def connection():
    def _connection(*args, **kwargs):
        return DataConnection(
            id="a66445bb-2c98-441b-a26d-87b3389fcf08",
            integrationId="adeb7fe9-4c64-4848-9e0d-175317876b6f",
            sourceId="d3a7993f-8165-46ef-8c61-f3c06c3ef88a",
            platformName="QuickBooks Online",
            linkUrl="https://link-api.codat.io/companies/bd40f311-761a-41b0-b295-c295c8213e16/connections/a66445bb-2c98-441b-a26d-87b3389fcf08/start",
            status="Deauthorized",
            created=datetime.datetime(
                2019, 10, 22, 9, 26, tzinfo=datetime.timezone.utc
            ),
            sourceType="Accounting",
            lastSync=datetime.datetime(
                2020, 9, 2, 7, 41, 29, 410041, tzinfo=datetime.timezone.utc
            ),
            DataConnectionErrors=None,
        )

    return _connection


@pytest.fixture
def data_sets():
    def _data_sets(*args, **kwargs):
        return DataSetMetaDataPaginatedResponse(
            results=[
                DataSetMetadata(
                    id="49092cf7-ae8c-4c29-8fdf-21e006027c89",
                    companyId="bd40f311-761a-41b0-b295-c295c8213e16",
                    connectionId="a66445bb-2c98-441b-a26d-87b3389fcf08",
                    dataType="profitAndLoss",
                    status="Complete",
                    errorMessage=None,
                    requested="2020-08-28T17:34:37.6965052Z",
                    progress=100,
                    isCompleted=True,
                    isErrored=False,
                )
            ],
            pageNumber=1,
            pageSize=100,
            totalResults=1,
        )

    return _data_sets


@pytest.fixture
def data_set():
    def _data_set(*args, **kwargs):
        return DataSetMetadata(
            id="49092cf7-ae8c-4c29-8fdf-21e006027c89",
            companyId="bd40f311-761a-41b0-b295-c295c8213e16",
            connectionId="a66445bb-2c98-441b-a26d-87b3389fcf08",
            dataType="profitAndLoss",
            status="Complete",
            errorMessage=None,
            requested="2020-08-28T17:34:37.6965052Z",
            progress=100,
            isCompleted=True,
            isErrored=False,
        )

    return _data_set


@pytest.fixture
def sync_settings():
    def _sync_settings(*args, **kwargs):
        return SyncSettings(
            companyId="bd40f311-761a-41b0-b295-c295c8213e16",
            settings=[
                SyncSetting(
                    dataType="chartOfAccounts",
                    fetchOnFirstLink=True,
                    syncSchedule=720,
                    syncOrder=1,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="bills",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=8,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="billPayments",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=9,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="company",
                    fetchOnFirstLink=True,
                    syncSchedule=720,
                    syncOrder=0,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="creditNotes",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=5,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="customers",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=3,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="invoices",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=4,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="journals",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=40,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="journalEntries",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=15,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="payments",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=6,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="suppliers",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=7,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="bankStatements",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=13,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="balanceSheet",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=10,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=24,
                ),
                SyncSetting(
                    dataType="profitAndLoss",
                    fetchOnFirstLink=True,
                    syncSchedule=24,
                    syncOrder=11,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=24,
                ),
                SyncSetting(
                    dataType="taxRates",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=2,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="items",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=14,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="bankAccounts",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=2,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="bankTransactions",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=3,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="billCreditNotes",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=18,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="trackingCategories",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=20,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="cashFlowStatement",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=7,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="purchaseOrders",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=22,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="accountTransactions",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=28,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="transfers",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=29,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="directCosts",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=30,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="directIncomes",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=31,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="paymentMethods",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=35,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="salesOrders",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=43,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="banking-accountBalances",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=36,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="banking-accounts",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=37,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="banking-transactionCategories",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=38,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="banking-transactions",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=39,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-orders",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=23,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-products",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=24,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-customers",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=27,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-disputes",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=25,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-transactions",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=26,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-paymentMethods",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=41,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-payments",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=27,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-companyInfo",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=32,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-locations",
                    fetchOnFirstLink=True,
                    syncSchedule=0,
                    syncOrder=34,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
                SyncSetting(
                    dataType="commerce-taxComponents",
                    fetchOnFirstLink=False,
                    syncSchedule=0,
                    syncOrder=42,
                    syncFromUtc=None,
                    syncFromWindow=None,
                    monthsToSync=None,
                ),
            ],
            overridesDefaults=True,
        )

    return _sync_settings


@pytest.fixture
def data_status():
    def _datastatus(*args, **kwargs):
        return DataStatus(
            chartOfAccounts=DataTypeStatus(
                dataType="chartOfAccounts",
                lastSuccessfulSync=datetime.datetime(
                    2020, 9, 1, 19, 33, 9, 547111, tzinfo=datetime.timezone.utc
                ),
                currentStatus="AuthError",
                latestSyncId="ae42ec88-a090-4e30-85f7-05feb7ea3fb2",
                latestSuccessfulSyncId="692ef0fe-eb0d-4fad-b226-e841ccaa3a21",
            ),
            bills=DataTypeStatus(
                dataType="bills",
                lastSuccessfulSync=datetime.datetime(
                    2020, 9, 1, 19, 33, 11, 344033, tzinfo=datetime.timezone.utc
                ),
                currentStatus="AuthError",
                latestSyncId="25085113-24a3-49eb-83b9-15ce63b84c24",
                latestSuccessfulSyncId="f5597550-b5fd-42f8-994b-3b8156f0cc59",
            ),
            billPayments=DataTypeStatus(
                dataType="billPayments",
                lastSuccessfulSync=datetime.datetime(
                    2020, 9, 1, 19, 33, 10, 108916, tzinfo=datetime.timezone.utc
                ),
                currentStatus="AuthError",
                latestSyncId="78786a14-51f4-4c08-b520-c0be56c0c1b1",
                latestSuccessfulSyncId="2a0c9996-7a7a-4ed8-9daf-9ca890925265",
            ),
            company=DataTypeStatus(
                dataType="company",
                lastSuccessfulSync=datetime.datetime(
                    2020, 9, 1, 19, 33, 8, 343578, tzinfo=datetime.timezone.utc
                ),
                currentStatus="AuthError",
                latestSyncId="9d098dc7-3564-4307-b66d-a8b2cdb3b7f9",
                latestSuccessfulSyncId="185b52fc-4bdd-4678-8c31-b85f72b4e697",
            ),
        )

    return _datastatus
