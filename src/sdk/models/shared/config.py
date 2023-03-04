from __future__ import annotations
import dataclasses
from ..shared import ledgerstorage as shared_ledgerstorage
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Config:
    storage: shared_ledgerstorage.LedgerStorage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    