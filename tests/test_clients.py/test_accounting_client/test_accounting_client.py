from pycompanydata.clients.accounting_client import AccountingClient
from pycompanydata.data_types.accounting.account_transactions import (
    AccountTransaction,
    AccountTransactionsPaginatedResponse,
)
from pycompanydata.data_types.accounting.accounts import (
    Account,
    AccountsPaginatedResponse,
)
from pycompanydata.handlers.accounting.account_transaction_handler import (
    AccountTransactionHandler,
)
from pycompanydata.handlers.accounting.accounts_handler import AccountsHandler


class TestAccountingClientClass:
    def test_get_accounts(self, basic_auth_key, monkeypatch, accounts, random_guid):
        monkeypatch.setattr(AccountsHandler, "get_all_accounts", accounts)
        codat = AccountingClient(key=basic_auth_key, env="prod")
        result = codat.get_accounts(random_guid)
        assert type(result) == AccountsPaginatedResponse

    def test_get_account(self, basic_auth_key, monkeypatch, account, random_guid):
        monkeypatch.setattr(AccountsHandler, "get_single_account", account)
        codat = AccountingClient(key=basic_auth_key, env="prod")
        result = codat.get_account(random_guid, random_guid)
        assert type(result) == Account

    def test_get_account_transactions(
        self, basic_auth_key, monkeypatch, account_transactions, random_guid
    ):
        monkeypatch.setattr(
            AccountTransactionHandler,
            "get_all_account_transactions",
            account_transactions,
        )
        codat = AccountingClient(key=basic_auth_key, env="prod")
        result = codat.get_account_transactions(random_guid, random_guid)
        assert type(result) == AccountTransactionsPaginatedResponse

    def test_get_account_transaction(
        self, basic_auth_key, monkeypatch, account_transaction, random_guid
    ):
        monkeypatch.setattr(
            AccountTransactionHandler,
            "get_single_account_transaction",
            account_transaction,
        )
        codat = AccountingClient(key=basic_auth_key, env="prod")
        result = codat.get_account_transaction(random_guid, random_guid, random_guid)
        assert type(result) == AccountTransaction
