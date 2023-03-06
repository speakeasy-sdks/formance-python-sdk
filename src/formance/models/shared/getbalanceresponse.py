from __future__ import annotations
import dataclasses
from ..shared import balancewithassets as shared_balancewithassets
from dataclasses_json import Undefined, dataclass_json
from formance import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBalanceResponse:
    data: shared_balancewithassets.BalanceWithAssets = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    