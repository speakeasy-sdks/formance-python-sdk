from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from formance import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TasksCursorCursor:
    data: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    has_more: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasMore') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize') }})
    next: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TasksCursor:
    cursor: TasksCursorCursor = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursor') }})
    