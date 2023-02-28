from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class DeleteScopeFromClientPathParams:
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    scope_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'scopeId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteScopeFromClientRequest:
    path_params: DeleteScopeFromClientPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteScopeFromClientResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    