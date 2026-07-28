---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_mx_uplink_bandwidth module – Manage uplinks on Meraki MX appliances"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_mx_uplink_bandwidth_module.html
fetched_at: 2026-07-28T01:32:43+00:00
---
# cisco.meraki.meraki_mx_uplink_bandwidth module – Manage uplinks on Meraki MX appliances

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/ui/repo/published/cisco/meraki/) (version 2.17.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_uplink_bandwidth`.

New in cisco.meraki 1.1.0

- [DEPRECATED](meraki_mx_uplink_bandwidth_module.md#deprecated)
- [Synopsis](meraki_mx_uplink_bandwidth_module.md#synopsis)
- [Parameters](meraki_mx_uplink_bandwidth_module.md#parameters)
- [Notes](meraki_mx_uplink_bandwidth_module.md#notes)
- [Examples](meraki_mx_uplink_bandwidth_module.md#examples)
- [Return Values](meraki_mx_uplink_bandwidth_module.md#return-values)
- [Status](meraki_mx_uplink_bandwidth_module.md#status)

## [DEPRECATED](meraki_mx_uplink_bandwidth_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_appliance_traffic_shaping_uplink_bandwidth

## [Synopsis](meraki_mx_uplink_bandwidth_module.md#id2)

- Configure and query information about uplinks on Meraki MX appliances.

## [Parameters](meraki_mx_uplink_bandwidth_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **cellular**  dictionary | Configuration of cellular uplink |
| **bandwidth_limits**  dictionary | Structure for configuring bandwidth limits |
| **limit_down**  integer | Maximum download speed for interface |
| **limit_up**  integer | Maximum upload speed for interface |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID of network which VLAN is in or should be in. |
| **net_name**  aliases: network  string | Name of network which VLAN is in or should be in. |
| **org_id**  string | ID of organization associated to a network. |
| **org_name**  aliases: organization  string | Name of organization associated to a network. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **state**  string | Specifies whether object should be queried, created/modified, or removed.  **Choices:**   - `"absent"` - `"present"` - `"query"` ← (default) |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |
| **wan1**  dictionary | Configuration of WAN1 uplink |
| **bandwidth_limits**  dictionary | Structure for configuring bandwidth limits |
| **limit_down**  integer | Maximum download speed for interface |
| **limit_up**  integer | Maximum upload speed for interface |
| **wan2**  dictionary | Configuration of WAN2 uplink |
| **bandwidth_limits**  dictionary | Structure for configuring bandwidth limits |
| **limit_down**  integer | Maximum download speed for interface |
| **limit_up**  integer | Maximum upload speed for interface |

## [Notes](meraki_mx_uplink_bandwidth_module.md#id4)

> **Note:**
>
> - Some of the options are likely only used for developers within Meraki.
> - Module was formerly named [cisco.meraki.meraki_mx_uplink](https://docs.ansible.com/ansible/7/collections/cisco/meraki/meraki_mx_uplink_module.html#ansible-collections-cisco-meraki-meraki-mx-uplink-module "(in Ansible v7)").
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_uplink_bandwidth_module.md#id5)

```yaml+jinja
- name: Set MX uplink settings
  meraki_mx_uplink_bandwidth:
    auth_key: '{{auth_key}}'
    state: present
    org_name: '{{test_org_name}}'
    net_name: '{{test_net_name}} - Uplink'
    wan1:
      bandwidth_limits:
        limit_down: 1000000
        limit_up: 1000
    cellular:
      bandwidth_limits:
        limit_down: 0
        limit_up: 0
  delegate_to: localhost

- name: Query MX uplink settings
  meraki_mx_uplink_bandwidth:
    auth_key: '{{auth_key}}'
    state: query
    org_name: '{{test_org_name}}'
    net_name: '{{test_net_name}} - Uplink'
  delegate_to: localhost
```

## [Return Values](meraki_mx_uplink_bandwidth_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the organization which was created or modified  **Returned:** success |
| **cellular**  complex | cellular interface  **Returned:** success |
| **bandwidth_limits**  complex | Structure for uplink bandwidth limits  **Returned:** success |
| **limit_down**  integer | Download bandwidth limit  **Returned:** success |
| **limit_up**  integer | Upload bandwidth limit  **Returned:** success |
| **wan1**  complex | WAN1 interface  **Returned:** success |
| **bandwidth_limits**  complex | Structure for uplink bandwidth limits  **Returned:** success |
| **limit_down**  integer | Download bandwidth limit  **Returned:** success |
| **limit_up**  integer | Upload bandwidth limit  **Returned:** success |
| **wan2**  complex | WAN2 interface  **Returned:** success |
| **bandwidth_limits**  complex | Structure for uplink bandwidth limits  **Returned:** success |
| **limit_down**  integer | Download bandwidth limit  **Returned:** success |
| **limit_up**  integer | Upload bandwidth limit  **Returned:** success |

## [Status](meraki_mx_uplink_bandwidth_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_mx_uplink_bandwidth_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
