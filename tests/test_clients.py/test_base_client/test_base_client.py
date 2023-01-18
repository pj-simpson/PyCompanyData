from pycodat.clients.base_client import BaseClient

class TestBaseClientClass:
    def test_base_client_init_with_api_key(self, basic_auth_key, encoded_auth_key):
        codat = BaseClient(key=basic_auth_key)
        assert codat.key == encoded_auth_key
    
    def test_base_client_init_with_auth_header(self, auth_header, encoded_auth_key):
        codat = BaseClient(key=auth_header)
        assert codat.key == encoded_auth_key

    def test_base_client_init_defaults_to_prod(self, basic_auth_key):
        codat = BaseClient(key=basic_auth_key)
        assert codat.env == "prod"

    def test_base_client_init_can_specify_environment(self):
        codat = BaseClient(key="NotImportant", env = "uat")
        assert codat.env == "uat"