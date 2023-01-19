import typing

from pycodat.data_types.accounting.bills import Bill
from pycodat.data_types.pagination import PaginatedResponse
from pycodat.handlers.base import BaseHandler


class BillsHandler(BaseHandler):
    def get_all_bills(self, company_id: str, query: str, order_by: str) -> typing.List[Bill]:
        path = f"{self.path}{company_id}/data/bills"
        return self._get_all_pages(Bill, path, query=query, orderBy=order_by)

    def get_pageof_bills(self, company_id: str, page_number: int, page_size: int, query: str,
                         order_by: str) -> PaginatedResponse[Bill]:
        path = f"{self.path}{company_id}/data/bills"
        return self._get_paginated_response(Bill, path, page=page_number, pageSize=page_size,
                                            query=query, orderBy=order_by)

    def get_single_bill(self, company_id: str, bill_id: str) -> Bill:
        path = f"{self.path}{company_id}/data/bills/{bill_id}"
        account = self.client.get(path)
        return Bill(**account)
