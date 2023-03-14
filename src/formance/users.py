import requests as requests_http
from . import utils
from formance.models import operations, shared
from typing import Optional

class Users:
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
        
    def list_users(self) -> operations.ListUsersResponse:
        r"""List users
        List users
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/auth/users'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListUsersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListUsersResponse])
                res.list_users_response = out

        return res

    def read_user(self, request: operations.ReadUserRequest) -> operations.ReadUserResponse:
        r"""Read user
        Read user
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ReadUserRequest, base_url, '/api/auth/users/{userId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ReadUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ReadUserResponse])
                res.read_user_response = out

        return res

    