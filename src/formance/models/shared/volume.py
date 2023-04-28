"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from formance import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Volume:
    
    input: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input') }})

    output: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('output') }})

    balance: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance'), 'exclude': lambda f: f is None }})

    