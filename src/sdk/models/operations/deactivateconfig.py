from __future__ import annotations
import dataclasses
from ..shared import configresponse as shared_configresponse
from typing import Optional


@dataclasses.dataclass
class DeactivateConfigPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeactivateConfigRequest:
    path_params: DeactivateConfigPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeactivateConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    config_response: Optional[shared_configresponse.ConfigResponse] = dataclasses.field(default=None)
    