# payments

## Overview

Everything related to Payments

### Available Operations

* [connectors_stripe_transfer](#connectors_stripe_transfer) - Transfer funds between Stripe accounts
* [get_connector_task](#get_connector_task) - Read a specific task of the connector
* [get_payment](#get_payment) - Get a payment
* [install_connector](#install_connector) - Install a connector
* [list_all_connectors](#list_all_connectors) - List all installed connectors
* [list_configs_available_connectors](#list_configs_available_connectors) - List the configs of each available connector
* [list_connector_tasks](#list_connector_tasks) - List tasks from a connector
* [list_payments](#list_payments) - List payments
* [paymentslist_accounts](#paymentslist_accounts) - List accounts
* [read_connector_config](#read_connector_config) - Read the config of a connector
* [reset_connector](#reset_connector) - Reset a connector
* [uninstall_connector](#uninstall_connector) - Uninstall a connector

## connectors_stripe_transfer

Execute a transfer between two Stripe accounts.

### Example Usage

```python
import formance
from formance.models import shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = shared.StripeTransferRequest(
    amount=100,
    asset='USD',
    destination='acct_1Gqj58KZcSIg2N2q',
    metadata={
        "quasi": 'reiciendis',
        "voluptatibus": 'vero',
        "nihil": 'praesentium',
    },
)

res = s.payments.connectors_stripe_transfer(req)

if res.stripe_transfer_response is not None:
    # handle response
```

## get_connector_task

Get a specific task associated to the connector.

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.GetConnectorTaskRequest(
    connector=shared.ConnectorEnum.BANKING_CIRCLE,
    task_id='ipsa',
)

res = s.payments.get_connector_task(req)

if res.task_response is not None:
    # handle response
```

## get_payment

Get a payment

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.GetPaymentRequest(
    payment_id='omnis',
)

res = s.payments.get_payment(req)

if res.payment_response is not None:
    # handle response
```

## install_connector

Install a connector by its name and config.

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.InstallConnectorRequest(
    request_body=shared.WiseConfig(
        api_key='XXX',
    ),
    connector=shared.ConnectorEnum.CURRENCY_CLOUD,
)

res = s.payments.install_connector(req)

if res.status_code == 200:
    # handle response
```

## list_all_connectors

List all installed connectors.

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


res = s.payments.list_all_connectors()

if res.connectors_response is not None:
    # handle response
```

## list_configs_available_connectors

List the configs of each available connector.

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


res = s.payments.list_configs_available_connectors()

if res.connectors_configs_response is not None:
    # handle response
```

## list_connector_tasks

List all tasks associated with this connector.

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ListConnectorTasksRequest(
    connector=shared.ConnectorEnum.STRIPE,
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=39187,
)

res = s.payments.list_connector_tasks(req)

if res.tasks_cursor is not None:
    # handle response
```

## list_payments

List payments

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ListPaymentsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=441711,
    sort=[
        'maiores',
        'dicta',
    ],
)

res = s.payments.list_payments(req)

if res.payments_cursor is not None:
    # handle response
```

## paymentslist_accounts

List accounts

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.PaymentslistAccountsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=359444,
    sort=[
        'iusto',
        'dicta',
    ],
)

res = s.payments.paymentslist_accounts(req)

if res.accounts_cursor is not None:
    # handle response
```

## read_connector_config

Read connector config

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ReadConnectorConfigRequest(
    connector=shared.ConnectorEnum.CURRENCY_CLOUD,
)

res = s.payments.read_connector_config(req)

if res.connector_config_response is not None:
    # handle response
```

## reset_connector

Reset a connector by its name.
It will remove the connector and ALL PAYMENTS generated with it.


### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ResetConnectorRequest(
    connector=shared.ConnectorEnum.DUMMY_PAY,
)

res = s.payments.reset_connector(req)

if res.status_code == 200:
    # handle response
```

## uninstall_connector

Uninstall a connector by its name.

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.UninstallConnectorRequest(
    connector=shared.ConnectorEnum.BANKING_CIRCLE,
)

res = s.payments.uninstall_connector(req)

if res.status_code == 200:
    # handle response
```
