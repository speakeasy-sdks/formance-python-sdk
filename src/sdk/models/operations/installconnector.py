from __future__ import annotations
import dataclasses
from ..shared import connector_enum as shared_connector_enum
from typing import Any


@dataclasses.dataclass
class InstallConnectorPathParams:
    connector: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class InstallConnectorRequest:
    path_params: InstallConnectorPathParams = dataclasses.field()
    request: Any = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class InstallConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    