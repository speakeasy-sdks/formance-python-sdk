from __future__ import annotations
import dataclasses
from ..shared import connector_enum as shared_connector_enum
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorsResponseData:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled'), 'exclude': lambda f: f is None }})
    provider: Optional[shared_connector_enum.ConnectorEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('provider'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorsResponse:
    data: list[ConnectorsResponseData] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    