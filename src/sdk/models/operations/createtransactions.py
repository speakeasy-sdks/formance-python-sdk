from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from ..shared import transactions as shared_transactions
from ..shared import transactionsresponse as shared_transactionsresponse
from typing import Optional


@dataclasses.dataclass
class CreateTransactionsPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateTransactionsRequest:
    path_params: CreateTransactionsPathParams = dataclasses.field()
    request: shared_transactions.Transactions = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateTransactionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    transactions_response: Optional[shared_transactionsresponse.TransactionsResponse] = dataclasses.field(default=None)
    