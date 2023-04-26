# clients

## Overview

Everything related to Clients

### Available Operations

* [add_scope_to_client](#add_scope_to_client) - Add scope to client
* [create_client](#create_client) - Create client
* [create_secret](#create_secret) - Add a secret to a client
* [delete_client](#delete_client) - Delete client
* [delete_scope_from_client](#delete_scope_from_client) - Delete scope from client
* [delete_secret](#delete_secret) - Delete a secret from a client
* [list_clients](#list_clients) - List clients
* [read_client](#read_client) - Read client
* [update_client](#update_client) - Update client

## add_scope_to_client

Add scope to client

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.AddScopeToClientRequest(
    client_id="temporibus",
    scope_id="ab",
)

res = s.clients.add_scope_to_client(req)

if res.status_code == 200:
    # handle response
```

## create_client

Create client

### Example Usage

```python
import formance
from formance.models import shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = shared.CreateClientRequest(
    description="quis",
    metadata={
        "deserunt": "perferendis",
    },
    name="Estelle Will",
    post_logout_redirect_uris=[
        "at",
        "maiores",
        "molestiae",
        "quod",
    ],
    public=False,
    redirect_uris=[
        "esse",
        "totam",
        "porro",
        "dolorum",
    ],
    trusted=False,
)

res = s.clients.create_client(req)

if res.create_client_response is not None:
    # handle response
```

## create_secret

Add a secret to a client

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.CreateSecretRequest(
    create_secret_request=shared.CreateSecretRequest(
        metadata={
            "nam": "officia",
        },
        name="Wayne Lind",
    ),
    client_id="totam",
)

res = s.clients.create_secret(req)

if res.create_secret_response is not None:
    # handle response
```

## delete_client

Delete client

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.DeleteClientRequest(
    client_id="beatae",
)

res = s.clients.delete_client(req)

if res.status_code == 200:
    # handle response
```

## delete_scope_from_client

Delete scope from client

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.DeleteScopeFromClientRequest(
    client_id="commodi",
    scope_id="molestiae",
)

res = s.clients.delete_scope_from_client(req)

if res.status_code == 200:
    # handle response
```

## delete_secret

Delete a secret from a client

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.DeleteSecretRequest(
    client_id="modi",
    secret_id="qui",
)

res = s.clients.delete_secret(req)

if res.status_code == 200:
    # handle response
```

## list_clients

List clients

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


res = s.clients.list_clients()

if res.list_clients_response is not None:
    # handle response
```

## read_client

Read client

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ReadClientRequest(
    client_id="impedit",
)

res = s.clients.read_client(req)

if res.read_client_response is not None:
    # handle response
```

## update_client

Update client

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.UpdateClientRequest(
    update_client_request=shared.UpdateClientRequest(
        description="cum",
        metadata={
            "ipsum": "excepturi",
            "aspernatur": "perferendis",
        },
        name="Faye Cormier",
        post_logout_redirect_uris=[
            "laboriosam",
            "hic",
            "saepe",
        ],
        public=False,
        redirect_uris=[
            "in",
            "corporis",
            "iste",
        ],
        trusted=False,
    ),
    client_id="iure",
)

res = s.clients.update_client(req)

if res.update_client_response is not None:
    # handle response
```
