"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

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
    r"""local server"""
    "https://{organization}.sandbox.formance.cloud",
    r"""sandbox server"""
]
"""Contains the list of servers available to the SDK"""

class Formance:
    r"""Open, modular foundation for unique payments flows
    
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
    r"""Everything related to Accounts"""
    balances: Balances
    r"""Everything related to Balances"""
    clients: Clients
    r"""Everything related to Clients"""
    ledger: Ledger
    r"""Everything related to Ledger"""
    logs: Logs
    r"""Everything related to Logs"""
    mapping: Mapping
    r"""Everything related to Mapping"""
    orchestration: Orchestration
    r"""Everything related to Orchestration"""
    payments: Payments
    r"""Everything related to Payments"""
    scopes: Scopes
    r"""Everything related to Scopes"""
    script: Script
    r"""Everything related to Script"""
    search: Search
    r"""Everything related to Search"""
    server: Server
    r"""Everything related to Server"""
    stats: Stats
    r"""Everything related to Stats"""
    transactions: Transactions
    r"""Everything related to Transactions"""
    users: Users
    r"""Everything related to Users"""
    wallets: Wallets
    r"""Everything related to Wallets"""
    webhooks: Webhooks
    r"""Everything related to Webhooks"""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.20.1"
    _gen_version: str = "2.34.7"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
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
        r"""Get server info"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/auth/_info'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetServerInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ServerInfo])
                res.server_info = out

        return res

    
    def paymentsget_server_info(self) -> operations.PaymentsgetServerInfoResponse:
        r"""Get server info"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/payments/_info'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PaymentsgetServerInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ServerInfo])
                res.server_info = out

        return res

    
    def searchget_server_info(self) -> operations.SearchgetServerInfoResponse:
        r"""Get server info"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/search/_info'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchgetServerInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ServerInfo])
                res.server_info = out

        return res

    