from pycodat.data_types.platform.datasetmetadata import (
    DataSetMetadata, DataSetMetaDataPaginatedResponse)
from pycodat.handlers.base import BaseHandler


class DataSetHandler(BaseHandler):

    path = "/companies/"

    def get_all_data_sets(self, company_id: str) -> DataSetMetaDataPaginatedResponse:
        result = self.client.get(self.path + company_id + "/data/history")
        return DataSetMetaDataPaginatedResponse(**result)

    def get_single_data_set(
        self, company_id: str, data_set_id: str
    ) -> DataSetMetaDataPaginatedResponse:
        result = self.client.get(
            self.path + company_id + "/data/history/" + data_set_id
        )
        return DataSetMetadata(**result)
