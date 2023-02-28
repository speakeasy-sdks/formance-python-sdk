from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from typing import Any, Optional


@dataclasses.dataclass
class CountAccountsPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CountAccountsQueryParams:
    address: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'address', 'style': 'form', 'explode': True }})
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    

@dataclasses.dataclass
class CountAccountsRequest:
    path_params: CountAccountsPathParams = dataclasses.field()
    query_params: CountAccountsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class CountAccountsResponse:
    content_type: str = dataclasses.field()
    headers: dict[str, list[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    