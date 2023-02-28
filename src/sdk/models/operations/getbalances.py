from __future__ import annotations
import dataclasses
from ..shared import balancescursorresponse as shared_balancescursorresponse
from ..shared import errorresponse as shared_errorresponse
from typing import Optional


@dataclasses.dataclass
class GetBalancesPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBalancesQueryParams:
    address: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'address', 'style': 'form', 'explode': True }})
    after: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    pagination_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pagination_token', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetBalancesRequest:
    path_params: GetBalancesPathParams = dataclasses.field()
    query_params: GetBalancesQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetBalancesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    balances_cursor_response: Optional[shared_balancescursorresponse.BalancesCursorResponse] = dataclasses.field(default=None)
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    