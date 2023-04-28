"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connector_enum as shared_connector_enum
from typing import Any, Optional


@dataclasses.dataclass
class InstallConnectorRequest:
    
    connector: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})

    r"""The name of the connector."""
    request_body: Any = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})

    

@dataclasses.dataclass
class InstallConnectorResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    