import pytest

from pycodat.handlers.accounting.account_transaction_handler import (
    AccountTransactionHandler,
)
from pycodat.handlers.accounting.accounts_handler import AccountsHandler
from pycodat.handlers.platform.companyhandler import CompanyHandler
from pycodat.handlers.platform.connectionhandler import ConnectionHandler
from pycodat.handlers.platform.datasetmetadatahandler import DataSetHandler
from pycodat.handlers.platform.datastatushandler import DataStatusHandler
from pycodat.handlers.platform.syncsettingshandler import SyncSettingHandler
from pycodat.rest_adapter import RestAdapter


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
