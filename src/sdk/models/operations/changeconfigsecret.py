from __future__ import annotations
import dataclasses
from ..shared import configchangesecret as shared_configchangesecret
from ..shared import configresponse as shared_configresponse
from typing import Optional


@dataclasses.dataclass
class ChangeConfigSecretPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ChangeConfigSecretRequest:
    path_params: ChangeConfigSecretPathParams = dataclasses.field()
    request: Optional[shared_configchangesecret.ConfigChangeSecret] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ChangeConfigSecretResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    config_response: Optional[shared_configresponse.ConfigResponse] = dataclasses.field(default=None)
    