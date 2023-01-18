import typing

from pycodat.clients.platform_client import BaseClient
from pycodat.data_types.accounting.account_transactions import (
    AccountTransaction,
    AccountTransactionsPaginatedResponse,
)
from pycodat.data_types.accounting.accounts import Account, AccountsPaginatedResponse
from pycodat.data_types.accounting.suppliers import Supplier
from pycodat.data_types.pagination import PaginatedResponse
from pycodat.handlers.accounting.account_transaction_handler import (
    AccountTransactionHandler,
)
from pycodat.handlers.accounting.accounts_handler import AccountsHandler
from pycodat.handlers.accounting.suppliers_handler import SuppliersHandler


class AccountingClient(BaseClient):
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

    def get_account_transactions(
        self, company_id: str, connection_id: str
    ) -> typing.List[AccountTransaction]:
        """Gets all account transactions from a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :param connection_id: Unique identifier for a company's connection
        :type connection_id: str
        :return: A list of account transactions
        :rtype: AccountTransactionsPaginatedResponse
        """

        account_transaction_handler = AccountTransactionHandler(self.key, self.env)
        account_transactions = account_transaction_handler.get_all_account_transactions(
            company_id, connection_id
        )
        return account_transactions

    def get_account_transactions_page(
        self, company_id: str, connection_id: str
    ) -> PaginatedResponse[AccountTransaction]:
        """Gets a page of account transactions from a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :param connection_id: Unique identifier for a company's connection
        :type connection_id: str
        :return: A list of account transactions
        :rtype: AccountTransactionsPaginatedResponse
        """

        account_transaction_handler = AccountTransactionHandler(self.key, self.env)
        account_transactions = account_transaction_handler.get_pageof_account_transactions(
            company_id, connection_id
        )
        return account_transactions

    def get_account_transaction(
        self, company_id: str, connection_id: str, account_transaction_id: str
    ) -> AccountTransaction:
        """Gets a single account transactions from a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :param connection_id: Unique identifier for a company's connection
        :type connection_id: str
        :param account_transaction_id: Unique identifier for an account transaction
        :type account_transaction_id: str
        :return: A single account transaction object
        :rtype: AccountTransaction
        """

        account_transaction_handler = AccountTransactionHandler(self.key, self.env)
        account_transaction = (
            account_transaction_handler.get_single_account_transaction(
                company_id, connection_id, account_transaction_id
            )
        )
        return account_transaction

    def get_supplier(self, company_id: str, supplier_id: str) -> Supplier:
        """Gets a single supplier from a company

        :param company_id: Unique identifier for a company
        :type company_id: str
        :param supplier_id: Unique identifier for the supplier
        :type supplier_id: str
        :return: A single supplier object
        :rtype: Supplier
        """
        suppliers_handler = SuppliersHandler(self.key, self.env)
        supplier = suppliers_handler.get_single_supplier(company_id, supplier_id)
        return supplier
