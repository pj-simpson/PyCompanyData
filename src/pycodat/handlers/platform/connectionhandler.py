from pycodat.data_types.platform.connections import (
    DataConnection,
    DataConnectionPaginatedResponse,
)
from pycodat.handlers.base import BaseHandler


class ConnectionHandler(BaseHandler):
    path = "/companies/"

    def get_company_connections(
        self, company_id: str, **kwargs
    ) -> DataConnectionPaginatedResponse:
        result = self.client.get(self.path + company_id + "/connections",**kwargs)
        return DataConnectionPaginatedResponse(**result)

    def get_single_company_connection(
        self, company_id: str, connection_id: str
    ) -> DataConnection:
        result = self.client.get(
            self.path + company_id + "/connections/" + connection_id
        )
        return DataConnection(**result)
