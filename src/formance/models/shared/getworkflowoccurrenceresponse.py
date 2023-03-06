from __future__ import annotations
import dataclasses
from ..shared import workflowoccurrence as shared_workflowoccurrence
from dataclasses_json import Undefined, dataclass_json
from formance import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWorkflowOccurrenceResponse:
    data: shared_workflowoccurrence.WorkflowOccurrence = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    