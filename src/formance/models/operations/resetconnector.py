from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connector_enum as shared_connector_enum
from typing import Optional


@dataclasses.dataclass
class ResetConnectorRequest:
    connector: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResetConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    