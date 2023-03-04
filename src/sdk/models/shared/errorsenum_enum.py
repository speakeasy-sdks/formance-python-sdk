from __future__ import annotations
from enum import Enum

class ErrorsEnumEnum(str, Enum):
    INTERNAL = "INTERNAL"
    INSUFFICIENT_FUND = "INSUFFICIENT_FUND"
    VALIDATION = "VALIDATION"
    CONFLICT = "CONFLICT"
    NO_SCRIPT = "NO_SCRIPT"
    COMPILATION_FAILED = "COMPILATION_FAILED"
    METADATA_OVERRIDE = "METADATA_OVERRIDE"
