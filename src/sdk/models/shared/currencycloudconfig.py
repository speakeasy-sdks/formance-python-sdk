from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CurrencyCloudConfig:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKey') }})
    login_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loginID') }})
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    polling_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pollingPeriod'), 'exclude': lambda f: f is None }})
    