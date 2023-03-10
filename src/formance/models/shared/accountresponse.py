from __future__ import annotations
import dataclasses
from ..shared import accountwithvolumesandbalances as shared_accountwithvolumesandbalances
from dataclasses_json import Undefined, dataclass_json
from formance import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountResponse:
    data: shared_accountwithvolumesandbalances.AccountWithVolumesAndBalances = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    