from __future__ import annotations
import dataclasses
from ..shared import error as shared_error
from typing import Any, Optional


@dataclasses.dataclass
class ListRunsPathParams:
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flowId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListRunsRequest:
    path_params: ListRunsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ListRunsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    list_runs_response: Optional[Any] = dataclasses.field(default=None)
    