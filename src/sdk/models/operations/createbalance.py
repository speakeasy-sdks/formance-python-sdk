from __future__ import annotations
import dataclasses
from ..shared import createbalancerequest as shared_createbalancerequest
from ..shared import createbalanceresponse as shared_createbalanceresponse
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class CreateBalancePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateBalanceRequest:
    path_params: CreateBalancePathParams = dataclasses.field()
    request: Optional[shared_createbalancerequest.CreateBalanceRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateBalanceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_balance_response: Optional[shared_createbalanceresponse.CreateBalanceResponse] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    