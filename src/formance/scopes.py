import requests as requests_http
from . import utils
from formance.models import operations, shared
from typing import Optional

class Scopes:
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
        
    def add_transient_scope(self, request: operations.AddTransientScopeRequest) -> operations.AddTransientScopeResponse:
        r"""Add a transient scope to a scope
        Add a transient scope to a scope
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/api/auth/scopes/{scopeId}/transient/{transientScopeId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('PUT', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddTransientScopeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass

        return res

    def create_scope(self, request: operations.CreateScopeRequest) -> operations.CreateScopeResponse:
        r"""Create scope
        Create scope
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/auth/scopes'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateScopeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateScopeResponse])
                res.create_scope_response = out

        return res

    def delete_scope(self, request: operations.DeleteScopeRequest) -> operations.DeleteScopeResponse:
        r"""Delete scope
        Delete scope
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/api/auth/scopes/{scopeId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteScopeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass

        return res

    def delete_transient_scope(self, request: operations.DeleteTransientScopeRequest) -> operations.DeleteTransientScopeResponse:
        r"""Delete a transient scope from a scope
        Delete a transient scope from a scope
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/api/auth/scopes/{scopeId}/transient/{transientScopeId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteTransientScopeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass

        return res

    def list_scopes(self) -> operations.ListScopesResponse:
        r"""List scopes
        List Scopes
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/auth/scopes'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListScopesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListScopesResponse])
                res.list_scopes_response = out

        return res

    def read_scope(self, request: operations.ReadScopeRequest) -> operations.ReadScopeResponse:
        r"""Read scope
        Read scope
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/api/auth/scopes/{scopeId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ReadScopeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ReadScopeResponse])
                res.read_scope_response = out

        return res

    def update_scope(self, request: operations.UpdateScopeRequest) -> operations.UpdateScopeResponse:
        r"""Update scope
        Update scope
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/api/auth/scopes/{scopeId}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateScopeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UpdateScopeResponse])
                res.update_scope_response = out

        return res

    