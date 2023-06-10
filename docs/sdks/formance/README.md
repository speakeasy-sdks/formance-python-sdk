# Formance SDK

## Overview

Formance Stack API: Open, modular foundation for unique payments flows

# Introduction
This API is documented in **OpenAPI format**.

# Authentication
Formance Stack offers one forms of authentication:
  - OAuth2
OAuth2 - an open protocol to allow secure authorization in a simple
and standard method from web, mobile and desktop applications.
<SecurityDefinitions />


### Available Operations

* [get_server_info](#get_server_info) - Get server info
* [paymentsget_server_info](#paymentsget_server_info) - Get server info
* [searchget_server_info](#searchget_server_info) - Get server info

## get_server_info

Get server info

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)


res = s.formance.get_server_info()

if res.server_info is not None:
    # handle response
```


### Response

**[operations.GetServerInfoResponse](../../models/operations/getserverinforesponse.md)**


## paymentsget_server_info

Get server info

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)


res = s.formance.paymentsget_server_info()

if res.server_info is not None:
    # handle response
```


### Response

**[operations.PaymentsgetServerInfoResponse](../../models/operations/paymentsgetserverinforesponse.md)**


## searchget_server_info

Get server info

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)


res = s.formance.searchget_server_info()

if res.server_info is not None:
    # handle response
```


### Response

**[operations.SearchgetServerInfoResponse](../../models/operations/searchgetserverinforesponse.md)**

