from __future__ import annotations
import dataclasses
from ..shared import payment as shared_payment
from dataclasses_json import Undefined, dataclass_json
from formance import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentResponse:
    data: shared_payment.Payment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    