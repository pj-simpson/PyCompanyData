import datetime
import uuid

import pytest

from pycodat.data_types.pagination import LinkHref, PaginationLinks
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
def random_guid():
    def _random_guid():
        return uuid.uuid4().hex

    return _random_guid
