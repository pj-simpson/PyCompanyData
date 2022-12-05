import datetime
import typing

from pydantic import BaseModel

from pycodat.data_types.accounting.account_transactions import (
    AccountTransaction,
    AccountTransactionsPaginatedResponse,
)
from pycodat.data_types.accounting.accounts import Account, AccountsPaginatedResponse
from pycodat.data_types.pagination import PaginatedResponse
from pycodat.data_types.platform.connections import (
    DataConnection,
    DataConnectionPaginatedResponse,
)
from pycodat.data_types.platform.datasetmetadata import (
    DataSetMetadata,
    DataSetMetaDataPaginatedResponse,
)
from pycodat.handlers.accounting.account_transaction_handler import (
    AccountTransactionHandler,
)
from pycodat.handlers.accounting.accounts_handler import AccountsHandler
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

    def get_accounts(self, **kwargs) -> AccountsPaginatedResponse:

        connection_handler = AccountsHandler(self.key, self.env)
        connection = connection_handler.get_all_accounts(self.id, **kwargs)
        return connection

    def get_account(self, account_id: str) -> Account:

        accounts_handler = AccountsHandler(self.key, self.env)
        account = accounts_handler.get_single_account(self.id, account_id)
        return account

    def get_account_transactions(
        self, connection_id: str
    ) -> AccountTransactionsPaginatedResponse:

        account_transaction_handler = AccountTransactionHandler(self.key, self.env)
        account_transactions = account_transaction_handler.get_all_account_transactions(
            self.id, connection_id
        )
        return account_transactions

    def get_account_transaction(
        self, connection_id: str, account_transaction_id: str
    ) -> AccountTransaction:

        account_transaction_handler = AccountTransactionHandler(self.key, self.env)
        account_transaction = (
            account_transaction_handler.get_single_account_transaction(
                self.id, connection_id, account_transaction_id
            )
        )
        return account_transaction


class CompanyPaginatedResponse(PaginatedResponse):
    results: typing.List[Company] = []
