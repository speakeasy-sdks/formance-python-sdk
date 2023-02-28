from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import posting as shared_posting
from ..shared import walletsvolume as shared_walletsvolume
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletsTransaction:
    postings: list[shared_posting.Posting] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('postings') }})
    timestamp: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('timestamp'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    txid: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('txid') }})
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    post_commit_volumes: Optional[dict[str, dict[str, shared_walletsvolume.WalletsVolume]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postCommitVolumes'), 'exclude': lambda f: f is None }})
    pre_commit_volumes: Optional[dict[str, dict[str, shared_walletsvolume.WalletsVolume]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('preCommitVolumes'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    