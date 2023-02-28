from __future__ import annotations
import dataclasses
from ..shared import balance as shared_balance
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateBalanceResponse:
    data: shared_balance.Balance = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    