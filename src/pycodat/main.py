import base64

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


def encode_key_to_base_64(key: str) -> str:
    key_bytes = key.encode("ascii")
    base64_key = base64.b64encode(key_bytes)
    base64_key_string = base64_key.decode("ascii")
    return base64_key_string


class Codat:
    """The main class which acts as an interface to access the Codat API."""

    def __init__(self, key: str, env: str = "prod",) -> None:
        """initialization dunder method

        :param key: Codat portal API Key
        :type key: str
        :param env: name of the Codat environment used, defaults to "prod"
        :type env: str, optional
        """
        encoded_key = encode_key_to_base_64(key)
        self.key = encoded_key
        self.env = env

    def get_companies(self,**kwargs) -> CompanyPaginatedResponse:
        """Gets all companies

        :return: A list of companies
        :rtype: CompanyPaginatedResponse
        """
        company_handler = CompanyHandler(self.key, self.env)
        company = company_handler.get_all_companies(**kwargs)
        return company

    def get_company(self, company_id: str) -> Company:
        """Gets a single company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :return: A single company
        :rtype: Company
        """

        company_handler = CompanyHandler(self.key, self.env)
        company = company_handler.get_single_company(company_id)
        return company

    # TODO Get Settings
    # doesnt seem that important - might skip this for now.

    def get_sync_settings(self, company_id: str) -> SyncSettings:
        """Gets the sync settings for a single company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :return: Sync settings for a company
        :rtype: SyncSettings
        """

        sync_settings_handler = SyncSettingHandler(self.key, self.env)
        sync_settings = sync_settings_handler.get_sync_settings(company_id)
        return sync_settings

    def get_connections(self, company_id: str,**kwargs) -> DataConnectionPaginatedResponse:
        """Gets the connections for a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :return: List of all of a companies connections
        :rtype: DataConnectionPaginatedResponse
        """

        connection_handler = ConnectionHandler(self.key, self.env)
        connection = connection_handler.get_company_connections(company_id,**kwargs)
        return connection

    def get_connection(self, company_id: str, connection_id: str) -> DataConnection:
        """Gets a single connection for a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :param connection_id: Unique identifier for a connection
        :type connection_id: str
        :return: The details of a single connection
        :rtype: DataConnection
        """

        connection_handler = ConnectionHandler(self.key, self.env)
        connection = connection_handler.get_single_company_connection(
            company_id, connection_id
        )
        return connection

    def get_data_sets(self, company_id: str, **kwargs) -> DataSetMetaDataPaginatedResponse:
        """Gets the metadata history for a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :return: A list of all the data sets and their metadata
        :rtype: DataSetMetaDataPaginatedResponse
        """

        data_set_metadata_handler = DataSetHandler(self.key, self.env)
        data_set_metadata_history = data_set_metadata_handler.get_all_data_sets(
            company_id,**kwargs
        )
        return data_set_metadata_history

    def get_data_set(self, company_id: str, data_set_id: str) -> DataSetMetadata:
        """Gets a single dataset for a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :param data_set_id: Unique identifier for a dataset
        :type data_set_id: str
        :return: The metadata for a single dataset
        :rtype: DataSetMetadata
        """
        data_set_metadata_handler = DataSetHandler(self.key, self.env)
        data_set_metadata = data_set_metadata_handler.get_single_data_set(
            company_id, data_set_id
        )
        return data_set_metadata

    def get_data_status(self, company_id: str) -> DataStatus:
        """Gets the current status of each dataset that a company has

        :param company_id: Unique identifier for a company
        :type company_id: str
        :return: Description of the current status of each dataset that the company has
        :rtype: DataStatus
        """
        data_status_handler = DataStatusHandler(self.key, self.env)
        data_status = data_status_handler.get_company_data_status(company_id)
        return data_status

    # TODO Add Tox... maybe later
    # TODO Add Kwargs support
