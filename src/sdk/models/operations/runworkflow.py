from __future__ import annotations
import dataclasses
from ..shared import error as shared_error
from ..shared import runworkflowresponse as shared_runworkflowresponse
from typing import Optional


@dataclasses.dataclass
class RunWorkflowPathParams:
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flowId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RunWorkflowQueryParams:
    wait: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'wait', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class RunWorkflowRequest:
    path_params: RunWorkflowPathParams = dataclasses.field()
    query_params: RunWorkflowQueryParams = dataclasses.field()
    request: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class RunWorkflowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    run_workflow_response: Optional[shared_runworkflowresponse.RunWorkflowResponse] = dataclasses.field(default=None)
    