import typing

from pycodat.data_types.accounting.account_transactions import AccountTransaction

from pycodat.data_types.pagination import PaginatedResponse
from pycodat.handlers.base import BaseHandler


class AccountTransactionHandler(BaseHandler):
    def get_all_account_transactions(
        self, company_id: str, connection_id: str
    ) -> typing.List[AccountTransaction]:
        path = f"{self.path}{company_id}/connections/{connection_id}/data/accounttransactions"
        return self._get_all_pages(AccountTransaction, path)

    def get_pageof_account_transactions(
        self, company_id: str, connection_id: str
    ) -> PaginatedResponse[AccountTransaction]:
        path = f"{self.path}{company_id}/connections/{connection_id}/data/accounttransactions"
        return self._get_paginated_response(AccountTransaction, path)

    def get_single_account_transaction(
        self, company_id: str, connection_id: str, account_transaction_id: str
    ) -> AccountTransaction:
        path = f"{self.path}{company_id}/connections/{connection_id}/data/accounttransactions{account_transaction_id}"
        account_transaction = self.client.get(path)
        return AccountTransaction(**account_transaction)
