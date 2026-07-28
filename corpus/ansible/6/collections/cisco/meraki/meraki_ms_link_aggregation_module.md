---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_ms_link_aggregation module – Manage link aggregations on MS switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_ms_link_aggregation_module.html
fetched_at: 2026-07-27T17:00:28+00:00
---
# cisco.meraki.meraki_ms_link_aggregation module – Manage link aggregations on MS switches

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
> To use it in a playbook, specify: `cisco.meraki.meraki_ms_link_aggregation`.

New in cisco.meraki 1.2.0

- [Synopsis](meraki_ms_link_aggregation_module.md#synopsis)
- [Parameters](meraki_ms_link_aggregation_module.md#parameters)
- [Notes](meraki_ms_link_aggregation_module.md#notes)
- [Examples](meraki_ms_link_aggregation_module.md#examples)
- [Return Values](meraki_ms_link_aggregation_module.md#return-values)

## [Synopsis](meraki_ms_link_aggregation_module.md#id1)

- Allows for management of MS switch link aggregations in a Meraki environment.

## [Parameters](meraki_ms_link_aggregation_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **lag_id**  string | ID of lag to query or modify. |
| **net_id**  string | ID of network. |
| **net_name**  string | Name of network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | Specifies whether SNMP information should be queried or modified.  Choices:   - `"absent"` - `"query"` - `"present"` ← (default) |
| **switch_ports**  list / elements=dictionary | List of switchports to include in link aggregation. |
| **port_id**  string | Port number which should be included in link aggregation. |
| **serial**  string | Serial number of switch to own link aggregation. |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_ms_link_aggregation_module.md#id3)

> **Note:**
>
> - Switch profile ports are not supported in this module.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_ms_link_aggregation_module.md#id4)

```yaml+jinja
- name: Create LAG
  meraki_ms_link_aggregation:
    auth_key: '{{auth_key}}'
    state: present
    org_name: '{{test_org_name}}'
    net_name: '{{test_switch_net_name}}'
    switch_ports:
      - serial: '{{serial_switch}}'
        port_id: "1"
      - serial: '{{serial_switch}}'
        port_id: "2"
  delegate_to: localhost

- name: Update LAG
  meraki_ms_link_aggregation:
    auth_key: '{{auth_key}}'
    state: present
    org_name: '{{test_org_name}}'
    net_name: '{{test_switch_net_name}}'
    lag_id: '{{lag_id}}'
    switch_ports:
      - serial: '{{serial_switch}}'
        port_id: "1"
      - serial: '{{serial_switch}}'
        port_id: "2"
      - serial: '{{serial_switch}}'
        port_id: "3"
      - serial: '{{serial_switch}}'
        port_id: "4"
  delegate_to: localhost
```

## [Return Values](meraki_ms_link_aggregation_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | List of aggregated links.  Returned: success |
| **id**  string | ID of link aggregation.  Returned: success  Sample: `"MTK3M4A2ZDdfM3=="` |
| **switch_ports**  complex | List of switch ports to be included in link aggregation.  Returned: success |
| **port_id**  string | Port number.  Returned: success  Sample: `"1"` |
| **serial**  string | Serial number of switch on which port resides.  Returned: success  Sample: `"ABCD-1234-WXYZ"` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
