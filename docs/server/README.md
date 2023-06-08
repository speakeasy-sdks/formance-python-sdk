# server

## Overview

Everything related to Server

### Available Operations

* [get_info](#get_info) - Show server information

## get_info

Show server information

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)


res = s.server.get_info()

if res.config_info_response is not None:
    # handle response
```
