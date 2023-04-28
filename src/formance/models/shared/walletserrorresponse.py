"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from formance import utils

class WalletsErrorResponseErrorCodeEnum(str, Enum):
    VALIDATION = 'VALIDATION'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletsErrorResponse:
    r"""Error"""
    
    error_code: WalletsErrorResponseErrorCodeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorCode') }})

    error_message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage') }})

    