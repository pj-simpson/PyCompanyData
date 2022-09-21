import pytest

from pycodat.data_types.platform.company import Company, CompanyPaginatedResponse
from pycodat.data_types.platform.connections import (
    DataConnection,
    DataConnectionPaginatedResponse,
)
from pycodat.data_types.platform.datasetmetadata import (
    DataSetMetadata,
    DataSetMetaDataPaginatedResponse,
)
from pycodat.data_types.platform.datastatus import DataStatus
from pycodat.data_types.platform.syncsettings import SyncSettings
from pycodat.handlers.platform.companyhandler import CompanyHandler
from pycodat.handlers.platform.connectionhandler import ConnectionHandler
from pycodat.handlers.platform.datasetmetadatahandler import DataSetHandler
from pycodat.handlers.platform.datastatushandler import DataStatusHandler
from pycodat.handlers.platform.syncsettingshandler import SyncSettingHandler
from pycodat.rest_adapter import RestAdapter


class TestCompanyHandlers:
    def test_company_handler_get_all_companies(
        self, monkeypatch, companies_raw_json, basic_auth_key
    ):
        monkeypatch.setattr(RestAdapter, "get", companies_raw_json)
        handler = CompanyHandler(basic_auth_key, "prod")
        result = handler.get_all_companies()

        assert type(result) == CompanyPaginatedResponse

    def test_company_handler_get_single_company(
        self, monkeypatch, company_raw_json, basic_auth_key, random_guid
    ):
        monkeypatch.setattr(RestAdapter, "get", company_raw_json)
        handler = CompanyHandler(basic_auth_key, "prod")
        company_id = random_guid()

        result = handler.get_single_company(company_id)

        assert type(result) == Company


class TestConnectionHandlers:
    def test_connection_handler_get_company_connections(
        self, monkeypatch, connections_raw_json, basic_auth_key, random_guid
    ):
        monkeypatch.setattr(RestAdapter, "get", connections_raw_json)
        handler = ConnectionHandler(basic_auth_key, "prod")
        company_id = random_guid()

        result = handler.get_company_connections(company_id)

        assert type(result) == DataConnectionPaginatedResponse

    def test_connection_handler_get_single_company_connection(
        self, monkeypatch, connection_raw_json, basic_auth_key, random_guid
    ):
        monkeypatch.setattr(RestAdapter, "get", connection_raw_json)
        handler = ConnectionHandler(basic_auth_key, "prod")
        company_id = random_guid()
        connection_id = random_guid()

        result = handler.get_single_company_connection(company_id, connection_id)

        assert type(result) == DataConnection


class TestDataSetHandlers:
    def test_dataset_handler_get_data_set_history(
        self,
        monkeypatch,
        data_sets_raw_json,
        basic_auth_key,
        random_guid,
    ):
        monkeypatch.setattr(RestAdapter, "get", data_sets_raw_json)
        handler = DataSetHandler(basic_auth_key, "prod")
        company_id = random_guid()

        result = handler.get_all_data_sets(company_id)

        assert type(result) == DataSetMetaDataPaginatedResponse

    def test_dataset_handler_get_single_data_set(
        self,
        monkeypatch,
        data_set_raw_json,
        basic_auth_key,
        random_guid,
    ):
        monkeypatch.setattr(RestAdapter, "get", data_set_raw_json)
        handler = DataSetHandler(basic_auth_key, "prod")
        company_id = random_guid()
        data_set_id = random_guid()

        result = handler.get_single_data_set(company_id, data_set_id)

        assert type(result) == DataSetMetadata


class TestSyncSettingHandlers:
    def test_sync_setting_handler_get_sync_settings(
        self,
        monkeypatch,
        sync_settings_raw_json,
        basic_auth_key,
        random_guid,
    ):
        monkeypatch.setattr(RestAdapter, "get", sync_settings_raw_json)
        handler = SyncSettingHandler(basic_auth_key, "prod")
        company_id = random_guid()

        result = handler.get_sync_settings(company_id)

        assert type(result) == SyncSettings


class TestDataStatusHandlers:
    def test_data_status_handler_get_sync_settings(
        self,
        monkeypatch,
        data_status_raw_json,
        basic_auth_key,
        random_guid,
    ):
        monkeypatch.setattr(RestAdapter, "get", data_status_raw_json)
        handler = DataStatusHandler(basic_auth_key, "prod")
        company_id = random_guid()

        result = handler.get_company_data_status(company_id)

        assert type(result) == DataStatus
