from __future__ import annotations
import dataclasses
from ..shared import connector_enum as shared_connector_enum
from ..shared import taskresponse as shared_taskresponse
from typing import Optional


@dataclasses.dataclass
class GetConnectorTaskPathParams:
    connector: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    task_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taskId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetConnectorTaskRequest:
    path_params: GetConnectorTaskPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetConnectorTaskResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    task_response: Optional[shared_taskresponse.TaskResponse] = dataclasses.field(default=None)
    