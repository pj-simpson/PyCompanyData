import pytest

from pycodat.clients.accounting_client import AccountingClient
from pycodat.data_types.accounting.accounts import Account, AccountsPaginatedResponse
from pycodat.handlers.accounting.accounts_handler import AccountsHandler


class TestAccountingClientClass:
    def test_accounting_class_init(self, basic_auth_key, encoded_auth_key):
        codat = AccountingClient(key=basic_auth_key, env="uat")
        assert codat.key == encoded_auth_key
        assert codat.env == "uat"

    def test_accounting_class_init_not_env_supplied(
        self, basic_auth_key, encoded_auth_key
    ):
        codat = AccountingClient(key=basic_auth_key)
        assert codat.key == encoded_auth_key
        assert codat.env == "prod"

    def test_accounting_class_init_missing_key(self):
        with pytest.raises(TypeError):
            codat = AccountingClient(env="prod")

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
