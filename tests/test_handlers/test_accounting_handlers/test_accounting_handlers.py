from pycodat.data_types.accounting.accounts import AccountsPaginatedResponse
from pycodat.handlers.accounting.accounts_handler import AccountsHandler
import pytest
from pycodat.rest_adapter import RestAdapter


class TestAccountHandlers:
    def test_accounts_handler_init(self, basic_auth_key):
        handler = AccountsHandler(basic_auth_key, "prod")
        assert handler.path == "/companies/"
        assert type(handler.client) == RestAdapter

    def test_accounts_handler_get_all_accounts(
        self, monkeypatch, accounts_raw_json, basic_auth_key, random_guid
    ):
        monkeypatch.setattr(RestAdapter, "get", accounts_raw_json)
        handler = AccountsHandler(basic_auth_key, "prod")
        company_id = random_guid()
        result = handler.get_all_accounts(company_id)

        assert type(result) == AccountsPaginatedResponse
