from __future__ import annotations
import dataclasses
from ..shared import errorsenum_enum as shared_errorsenum_enum
from ..shared import transaction as shared_transaction
from dataclasses_json import Undefined, dataclass_json
from formance import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ScriptResponse:
    details: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    error_code: Optional[shared_errorsenum_enum.ErrorsEnumEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorCode'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage'), 'exclude': lambda f: f is None }})
    transaction: Optional[shared_transaction.Transaction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction'), 'exclude': lambda f: f is None }})
    