from __future__ import annotations
import dataclasses
from ..shared import debitwalletrequest as shared_debitwalletrequest
from ..shared import debitwalletresponse as shared_debitwalletresponse
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class DebitWalletPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DebitWalletRequest:
    path_params: DebitWalletPathParams = dataclasses.field()
    request: Optional[shared_debitwalletrequest.DebitWalletRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class DebitWalletResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    debit_wallet_response: Optional[shared_debitwalletresponse.DebitWalletResponse] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    