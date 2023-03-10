from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import walletserrorresponse as shared_walletserrorresponse
from dataclasses_json import Undefined, dataclass_json
from formance import utils
from typing import Any, Optional


@dataclasses.dataclass
class UpdateWalletPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateWalletRequestBody:
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UpdateWalletRequest:
    path_params: UpdateWalletPathParams = dataclasses.field()
    request: Optional[UpdateWalletRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateWalletResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    