from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connector_enum as shared_connector_enum
from ..shared import taskscursor as shared_taskscursor
from typing import Optional


@dataclasses.dataclass
class ListConnectorTasksRequest:
    connector: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListConnectorTasksResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    tasks_cursor: Optional[shared_taskscursor.TasksCursor] = dataclasses.field(default=None)
    