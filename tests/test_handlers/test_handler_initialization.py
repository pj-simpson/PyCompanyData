import pytest

from pycompanydata.handlers.accounting.account_transaction_handler import (
    AccountTransactionHandler,
)
from pycompanydata.handlers.accounting.accounts_handler import AccountsHandler
from pycompanydata.handlers.platform.companyhandler import CompanyHandler
from pycompanydata.handlers.platform.connectionhandler import ConnectionHandler
from pycompanydata.handlers.platform.datasetmetadatahandler import DataSetHandler
from pycompanydata.handlers.platform.datastatushandler import DataStatusHandler
from pycompanydata.handlers.platform.syncsettingshandler import SyncSettingHandler
from pycompanydata.rest_adapter import RestAdapter


class TestHandlersInitialization:
    @pytest.mark.parametrize(
        "handlertype",
        [
            AccountsHandler,
            AccountTransactionHandler,
            CompanyHandler,
            ConnectionHandler,
            DataSetHandler,
            SyncSettingHandler,
            DataStatusHandler,
        ],
    )
    def test_all_handler_init(self, basic_auth_key, handlertype, envs):
        handler = handlertype(basic_auth_key, envs)
        assert handler.path == "companies/"
        assert type(handler.client) == RestAdapter
