from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletsVolume:
    balance: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('balance') }})
    input: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('input') }})
    output: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('output') }})
    