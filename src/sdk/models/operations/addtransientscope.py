from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class AddTransientScopePathParams:
    scope_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'scopeId', 'style': 'simple', 'explode': False }})
    transient_scope_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transientScopeId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddTransientScopeRequest:
    path_params: AddTransientScopePathParams = dataclasses.field()
    

@dataclasses.dataclass
class AddTransientScopeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    