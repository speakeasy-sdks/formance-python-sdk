import requests
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Clients:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
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
        
        url = utils.generate_url(base_url, "/api/auth/clients/{clientId}/scopes/{scopeId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("PUT", url)
        content_type = r.headers.get("Content-Type")

        res = operations.AddScopeToClientResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def create_client(self, request: operations.CreateClientRequest) -> operations.CreateClientResponse:
        r"""Create client
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/auth/clients"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateClientResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateClientResponse])
                res.create_client_response = out

        return res

    
    def create_secret(self, request: operations.CreateSecretRequest) -> operations.CreateSecretResponse:
        r"""Add a secret to a client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/auth/clients/{clientId}/secrets", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateSecretResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateSecretResponse])
                res.create_secret_response = out

        return res

    
    def delete_client(self, request: operations.DeleteClientRequest) -> operations.DeleteClientResponse:
        r"""Delete client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/auth/clients/{clientId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteClientResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def delete_scope_from_client(self, request: operations.DeleteScopeFromClientRequest) -> operations.DeleteScopeFromClientResponse:
        r"""Delete scope from client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/auth/clients/{clientId}/scopes/{scopeId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteScopeFromClientResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def delete_secret(self, request: operations.DeleteSecretRequest) -> operations.DeleteSecretResponse:
        r"""Delete a secret from a client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/auth/clients/{clientId}/secrets/{secretId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteSecretResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def list_clients(self) -> operations.ListClientsResponse:
        r"""List clients
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/auth/clients"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListClientsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListClientsResponse])
                res.list_clients_response = out

        return res

    
    def read_client(self, request: operations.ReadClientRequest) -> operations.ReadClientResponse:
        r"""Read client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/auth/clients/{clientId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ReadClientResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ReadClientResponse])
                res.read_client_response = out

        return res

    
    def update_client(self, request: operations.UpdateClientRequest) -> operations.UpdateClientResponse:
        r"""Update client
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/auth/clients/{clientId}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateClientResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.UpdateClientResponse])
                res.update_client_response = out

        return res

    