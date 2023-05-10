"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from formance.models import operations, shared
from typing import Optional

class Script:
    r"""Everything related to Script"""
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
        
    
    def run_script(self, request: operations.RunScriptRequest) -> operations.RunScriptResponse:
        r"""Execute a Numscript
        This route is deprecated, and has been merged into `POST /{ledger}/transactions`.
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RunScriptRequest, base_url, '/api/ledger/{ledger}/script', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "script", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.RunScriptRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RunScriptResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ScriptResponse])
                res.script_response = out

        return res

    