import typing

from pycodat.data_types.accounting.suppliers import Supplier
from pycodat.data_types.pagination import PaginatedResponse
from pycodat.handlers.base import BaseHandler


class SuppliersHandler(BaseHandler):
    def get_all_suppliers(self, company_id: str, query: str, order_by: str) -> typing.List[Supplier]:
        path = f"{self.path}{company_id}/data/suppliers"
        return self._get_all_pages(Supplier, path, query=query, orderBy=order_by)

    def get_pageof_suppliers(self, company_id: str, page_number: int, page_size: int, query: str,
                             order_by: str) -> PaginatedResponse[Supplier]:
        path = f"{self.path}{company_id}/data/suppliers"
        return self._get_paginated_response(Supplier, path, page=page_number, pageSize=page_size,
                                            query=query, orderBy=order_by)

    def get_single_supplier(self, company_id: str, supplier_id: str) -> Supplier:
        path = f"{self.path}{company_id}/data/suppliers/{supplier_id}"
        account = self.client.get(path)
        return Supplier(**account)
