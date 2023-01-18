import typing

from pycodat.rest_adapter import RestAdapter
from pycodat.data_types.pagination import PaginatedResponse

T = typing.TypeVar("T")


class BaseHandler:
    def __init__(self, key: str, env: str) -> None:
        self.key = key
        self.env = env
        self.client = RestAdapter(host=env, key=key)
        self.path = "companies/"

    def _get_paginated_response(self, model, path, **kwargs) -> PaginatedResponse[T]:
        kwargs = {key: value for key, value in kwargs.items() if value is not None}
        response = self.client.get(path, **kwargs)
        return PaginatedResponse[model](**response)

    def _get_all_pages(self, model, path, **kwargs) -> typing.List[T]:
        page_number = 1
        results = []
        while True:
            response = self._get_paginated_response(model, path, page=page_number, pageSize=100, **kwargs)
            results += response.results
            page_number += 1
            if not response.links.next:
                break
        return results


