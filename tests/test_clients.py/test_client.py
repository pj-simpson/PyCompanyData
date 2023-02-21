import pytest

from pycompanydata.clients.accounting_client import AccountingClient
from pycompanydata.clients.base_client import BaseClient
from pycompanydata.clients.platform_client import PlatformClient


@pytest.mark.parametrize("client", [BaseClient, AccountingClient, PlatformClient])
class TestClientClassInit:
    def test_client_init_with_api_key(self, client, basic_auth_key, encoded_auth_key):
        codat = client(key=basic_auth_key)
        assert codat.key == encoded_auth_key

    def test_client_init_with_auth_header(self, client, auth_header, encoded_auth_key):
        codat = client(key=auth_header)
        assert codat.key == encoded_auth_key

    def test_client_init_defaults_to_prod(self, client, basic_auth_key):
        codat = client(key=basic_auth_key)
        assert codat.env == "prod"

    def test_client_init_can_specify_environment(self, client):
        codat = client(key="NotImportant", env="uat")
        assert codat.env == "uat"

    def test_client_init_missing_key(self, client):
        with pytest.raises(TypeError):
            client(env="prod")
