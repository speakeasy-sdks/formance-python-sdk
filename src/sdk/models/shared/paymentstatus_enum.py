from __future__ import annotations
import dataclasses
from enum import Enum

class PaymentStatusEnum(str, Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    TERMINATED = "TERMINATED"
    FAILED = "FAILED"
