from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import connector_enum as shared_connector_enum
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from formance import utils
from marshmallow import fields

class PaymentsAccountTypeEnum(str, Enum):
    TARGET = "TARGET"
    SOURCE = "SOURCE"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentsAccount:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    provider: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference') }})
    type: PaymentsAccountTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    