from __future__ import annotations
import dataclasses
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class VoidHoldPathParams:
    hold_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'hold_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class VoidHoldRequest:
    path_params: VoidHoldPathParams = dataclasses.field()
    

@dataclasses.dataclass
class VoidHoldResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    