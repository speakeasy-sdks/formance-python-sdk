import requests
from . import utils
from sdk.models import operations, shared
from typing import Any, Optional

class Payments:
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

    
    def connectors_stripe_transfer(self, request: operations.ConnectorsStripeTransferRequest) -> operations.ConnectorsStripeTransferResponse:
        r"""Transfer funds between Stripe accounts
        Execute a transfer between two Stripe accounts.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/payments/connectors/stripe/transfer"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ConnectorsStripeTransferResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[dict[str, Any]])
                res.stripe_transfer_response = out

        return res

    
    def get_connector_task(self, request: operations.GetConnectorTaskRequest) -> operations.GetConnectorTaskResponse:
        r"""Read a specific task of the connector
        Get a specific task associated to the connector.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/payments/connectors/{connector}/tasks/{taskId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetConnectorTaskResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.TaskResponse])
                res.task_response = out

        return res

    
    def get_payment(self, request: operations.GetPaymentRequest) -> operations.GetPaymentResponse:
        r"""Get a payment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/payments/payments/{paymentId}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetPaymentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaymentResponse])
                res.payment_response = out

        return res

    
    def install_connector(self, request: operations.InstallConnectorRequest) -> operations.InstallConnectorResponse:
        r"""Install a connector
        Install a connector by its name and config.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/payments/connectors/{connector}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.InstallConnectorResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def list_all_connectors(self) -> operations.ListAllConnectorsResponse:
        r"""List all installed connectors
        List all installed connectors.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/payments/connectors"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListAllConnectorsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ConnectorsResponse])
                res.connectors_response = out

        return res

    
    def list_configs_available_connectors(self) -> operations.ListConfigsAvailableConnectorsResponse:
        r"""List the configs of each available connector
        List the configs of each available connector.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/payments/connectors/configs"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListConfigsAvailableConnectorsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ConnectorsConfigsResponse])
                res.connectors_configs_response = out

        return res

    
    def list_connector_tasks(self, request: operations.ListConnectorTasksRequest) -> operations.ListConnectorTasksResponse:
        r"""List tasks from a connector
        List all tasks associated with this connector.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/payments/connectors/{connector}/tasks", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListConnectorTasksResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.TasksCursor])
                res.tasks_cursor = out

        return res

    
    def list_payments(self, request: operations.ListPaymentsRequest) -> operations.ListPaymentsResponse:
        r"""List payments
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/payments/payments"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListPaymentsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaymentsCursor])
                res.payments_cursor = out

        return res

    
    def paymentslist_accounts(self, request: operations.PaymentslistAccountsRequest) -> operations.PaymentslistAccountsResponse:
        r"""List accounts
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/payments/accounts"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.PaymentslistAccountsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.AccountsCursor])
                res.accounts_cursor = out

        return res

    
    def read_connector_config(self, request: operations.ReadConnectorConfigRequest) -> operations.ReadConnectorConfigResponse:
        r"""Read the config of a connector
        Read connector config
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/payments/connectors/{connector}/config", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ReadConnectorConfigResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ConnectorConfigResponse])
                res.connector_config_response = out

        return res

    
    def reset_connector(self, request: operations.ResetConnectorRequest) -> operations.ResetConnectorResponse:
        r"""Reset a connector
        Reset a connector by its name.
        It will remove the connector and ALL PAYMENTS generated with it.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/payments/connectors/{connector}/reset", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("POST", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ResetConnectorResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def uninstall_connector(self, request: operations.UninstallConnectorRequest) -> operations.UninstallConnectorResponse:
        r"""Uninstall a connector
        Uninstall a connector by its name.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/payments/connectors/{connector}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.UninstallConnectorResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    