from __future__ import annotations
import dataclasses
from ..shared import configresponse as shared_configresponse
from typing import Optional


@dataclasses.dataclass
class ActivateConfigPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ActivateConfigRequest:
    path_params: ActivateConfigPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ActivateConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    config_response: Optional[shared_configresponse.ConfigResponse] = dataclasses.field(default=None)
    