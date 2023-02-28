from __future__ import annotations
import dataclasses
from ..shared import configresponse as shared_configresponse
from ..shared import configuser as shared_configuser
from typing import Optional


@dataclasses.dataclass
class InsertConfigRequest:
    request: shared_configuser.ConfigUser = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class InsertConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    config_response: Optional[shared_configresponse.ConfigResponse] = dataclasses.field(default=None)
    insert_config_400_text_plain_string: Optional[str] = dataclasses.field(default=None)
    