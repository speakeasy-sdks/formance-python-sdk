from __future__ import annotations
import dataclasses
from ..shared import transactiondata as shared_transactiondata
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Transactions:
    transactions: list[shared_transactiondata.TransactionData] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions') }})
    