from pycodat.data_types.accounting.suppliers import Supplier
from pycodat.handlers.base import BaseHandler


class SuppliersHandler(BaseHandler):
    def get_single_supplier(self, company_id: str, supplier_id: str) -> Supplier:
        result = self.client.get(
            self.path + company_id + "/data/suppliers/" + supplier_id
        )
        supplier = Supplier(**result)
        return supplier
