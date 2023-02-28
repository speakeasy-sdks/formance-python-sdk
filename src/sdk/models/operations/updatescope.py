from __future__ import annotations
import dataclasses
from ..shared import updatescoperequest as shared_updatescoperequest
from ..shared import updatescoperesponse as shared_updatescoperesponse
from typing import Optional


@dataclasses.dataclass
class UpdateScopePathParams:
    scope_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'scopeId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateScopeRequest:
    path_params: UpdateScopePathParams = dataclasses.field()
    request: Optional[shared_updatescoperequest.UpdateScopeRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateScopeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    update_scope_response: Optional[shared_updatescoperesponse.UpdateScopeResponse] = dataclasses.field(default=None)
    