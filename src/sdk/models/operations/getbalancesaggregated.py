from __future__ import annotations
import dataclasses
from ..shared import aggregatebalancesresponse as shared_aggregatebalancesresponse
from ..shared import errorresponse as shared_errorresponse
from typing import Optional


@dataclasses.dataclass
class GetBalancesAggregatedPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBalancesAggregatedQueryParams:
    address: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'address', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetBalancesAggregatedRequest:
    path_params: GetBalancesAggregatedPathParams = dataclasses.field()
    query_params: GetBalancesAggregatedQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetBalancesAggregatedResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    aggregate_balances_response: Optional[shared_aggregatebalancesresponse.AggregateBalancesResponse] = dataclasses.field(default=None)
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    