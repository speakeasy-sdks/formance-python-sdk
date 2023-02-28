from __future__ import annotations
import dataclasses
from ..shared import stripetransferrequest as shared_stripetransferrequest
from typing import Any, Optional


@dataclasses.dataclass
class ConnectorsStripeTransferRequest:
    request: shared_stripetransferrequest.StripeTransferRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ConnectorsStripeTransferResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    stripe_transfer_response: Optional[dict[str, Any]] = dataclasses.field(default=None)
    