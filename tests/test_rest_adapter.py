import os

import pytest
import requests

from pycodat.data_types.platform.exceptions import CodatException
from pycodat.rest_adapter import RestAdapter


class TestRestAdapterInit:
    def test_rest_adapter_init_prod_host(self, encoded_auth_key):
        rest_adapter = RestAdapter("prod", encoded_auth_key)
        assert rest_adapter.host == "https://api.codat.io/"
        assert rest_adapter.headers == {"Authorization": f"Basic {encoded_auth_key}"}

    def test_rest_adapter_init_uat_host(self, encoded_auth_key):
        rest_adapter = RestAdapter("uat", encoded_auth_key)
        assert rest_adapter.host == "https://api-uat.codat.io/"
        assert rest_adapter.headers == {"Authorization": f"Basic {encoded_auth_key}"}

    def test_rest_adapter_incorrect_env(self, encoded_auth_key):
        with pytest.raises(TypeError):
            rest_adapter = RestAdapter("stage", encoded_auth_key)

    def test_rest_adapter_no_credentials(self):
        with pytest.raises(TypeError):
            rest_adapter = RestAdapter(host="prod")

    def test_rest_adapter_no_env(self, encoded_auth_key):
        with pytest.raises(TypeError):
            rest_adapter = RestAdapter(key=encoded_auth_key)


class TestRestAdapterGet:
    def test_rest_adapter_get(
        self, monkeypatch, basic_rest_adapter, mock_successful_get
    ):

        monkeypatch.setattr(requests, "get", mock_successful_get)
        rest_adapter = basic_rest_adapter
        response = rest_adapter.get("somepath/")
        assert response["mock_key"] == "mock_response"

    def test_rest_adapter_get_non_200_resp(
        self, monkeypatch, basic_rest_adapter, mock_404_get
    ):
        with pytest.raises(CodatException):
            monkeypatch.setattr(requests, "get", mock_404_get)
            rest_adapter = basic_rest_adapter
            response = rest_adapter.get("some/other/path/")

    def test_rest_adapter_get_no_path_supplied(self, basic_rest_adapter):
        with pytest.raises(TypeError):
            rest_adapter = basic_rest_adapter
            response = rest_adapter.get()

    def test_rest_adapter_kwargs(
        self, monkeypatch, basic_rest_adapter, mock_successful_get
    ):
        monkeypatch.setattr(requests, "get", mock_successful_get)
        rest_adapter = basic_rest_adapter
        response = rest_adapter.get("somepath/", me="thing", you=0)
        assert response["mock_key"] == "mock_response"


class TestRestAdapterEnvironments:
    @pytest.mark.skip(reason="Need to research monkeypatching env variables more")
    def test_rest_adapter_dev_init_no_CODAT_DEV_ENV_set(self, encoded_auth_key):
        rest_adapter = RestAdapter("dev", encoded_auth_key)
        assert rest_adapter.environments.dev == "api.codat.io"
        assert rest_adapter.host == "https://api.codat.io/"

    @pytest.mark.skip(reason="Need to research monkeypatching env variables more")
    def test_rest_adapter_dev_init_CODAT_DEV_ENV_set_correctly(
        self, dev_env_setup, encoded_auth_key
    ):

        # >>> from collections import namedtuple
        # >>> Environments = namedtuple("Environments", ["prod", "uat","dev"])
        # >>> environments = Environments("api.codat.io", "api-uat.codat.io", os.environ.get('CODAT_DEV_ENV','api.codat.io'))
        # >>> environments.dev
        # 'integration.codat.io'

        rest_adapter = RestAdapter("dev", encoded_auth_key)
        assert rest_adapter.environments.dev == "something.com"
        assert rest_adapter.host == "https://something.com/"
