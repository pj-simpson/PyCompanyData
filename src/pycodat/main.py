import base64

from pycodat.data_types.platform.company import (Company,
                                                 CompanyPaginatedResponse)
from pycodat.data_types.platform.connections import (
    DataConnection, DataConnectionPaginatedResponse)
from pycodat.data_types.platform.datasetmetadata import (
    DataSetMetadata, DataSetMetaDataPaginatedResponse)
from pycodat.data_types.platform.syncsettings import SyncSettings
from pycodat.handlers.platform.companyhandler import CompanyHandler
from pycodat.handlers.platform.connectionhandler import ConnectionHandler
from pycodat.handlers.platform.datasetmetadatahandler import DataSetHandler
from pycodat.handlers.platform.syncsettingshandler import SyncSettingHandler


def encode_key_to_base_64(key:str) -> str:
        key_bytes = key.encode('ascii')
        base64_key = base64.b64encode(key_bytes)
        base64_key_string = base64_key.decode('ascii')
        return base64_key_string

class Codat:
    def __init__(self, key: str, env: str = "prod"):

        encoded_key = encode_key_to_base_64(key)
        self.key = encoded_key
        self.env = env

    def get_companies(self) -> CompanyPaginatedResponse:
        company_handler = CompanyHandler(self.key, self.env)
        company = company_handler.get_all_companies()
        return company

    def get_company(self, company_id: str) -> Company:

        company_handler = CompanyHandler(self.key, self.env)
        company = company_handler.get_single_company(company_id)
        return company

    # TODO Get Settings
    # doesnt seem that important - might skip this for now. 

    def get_sync_settings(self, company_id: str) -> SyncSettings:

        sync_settings_handler = SyncSettingHandler(self.key, self.env)
        sync_settings = sync_settings_handler.get_sync_settings(company_id)
        return sync_settings

    def get_connections(self, company_id: str) -> DataConnectionPaginatedResponse:

        connection_handler = ConnectionHandler(self.key, self.env)
        connection = connection_handler.get_company_connections(company_id)
        return connection

    def get_connection(self, company_id: str, connection_id: str) -> DataConnection:

        connection_handler = ConnectionHandler(self.key, self.env)
        connection = connection_handler.get_single_company_connection(
            company_id, connection_id
        )
        return connection

    def get_data_sets(self, company_id: str) -> DataSetMetaDataPaginatedResponse:

        data_set_metadata_handler = DataSetHandler(self.key, self.env)
        data_set_metadata_history = data_set_metadata_handler.get_all_data_sets(
            company_id
        )
        return data_set_metadata_history

    def get_data_set(self, company_id: str, data_set_id: str) -> DataSetMetadata:
        data_set_metadata_handler = DataSetHandler(self.key, self.env)
        data_set_metadata = data_set_metadata_handler.get_single_data_set(
            company_id, data_set_id
        )
        return data_set_metadata

    # TODO Get Data Status?
    # TODO Add pre-commit hooks
    # TODO Add MyPy
