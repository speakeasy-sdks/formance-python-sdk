from __future__ import annotations
import dataclasses
from ..shared import getholdresponse as shared_getholdresponse
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class GetHoldPathParams:
    hold_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'holdID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetHoldRequest:
    path_params: GetHoldPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetHoldResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_hold_response: Optional[shared_getholdresponse.GetHoldResponse] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    