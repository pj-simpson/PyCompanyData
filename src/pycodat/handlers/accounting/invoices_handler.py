import typing

from pycodat.data_types.accounting.invoices import Invoice
from pycodat.data_types.pagination import PaginatedResponse
from pycodat.handlers.base import BaseHandler

class InvoicesHandler(BaseHandler):
    def get_all_invoices(self, company_id: str, query: str, order_by: str) -> typing.List[Invoice]:
        path = f"{self.path}{company_id}/data/invoices"
        invoices = self._get_all_pages(Invoice, path, query=query, orderBy=order_by)
        return invoices

    def get_pageof_invoices(self, company_id: str, page_number: int, page_size: int, query: str, order_by: str) -> PaginatedResponse[Invoice]:
        path = f"{self.path}{company_id}/data/invoices"
        invoices = self._get_paginated_response(Invoice, path, page=page_number, pageSize=page_size, query=query, orderBy=order_by)
        return invoices

    def get_single_invoice(self, company_id: str, invoice_id: str) -> Invoice:
        path = f"{self.path}{company_id}/data/invoices/{invoice_id}"
        result = self.client.get(path)
        invoice = Invoice(**result)
        return invoice
