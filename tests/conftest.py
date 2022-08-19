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
from pycodat.data_types.platform.pagination import LinkHref, PaginationLinks
from pycodat.data_types.platform.syncsettings import SyncSetting, SyncSettings
from pycodat.rest_adapter import RestAdapter


@pytest.fixture
def basic_auth_key(scope="session"):
    return "CX6U9lovZSSNQhSRUqJpSIbDs1O2IjrNp75fyBEq"


@pytest.fixture
def encoded_auth_key(scope="session"):
    return "Q1g2VTlsb3ZaU1NOUWhTUlVxSnBTSWJEczFPMklqck5wNzVmeUJFcQ=="


@pytest.fixture(autouse=True)
def dev_env_setup(monkeypatch):
    monkeypatch.setenv("CODAT_DEV_ENV", "something.com")


@pytest.fixture
def basic_rest_adapter(encoded_auth_key, scope="class"):
    rest_adapter = RestAdapter("prod", encoded_auth_key)
    return rest_adapter


class MockSuccessResponse:

    status_code = 201

    url = "https://api.codat.io/somepath/?me=thing&you=0"

    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

    @staticmethod
    def raise_for_status():
        return None


class Mock404Response:

    status_code = 404

    @staticmethod
    def raise_for_status():
        raise CodatException

    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.fixture
def mock_successful_get():
    def _mock_successful_get(*args, **kwargs):
        mock_success_response = MockSuccessResponse()
        return mock_success_response

    return _mock_successful_get


@pytest.fixture
def mock_404_get():
    def _mock_404_get(*args, **kwargs):
        mock_404_response = Mock404Response()
        return mock_404_response

    return _mock_404_get


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
def companies_raw_json():
    def _companies_raw_json(*args, **kwargs):
        return {
            "results": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "string",
                    "platform": "string",
                    "redirect": "string",
                    "lastSync": "2022-08-15T14:41:15.076Z",
                    "dataConnections": [
                        {
                            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                            "integrationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                            "sourceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                            "platformName": "string",
                            "linkUrl": "string",
                            "status": "string",
                            "lastSync": "2022-08-15T14:41:15.076Z",
                            "created": "2022-08-15T14:41:15.076Z",
                            "sourceType": "string",
                            "dataConnectionErrors": [
                                {
                                    "statusCode": "string",
                                    "statusText": "string",
                                    "errorMessage": "string",
                                    "erroredOnUtc": "2022-08-15T14:41:15.076Z",
                                }
                            ],
                        }
                    ],
                    "created": "2022-08-15T14:41:15.076Z",
                    "createdByUserName": "string",
                }
            ],
            "pageNumber": 0,
            "pageSize": 0,
            "totalResults": 0,
            "_links": {
                "self": {"href": "string"},
                "current": {"href": "string"},
                "next": {"href": "string"},
                "previous": {"href": "string"},
            },
        }

    return _companies_raw_json


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
def random_guid():
    def _random_guid():
        return uuid.uuid4().hex

    return _random_guid


@pytest.fixture
def company_raw_json():
    def _company_raw_json(*args, **kwargs):
        return {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": "string",
            "platform": "string",
            "redirect": "string",
            "lastSync": "2022-08-13T09:03:23.533Z",
            "dataConnections": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "integrationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "sourceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "platformName": "string",
                    "linkUrl": "string",
                    "status": "string",
                    "lastSync": "2022-08-13T09:03:23.533Z",
                    "created": "2022-08-13T09:03:23.533Z",
                    "sourceType": "string",
                    "dataConnectionErrors": [
                        {
                            "statusCode": "string",
                            "statusText": "string",
                            "errorMessage": "string",
                            "erroredOnUtc": "2022-08-13T09:03:23.533Z",
                        }
                    ],
                }
            ],
            "created": "2022-08-13T09:03:23.533Z",
            "createdByUserName": "string",
        }

    return _company_raw_json


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
def connection_raw_json():
    def _connection_raw_json(*args, **kwargs):
        return {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "integrationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "sourceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "platformName": "string",
            "linkUrl": "string",
            "status": "string",
            "lastSync": "2022-08-15T14:07:48.540Z",
            "created": "2022-08-15T14:07:48.540Z",
            "sourceType": "string",
            "dataConnectionErrors": [
                {
                    "statusCode": "string",
                    "statusText": "string",
                    "errorMessage": "string",
                    "erroredOnUtc": "2022-08-15T14:07:48.540Z",
                }
            ],
        }

    return _connection_raw_json


@pytest.fixture
def connections_raw_json():
    def _connections_raw_json(*args, **kwargs):
        return {
            "results": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "integrationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "sourceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "platformName": "string",
                    "linkUrl": "string",
                    "status": "string",
                    "lastSync": "2022-08-14T15:12:00.640Z",
                    "created": "2022-08-14T15:12:00.640Z",
                    "sourceType": "string",
                    "dataConnectionErrors": [
                        {
                            "statusCode": "string",
                            "statusText": "string",
                            "errorMessage": "string",
                            "erroredOnUtc": "2022-08-14T15:12:00.640Z",
                        }
                    ],
                }
            ],
            "pageNumber": 0,
            "pageSize": 0,
            "totalResults": 0,
            "_links": {
                "self": {"href": "string"},
                "current": {"href": "string"},
                "next": {"href": "string"},
                "previous": {"href": "string"},
            },
        }

    return _connections_raw_json


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
def data_sets_raw_json():
    def _data_sets_raw_json(*args, **kwargs):
        return {
            "results": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "companyId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "connectionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "dataType": "string",
                    "status": "Initial",
                    "errorMessage": "string",
                    "requested": "2022-08-15T09:36:22.249Z",
                    "completed": "2022-08-15T09:36:22.249Z",
                    "progress": 0,
                    "isCompleted": True,
                    "isErrored": True,
                    "validationinformationUrl": "string",
                }
            ],
            "pageNumber": 0,
            "pageSize": 0,
            "totalResults": 0,
            "_links": {
                "self": {"href": "string"},
                "current": {"href": "string"},
                "next": {"href": "string"},
                "previous": {"href": "string"},
            },
        }

    return _data_sets_raw_json


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
def data_set_raw_json():
    def _data_set_raw_json(*args, **kwargs):
        return {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "companyId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "connectionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "dataType": "string",
            "status": "Initial",
            "errorMessage": "string",
            "requested": "2022-08-15T09:36:22.249Z",
            "completed": "2022-08-15T09:36:22.249Z",
            "progress": 0,
            "isCompleted": True,
            "isErrored": True,
            "validationinformationUrl": "string",
        }

    return _data_set_raw_json


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
def sync_settings_raw_json():
    def _sync_settings_raw_json(*args, **kwargs):
        return {
            "companyId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "settings": [
                {
                    "dataType": "string",
                    "fetchOnFirstLink": True,
                    "syncSchedule": 0,
                    "syncOrder": 0,
                    "syncFromUtc": "2022-08-16T16:14:18.344Z",
                    "syncFromWindow": 0,
                    "monthsToSync": 0,
                }
            ],
            "overridesDefaults": True,
        }

    return _sync_settings_raw_json


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


@pytest.fixture
def data_status_raw_json():
    def _data_status_raw_json(*args, **kwargs):
        return {
            "items": {
                "dataType": "items",
                "lastSuccessfulSync": "2020-09-02T07:41:31.4106471Z",
                "currentStatus": "FetchError",
                "latestSyncId": "6c098972-edad-43aa-afb4-026396c72de9",
                "latestSuccessfulSyncId": "5a380cba-5c4a-4a1b-b023-d88c7019cd7a",
            },
            "chartOfAccounts": {
                "dataType": "chartOfAccounts",
                "lastSuccessfulSync": "2020-09-01T19:33:09.547111Z",
                "currentStatus": "AuthError",
                "latestSyncId": "ae42ec88-a090-4e30-85f7-05feb7ea3fb2",
                "latestSuccessfulSyncId": "692ef0fe-eb0d-4fad-b226-e841ccaa3a21",
            },
            "profitAndLoss": {
                "dataType": "profitAndLoss",
                "lastSuccessfulSync": "2020-09-01T19:33:21.9664862Z",
                "currentStatus": "AuthError",
                "latestSyncId": "e2927d99-4348-4f19-aa47-bc998d04de6d",
                "latestSuccessfulSyncId": "d6e39584-e4fd-43a2-a092-0ae7fb9c3db6",
            },
            "taxRates": {
                "dataType": "taxRates",
                "lastSuccessfulSync": "2020-09-01T19:33:21.4397843Z",
                "currentStatus": "AuthError",
                "latestSyncId": "c06ee101-0c65-4585-b0cb-b92bdd1606a3",
                "latestSuccessfulSyncId": "04fe4ac0-26fb-40e7-b452-0c048798cb49",
            },
            "bills": {
                "dataType": "bills",
                "lastSuccessfulSync": "2020-09-01T19:33:11.3440337Z",
                "currentStatus": "AuthError",
                "latestSyncId": "25085113-24a3-49eb-83b9-15ce63b84c24",
                "latestSuccessfulSyncId": "f5597550-b5fd-42f8-994b-3b8156f0cc59",
            },
            "creditNotes": {
                "dataType": "creditNotes",
                "lastSuccessfulSync": "2020-09-01T19:33:10.4995773Z",
                "currentStatus": "AuthError",
                "latestSyncId": "8b103f16-f4d7-4b15-b967-633932f0b6d4",
                "latestSuccessfulSyncId": "42096bc3-e840-4d33-8ca5-245827f5a7b5",
            },
            "balanceSheet": {
                "dataType": "balanceSheet",
                "lastSuccessfulSync": "2020-09-01T19:33:16.9389217Z",
                "currentStatus": "AuthError",
                "latestSyncId": "ce0eacea-994f-480b-bd3c-37450a6e94b2",
                "latestSuccessfulSyncId": "86d74055-8b0d-4179-8723-60f1b598992c",
            },
            "customers": {
                "dataType": "customers",
                "lastSuccessfulSync": "2020-09-01T19:33:10.8752855Z",
                "currentStatus": "AuthError",
                "latestSyncId": "96802e7d-de9a-4755-9f5e-3a4bfc946cbc",
                "latestSuccessfulSyncId": "5395c897-9db8-4594-8bda-d85ba878c725",
            },
            "trackingCategories": {
                "dataType": "trackingCategories",
                "lastSuccessfulSync": "2020-09-01T19:33:18.3228415Z",
                "currentStatus": "AuthError",
                "latestSyncId": "2c1b1f5e-4b0a-4a97-8476-58d423e03c57",
                "latestSuccessfulSyncId": "f1fbbf56-11ea-4ef8-b29b-ac7eeb46a36b",
            },
            "invoices": {
                "dataType": "invoices",
                "lastSuccessfulSync": "2020-09-01T19:33:22.7007125Z",
                "currentStatus": "AuthError",
                "latestSyncId": "c450c808-649b-4054-b559-749d9383da74",
                "latestSuccessfulSyncId": "8fb14f57-71ed-44a0-b362-92fdb7425e18",
            },
            "billCreditNotes": {
                "dataType": "billCreditNotes",
                "lastSuccessfulSync": "2020-09-02T07:41:29.0965328Z",
                "currentStatus": "FetchError",
                "latestSyncId": "ad375ae9-c4b8-4677-8b1d-fb4b53885555",
                "latestSuccessfulSyncId": "fb68327d-7437-424e-96dd-74bf87c01266",
            },
            "billPayments": {
                "dataType": "billPayments",
                "lastSuccessfulSync": "2020-09-01T19:33:10.1089162Z",
                "currentStatus": "AuthError",
                "latestSyncId": "78786a14-51f4-4c08-b520-c0be56c0c1b1",
                "latestSuccessfulSyncId": "2a0c9996-7a7a-4ed8-9daf-9ca890925265",
            },
            "suppliers": {
                "dataType": "suppliers",
                "lastSuccessfulSync": "2020-09-01T19:33:20.8772457Z",
                "currentStatus": "AuthError",
                "latestSyncId": "11399363-358d-4378-8493-a8535b67f0d3",
                "latestSuccessfulSyncId": "8e649c98-f0fd-4267-9634-b667b890b2f6",
            },
            "company": {
                "dataType": "company",
                "lastSuccessfulSync": "2020-09-01T19:33:08.3435782Z",
                "currentStatus": "AuthError",
                "latestSyncId": "9d098dc7-3564-4307-b66d-a8b2cdb3b7f9",
                "latestSuccessfulSyncId": "185b52fc-4bdd-4678-8c31-b85f72b4e697",
            },
            "journalEntries": {
                "dataType": "journalEntries",
                "lastSuccessfulSync": "2020-09-01T19:33:21.471416Z",
                "currentStatus": "AuthError",
                "latestSyncId": "e51560f4-876f-4eb8-a57b-b99db114628a",
                "latestSuccessfulSyncId": "e1cd0f90-d688-4419-b341-d198afca65dc",
            },
            "payments": {
                "dataType": "payments",
                "lastSuccessfulSync": "2020-09-01T19:33:22.6430207Z",
                "currentStatus": "AuthError",
                "latestSyncId": "63eb8516-489a-403f-aecc-f8ce2bb0f564",
                "latestSuccessfulSyncId": "cfe66857-ff7a-46ed-9d49-cd90d8a9d935",
            },
        }

    return _data_status_raw_json
