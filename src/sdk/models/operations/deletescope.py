from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class DeleteScopePathParams:
    scope_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'scopeId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteScopeRequest:
    path_params: DeleteScopePathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteScopeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    