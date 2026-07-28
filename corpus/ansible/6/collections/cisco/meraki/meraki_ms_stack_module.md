---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_ms_stack module – Modify switch stacking configuration in Meraki."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_ms_stack_module.html
fetched_at: 2026-07-27T17:00:29+00:00
---
# cisco.meraki.meraki_ms_stack module – Modify switch stacking configuration in Meraki.

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
> To use it in a playbook, specify: `cisco.meraki.meraki_ms_stack`.

New in cisco.meraki 1.3.0

- [Synopsis](meraki_ms_stack_module.md#synopsis)
- [Parameters](meraki_ms_stack_module.md#parameters)
- [Notes](meraki_ms_stack_module.md#notes)
- [Examples](meraki_ms_stack_module.md#examples)
- [Return Values](meraki_ms_stack_module.md#return-values)

## [Synopsis](meraki_ms_stack_module.md#id1)

- Allows for modification of Meraki MS switch stacks.

## [Parameters](meraki_ms_stack_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **name**  string | Name of stack. |
| **net_id**  string | ID of network which MX firewall is in. |
| **net_name**  string | Name of network which MX firewall is in. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **serials**  list / elements=string | List of switch serial numbers which should be included or removed from a stack. |
| **stack_id**  string | ID of stack which is to be modified or deleted. |
| **state**  string | Create or modify an organization.  Choices:   - `"present"` ← (default) - `"query"` - `"absent"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_ms_stack_module.md#id3)

> **Note:**
>
> - Not all actions are idempotent. Specifically, creating a new stack will error if any switch is already in a stack.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_ms_stack_module.md#id4)

```yaml+jinja
- name: Create new stack
  meraki_switch_stack:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    name: Test stack
    serials:
    - "ABCD-1231-4579"
    - "ASDF-4321-0987"

- name: Add switch to stack
  meraki_switch_stack:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    stack_id: ABC12340987
    serials:
    - "ABCD-1231-4579"

- name: Remove switch from stack
  meraki_switch_stack:
    auth_key: abc123
    state: absent
    org_name: YourOrg
    net_name: YourNet
    stack_id: ABC12340987
    serials:
    - "ABCD-1231-4579"

- name: Query one stack
  meraki_switch_stack:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
    stack_id: ABC12340987
```

## [Return Values](meraki_ms_stack_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | VPN settings.  Returned: success |
| **id**  string | ID of switch stack.  Returned: always  Sample: `"7636"` |
| **name**  string | Descriptive name of switch stack.  Returned: always  Sample: `"MyStack"` |
| **serials**  list / elements=string | List of serial numbers in switch stack.  Returned: always  Sample: `["QBZY-XWVU-TSRQ", "QBAB-CDEF-GHIJ"]` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
