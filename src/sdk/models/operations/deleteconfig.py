from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class DeleteConfigPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteConfigRequest:
    path_params: DeleteConfigPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    