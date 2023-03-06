from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from formance import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DummyPayConfig:
    directory: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('directory') }})
    file_generation_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fileGenerationPeriod'), 'exclude': lambda f: f is None }})
    file_polling_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filePollingPeriod'), 'exclude': lambda f: f is None }})
    