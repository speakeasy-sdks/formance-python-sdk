from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import paymentresponse as shared_paymentresponse
from typing import Optional


@dataclasses.dataclass
class GetPaymentRequest:
    payment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'paymentId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetPaymentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    payment_response: Optional[shared_paymentresponse.PaymentResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    