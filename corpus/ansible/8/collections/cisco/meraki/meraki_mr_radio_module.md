---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_mr_radio module – Manage device radio settings for Meraki wireless networks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_mr_radio_module.html
fetched_at: 2026-07-28T01:32:25+00:00
---
# cisco.meraki.meraki_mr_radio module – Manage device radio settings for Meraki wireless networks

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
> To use it in a playbook, specify: `cisco.meraki.meraki_mr_radio`.

- [DEPRECATED](meraki_mr_radio_module.md#deprecated)
- [Synopsis](meraki_mr_radio_module.md#synopsis)
- [Parameters](meraki_mr_radio_module.md#parameters)
- [Notes](meraki_mr_radio_module.md#notes)
- [Examples](meraki_mr_radio_module.md#examples)
- [Return Values](meraki_mr_radio_module.md#return-values)
- [Status](meraki_mr_radio_module.md#status)

## [DEPRECATED](meraki_mr_radio_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.devices_wireless_radio_settings

## [Synopsis](meraki_mr_radio_module.md#id2)

- Allows for configuration of radio settings in Meraki MR wireless networks.

## [Parameters](meraki_mr_radio_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **five_ghz_settings**  dictionary | Manual radio settings for 5 GHz.  **Default:** `{}` |
| **channel**  integer | Sets a manual channel for 5 GHz.  **Choices:**   - `36` - `40` - `44` - `48` - `52` - `56` - `60` - `64` - `100` - `104` - `108` - `112` - `116` - `120` - `124` - `128` - `132` - `136` - `140` - `144` - `149` - `153` - `157` - `161` - `165` |
| **channel_width**  string | Sets a manual channel for 5 GHz.  Can be ‘0’, ‘20’, ‘40’, or ‘80’ or null for using auto channel width.  **Choices:**   - `"auto"` - `"20"` - `"40"` - `"80"` |
| **target_power**  integer | Set a manual target power for 5 GHz.  Can be between ‘8’ or ‘30’ or null for using auto power range. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID of a network. |
| **net_name**  aliases: network  string | Name of a network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **rf_profile_id**  string | The ID of an RF profile to assign to the device.  If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device.  Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power). |
| **rf_profile_name**  string | The name of an RF profile to assign to the device.  Similar to ``rf_profile_id``, but requires ``net_id`` (preferred) or ``net_name``. |
| **serial**  string | Serial number of a device to query. |
| **state**  string | Query or edit radio settings on a device.  **Choices:**   - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **two_four_ghz_settings**  dictionary | Manual radio settings for 2.4 GHz.  **Default:** `{}` |
| **channel**  integer | Sets a manual channel for 2.4 GHz.  Can be ‘1’, ‘2’, ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, ‘9’, ‘10’, ‘11’, ‘12’, ‘13’ or ‘14’ or null for using auto channel.  **Choices:**   - `1` - `2` - `3` - `4` - `5` - `6` - `7` - `8` - `9` - `10` - `11` - `12` - `13` - `14` |
| **target_power**  integer | Set a manual target power for 2.4 GHz.  Can be between ‘5’ or ‘30’ or null for using auto power range. |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_mr_radio_module.md#id4)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mr_radio_module.md#id5)

```yaml+jinja
- name: Query a device's radio configuration
  meraki_mr_radio:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    serial: YourSerialNumber
    state: query
  delegate_to: localhost
- name: Configure a device's radios
  meraki_mr_radio:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    serial: YourSerialNumber
    state: present
    five_ghz_settings:
      channel: 56
      channel_width: 20
      target_power: 10
    two_four_ghz_settings:
      channel: 6
      target_power: 12
    rf_profile_name: Test Profile
  delegate_to: localhost
```

## [Return Values](meraki_mr_radio_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | RF settings configured on a specific device.  **Returned:** success |
| **five_ghz_settings**  dictionary | Configured manual radio settings for 5 GHz.  **Returned:** success |
| **channel**  string | Configured manual channel for 5 GHz.  Null indicates auto channel.  **Returned:** success  **Sample:** `"56"` |
| **channel_width**  string | Configured manual channel for 5 GHz.  Null indicates auto channel width.  **Returned:** success  **Sample:** `"40"` |
| **target_power**  integer | Configured manual target power for 5 GHz.  Null indicates auto power.  **Returned:** success  **Sample:** `25` |
| **rf_profile_id**  string | The ID of an RF profile assigned to the device.  Null indicates the appropriate basic RF profile (indoor or outdoor) is assigned to the device.  **Returned:** success |
| **serial**  string | Serial number of the device that was configured.  **Returned:** success  **Sample:** `"xyz"` |
| **two_four_ghz_settings**  dictionary | Configured manual radio settings for 2.4 GHz.  **Returned:** success |
| **channel**  string | Configured manual channel for 2.4 GHz.  Null indicates auto channel.  **Returned:** success  **Sample:** `"11"` |
| **target_power**  integer | Configured manual target power for 2.4 GHz.  Null indicates auto power.  **Returned:** success  **Sample:** `15` |

## [Status](meraki_mr_radio_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_mr_radio_module.md#deprecated).

### Authors

- Tyler Christiansen (@supertylerc)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
