from __future__ import annotations
import dataclasses
from ..shared import paymentmetadatachangelog as shared_paymentmetadatachangelog
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentMetadata:
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    changelog: Optional[shared_paymentmetadatachangelog.PaymentMetadataChangelog] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changelog'), 'exclude': lambda f: f is None }})
    