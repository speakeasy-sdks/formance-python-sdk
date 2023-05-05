# users

## Overview

Everything related to Users

### Available Operations

* [list_users](#list_users) - List users
* [read_user](#read_user) - Read user

## list_users

List users

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


res = s.users.list_users()

if res.list_users_response is not None:
    # handle response
```

## read_user

Read user

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)

req = operations.ReadUserRequest(
    user_id='quasi',
)

res = s.users.read_user(req)

if res.read_user_response is not None:
    # handle response
```
