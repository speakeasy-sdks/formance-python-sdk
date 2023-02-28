from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import connector_enum as shared_connector_enum
from ..shared import paymentadjustment as shared_paymentadjustment
from ..shared import paymentmetadata as shared_paymentmetadata
from ..shared import paymentstatus_enum as shared_paymentstatus_enum
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Any

class PaymentSchemeEnum(str, Enum):
    VISA = "visa"
    MASTERCARD = "mastercard"
    AMEX = "amex"
    DINERS = "diners"
    DISCOVER = "discover"
    JCB = "jcb"
    UNIONPAY = "unionpay"
    SEPA_DEBIT = "sepa debit"
    SEPA_CREDIT = "sepa credit"
    SEPA = "sepa"
    APPLE_PAY = "apple pay"
    GOOGLE_PAY = "google pay"
    A2A = "a2a"
    ACH_DEBIT = "ach debit"
    ACH = "ach"
    RTP = "rtp"
    UNKNOWN = "unknown"
    OTHER = "other"

class PaymentTypeEnum(str, Enum):
    PAY_IN = "PAY-IN"
    PAYOUT = "PAYOUT"
    TRANSFER = "TRANSFER"
    OTHER = "OTHER"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Payment:
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountID') }})
    adjustments: list[shared_paymentadjustment.PaymentAdjustment] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('adjustments') }})
    asset: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('asset') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    initial_amount: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('initialAmount') }})
    metadata: list[shared_paymentmetadata.PaymentMetadata] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata') }})
    provider: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('provider') }})
    raw: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('raw') }})
    reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference') }})
    scheme: PaymentSchemeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('scheme') }})
    status: shared_paymentstatus_enum.PaymentStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    type: PaymentTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    