<div align="center">
    <picture>
        <source srcset="https://user-images.githubusercontent.com/6267663/221572723-e77f55a3-5d19-4a13-94f8-e7b0b340d71e.svg" media="(prefers-color-scheme: dark)">
        <img src="https://user-images.githubusercontent.com/6267663/221572726-6982541c-d1cf-4d9f-9bbf-cd774a2713e6.svg">
    </picture>
   <h1>Formance Python SDK</h1>
   <p><strong>Open Source Ledger for money-moving platforms</strong></p>
   <p>Build and track custom fit money flows on a scalable financial infrastructure.</p>
   <a href="https://docs.formance.com/api/stack/v1.0#section/Introduction"><img src="https://img.shields.io/static/v1?label=Docs&message=Docs&color=000&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/formance-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/formance-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://join.slack.com/t/formance-community/shared_invite/zt-1of48xmgy-Jc6RH8gzcWf5D0qD2HBPQA"><img src="https://img.shields.io/static/v1?label=Slack&message=Join&color=7289da&style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install formance-python-sdk
```
<!-- End SDK Installation -->

[![Run on Repl.it](https://repl.it/badge/github/speakeasy-sdks/formance-python-sdk)](https://replit.com/join/edjyvnqhol-sagarbatchu1)

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


res = s.get_server_info()

if res.server_info is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [Formance SDK](docs/formance/README.md)

* [get_server_info](docs/formance/README.md#get_server_info) - Get server info
* [paymentsget_server_info](docs/formance/README.md#paymentsget_server_info) - Get server info
* [searchget_server_info](docs/formance/README.md#searchget_server_info) - Get server info

### [accounts](docs/accounts/README.md)

* [add_metadata_to_account](docs/accounts/README.md#add_metadata_to_account) - Add metadata to an account
* [count_accounts](docs/accounts/README.md#count_accounts) - Count the accounts from a ledger
* [get_account](docs/accounts/README.md#get_account) - Get account by its address
* [list_accounts](docs/accounts/README.md#list_accounts) - List accounts from a ledger

### [balances](docs/balances/README.md)

* [get_balances](docs/balances/README.md#get_balances) - Get the balances from a ledger's account
* [get_balances_aggregated](docs/balances/README.md#get_balances_aggregated) - Get the aggregated balances from selected accounts

### [clients](docs/clients/README.md)

* [add_scope_to_client](docs/clients/README.md#add_scope_to_client) - Add scope to client
* [create_client](docs/clients/README.md#create_client) - Create client
* [create_secret](docs/clients/README.md#create_secret) - Add a secret to a client
* [delete_client](docs/clients/README.md#delete_client) - Delete client
* [delete_scope_from_client](docs/clients/README.md#delete_scope_from_client) - Delete scope from client
* [delete_secret](docs/clients/README.md#delete_secret) - Delete a secret from a client
* [list_clients](docs/clients/README.md#list_clients) - List clients
* [read_client](docs/clients/README.md#read_client) - Read client
* [update_client](docs/clients/README.md#update_client) - Update client

### [ledger](docs/ledger/README.md)

* [get_ledger_info](docs/ledger/README.md#get_ledger_info) - Get information about a ledger

### [logs](docs/logs/README.md)

* [list_logs](docs/logs/README.md#list_logs) - List the logs from a ledger

### [mapping](docs/mapping/README.md)

* [get_mapping](docs/mapping/README.md#get_mapping) - Get the mapping of a ledger
* [update_mapping](docs/mapping/README.md#update_mapping) - Update the mapping of a ledger

### [orchestration](docs/orchestration/README.md)

* [create_workflow](docs/orchestration/README.md#create_workflow) - Create workflow
* [get_flow](docs/orchestration/README.md#get_flow) - Get a flow by id
* [get_workflow_occurrence](docs/orchestration/README.md#get_workflow_occurrence) - Get a workflow occurrence by id
* [list_flows](docs/orchestration/README.md#list_flows) - List registered flows
* [list_runs](docs/orchestration/README.md#list_runs) - List occurrences of a workflow
* [orchestrationget_server_info](docs/orchestration/README.md#orchestrationget_server_info) - Get server info
* [run_workflow](docs/orchestration/README.md#run_workflow) - Run workflow

### [payments](docs/payments/README.md)

* [connectors_stripe_transfer](docs/payments/README.md#connectors_stripe_transfer) - Transfer funds between Stripe accounts
* [get_connector_task](docs/payments/README.md#get_connector_task) - Read a specific task of the connector
* [get_payment](docs/payments/README.md#get_payment) - Get a payment
* [install_connector](docs/payments/README.md#install_connector) - Install a connector
* [list_all_connectors](docs/payments/README.md#list_all_connectors) - List all installed connectors
* [list_configs_available_connectors](docs/payments/README.md#list_configs_available_connectors) - List the configs of each available connector
* [list_connector_tasks](docs/payments/README.md#list_connector_tasks) - List tasks from a connector
* [list_payments](docs/payments/README.md#list_payments) - List payments
* [paymentslist_accounts](docs/payments/README.md#paymentslist_accounts) - List accounts
* [read_connector_config](docs/payments/README.md#read_connector_config) - Read the config of a connector
* [reset_connector](docs/payments/README.md#reset_connector) - Reset a connector
* [uninstall_connector](docs/payments/README.md#uninstall_connector) - Uninstall a connector

### [scopes](docs/scopes/README.md)

* [add_transient_scope](docs/scopes/README.md#add_transient_scope) - Add a transient scope to a scope
* [create_scope](docs/scopes/README.md#create_scope) - Create scope
* [delete_scope](docs/scopes/README.md#delete_scope) - Delete scope
* [delete_transient_scope](docs/scopes/README.md#delete_transient_scope) - Delete a transient scope from a scope
* [list_scopes](docs/scopes/README.md#list_scopes) - List scopes
* [read_scope](docs/scopes/README.md#read_scope) - Read scope
* [update_scope](docs/scopes/README.md#update_scope) - Update scope

### [script](docs/script/README.md)

* [~~run_script~~](docs/script/README.md#run_script) - Execute a Numscript :warning: **Deprecated**

### [search](docs/search/README.md)

* [search](docs/search/README.md#search) - Search

### [server](docs/server/README.md)

* [get_info](docs/server/README.md#get_info) - Show server information

### [stats](docs/stats/README.md)

* [read_stats](docs/stats/README.md#read_stats) - Get statistics from a ledger

### [transactions](docs/transactions/README.md)

* [create_transactions](docs/transactions/README.md#create_transactions) - Create a new batch of transactions to a ledger
* [add_metadata_on_transaction](docs/transactions/README.md#add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [count_transactions](docs/transactions/README.md#count_transactions) - Count the transactions from a ledger
* [create_transaction](docs/transactions/README.md#create_transaction) - Create a new transaction to a ledger
* [get_transaction](docs/transactions/README.md#get_transaction) - Get transaction from a ledger by its ID
* [list_transactions](docs/transactions/README.md#list_transactions) - List transactions from a ledger
* [revert_transaction](docs/transactions/README.md#revert_transaction) - Revert a ledger transaction by its ID

### [users](docs/users/README.md)

* [list_users](docs/users/README.md#list_users) - List users
* [read_user](docs/users/README.md#read_user) - Read user

### [wallets](docs/wallets/README.md)

* [confirm_hold](docs/wallets/README.md#confirm_hold) - Confirm a hold
* [create_balance](docs/wallets/README.md#create_balance) - Create a balance
* [create_wallet](docs/wallets/README.md#create_wallet) - Create a new wallet
* [credit_wallet](docs/wallets/README.md#credit_wallet) - Credit a wallet
* [debit_wallet](docs/wallets/README.md#debit_wallet) - Debit a wallet
* [get_balance](docs/wallets/README.md#get_balance) - Get detailed balance
* [get_hold](docs/wallets/README.md#get_hold) - Get a hold
* [get_holds](docs/wallets/README.md#get_holds) - Get all holds for a wallet
* [get_transactions](docs/wallets/README.md#get_transactions)
* [get_wallet](docs/wallets/README.md#get_wallet) - Get a wallet
* [list_balances](docs/wallets/README.md#list_balances) - List balances of a wallet
* [list_wallets](docs/wallets/README.md#list_wallets) - List all wallets
* [update_wallet](docs/wallets/README.md#update_wallet) - Update a wallet
* [void_hold](docs/wallets/README.md#void_hold) - Cancel a hold
* [walletsget_server_info](docs/wallets/README.md#walletsget_server_info) - Get server info

### [webhooks](docs/webhooks/README.md)

* [activate_config](docs/webhooks/README.md#activate_config) - Activate one config
* [change_config_secret](docs/webhooks/README.md#change_config_secret) - Change the signing secret of a config
* [deactivate_config](docs/webhooks/README.md#deactivate_config) - Deactivate one config
* [delete_config](docs/webhooks/README.md#delete_config) - Delete one config
* [get_many_configs](docs/webhooks/README.md#get_many_configs) - Get many configs
* [insert_config](docs/webhooks/README.md#insert_config) - Insert a new config
* [test_config](docs/webhooks/README.md#test_config) - Test one config
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
