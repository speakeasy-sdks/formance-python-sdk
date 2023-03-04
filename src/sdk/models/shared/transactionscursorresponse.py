from __future__ import annotations
import dataclasses
from ..shared import transaction as shared_transaction
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionsCursorResponseCursor:
    data: list[shared_transaction.Transaction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    has_more: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasMore') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize') }})
    next: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionsCursorResponse:
    cursor: TransactionsCursorResponseCursor = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursor') }})
    