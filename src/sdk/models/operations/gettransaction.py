from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from ..shared import transactionresponse as shared_transactionresponse
from typing import Optional


@dataclasses.dataclass
class GetTransactionPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    txid: int = dataclasses.field(metadata={'path_param': { 'field_name': 'txid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTransactionRequest:
    path_params: GetTransactionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetTransactionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    transaction_response: Optional[shared_transactionresponse.TransactionResponse] = dataclasses.field(default=None)
    