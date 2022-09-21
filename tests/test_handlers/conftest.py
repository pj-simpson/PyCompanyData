import pytest


@pytest.fixture(name="envs", params=("prod", "uat"))
# this uses pytest's request fixture - not an http request!
def _envs(request):
    return request.param
