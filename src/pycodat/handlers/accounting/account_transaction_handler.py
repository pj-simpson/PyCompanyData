from pycodat.data_types.accounting.account_transactions import AccountTransaction
from pycodat.handlers.base import BaseHandler


class AccountTransactionHandler(BaseHandler):

    path = "companies/"

    def get_single_account_transaction(
        self, company_id: str, connection_id: str, account_transaction_id: str
    ) -> AccountTransaction:
        result = self.client.get(
            self.path
            + company_id
            + "/connections/"
            + connection_id
            + "/data/accounttransactions/"
            + account_transaction_id
        )
        account_transaction = AccountTransaction(**result)
        return account_transaction
