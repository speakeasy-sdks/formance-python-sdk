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
        authorization="",
    ),
)

req = operations.AddScopeToClientRequest(
    client_id='error',
    scope_id='deserunt',
)

res = s.clients.add_scope_to_client(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.AddScopeToClientRequest](../../models/operations/addscopetoclientrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.AddScopeToClientResponse](../../models/operations/addscopetoclientresponse.md)**


## create_client

Create client

### Example Usage

```python
import formance
from formance.models import shared

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = shared.CreateClientRequest(
    description='suscipit',
    metadata={
        "magnam": 'debitis',
        "ipsa": 'delectus',
    },
    name='Laurie Kreiger',
    post_logout_redirect_uris=[
        'iusto',
        'excepturi',
        'nisi',
    ],
    public=False,
    redirect_uris=[
        'temporibus',
        'ab',
        'quis',
        'veritatis',
    ],
    trusted=False,
)

res = s.clients.create_client(req)

if res.create_client_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.CreateClientRequest](../../models/shared/createclientrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateClientResponse](../../models/operations/createclientresponse.md)**


## create_secret

Add a secret to a client

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.CreateSecretRequest(
    create_secret_request=shared.CreateSecretRequest(
        metadata={
            "perferendis": 'ipsam',
            "repellendus": 'sapiente',
            "quo": 'odit',
        },
        name='Wilfred Wolff',
    ),
    client_id='quod',
)

res = s.clients.create_secret(req)

if res.create_secret_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateSecretRequest](../../models/operations/createsecretrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateSecretResponse](../../models/operations/createsecretresponse.md)**


## delete_client

Delete client

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.DeleteClientRequest(
    client_id='esse',
)

res = s.clients.delete_client(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteClientRequest](../../models/operations/deleteclientrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteClientResponse](../../models/operations/deleteclientresponse.md)**


## delete_scope_from_client

Delete scope from client

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.DeleteScopeFromClientRequest(
    client_id='totam',
    scope_id='porro',
)

res = s.clients.delete_scope_from_client(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeleteScopeFromClientRequest](../../models/operations/deletescopefromclientrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.DeleteScopeFromClientResponse](../../models/operations/deletescopefromclientresponse.md)**


## delete_secret

Delete a secret from a client

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.DeleteSecretRequest(
    client_id='dolorum',
    secret_id='dicta',
)

res = s.clients.delete_secret(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteSecretRequest](../../models/operations/deletesecretrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteSecretResponse](../../models/operations/deletesecretresponse.md)**


## list_clients

List clients

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)


res = s.clients.list_clients()

if res.list_clients_response is not None:
    # handle response
```


### Response

**[operations.ListClientsResponse](../../models/operations/listclientsresponse.md)**


## read_client

Read client

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.ReadClientRequest(
    client_id='nam',
)

res = s.clients.read_client(req)

if res.read_client_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ReadClientRequest](../../models/operations/readclientrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ReadClientResponse](../../models/operations/readclientresponse.md)**


## update_client

Update client

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.UpdateClientRequest(
    update_client_request=shared.UpdateClientRequest(
        description='officia',
        metadata={
            "fugit": 'deleniti',
            "hic": 'optio',
            "totam": 'beatae',
        },
        name='Tanya Gleason',
        post_logout_redirect_uris=[
            'esse',
            'ipsum',
            'excepturi',
        ],
        public=False,
        redirect_uris=[
            'perferendis',
        ],
        trusted=False,
    ),
    client_id='ad',
)

res = s.clients.update_client(req)

if res.update_client_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateClientRequest](../../models/operations/updateclientrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateClientResponse](../../models/operations/updateclientresponse.md)**

