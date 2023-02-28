from __future__ import annotations
import dataclasses
from ..shared import listbalancesresponse as shared_listbalancesresponse
from typing import Optional


@dataclasses.dataclass
class ListBalancesPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListBalancesRequest:
    path_params: ListBalancesPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ListBalancesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_balances_response: Optional[shared_listbalancesresponse.ListBalancesResponse] = dataclasses.field(default=None)
    