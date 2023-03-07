from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class AddScopeToClientPathParams:
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    scope_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'scopeId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddScopeToClientRequest:
    path_params: AddScopeToClientPathParams = dataclasses.field()
    

@dataclasses.dataclass
class AddScopeToClientResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    