from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Any

class LogTypeEnum(str, Enum):
    NEW_TRANSACTION = "NEW_TRANSACTION"
    SET_METADATA = "SET_METADATA"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Log:
    data: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    date_: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    hash: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hash') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    type: LogTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    