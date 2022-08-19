import datetime
import typing

from pydantic import BaseModel

from pycodat.data_types.platform.connections import (
    DataConnection,
    DataConnectionPaginatedResponse,
)
from pycodat.data_types.platform.datasetmetadata import (
    DataSetMetadata,
    DataSetMetaDataPaginatedResponse,
)
from pycodat.data_types.platform.pagination import PaginatedResponse
from pycodat.handlers.platform.connectionhandler import ConnectionHandler
from pycodat.handlers.platform.datasetmetadatahandler import DataSetHandler

from ...handlers.platform.datastatushandler import DataStatusHandler
from ...handlers.platform.syncsettingshandler import SyncSettingHandler
from .datastatus import DataStatus
from .syncsettings import SyncSettings


class Company(BaseModel):
    id: str
    name: str
    platform: str
    redirect: str
    created: typing.Optional[datetime.datetime] = None
    lastSync: typing.Optional[str] = None
    dataConnections: typing.Optional[typing.List[DataConnection]] = None
    createdByUserName: typing.Optional[str] = None
    key: str = ""
    env: str = ""

    def _set_env_and_key(self, key: str, env: str):
        self.key: str = key
        self.env: str = env

    def get_connections(self) -> DataConnectionPaginatedResponse:

        connection_handler = ConnectionHandler(key=self.key, env=self.env)

        connection = connection_handler.get_company_connections(self.id)
        return connection

    def get_connection(self, connection_id: str) -> DataConnection:
        connection_handler = ConnectionHandler(key=self.key, env=self.env)

        connection = connection_handler.get_single_company_connection(
            self.id, connection_id
        )
        return connection

    def get_sync_settings(self) -> SyncSettings:

        sync_settings_handler = SyncSettingHandler(key=self.key, env=self.env)
        sync_settings = sync_settings_handler.get_sync_settings(self.id)
        return sync_settings

    def get_data_sets(self) -> DataSetMetaDataPaginatedResponse:

        data_set_metadata_handler = DataSetHandler(self.key, self.env)
        data_set_metadata_history = data_set_metadata_handler.get_all_data_sets(self.id)
        return data_set_metadata_history

    def get_data_set(self, data_set_id: str) -> DataSetMetadata:
        data_set_metadata_handler = DataSetHandler(self.key, self.env)
        data_set_metadata = data_set_metadata_handler.get_single_data_set(
            self.id, data_set_id
        )
        return data_set_metadata

    def get_data_status(self) -> DataStatus:
        data_status_handler = DataStatusHandler(self.key, self.env)
        data_status = data_status_handler.get_company_data_status(self.id)
        return data_status


class CompanyPaginatedResponse(PaginatedResponse):
    results: typing.List[Company] = []
