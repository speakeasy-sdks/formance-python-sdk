"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from formance import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LedgerAccountSubject:
    identifier: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identifier') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    

