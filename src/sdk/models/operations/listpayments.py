from __future__ import annotations
import dataclasses
from ..shared import paymentscursor as shared_paymentscursor
from typing import Optional


@dataclasses.dataclass
class ListPaymentsQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    sort: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListPaymentsRequest:
    query_params: ListPaymentsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListPaymentsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    payments_cursor: Optional[shared_paymentscursor.PaymentsCursor] = dataclasses.field(default=None)
    