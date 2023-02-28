from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from typing import Any, Optional


@dataclasses.dataclass
class AddMetadataOnTransactionPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    txid: int = dataclasses.field(metadata={'path_param': { 'field_name': 'txid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddMetadataOnTransactionRequest:
    path_params: AddMetadataOnTransactionPathParams = dataclasses.field()
    request: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class AddMetadataOnTransactionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    