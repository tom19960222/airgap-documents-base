---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_ms_switchport module – Manage switchports on a switch in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_ms_switchport_module.html
fetched_at: 2026-07-28T01:32:34+00:00
---
# cisco.meraki.meraki_ms_switchport module – Manage switchports on a switch in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_ms_switchport`.

- [DEPRECATED](meraki_ms_switchport_module.md#deprecated)
- [Synopsis](meraki_ms_switchport_module.md#synopsis)
- [Parameters](meraki_ms_switchport_module.md#parameters)
- [Notes](meraki_ms_switchport_module.md#notes)
- [Examples](meraki_ms_switchport_module.md#examples)
- [Return Values](meraki_ms_switchport_module.md#return-values)
- [Status](meraki_ms_switchport_module.md#status)

## [DEPRECATED](meraki_ms_switchport_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.devices_switch_ports

## [Synopsis](meraki_ms_switchport_module.md#id2)

- Allows for management of switchports settings for Meraki MS switches.

## [Parameters](meraki_ms_switchport_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_policy_number**  integer | Number of the access policy to apply.  Only applicable to access port types. |
| **access_policy_type**  string | Type of access policy to apply to port.  **Choices:**   - `"Open"` - `"Custom access policy"` - `"MAC allow list"` - `"Sticky MAC allow list"` |
| **allowed_vlans**  list / elements=string | List of VLAN numbers to be allowed on switchport.  **Default:** `["all"]` |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **enabled**  boolean | Whether a switchport should be enabled or disabled.  **Choices:**   - `false` - `true` ← (default) |
| **flexible_stacking_enabled**  boolean | Whether flexible stacking capabilities are supported on the port.  **Choices:**   - `false` - `true` |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **isolation_enabled**  boolean | Isolation status of switchport.  **Choices:**   - `false` ← (default) - `true` |
| **link_negotiation**  string | Link speed for the switchport.  **Choices:**   - `"1 Gigabit full duplex (auto)"` - `"1 Gigabit full duplex (forced)"` - `"10 Gigabit full duplex (auto)"` - `"10 Gigabit full duplex (forced)"` - `"100 Megabit (auto)"` - `"100 Megabit full duplex (forced)"` - `"2.5 Gigabit full duplex (auto)"` - `"2.5 Gigabit full duplex (forced)"` - `"5 Gigabit full duplex (auto)"` - `"5 Gigabit full duplex (forced)"` - `"Auto negotiate"` ← (default) |
| **mac_allow_list**  dictionary | MAC addresses list that are allowed on a port.  Only applicable to access port type.  Only applicable to access_policy_type “MAC allow list”. |
| **macs**  list / elements=string | List of MAC addresses to update with based on state option. |
| **state**  string | The state the configuration should be left in.  Merged, MAC addresses provided will be added to the current allow list.  Replaced, All MAC addresses are overwritten, only the MAC addresses provided with exist in the allow list.  Deleted, Remove the MAC addresses provided from the current allow list.  **Choices:**   - `"merged"` - `"replaced"` ← (default) - `"deleted"` |
| **name**  aliases: description  string | Switchport description. |
| **number**  string | Port number. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **poe_enabled**  boolean | Enable or disable Power Over Ethernet on a port.  **Choices:**   - `false` - `true` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **rstp_enabled**  boolean | Enable or disable Rapid Spanning Tree Protocol on a port.  **Choices:**   - `false` - `true` ← (default) |
| **serial**  string / required | Serial nubmer of the switch. |
| **state**  string | Specifies whether a switchport should be queried or modified.  **Choices:**   - `"query"` ← (default) - `"present"` |
| **sticky_mac_allow_list**  dictionary | MAC addresses list that are allowed on a port.  Only applicable to access port type.  Only applicable to access_policy_type “Sticky MAC allow list”. |
| **macs**  list / elements=string | List of MAC addresses to update with based on state option. |
| **state**  string | The state the configuration should be left in.  Merged, MAC addresses provided will be added to the current allow list.  Replaced, All MAC addresses are overwritten, only the MAC addresses provided with exist in the allow list.  Deleted, Remove the MAC addresses provided from the current allow list.  **Choices:**   - `"merged"` - `"replaced"` ← (default) - `"deleted"` |
| **sticky_mac_allow_list_limit**  integer | The number of MAC addresses allowed in the sticky port allow list.  Only applicable to access port type.  Only applicable to access_policy_type “Sticky MAC allow list”.  The value must be equal to or greater then the list size of sticky_mac_allow_list. Value will be checked for validity, during processing. |
| **stp_guard**  string | Set state of STP guard.  **Choices:**   - `"disabled"` ← (default) - `"root guard"` - `"bpdu guard"` - `"loop guard"` |
| **tags**  list / elements=string | List of tags to assign to a port. |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **type**  string | Set port type.  **Choices:**   - `"access"` ← (default) - `"trunk"` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vlan**  integer | VLAN number assigned to port.  If a port is of type trunk, the specified VLAN is the native VLAN.  Setting value to 0 on a trunk will clear the VLAN. |
| **voice_vlan**  integer | VLAN number assigned to a port for voice traffic.  Only applicable to access port type.  Only applicable if voice_vlan_state is set to present. |
| **voice_vlan_state**  string | Specifies whether voice vlan configuration should be present or absent.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](meraki_ms_switchport_module.md#id4)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_ms_switchport_module.md#id5)

```yaml+jinja
- name: Query information about all switchports on a switch
  meraki_switchport:
    auth_key: abc12345
    state: query
    serial: ABC-123
  delegate_to: localhost

- name: Query information about all switchports on a switch
  meraki_switchport:
    auth_key: abc12345
    state: query
    serial: ABC-123
    number: 2
  delegate_to: localhost

- name: Name switchport
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 7
    name: Test Port
  delegate_to: localhost

- name: Configure access port with voice VLAN
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 7
    enabled: true
    name: Test Port
    tags: desktop
    type: access
    vlan: 10
    voice_vlan: 11
  delegate_to: localhost

- name: Check access port for idempotency
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 7
    enabled: true
    name: Test Port
    tags: desktop
    type: access
    vlan: 10
    voice_vlan: 11
  delegate_to: localhost

- name: Configure trunk port with specific VLANs
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 7
    enabled: true
    name: Server port
    tags: server
    type: trunk
    allowed_vlans:
      - 10
      - 15
      - 20
  delegate_to: localhost

- name: Configure access port with sticky MAC allow list and limit.
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 5
    sticky_mac_allow_limit: 3
    sticky_mac_allow_list:
        macs:
          - aa:aa:bb:bb:cc:cc
          - bb:bb:aa:aa:cc:cc
          - 11:aa:bb:bb:cc:cc
        state: replaced
    delegate_to: localhost

- name: Delete an existing MAC address from the sticky MAC allow list.
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 5
    sticky_mac_allow_list:
        macs:
          - aa:aa:bb:bb:cc:cc
        state: deleted
    delegate_to: localhost

- name: Add a MAC address to sticky MAC allow list.
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 5
    sticky_mac_allow_list:
        macs:
          - 22:22:bb:bb:cc:cc
        state: merged
    delegate_to: localhost
```

## [Return Values](meraki_ms_switchport_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information queried or updated switchports.  **Returned:** success |
| **access_policy_number**  integer | Number of assigned access policy. Only applicable to access ports.  **Returned:** success  **Sample:** `1234` |
| **access_policy_type**  string | Type of access policy assigned to port  **Returned:** success, when assigned  **Sample:** `"MAC allow list"` |
| **allowed_vlans**  string | List of VLANs allowed on an access port  **Returned:** success, when port is set as access  **Sample:** `"all"` |
| **enabled**  boolean | Enabled state of port.  **Returned:** success  **Sample:** `true` |
| **flexible_stacking_enabled**  boolean | Whether flexible stacking capabilities are enabled on the port.  **Returned:** success |
| **isolation_enabled**  boolean | Port isolation status of port.  **Returned:** success  **Sample:** `true` |
| **link_negotiation**  string | Link speed for the port.  **Returned:** success  **Sample:** `"Auto negotiate"` |
| **mac_allow_list**  list / elements=string | List of MAC addresses currently allowed on a non-sticky port. Used with access_policy_type of MAC allow list.  **Returned:** success  **Sample:** `["11:aa:bb:bb:cc:cc", "22:aa:bb:bb:cc:cc", "33:aa:bb:bb:cc:cc"]` |
| **name**  string | Human friendly description of port.  **Returned:** success  **Sample:** `"Jim Phone Port"` |
| **number**  integer | Number of port.  **Returned:** success  **Sample:** `1` |
| **poe_enabled**  boolean | Power Over Ethernet enabled state of port.  **Returned:** success  **Sample:** `true` |
| **port_schedule_id**  string | Unique ID of assigned port schedule  **Returned:** success |
| **rstp_enabled**  boolean | Enabled or disabled state of Rapid Spanning Tree Protocol (RSTP)  **Returned:** success  **Sample:** `true` |
| **sticky_mac_allow_list**  list / elements=string | List of MAC addresses currently allowed on a sticky port. Used with access_policy_type of Sticky MAC allow list.  **Returned:** success  **Sample:** `["11:aa:bb:bb:cc:cc", "22:aa:bb:bb:cc:cc", "33:aa:bb:bb:cc:cc"]` |
| **sticky_mac_allow_list_limit**  integer | Number of MAC addresses allowed on a sticky port.  **Returned:** success  **Sample:** `6` |
| **stp_guard**  string | State of STP guard  **Returned:** success  **Sample:** `"Root Guard"` |
| **tags**  list / elements=string | List of tags assigned to port.  **Returned:** success  **Sample:** `["phone", "marketing"]` |
| **type**  string | Type of switchport.  **Returned:** success  **Sample:** `"trunk"` |
| **udld**  string | Alert state of UDLD  **Returned:** success  **Sample:** `"Alert only"` |
| **vlan**  integer | VLAN assigned to port.  **Returned:** success  **Sample:** `10` |
| **voice_vlan**  integer | VLAN assigned to port with voice VLAN enabled devices.  **Returned:** success  **Sample:** `20` |

## [Status](meraki_ms_switchport_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_ms_switchport_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
