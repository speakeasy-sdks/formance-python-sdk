from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from formance import utils
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateWorkflowRequest:
    stages: list[dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stages') }})
    