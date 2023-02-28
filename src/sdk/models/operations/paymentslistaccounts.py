from __future__ import annotations
import dataclasses
from ..shared import accountscursor as shared_accountscursor
from typing import Optional


@dataclasses.dataclass
class PaymentslistAccountsQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    sort: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PaymentslistAccountsRequest:
    query_params: PaymentslistAccountsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PaymentslistAccountsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    accounts_cursor: Optional[shared_accountscursor.AccountsCursor] = dataclasses.field(default=None)
    