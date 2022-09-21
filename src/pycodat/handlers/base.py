from pycodat.rest_adapter import RestAdapter


class BaseHandler:
    def __init__(self, key: str, env: str) -> None:
        self.key = key
        self.env = env
        self.client = RestAdapter(host=env, key=key)
        self.path = "companies/"
