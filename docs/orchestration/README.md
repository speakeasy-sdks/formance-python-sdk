# orchestration

## Overview

Everything related to Orchestration

### Available Operations

* [create_workflow](#create_workflow) - Create workflow
* [get_flow](#get_flow) - Get a flow by id
* [get_workflow_occurrence](#get_workflow_occurrence) - Get a workflow occurrence by id
* [list_flows](#list_flows) - List registered flows
* [list_runs](#list_runs) - List occurrences of a workflow
* [orchestrationget_server_info](#orchestrationget_server_info) - Get server info
* [run_workflow](#run_workflow) - Run workflow

## create_workflow

Create a workflow

### Example Usage

```python
import formance
from formance.models import shared

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = shared.CreateWorkflowRequest(
    stages=[
        {
            "architecto": 'mollitia',
            "dolorem": 'culpa',
            "consequuntur": 'repellat',
            "mollitia": 'occaecati',
        },
        {
            "commodi": 'quam',
            "molestiae": 'velit',
        },
        {
            "quia": 'quis',
            "vitae": 'laborum',
            "animi": 'enim',
        },
        {
            "quo": 'sequi',
        },
    ],
)

res = s.orchestration.create_workflow(req)

if res.create_workflow_response is not None:
    # handle response
```

## get_flow

Get a flow by id

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.GetFlowRequest(
    flow_id='tenetur',
)

res = s.orchestration.get_flow(req)

if res.get_workflow_response is not None:
    # handle response
```

## get_workflow_occurrence

Get a workflow occurrence by id

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.GetWorkflowOccurrenceRequest(
    flow_id='ipsam',
    run_id='id',
)

res = s.orchestration.get_workflow_occurrence(req)

if res.get_workflow_occurrence_response is not None:
    # handle response
```

## list_flows

List registered flows

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)


res = s.orchestration.list_flows()

if res.list_workflows_response is not None:
    # handle response
```

## list_runs

List occurrences of a workflow

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.ListRunsRequest(
    flow_id='possimus',
)

res = s.orchestration.list_runs(req)

if res.list_runs_response is not None:
    # handle response
```

## orchestrationget_server_info

Get server info

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)


res = s.orchestration.orchestrationget_server_info()

if res.server_info is not None:
    # handle response
```

## run_workflow

Run workflow

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.RunWorkflowRequest(
    request_body={
        "quasi": 'error',
    },
    flow_id='temporibus',
    wait=False,
)

res = s.orchestration.run_workflow(req)

if res.run_workflow_response is not None:
    # handle response
```
