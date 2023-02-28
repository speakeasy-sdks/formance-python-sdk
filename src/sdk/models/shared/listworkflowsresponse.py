from __future__ import annotations
import dataclasses
from ..shared import workflow as shared_workflow
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListWorkflowsResponse:
    data: list[shared_workflow.Workflow] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    