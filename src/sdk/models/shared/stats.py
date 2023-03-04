from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Stats:
    accounts: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts') }})
    transactions: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions') }})
    