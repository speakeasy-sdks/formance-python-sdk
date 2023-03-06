from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from formance import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Hold:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    metadata: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    wallet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('walletID') }})
    destination: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination'), 'exclude': lambda f: f is None }})
    