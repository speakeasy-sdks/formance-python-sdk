"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ConnectorEnum(str, Enum):
    r"""The name of the connector."""
    STRIPE = "STRIPE"
    DUMMY_PAY = "DUMMY-PAY"
    WISE = "WISE"
    MODULR = "MODULR"
    CURRENCY_CLOUD = "CURRENCY-CLOUD"
    BANKING_CIRCLE = "BANKING-CIRCLE"