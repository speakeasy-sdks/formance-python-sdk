from __future__ import annotations
import dataclasses
from ..shared import connector_enum as shared_connector_enum
from ..shared import connectorconfigresponse as shared_connectorconfigresponse
from typing import Optional


@dataclasses.dataclass
class ReadConnectorConfigPathParams:
    connector: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ReadConnectorConfigRequest:
    path_params: ReadConnectorConfigPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ReadConnectorConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connector_config_response: Optional[shared_connectorconfigresponse.ConnectorConfigResponse] = dataclasses.field(default=None)
    