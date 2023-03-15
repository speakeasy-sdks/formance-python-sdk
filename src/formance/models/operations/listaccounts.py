from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accountscursorresponse as shared_accountscursorresponse
from ..shared import errorresponse as shared_errorresponse
from enum import Enum
from typing import Any, Optional

class ListAccountsBalanceOperatorEnum(str, Enum):
    GTE = "gte"
    LTE = "lte"
    GT = "gt"
    LT = "lt"
    E = "e"
    NE = "ne"


@dataclasses.dataclass
class ListAccountsRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    address: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'address', 'style': 'form', 'explode': True }})
    after: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    balance: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'balance', 'style': 'form', 'explode': True }})
    balance_operator: Optional[ListAccountsBalanceOperatorEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'balanceOperator', 'style': 'form', 'explode': True }})
    balance_operator_deprecated: Optional[ListAccountsBalanceOperatorEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'balance_operator', 'style': 'form', 'explode': True }})
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    page_size_deprecated: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    pagination_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pagination_token', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListAccountsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    accounts_cursor_response: Optional[shared_accountscursorresponse.AccountsCursorResponse] = dataclasses.field(default=None)
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    