from __future__ import annotations
import dataclasses
from ..shared import error as shared_error
from ..shared import getworkflowresponse as shared_getworkflowresponse
from typing import Optional


@dataclasses.dataclass
class GetFlowPathParams:
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flowId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetFlowRequest:
    path_params: GetFlowPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetFlowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get_workflow_response: Optional[shared_getworkflowresponse.GetWorkflowResponse] = dataclasses.field(default=None)
    