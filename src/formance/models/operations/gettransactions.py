from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import gettransactionsresponse as shared_gettransactionsresponse
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class GetTransactionsRequest:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    wallet_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'wallet_id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetTransactionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_transactions_response: Optional[shared_gettransactionsresponse.GetTransactionsResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    