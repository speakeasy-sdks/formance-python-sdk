from __future__ import annotations
import dataclasses
from ..shared import createwalletrequest as shared_createwalletrequest
from ..shared import createwalletresponse as shared_createwalletresponse
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class CreateWalletRequest:
    request: Optional[shared_createwalletrequest.CreateWalletRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateWalletResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_wallet_response: Optional[shared_createwalletresponse.CreateWalletResponse] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    