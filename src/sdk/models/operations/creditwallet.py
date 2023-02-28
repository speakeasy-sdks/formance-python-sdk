from __future__ import annotations
import dataclasses
from ..shared import creditwalletrequest as shared_creditwalletrequest
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class CreditWalletPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreditWalletRequest:
    path_params: CreditWalletPathParams = dataclasses.field()
    request: Optional[shared_creditwalletrequest.CreditWalletRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreditWalletResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    