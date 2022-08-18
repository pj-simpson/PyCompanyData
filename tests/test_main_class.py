import typing

import pytest

from pycodat.data_types.platform.company import (Company,
                                                 CompanyPaginatedResponse)
from pycodat.data_types.platform.connections import (
    DataConnection, DataConnectionPaginatedResponse)
from pycodat.data_types.platform.datasetmetadata import (
    DataSetMetadata, DataSetMetaDataPaginatedResponse)
from pycodat.data_types.platform.datastatus import DataStatus
from pycodat.data_types.platform.exceptions import CodatException
from pycodat.data_types.platform.syncsettings import SyncSettings
from pycodat.handlers.platform.companyhandler import CompanyHandler
from pycodat.handlers.platform.connectionhandler import ConnectionHandler
from pycodat.handlers.platform.datasetmetadatahandler import DataSetHandler
from pycodat.handlers.platform.datastatushandler import DataStatusHandler
from pycodat.handlers.platform.syncsettingshandler import SyncSettingHandler
from pycodat.main import Codat


class TestMainClass:
    def test_main_class_init(self, basic_auth_key, encoded_auth_key):
        codat = Codat(key=basic_auth_key, env="uat")
        assert codat.key == encoded_auth_key
        assert codat.env == "uat"

    def test_main_class_init_not_env_supplied(self, basic_auth_key, encoded_auth_key):
        codat = Codat(key=basic_auth_key)
        assert codat.key == encoded_auth_key
        assert codat.env == "prod"

    def test_main_class_init_missing_key(self):
        with pytest.raises(TypeError):
            codat = Codat(env="prod")

    def test_get_companies(self, basic_auth_key, monkeypatch, companies):
        monkeypatch.setattr(CompanyHandler, "get_all_companies", companies)
        codat = Codat(key=basic_auth_key, env="prod")
        result = codat.get_companies()
        assert type(result) == CompanyPaginatedResponse

    def test_get_company(self, basic_auth_key, monkeypatch, company, random_guid):
        monkeypatch.setattr(CompanyHandler, "get_single_company", company)
        codat = Codat(key=basic_auth_key, env="prod")
        result = codat.get_company(random_guid)
        assert type(result) == Company

    def test_get_company_no_id_supplied(self, basic_auth_key):
        with pytest.raises(TypeError):
            codat = Codat(key=basic_auth_key, env="prod")
            result = codat.get_company()

    def test_get_connections(
        self, basic_auth_key, monkeypatch, connections, random_guid
    ):
        monkeypatch.setattr(ConnectionHandler, "get_company_connections", connections)
        codat = Codat(key=basic_auth_key, env="prod")
        result = codat.get_connections(random_guid)
        assert type(result) == DataConnectionPaginatedResponse
        assert type(result.results) == list

    def test_get_connections_no_id_supplied(self, basic_auth_key):
        with pytest.raises(TypeError):
            codat = Codat(key=basic_auth_key, env="prod")
            result = codat.get_connections()

    def test_get_connection(self, basic_auth_key, monkeypatch, connection, random_guid):
        monkeypatch.setattr(
            ConnectionHandler, "get_single_company_connection", connection
        )
        codat = Codat(key=basic_auth_key, env="prod")
        result = codat.get_connection(random_guid, random_guid)
        assert type(result) == DataConnection

    def test_get_connections_no_id_supplied(self, basic_auth_key):
        with pytest.raises(TypeError):
            codat = Codat(key=basic_auth_key, env="prod")
            result = codat.get_connection()

    def test_get_data_set_history(
        self, basic_auth_key, monkeypatch, data_sets, random_guid
    ):
        monkeypatch.setattr(DataSetHandler, "get_all_data_sets", data_sets)
        codat = Codat(key=basic_auth_key, env="prod")
        result = codat.get_data_sets(random_guid)
        assert type(result) == DataSetMetaDataPaginatedResponse
        assert type(result.results) == list

    def test_get_data_set_history_no_id_supplied(self, basic_auth_key):
        with pytest.raises(TypeError):
            codat = Codat(key=basic_auth_key, env="prod")
            result = codat.get_data_sets()

    def test_get_data_set(self, basic_auth_key, monkeypatch, data_set, random_guid):
        monkeypatch.setattr(DataSetHandler, "get_single_data_set", data_set)
        codat = Codat(key=basic_auth_key, env="prod")
        result = codat.get_data_set(random_guid, random_guid)
        assert type(result) == DataSetMetadata

    def test_get_data_set_no_id_supplied(self, basic_auth_key):
        with pytest.raises(TypeError):
            codat = Codat(key=basic_auth_key, env="prod")
            result = codat.get_data_set()

    def test_get_sync_settings(
        self, basic_auth_key, monkeypatch, sync_settings, random_guid
    ):
        monkeypatch.setattr(SyncSettingHandler, "get_sync_settings", sync_settings)
        codat = Codat(key=basic_auth_key, env="prod")
        result = codat.get_sync_settings(random_guid)
        assert type(result) == SyncSettings

    def test_get_sync_settings_no_id_supplied(self, basic_auth_key):
        with pytest.raises(TypeError):
            codat = Codat(key=basic_auth_key, env="prod")
            result = codat.get_sync_settings()

    def test_get_data_status(
        self, basic_auth_key, monkeypatch, data_status, random_guid
    ):
        monkeypatch.setattr(DataStatusHandler, "get_company_data_status", data_status)
        codat = Codat(key=basic_auth_key, env="prod")
        result = codat.get_data_status(random_guid)
        assert type(result) == DataStatus

    def test_test_get_data_status_no_id_supplied(self, basic_auth_key):
        with pytest.raises(TypeError):
            codat = Codat(key=basic_auth_key, env="prod")
            result = codat.get_data_status()
