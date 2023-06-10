# scopes

## Overview

Everything related to Scopes

### Available Operations

* [add_transient_scope](#add_transient_scope) - Add a transient scope to a scope
* [create_scope](#create_scope) - Create scope
* [delete_scope](#delete_scope) - Delete scope
* [delete_transient_scope](#delete_transient_scope) - Delete a transient scope from a scope
* [list_scopes](#list_scopes) - List scopes
* [read_scope](#read_scope) - Read scope
* [update_scope](#update_scope) - Update scope

## add_transient_scope

Add a transient scope to a scope

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.AddTransientScopeRequest(
    scope_id='aut',
    transient_scope_id='quasi',
)

res = s.scopes.add_transient_scope(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.AddTransientScopeRequest](../../models/operations/addtransientscoperequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.AddTransientScopeResponse](../../models/operations/addtransientscoperesponse.md)**


## create_scope

Create scope

### Example Usage

```python
import formance
from formance.models import shared

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = shared.CreateScopeRequest(
    label='error',
    metadata={
        "laborum": 'quasi',
        "reiciendis": 'voluptatibus',
        "vero": 'nihil',
        "praesentium": 'voluptatibus',
    },
)

res = s.scopes.create_scope(req)

if res.create_scope_response is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.CreateScopeRequest](../../models/shared/createscoperequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreateScopeResponse](../../models/operations/createscoperesponse.md)**


## delete_scope

Delete scope

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.DeleteScopeRequest(
    scope_id='ipsa',
)

res = s.scopes.delete_scope(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.DeleteScopeRequest](../../models/operations/deletescoperequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.DeleteScopeResponse](../../models/operations/deletescoperesponse.md)**


## delete_transient_scope

Delete a transient scope from a scope

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.DeleteTransientScopeRequest(
    scope_id='omnis',
    transient_scope_id='voluptate',
)

res = s.scopes.delete_transient_scope(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.DeleteTransientScopeRequest](../../models/operations/deletetransientscoperequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.DeleteTransientScopeResponse](../../models/operations/deletetransientscoperesponse.md)**


## list_scopes

List Scopes

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)


res = s.scopes.list_scopes()

if res.list_scopes_response is not None:
    # handle response
```


### Response

**[operations.ListScopesResponse](../../models/operations/listscopesresponse.md)**


## read_scope

Read scope

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.ReadScopeRequest(
    scope_id='cum',
)

res = s.scopes.read_scope(req)

if res.read_scope_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ReadScopeRequest](../../models/operations/readscoperequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ReadScopeResponse](../../models/operations/readscoperesponse.md)**


## update_scope

Update scope

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.UpdateScopeRequest(
    update_scope_request=shared.UpdateScopeRequest(
        label='perferendis',
        metadata={
            "reprehenderit": 'ut',
        },
    ),
    scope_id='maiores',
)

res = s.scopes.update_scope(req)

if res.update_scope_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UpdateScopeRequest](../../models/operations/updatescoperequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.UpdateScopeResponse](../../models/operations/updatescoperesponse.md)**

