from __future__ import annotations
import dataclasses
from ..shared import createworkflowrequest as shared_createworkflowrequest
from ..shared import createworkflowresponse as shared_createworkflowresponse
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class CreateWorkflowRequest:
    request: Optional[shared_createworkflowrequest.CreateWorkflowRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateWorkflowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_workflow_response: Optional[shared_createworkflowresponse.CreateWorkflowResponse] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    