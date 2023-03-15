from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getholdresponse as shared_getholdresponse
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class GetHoldRequest:
    hold_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'holdID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetHoldResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_hold_response: Optional[shared_getholdresponse.GetHoldResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    