__version__ = "0.1.1"

from pycodat.clients.accounting_client import AccountingClient
from pycodat.clients.platform_client import PlatformClient


class Codat(AccountingClient, PlatformClient):
    """The main class which acts as an interface to the Codat API."""

    pass
