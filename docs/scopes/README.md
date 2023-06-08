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
    scope_id='commodi',
    transient_scope_id='repudiandae',
)

res = s.scopes.add_transient_scope(req)

if res.status_code == 200:
    # handle response
```

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
    label='quae',
    metadata={
        "quidem": 'molestias',
    },
)

res = s.scopes.create_scope(req)

if res.create_scope_response is not None:
    # handle response
```

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
    scope_id='excepturi',
)

res = s.scopes.delete_scope(req)

if res.status_code == 200:
    # handle response
```

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
    scope_id='pariatur',
    transient_scope_id='modi',
)

res = s.scopes.delete_transient_scope(req)

if res.status_code == 200:
    # handle response
```

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
    scope_id='praesentium',
)

res = s.scopes.read_scope(req)

if res.read_scope_response is not None:
    # handle response
```

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
        label='rem',
        metadata={
            "quasi": 'repudiandae',
            "sint": 'veritatis',
            "itaque": 'incidunt',
            "enim": 'consequatur',
        },
    ),
    scope_id='est',
)

res = s.scopes.update_scope(req)

if res.update_scope_response is not None:
    # handle response
```
