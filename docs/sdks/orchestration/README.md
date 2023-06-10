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
            "saepe": 'quidem',
            "architecto": 'ipsa',
        },
        {
            "est": 'mollitia',
            "laborum": 'dolores',
            "dolorem": 'corporis',
            "explicabo": 'nobis',
        },
        {
            "omnis": 'nemo',
            "minima": 'excepturi',
        },
    ],
)

res = s.orchestration.create_workflow(req)

if res.create_workflow_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.CreateWorkflowRequest](../../models/shared/createworkflowrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateWorkflowResponse](../../models/operations/createworkflowresponse.md)**


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
    flow_id='accusantium',
)

res = s.orchestration.get_flow(req)

if res.get_workflow_response is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetFlowRequest](../../models/operations/getflowrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetFlowResponse](../../models/operations/getflowresponse.md)**


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
    flow_id='iure',
    run_id='culpa',
)

res = s.orchestration.get_workflow_occurrence(req)

if res.get_workflow_occurrence_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetWorkflowOccurrenceRequest](../../models/operations/getworkflowoccurrencerequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetWorkflowOccurrenceResponse](../../models/operations/getworkflowoccurrenceresponse.md)**


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


### Response

**[operations.ListFlowsResponse](../../models/operations/listflowsresponse.md)**


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
    flow_id='doloribus',
)

res = s.orchestration.list_runs(req)

if res.list_runs_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ListRunsRequest](../../models/operations/listrunsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.ListRunsResponse](../../models/operations/listrunsresponse.md)**


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


### Response

**[operations.OrchestrationgetServerInfoResponse](../../models/operations/orchestrationgetserverinforesponse.md)**


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
        "architecto": 'mollitia',
        "dolorem": 'culpa',
        "consequuntur": 'repellat',
        "mollitia": 'occaecati',
    },
    flow_id='numquam',
    wait=False,
)

res = s.orchestration.run_workflow(req)

if res.run_workflow_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.RunWorkflowRequest](../../models/operations/runworkflowrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.RunWorkflowResponse](../../models/operations/runworkflowresponse.md)**

