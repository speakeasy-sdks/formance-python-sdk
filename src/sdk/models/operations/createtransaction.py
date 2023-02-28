from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from ..shared import posttransaction as shared_posttransaction
from ..shared import transactionsresponse as shared_transactionsresponse
from typing import Optional


@dataclasses.dataclass
class CreateTransactionPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateTransactionQueryParams:
    preview: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'preview', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CreateTransactionRequest:
    path_params: CreateTransactionPathParams = dataclasses.field()
    query_params: CreateTransactionQueryParams = dataclasses.field()
    request: shared_posttransaction.PostTransaction = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateTransactionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    transactions_response: Optional[shared_transactionsresponse.TransactionsResponse] = dataclasses.field(default=None)
    