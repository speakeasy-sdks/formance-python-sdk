from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listwalletsresponse as shared_listwalletsresponse
from typing import Any, Optional


@dataclasses.dataclass
class ListWalletsRequest:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListWalletsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_wallets_response: Optional[shared_listwalletsresponse.ListWalletsResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    