from __future__ import annotations
import dataclasses
from ..shared import error as shared_error
from ..shared import getworkflowoccurrenceresponse as shared_getworkflowoccurrenceresponse
from typing import Optional


@dataclasses.dataclass
class GetWorkflowOccurrencePathParams:
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flowId', 'style': 'simple', 'explode': False }})
    run_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'runId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetWorkflowOccurrenceRequest:
    path_params: GetWorkflowOccurrencePathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetWorkflowOccurrenceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get_workflow_occurrence_response: Optional[shared_getworkflowoccurrenceresponse.GetWorkflowOccurrenceResponse] = dataclasses.field(default=None)
    