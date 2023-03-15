from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listbalancesresponse as shared_listbalancesresponse
from typing import Optional


@dataclasses.dataclass
class ListBalancesRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListBalancesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_balances_response: Optional[shared_listbalancesresponse.ListBalancesResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    