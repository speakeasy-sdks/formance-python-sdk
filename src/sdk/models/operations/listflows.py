from __future__ import annotations
import dataclasses
from ..shared import error as shared_error
from ..shared import listworkflowsresponse as shared_listworkflowsresponse
from typing import Optional


@dataclasses.dataclass
class ListFlowsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    list_workflows_response: Optional[shared_listworkflowsresponse.ListWorkflowsResponse] = dataclasses.field(default=None)
    