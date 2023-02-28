from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from ..shared import statsresponse as shared_statsresponse
from typing import Optional


@dataclasses.dataclass
class ReadStatsPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ReadStatsRequest:
    path_params: ReadStatsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ReadStatsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    stats_response: Optional[shared_statsresponse.StatsResponse] = dataclasses.field(default=None)
    