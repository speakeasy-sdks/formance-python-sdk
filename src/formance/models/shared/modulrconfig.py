from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from formance import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModulrConfig:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKey') }})
    api_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiSecret') }})
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    