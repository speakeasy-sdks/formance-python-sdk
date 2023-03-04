from __future__ import annotations
from enum import Enum

class PaymentStatusEnum(str, Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    TERMINATED = "TERMINATED"
    FAILED = "FAILED"
