from pycompanydata.data_types.accounting.account_transactions import AccountTransaction
from pycompanydata.data_types.accounting.accounts import Account
from pycompanydata.handlers.accounting.account_transaction_handler import (
    AccountTransactionHandler,
)
from pycompanydata.handlers.accounting.accounts_handler import AccountsHandler
from pycompanydata.rest_adapter import RestAdapter


class TestAccountHandlers:
    def test_accounts_handler_get_all_accounts(
        self, monkeypatch, accounts_raw_json, basic_auth_key, random_guid
    ):
        monkeypatch.setattr(RestAdapter, "get", accounts_raw_json)
        handler = AccountsHandler(basic_auth_key, "prod")
        company_id = random_guid()
        result = handler.get_all_accounts(company_id, query="", order_by="")

        assert type(result) == list
        assert type(result[0]) == Account

    def test_account_handler_get_single_account(
        self, monkeypatch, account_raw_json, basic_auth_key, random_guid
    ):
        monkeypatch.setattr(RestAdapter, "get", account_raw_json)
        handler = AccountsHandler(basic_auth_key, "prod")
        company_id = random_guid()
        account_id = random_guid()
        result = handler.get_single_account(company_id, account_id)

        assert type(result) == Account


class TestAccountTransactionHandler:
    def test_account_transaction_handler_get_all_account_transactions(
        self, monkeypatch, account_transactions_raw_json, basic_auth_key, random_guid
    ):
        monkeypatch.setattr(RestAdapter, "get", account_transactions_raw_json)
        handler = AccountTransactionHandler(basic_auth_key, "prod")
        company_id = random_guid()
        connection_id = random_guid()

        result = handler.get_all_account_transactions(
            company_id, connection_id, query="", order_by=""
        )

        assert type(result) == list
        assert type(result[0]) == AccountTransaction

    def test_account_transaction_handler_get_single_account_transaction(
        self, monkeypatch, account_transaction_raw_json, basic_auth_key, random_guid
    ):
        monkeypatch.setattr(RestAdapter, "get", account_transaction_raw_json)
        handler = AccountTransactionHandler(basic_auth_key, "prod")
        company_id = random_guid()
        connection_id = random_guid()
        account_id = random_guid()

        result = handler.get_single_account_transaction(
            company_id, connection_id, account_id
        )

        assert type(result) == AccountTransaction
