__doc__ = """ SDK Documentation: Open, modular foundation for unique payments flows

# Introduction
This API is documented in **OpenAPI format**.

# Authentication
Formance Stack offers one forms of authentication:
  - OAuth2
OAuth2 - an open protocol to allow secure authorization in a simple
and standard method from web, mobile and desktop applications.
<SecurityDefinitions />
"""
import requests as requests_http
from . import utils
from .accounts import Accounts
from .balances import Balances
from .clients import Clients
from .ledger import Ledger
from .logs import Logs
from .mapping import Mapping
from .orchestration import Orchestration
from .payments import Payments
from .scopes import Scopes
from .script import Script
from .search import Search
from .server import Server
from .stats import Stats
from .transactions import Transactions
from .users import Users
from .wallets import Wallets
from .webhooks import Webhooks
from formance.models import operations, shared
from typing import Optional

SERVERS = [
	"http://localhost",
	"https://{organization}.sandbox.formance.cloud",
]

class Formance:
    r"""SDK Documentation: Open, modular foundation for unique payments flows
    
    # Introduction
    This API is documented in **OpenAPI format**.
    
    # Authentication
    Formance Stack offers one forms of authentication:
      - OAuth2
    OAuth2 - an open protocol to allow secure authorization in a simple
    and standard method from web, mobile and desktop applications.
    <SecurityDefinitions />
    """
    accounts: Accounts
    balances: Balances
    clients: Clients
    ledger: Ledger
    logs: Logs
    mapping: Mapping
    orchestration: Orchestration
    payments: Payments
    scopes: Scopes
    script: Script
    search: Search
    server: Server
    stats: Stats
    transactions: Transactions
    users: Users
    wallets: Wallets
    webhooks: Webhooks
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _security: shared.Security
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.0.1"
    _gen_version: str = "1.8.7"

    def __init__(self) -> None:
        self._client = requests_http.Session()
        self._security_client = requests_http.Session()
        self._init_sdks()

    def config_server_url(self, server_url: str, params: dict[str, str] = None):
        if params is not None:
            self._server_url = utils.template_url(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    

    def config_client(self, client: requests_http.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        self._init_sdks()
    
    def config_security(self, security: shared.Security):
        self._security = security
        self._security_client = utils.configure_security_client(self._client, security)
        self._init_sdks()
    
    def _init_sdks(self):
        self.accounts = Accounts(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.balances = Balances(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.clients = Clients(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.ledger = Ledger(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.logs = Logs(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.mapping = Mapping(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.orchestration = Orchestration(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.payments = Payments(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.scopes = Scopes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.script = Script(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.search = Search(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.server = Server(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.stats = Stats(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transactions = Transactions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.users = Users(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.wallets = Wallets(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.webhooks = Webhooks(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    def get_server_info(self) -> operations.GetServerInfoResponse:
        r"""Get server info
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/auth/_info'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetServerInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ServerInfo])
                res.server_info = out

        return res

    def paymentsget_server_info(self) -> operations.PaymentsgetServerInfoResponse:
        r"""Get server info
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/payments/_info'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PaymentsgetServerInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ServerInfo])
                res.server_info = out

        return res

    def searchget_server_info(self) -> operations.SearchgetServerInfoResponse:
        r"""Get server info
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/search/_info'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchgetServerInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ServerInfo])
                res.server_info = out

        return res

    