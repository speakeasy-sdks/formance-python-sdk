from __future__ import annotations
import dataclasses
from ..shared import hold as shared_hold
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DebitWalletResponse:
    data: shared_hold.Hold = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    