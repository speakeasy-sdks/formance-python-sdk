from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import confirmholdrequest as shared_confirmholdrequest
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class ConfirmHoldRequest:
    hold_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'hold_id', 'style': 'simple', 'explode': False }})
    confirm_hold_request: Optional[shared_confirmholdrequest.ConfirmHoldRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ConfirmHoldResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    