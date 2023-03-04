from __future__ import annotations
import dataclasses
from ..shared import config as shared_config
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigInfo:
    config: shared_config.Config = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('config') }})
    server: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('server') }})
    version: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version') }})
    