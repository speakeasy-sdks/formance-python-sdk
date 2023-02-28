from __future__ import annotations
import dataclasses
from ..shared import monetary as shared_monetary
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditWalletRequest:
    amount: shared_monetary.Monetary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    sources: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sources') }})
    balance: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('balance'), 'exclude': lambda f: f is None }})
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    