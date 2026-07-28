---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_ms_access_policies module – Manage Switch Access Policies in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_ms_access_policies_module.html
fetched_at: 2026-07-28T01:32:29+00:00
---
# cisco.meraki.meraki_ms_access_policies module – Manage Switch Access Policies in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_ms_access_policies`.

- [DEPRECATED](meraki_ms_access_policies_module.md#deprecated)
- [Synopsis](meraki_ms_access_policies_module.md#synopsis)
- [Parameters](meraki_ms_access_policies_module.md#parameters)
- [Notes](meraki_ms_access_policies_module.md#notes)
- [Examples](meraki_ms_access_policies_module.md#examples)
- [Return Values](meraki_ms_access_policies_module.md#return-values)
- [Status](meraki_ms_access_policies_module.md#status)

## [DEPRECATED](meraki_ms_access_policies_module.md#id2)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_switch_access_policies

## [Synopsis](meraki_ms_access_policies_module.md#id3)

- Module for managing a Switch Access Policies in the Meraki cloud

## [Parameters](meraki_ms_access_policies_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **access_policy_type**  string | Set type of the access policy  **Choices:**   - `"802.1x"` - `"MAC authentication bypass"` - `"Hybrid authentication"` |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **auth_method**  string | Set authentication method in the policy.  **Choices:**   - `"Meraki authentication"` - `"my RADIUS server"` |
| **data_vlan_id**  integer | Set a Data VLAN ID for Critical Auth VLAN |
| **guest_vlan**  integer | Guest Vlan |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **host_mode**  string | Choose the Host Mode for the access policy.  **Choices:**   - `"Single-Host"` - `"Multi-Domain"` - `"Multi-Host"` - `"Multi-Auth"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **name**  string | Name of Access Policy. |
| **net_id**  string | ID of network. |
| **net_name**  aliases: name, network  string | Name of a network. |
| **number**  aliases: access_policy_number  integer | Number of the access_policy. |
| **org_id**  string | ID of organization associated to a network. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **radius_accounting_enabled**  boolean | Enable or disable RADIUS accounting.  **Choices:**   - `false` - `true` |
| **radius_accounting_servers**  list / elements=dictionary | List of RADIUS servers for RADIUS accounting. |
| **host**  string / required | IP address or hostname of RADIUS server. |
| **port**  integer | Port number RADIUS server is listening to. |
| **secret**  string | RADIUS password. |
| **radius_attribute_group_policy_name**  string | Enable that attribute for a RADIUS  **Choices:**   - `"Filter-Id"` - `""` ← (default) |
| **radius_coa_enabled**  boolean | Enable or disable RADIUS CoA (Change of Authorization).  **Choices:**   - `false` - `true` |
| **radius_servers**  list / elements=dictionary | List of RADIUS servers. |
| **host**  string / required | IP address or hostname of RADIUS server. |
| **port**  integer | Port number RADIUS server is listening to. |
| **secret**  string | RADIUS password.  Setting password is not idempotent. |
| **radius_testing**  boolean | Set status of testing a radius.  **Choices:**   - `false` - `true` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **state**  string | Specifies whether SNMP information should be queried or modified.  **Choices:**   - `"absent"` - `"query"` - `"present"` ← (default) |
| **suspend_port_bounce**  boolean | Enable or disable the Suspend Port Bounce when RADIUS servers are unreachable.  **Choices:**   - `false` ← (default) - `true` |
| **systems_management_enrollment**  boolean | Set if the Systems Management Enrollemnt is enabled or disabled  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |
| **voice_vlan_clients**  boolean | If is enabled that means Voice VLAN client require authentication  **Choices:**   - `false` - `true` ← (default) |
| **voice_vlan_id**  integer | Set a Voice VLAN ID for Critical Auth VLAN |

## [Notes](meraki_ms_access_policies_module.md#id5)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_ms_access_policies_module.md#id6)

```yaml+jinja
- name: Create access policy with auth_method is "Meraki authentication"
  cisco.meraki.meraki_ms_access_policies:
    auth_key: abc123
    state: present
    name: "Meraki authentication policy"
    auth_method: "Meraki authentication"
    net_name: YourNet
    org_name: YourOrg
  delegate_to: localhost

- name: Create access policy with auth_method is "my Radius Server"
  cisco.meraki.meraki_ms_access_policies:
    auth_key: abc123
    access_policy_type: "802.1x"
    host_mode: "Single-Host"
    state: present
    name: "Meraki authentication policy"
    auth_method: "my RADIUS server"
    radius_servers:
      - host: 192.0.1.18
        port: 7890
        secret: secret123
    net_name: YourNet
    org_name: YourOrg
    radius_coa_enabled: False
    radius_accounting_enabled: False
    guest_vlan: 10
    voice_vlan_clients: False
```

## [Return Values](meraki_ms_access_policies_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | List of Access Policies  **Returned:** success |
| **access_policy_type**  string | Type of the access policy  **Returned:** success  **Sample:** `"802.1x"` |
| **guest_vlan_id**  integer | ID of the Guest Vlan  **Returned:** success  **Sample:** `10` |
| **host_mode**  string | Choosen teh Host Mode for the access policy  **Returned:** success  **Sample:** `"Single-Host"` |
| **name**  string | Name of the Access Policy  **Returned:** success  **Sample:** `"Policy with 802.1x"` |
| **number**  integer | Number of the Access Policy  **Returned:** success  **Sample:** `1` |
| **radius**  complex | List of radius specific list  **Returned:** success |
| **critial_auth**  complex | Critial Auth List  **Returned:** success |
| **data_vlan_id**  integer | VLAN ID for data  **Returned:** success  **Sample:** `10` |
| **suspend_port_bounce**  boolean | Enable or disable suspend port bounce  **Returned:** success  **Sample:** `false` |
| **voice_vlan_id**  integer | VLAN ID for voice  **Returned:** success  **Sample:** `10` |
| **failed_auth_vlan_id**  integer | VLAN ID when failed auth  **Returned:** success  **Sample:** `11` |
| **re_authentication_interval**  integer | Interval of re-authentication  **Returned:** success |
| **radius_accounting_enabled**  boolean | Enable or disable RADIUS accounting.  **Returned:** success |
| **radius_accounting_servers**  list / elements=dictionary | List of RADIUS servers for RADIUS accounting.  **Returned:** success |
| **radius_attribute_group_policy_name**  string | Enable the radius group attribute  **Returned:** success  **Can only return:**   - `"11"` - `""`   **Sample:** `"11"` |
| **radius_coa_enabled**  boolean | Enable or disable RADIUS CoA (Change of Authorization).  **Returned:** success |
| **radius_servers**  list / elements=dictionary | List of RADIUS servers.  **Returned:** success |
| **radius_testing_enabled**  boolean | Enable or disable Radius Testing  **Returned:** success  **Sample:** `true` |
| **voice_vlan_clients**  boolean | Enable or disable Voice Vlan Clients  **Returned:** success  **Sample:** `false` |

## [Status](meraki_ms_access_policies_module.md#id8)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_ms_access_policies_module.md#deprecated).

### Authors

- Marcin Woźniak (@y0rune)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
