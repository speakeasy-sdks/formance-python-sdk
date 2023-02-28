from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LedgerStorage:
    driver: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('driver') }})
    ledgers: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('ledgers') }})
    