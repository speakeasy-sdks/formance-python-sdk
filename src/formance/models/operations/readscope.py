from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import readscoperesponse as shared_readscoperesponse
from typing import Optional


@dataclasses.dataclass
class ReadScopePathParams:
    scope_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'scopeId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ReadScopeRequest:
    path_params: ReadScopePathParams = dataclasses.field()
    

@dataclasses.dataclass
class ReadScopeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    read_scope_response: Optional[shared_readscoperesponse.ReadScopeResponse] = dataclasses.field(default=None)
    