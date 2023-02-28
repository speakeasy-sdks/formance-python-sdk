from __future__ import annotations
import dataclasses
from ..shared import getwalletresponse as shared_getwalletresponse
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class GetWalletPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetWalletRequest:
    path_params: GetWalletPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetWalletResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_wallet_response: Optional[shared_getwalletresponse.GetWalletResponse] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    