from __future__ import annotations
import dataclasses
from ..shared import createscoperequest as shared_createscoperequest
from ..shared import createscoperesponse as shared_createscoperesponse
from typing import Optional


@dataclasses.dataclass
class CreateScopeRequest:
    request: Optional[shared_createscoperequest.CreateScopeRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateScopeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_scope_response: Optional[shared_createscoperesponse.CreateScopeResponse] = dataclasses.field(default=None)
    