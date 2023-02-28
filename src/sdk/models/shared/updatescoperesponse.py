from __future__ import annotations
import dataclasses
from ..shared import scope as shared_scope
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateScopeResponse:
    data: Optional[shared_scope.Scope] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    