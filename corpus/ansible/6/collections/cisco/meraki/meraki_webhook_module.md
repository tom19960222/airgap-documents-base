---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_webhook module – Manage webhooks configured in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_webhook_module.html
fetched_at: 2026-07-27T17:00:44+00:00
---
# cisco.meraki.meraki_webhook module – Manage webhooks configured in the Meraki cloud

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/cisco/meraki) (version 2.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_webhook`.

- [Synopsis](meraki_webhook_module.md#synopsis)
- [Parameters](meraki_webhook_module.md#parameters)
- [Notes](meraki_webhook_module.md#notes)
- [Examples](meraki_webhook_module.md#examples)
- [Return Values](meraki_webhook_module.md#return-values)

## [Synopsis](meraki_webhook_module.md#id1)

- Configure and query information about webhooks within the Meraki cloud.

## [Parameters](meraki_webhook_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **name**  string | Name of webhook. |
| **net_id**  string | ID of network which configuration is applied to. |
| **net_name**  aliases: network  string | Name of network which configuration is applied to. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **shared_secret**  string | Secret password to use when accessing webhook. |
| **state**  string | Specifies whether object should be queried, created/modified, or removed.  Choices:   - `"absent"` - `"present"` - `"query"` ← (default) |
| **test**  string | Indicates whether to test or query status.  Choices:   - `"test"` |
| **test_id**  string | ID of webhook test query. |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **url**  string | URL to access when calling webhook. |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |
| **webhook_id**  string | Unique ID of webhook. |

## [Notes](meraki_webhook_module.md#id3)

> **Note:**
>
> - Some of the options are likely only used for developers within Meraki.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_webhook_module.md#id4)

```yaml+jinja
- name: Create webhook
  meraki_webhook:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    name: Test_Hook
    url: https://webhook.url/
    shared_secret: shhhdonttellanyone
  delegate_to: localhost

- name: Query one webhook
  meraki_webhook:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
    name: Test_Hook
  delegate_to: localhost

- name: Query all webhooks
  meraki_webhook:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
  delegate_to: localhost

- name: Delete webhook
  meraki_webhook:
    auth_key: abc123
    state: absent
    org_name: YourOrg
    net_name: YourNet
    name: Test_Hook
  delegate_to: localhost

- name: Test webhook
  meraki_webhook:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    test: test
    url: https://webhook.url/abc123
  delegate_to: localhost

- name: Get webhook status
  meraki_webhook:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    test: status
    test_id: abc123531234
  delegate_to: localhost
```

## [Return Values](meraki_webhook_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | List of administrators.  Returned: success |
| **id**  string | Unique ID of webhook.  Returned: success  Sample: `"aHR0cHM6Ly93ZWJob22LnvpdGUvOGViNWI3NmYtYjE2Ny00Y2I4LTlmYzQtND32Mj3F5NzIaMjQ0"` |
| **name**  string | Descriptive name of webhook.  Returned: success  Sample: `"Test_Hook"` |
| **networkId**  string | ID of network containing webhook object.  Returned: success  Sample: `"N_12345"` |
| **shared_secret**  string | Password for webhook.  Returned: success  Sample: `"VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"` |
| **status**  string | Status of webhook test.  Returned: success, when testing webhook  Sample: `"enqueued"` |
| **url**  string | URL of webhook endpoint.  Returned: success  Sample: `"https://webhook.url/abc123"` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
