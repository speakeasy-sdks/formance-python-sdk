from __future__ import annotations
import dataclasses
from ..shared import accountresponse as shared_accountresponse
from ..shared import errorresponse as shared_errorresponse
from typing import Optional


@dataclasses.dataclass
class GetAccountPathParams:
    address: str = dataclasses.field(metadata={'path_param': { 'field_name': 'address', 'style': 'simple', 'explode': False }})
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetAccountRequest:
    path_params: GetAccountPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetAccountResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    account_response: Optional[shared_accountresponse.AccountResponse] = dataclasses.field(default=None)
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    