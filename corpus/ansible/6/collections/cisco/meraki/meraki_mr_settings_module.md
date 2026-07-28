---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_mr_settings module – Manage general settings for Meraki wireless networks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_mr_settings_module.html
fetched_at: 2026-07-27T17:00:24+00:00
---
# cisco.meraki.meraki_mr_settings module – Manage general settings for Meraki wireless networks

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
> To use it in a playbook, specify: `cisco.meraki.meraki_mr_settings`.

- [Synopsis](meraki_mr_settings_module.md#synopsis)
- [Parameters](meraki_mr_settings_module.md#parameters)
- [Notes](meraki_mr_settings_module.md#notes)
- [Examples](meraki_mr_settings_module.md#examples)
- [Return Values](meraki_mr_settings_module.md#return-values)

## [Synopsis](meraki_mr_settings_module.md#id1)

- Allows for configuration of general settings in Meraki MR wireless networks.

## [Parameters](meraki_mr_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **ipv6_bridge_enabled**  boolean | Toggle for enabling or disabling IPv6 bridging in a network.  If enabled, SSIDs must also be configured to use bridge mode.  Choices:   - `false` - `true` |
| **led_lights_on**  boolean | Toggle for enabling or disabling LED lights on all APs in the network.  Choices:   - `false` - `true` |
| **location_analytics_enabled**  boolean | Toggle for enabling or disabling location analytics for your network.  Choices:   - `false` - `true` |
| **meshing_enabled**  boolean | Toggle for enabling or disabling meshing in a network.  Choices:   - `false` - `true` |
| **net_id**  string | ID of network. |
| **net_name**  string | Name of network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | Query or edit wireless settings.  Choices:   - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **upgrade_strategy**  string | The upgrade strategy to apply to the network.  Requires firmware version MR 26.8 or higher.  Choices:   - `"minimize_upgrade_time"` - `"minimize_client_downtime"` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_mr_settings_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mr_settings_module.md#id4)

```yaml+jinja
- name: Query all settings
  meraki_mr_settings:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost
- name: Configure settings
  meraki_mr_settings:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    upgrade_strategy: minimize_upgrade_time
    ipv6_bridge_enabled: false
    led_lights_on: true
    location_analytics_enabled: true
    meshing_enabled: true
  delegate_to: localhost
```

## [Return Values](meraki_mr_settings_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | List of wireless settings.  Returned: success |
| **ipv6_bridge_enabled**  boolean | Toggle for enabling or disabling IPv6 bridging in a network.  If enabled, SSIDs must also be configured to use bridge mode.  Returned: success  Sample: `true` |
| **led_lights_on**  boolean | Toggle for enabling or disabling LED lights on all APs in the network.  Returned: success  Sample: `true` |
| **location_analytics_enabled**  boolean | Toggle for enabling or disabling location analytics for your network.  Returned: success  Sample: `true` |
| **meshing_enabled**  boolean | Toggle for enabling or disabling meshing in a network.  Returned: success  Sample: `true` |
| **upgrade_strategy**  string | The upgrade strategy to apply to the network.  Requires firmware version MR 26.8 or higher.  Returned: success  Sample: `"minimize_upgrade_time"` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
