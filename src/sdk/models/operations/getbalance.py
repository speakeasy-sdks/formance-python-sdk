from __future__ import annotations
import dataclasses
from ..shared import getbalanceresponse as shared_getbalanceresponse
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class GetBalancePathParams:
    balance_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'balanceName', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBalanceRequest:
    path_params: GetBalancePathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetBalanceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_balance_response: Optional[shared_getbalanceresponse.GetBalanceResponse] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    