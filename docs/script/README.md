# script

## Overview

Everything related to Script

### Available Operations

* [run_script](#run_script) - Execute a Numscript

## run_script

This route is deprecated, and has been merged into `POST /{ledger}/transactions`.


### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.RunScriptRequest(
    script=shared.Script(
        metadata={
            "explicabo": "deserunt",
            "distinctio": "quibusdam",
            "labore": "modi",
            "qui": "aliquid",
        },
        plain="vars {
    account $user
    }
    send [COIN 10] (
    	source = @world
    	destination = $user
    )
    ",
        reference="order_1234",
        vars={
            "quos": "perferendis",
            "magni": "assumenda",
            "ipsam": "alias",
        },
    ),
    ledger="ledger001",
    preview=True,
)

res = s.script.run_script(req)

if res.script_response is not None:
    # handle response
```
