from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateClientRequest:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    post_logout_redirect_uris: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postLogoutRedirectUris'), 'exclude': lambda f: f is None }})
    public: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('public'), 'exclude': lambda f: f is None }})
    redirect_uris: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('redirectUris'), 'exclude': lambda f: f is None }})
    trusted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trusted'), 'exclude': lambda f: f is None }})
    