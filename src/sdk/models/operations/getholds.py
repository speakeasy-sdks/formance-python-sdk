from __future__ import annotations
import dataclasses
from ..shared import getholdsresponse as shared_getholdsresponse
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Any, Optional


@dataclasses.dataclass
class GetHoldsQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    wallet_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'walletID', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetHoldsRequest:
    query_params: GetHoldsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetHoldsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_holds_response: Optional[shared_getholdsresponse.GetHoldsResponse] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    