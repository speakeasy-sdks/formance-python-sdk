import requests as requests_http
from . import utils
from formance.models import operations, shared
from typing import Optional

class Clients:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def add_scope_to_client(self, request: operations.AddScopeToClientRequest) -> operations.AddScopeToClientResponse:
        r"""Add scope to client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.AddScopeToClientRequest, base_url, '/api/auth/clients/{clientId}/scopes/{scopeId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('PUT', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddScopeToClientResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass

        return res

    def create_client(self, request: shared.CreateClientRequest) -> operations.CreateClientResponse:
        r"""Create client
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/auth/clients'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateClientResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateClientResponse])
                res.create_client_response = out

        return res

    def create_secret(self, request: operations.CreateSecretRequest) -> operations.CreateSecretResponse:
        r"""Add a secret to a client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateSecretRequest, base_url, '/api/auth/clients/{clientId}/secrets', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "create_secret_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateSecretResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateSecretResponse])
                res.create_secret_response = out

        return res

    def delete_client(self, request: operations.DeleteClientRequest) -> operations.DeleteClientResponse:
        r"""Delete client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteClientRequest, base_url, '/api/auth/clients/{clientId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteClientResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass

        return res

    def delete_scope_from_client(self, request: operations.DeleteScopeFromClientRequest) -> operations.DeleteScopeFromClientResponse:
        r"""Delete scope from client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteScopeFromClientRequest, base_url, '/api/auth/clients/{clientId}/scopes/{scopeId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteScopeFromClientResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass

        return res

    def delete_secret(self, request: operations.DeleteSecretRequest) -> operations.DeleteSecretResponse:
        r"""Delete a secret from a client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteSecretRequest, base_url, '/api/auth/clients/{clientId}/secrets/{secretId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteSecretResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass

        return res

    def list_clients(self) -> operations.ListClientsResponse:
        r"""List clients
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/auth/clients'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListClientsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListClientsResponse])
                res.list_clients_response = out

        return res

    def read_client(self, request: operations.ReadClientRequest) -> operations.ReadClientResponse:
        r"""Read client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ReadClientRequest, base_url, '/api/auth/clients/{clientId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ReadClientResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ReadClientResponse])
                res.read_client_response = out

        return res

    def update_client(self, request: operations.UpdateClientRequest) -> operations.UpdateClientResponse:
        r"""Update client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateClientRequest, base_url, '/api/auth/clients/{clientId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "update_client_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateClientResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UpdateClientResponse])
                res.update_client_response = out

        return res

    