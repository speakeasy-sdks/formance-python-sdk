from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listscopesresponse as shared_listscopesresponse
from typing import Optional


@dataclasses.dataclass
class ListScopesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_scopes_response: Optional[shared_listscopesresponse.ListScopesResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    