---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_ms_storm_control module – Manage storm control configuration on a switch in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_ms_storm_control_module.html
fetched_at: 2026-07-28T01:32:33+00:00
---
# cisco.meraki.meraki_ms_storm_control module – Manage storm control configuration on a switch in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_ms_storm_control`.

New in cisco.meraki 0.0.1

- [DEPRECATED](meraki_ms_storm_control_module.md#deprecated)
- [Synopsis](meraki_ms_storm_control_module.md#synopsis)
- [Parameters](meraki_ms_storm_control_module.md#parameters)
- [Notes](meraki_ms_storm_control_module.md#notes)
- [Examples](meraki_ms_storm_control_module.md#examples)
- [Return Values](meraki_ms_storm_control_module.md#return-values)
- [Status](meraki_ms_storm_control_module.md#status)

## [DEPRECATED](meraki_ms_storm_control_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_switch_storm_control

## [Synopsis](meraki_ms_storm_control_module.md#id2)

- Allows for management of storm control settings for Meraki MS switches.

## [Parameters](meraki_ms_storm_control_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **broadcast_threshold**  integer | Percentage (1 to 99) of total available port bandwidth for broadcast traffic type.  Default value 100 percent rate is to clear the configuration. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **multicast_threshold**  integer | Percentage (1 to 99) of total available port bandwidth for multicast traffic type.  Default value 100 percent rate is to clear the configuration. |
| **net_id**  string | ID of network. |
| **net_name**  string | Name of network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **state**  string | Specifies whether storm control configuration should be queried or modified.  **Choices:**   - `"query"` ← (default) - `"present"` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **unknown_unicast_threshold**  integer | Percentage (1 to 99) of total available port bandwidth for unknown unicast traffic type.  Default value 100 percent rate is to clear the configuration. |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_ms_storm_control_module.md#id4)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_ms_storm_control_module.md#id5)

```yaml+jinja
- name: Set broadcast settings
  meraki_switch_storm_control:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    broadcast_threshold: 75
    multicast_threshold: 70
    unknown_unicast_threshold: 65
  delegate_to: localhost

- name: Query storm control settings
  meraki_switch_storm_control:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
  delegate_to: localhost
```

## [Return Values](meraki_ms_storm_control_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information queried or updated storm control configuration.  **Returned:** success |
| **broadcast_threshold**  integer | Percentage (1 to 99) of total available port bandwidth for broadcast traffic type.  Default value 100 percent rate is to clear the configuration.  **Returned:** success  **Sample:** `42` |
| **multicast_threshold**  integer | Percentage (1 to 99) of total available port bandwidth for multicast traffic type.  Default value 100 percent rate is to clear the configuration.  **Returned:** success  **Sample:** `42` |
| **unknown_unicast_threshold**  integer | Percentage (1 to 99) of total available port bandwidth for unknown unicast traffic type.  Default value 100 percent rate is to clear the configuration.  **Returned:** success  **Sample:** `42` |

## [Status](meraki_ms_storm_control_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_ms_storm_control_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
