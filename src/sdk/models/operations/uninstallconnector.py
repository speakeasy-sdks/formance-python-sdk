from __future__ import annotations
import dataclasses
from ..shared import connector_enum as shared_connector_enum


@dataclasses.dataclass
class UninstallConnectorPathParams:
    connector: shared_connector_enum.ConnectorEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UninstallConnectorRequest:
    path_params: UninstallConnectorPathParams = dataclasses.field()
    

@dataclasses.dataclass
class UninstallConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    