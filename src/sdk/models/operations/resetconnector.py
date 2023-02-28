from __future__ import annotations
import dataclasses
from ..shared import connector_enum as shared_connector_enum


@dataclasses.dataclass
class ResetConnectorPathParams:
    connector: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResetConnectorRequest:
    path_params: ResetConnectorPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ResetConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    