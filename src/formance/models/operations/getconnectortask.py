from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connector_enum as shared_connector_enum
from ..shared import taskresponse as shared_taskresponse
from typing import Optional


@dataclasses.dataclass
class GetConnectorTaskRequest:
    connector: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    task_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taskId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetConnectorTaskResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    task_response: Optional[shared_taskresponse.TaskResponse] = dataclasses.field(default=None)
    