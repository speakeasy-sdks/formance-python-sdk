import requests
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Webhooks:
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

    
    def activate_config(self, request: operations.ActivateConfigRequest) -> operations.ActivateConfigResponse:
        r"""Activate one config
        Activate a webhooks config by ID, to start receiving webhooks to its endpoint.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/webhooks/configs/{id}/activate", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("PUT", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ActivateConfigResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ConfigResponse])
                res.config_response = out
        elif r.status_code == 304:
            pass

        return res

    
    def change_config_secret(self, request: operations.ChangeConfigSecretRequest) -> operations.ChangeConfigSecretResponse:
        r"""Change the signing secret of a config
        Change the signing secret of the endpoint of a webhooks config.
        
        If not passed or empty, a secret is automatically generated.
        The format is a random string of bytes of size 24, base64 encoded. (larger size after encoding)
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/webhooks/configs/{id}/secret/change", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ChangeConfigSecretResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ConfigResponse])
                res.config_response = out

        return res

    
    def deactivate_config(self, request: operations.DeactivateConfigRequest) -> operations.DeactivateConfigResponse:
        r"""Deactivate one config
        Deactivate a webhooks config by ID, to stop receiving webhooks to its endpoint.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/webhooks/configs/{id}/deactivate", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("PUT", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeactivateConfigResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ConfigResponse])
                res.config_response = out
        elif r.status_code == 304:
            pass

        return res

    
    def delete_config(self, request: operations.DeleteConfigRequest) -> operations.DeleteConfigResponse:
        r"""Delete one config
        Delete a webhooks config by ID.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/webhooks/configs/{id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteConfigResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def get_many_configs(self, request: operations.GetManyConfigsRequest) -> operations.GetManyConfigsResponse:
        r"""Get many configs
        Sorted by updated date descending
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/webhooks/configs"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetManyConfigsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ConfigsResponse])
                res.configs_response = out

        return res

    
    def insert_config(self, request: operations.InsertConfigRequest) -> operations.InsertConfigResponse:
        r"""Insert a new config
        Insert a new webhooks config.
        
        The endpoint should be a valid https URL and be unique.
        
        The secret is the endpoint's verification secret.
        If not passed or empty, a secret is automatically generated.
        The format is a random string of bytes of size 24, base64 encoded. (larger size after encoding)
        
        All eventTypes are converted to lower-case when inserted.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/webhooks/configs"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.InsertConfigResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ConfigResponse])
                res.config_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "text/plain"):
                res.insert_config_400_text_plain_string = r.content

        return res

    
    def test_config(self, request: operations.TestConfigRequest) -> operations.TestConfigResponse:
        r"""Test one config
        Test a config by sending a webhook to its endpoint.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/webhooks/configs/{id}/test", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.TestConfigResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.AttemptResponse])
                res.attempt_response = out

        return res

    