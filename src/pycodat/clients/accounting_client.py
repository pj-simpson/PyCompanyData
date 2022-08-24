from pycodat.clients.platform_client import PlatformClient
from pycodat.data_types.accounting.account_transactions import AccountTransaction
from pycodat.data_types.accounting.accounts import Account, AccountsPaginatedResponse
from pycodat.handlers.accounting.account_transaction_handler import (
    AccountTransactionHandler,
)
from pycodat.handlers.accounting.accounts_handler import AccountsHandler


class AccountingClient(PlatformClient):
    def get_accounts(self, company_id: str, **kwargs) -> AccountsPaginatedResponse:
        """Gets the accounts for a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :return: List of all of a companies accounts(a.k.a 'chart of accounts')
        :rtype: AccountsPaginatedResponse
        """

        accounts_handler = AccountsHandler(self.key, self.env)
        accounts = accounts_handler.get_all_accounts(company_id, **kwargs)
        return accounts

    def get_account(self, company_id: str, account_id: str) -> Account:
        """Gets a single account from a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :param account_id: unique identifier for an account
        :type account_id: str
        :return: A single account object
        :rtype: Account
        """
        accounts_handler = AccountsHandler(self.key, self.env)
        account = accounts_handler.get_single_account(company_id, account_id)
        return account

    def get_account_transactions(self):
        pass

    def get_account_transaction(
        self, company_id: str, connection_id: str, account_transaction_id: str
    ) -> AccountTransaction:
        """_summary_

        :param company_id: _description_
        :type company_id: str
        :param connection_id: _description_
        :type connection_id: str
        :param account_transaction_id: _description_
        :type account_transaction_id: str
        :return: _description_
        :rtype: AccountTransaction
        """

        account_transaction_handler = AccountTransactionHandler(self.key, self.env)
        account_transaction = (
            account_transaction_handler.get_single_account_transaction(
                company_id, connection_id, account_transaction_id
            )
        )
        return account_transaction
