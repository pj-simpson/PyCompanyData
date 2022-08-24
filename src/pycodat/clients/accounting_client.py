from pycodat.clients.platform_client import PlatformClient
from pycodat.data_types.accounting.accounts import AccountsPaginatedResponse
from pycodat.handlers.accounting.accounts_handler import AccountsHandler


class AccountingClient(PlatformClient):
    def get_accounts(self, company_id: str, **kwargs) -> AccountsPaginatedResponse:
        """Gets the accounts for a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :return: List of all of a companies accounts(a.k.a 'chart of accounts')
        :rtype: AccountsPaginatedResponse
        """

        connection_handler = AccountsHandler(self.key, self.env)
        connection = connection_handler.get_all_accounts(company_id, **kwargs)
        return connection
