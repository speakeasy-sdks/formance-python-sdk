from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from typing import Any, Optional


@dataclasses.dataclass
class GetLedgerInfoPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetLedgerInfoRequest:
    path_params: GetLedgerInfoPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetLedgerInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    ledger_info_response: Optional[Any] = dataclasses.field(default=None)
    