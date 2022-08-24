from pycodat.data_types.accounting.accounts import AccountsPaginatedResponse
from pycodat.handlers.base import BaseHandler


class AccountsHandler(BaseHandler):

    path = "/companies/"

    def get_all_accounts(self, company_id: str, **kwargs) -> AccountsPaginatedResponse:
        result = self.client.get(self.path + company_id + "/data/accounts", **kwargs)
        accounts = AccountsPaginatedResponse(**result)
        return accounts
