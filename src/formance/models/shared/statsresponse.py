from __future__ import annotations
import dataclasses
from ..shared import stats as shared_stats
from dataclasses_json import Undefined, dataclass_json
from formance import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StatsResponse:
    data: shared_stats.Stats = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    