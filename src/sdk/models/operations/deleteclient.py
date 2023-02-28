from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class DeleteClientPathParams:
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteClientRequest:
    path_params: DeleteClientPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteClientResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    