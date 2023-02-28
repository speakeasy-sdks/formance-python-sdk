from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorsConfigsResponseDataConnectorKey:
    data_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorsConfigsResponseDataConnector:
    key: ConnectorsConfigsResponseDataConnectorKey = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorsConfigsResponseData:
    connector: ConnectorsConfigsResponseDataConnector = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('connector') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorsConfigsResponse:
    data: ConnectorsConfigsResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    