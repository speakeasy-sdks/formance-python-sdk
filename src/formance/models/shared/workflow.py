from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import workflowconfig as shared_workflowconfig
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from formance import utils
from marshmallow import fields


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Workflow:
    config: shared_workflowconfig.WorkflowConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('config') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    