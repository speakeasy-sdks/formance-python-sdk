from __future__ import annotations
import dataclasses
from ..shared import walletwithbalances as shared_walletwithbalances
from dataclasses_json import Undefined, dataclass_json
from formance import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWalletResponse:
    data: shared_walletwithbalances.WalletWithBalances = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    