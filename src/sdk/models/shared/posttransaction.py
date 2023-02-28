from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import posting as shared_posting
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostTransactionScript:
    plain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('plain') }})
    vars: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('vars'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostTransaction:
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    postings: Optional[list[shared_posting.Posting]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postings'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    script: Optional[PostTransactionScript] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('script'), 'exclude': lambda f: f is None }})
    timestamp: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timestamp'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    