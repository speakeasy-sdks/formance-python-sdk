from __future__ import annotations
import dataclasses
from ..shared import confirmholdrequest as shared_confirmholdrequest
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class ConfirmHoldPathParams:
    hold_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'hold_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ConfirmHoldRequest:
    path_params: ConfirmHoldPathParams = dataclasses.field()
    request: Optional[shared_confirmholdrequest.ConfirmHoldRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ConfirmHoldResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    