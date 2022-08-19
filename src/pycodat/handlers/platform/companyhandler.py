import typing

from pycodat.data_types.platform.company import Company, CompanyPaginatedResponse
from pycodat.handlers.base import BaseHandler


def set_env_and_keys_for_many_companies(
    companies: typing.List[Company], key: str, env: str
) -> None:
    for comp in companies:
        comp._set_env_and_key(key=key, env=env)


class CompanyHandler(BaseHandler):

    path = "/companies/"

    def get_all_companies(self,**kwargs) -> CompanyPaginatedResponse:
        result = self.client.get(self.path,**kwargs)
        company = CompanyPaginatedResponse(**result)
        # hack to pass the key and env so the companies so they can instatiate handlers make rest calls
        set_env_and_keys_for_many_companies(company.results, self.key, self.env)
        return company

    def get_single_company(self, company_id: str) -> Company:
        result = self.client.get(self.path + company_id)
        company = Company(**result)
        # hack to pass the key and env so the datclass returned can instatiate handlers make rest calls
        company._set_env_and_key(key=self.key, env=self.env)
        return company
