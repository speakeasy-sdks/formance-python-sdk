from __future__ import annotations
import dataclasses
from enum import Enum

class ConnectorEnum(str, Enum):
    STRIPE = "STRIPE"
    DUMMY_PAY = "DUMMY-PAY"
    WISE = "WISE"
    MODULR = "MODULR"
    CURRENCY_CLOUD = "CURRENCY-CLOUD"
    BANKING_CIRCLE = "BANKING-CIRCLE"
