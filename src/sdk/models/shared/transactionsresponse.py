from __future__ import annotations
import dataclasses
from ..shared import transaction as shared_transaction
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionsResponse:
    data: list[shared_transaction.Transaction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    