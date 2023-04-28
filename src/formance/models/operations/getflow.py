"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from ..shared import getworkflowresponse as shared_getworkflowresponse
from typing import Optional


@dataclasses.dataclass
class GetFlowRequest:
    
    flow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'flowId', 'style': 'simple', 'explode': False }})

    r"""The flow id"""
    

@dataclasses.dataclass
class GetFlowResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    error: Optional[shared_error.Error] = dataclasses.field(default=None)

    r"""General error"""
    get_workflow_response: Optional[shared_getworkflowresponse.GetWorkflowResponse] = dataclasses.field(default=None)

    r"""The workflow"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    