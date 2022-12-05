from pycodat.data_types.accounting.accounts import Account, AccountsPaginatedResponse
from pycodat.handlers.base import BaseHandler


class AccountsHandler(BaseHandler):
    def get_all_accounts(self, company_id: str, **kwargs) -> AccountsPaginatedResponse:
        result = self.client.get(self.path + company_id + "/data/accounts", **kwargs)
        accounts = AccountsPaginatedResponse(**result)
        return accounts

    def get_single_account(self, company_id: str, account_id: str) -> Account:
        result = self.client.get(
            self.path + company_id + "/data/accounts/" + account_id
        )
        account = Account(**result)
        return account
