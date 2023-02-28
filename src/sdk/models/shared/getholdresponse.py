from __future__ import annotations
import dataclasses
from ..shared import expandeddebithold as shared_expandeddebithold
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHoldResponse:
    data: shared_expandeddebithold.ExpandedDebitHold = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    