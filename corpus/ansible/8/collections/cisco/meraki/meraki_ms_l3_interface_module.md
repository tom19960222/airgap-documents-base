---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_ms_l3_interface module – Manage routed interfaces on MS switches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_ms_l3_interface_module.html
fetched_at: 2026-07-28T01:32:29+00:00
---
# cisco.meraki.meraki_ms_l3_interface module – Manage routed interfaces on MS switches

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
> To use it in a playbook, specify: `cisco.meraki.meraki_ms_l3_interface`.

- [DEPRECATED](meraki_ms_l3_interface_module.md#deprecated)
- [Synopsis](meraki_ms_l3_interface_module.md#synopsis)
- [Parameters](meraki_ms_l3_interface_module.md#parameters)
- [Notes](meraki_ms_l3_interface_module.md#notes)
- [Examples](meraki_ms_l3_interface_module.md#examples)
- [Return Values](meraki_ms_l3_interface_module.md#return-values)
- [Status](meraki_ms_l3_interface_module.md#status)

## [DEPRECATED](meraki_ms_l3_interface_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.devices_switch_routing_interfaces

## [Synopsis](meraki_ms_l3_interface_module.md#id2)

- Allows for creation, management, and visibility into routed interfaces on Meraki MS switches.

## [Parameters](meraki_ms_l3_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **default_gateway**  string | The next hop for any traffic that isn’t going to a directly connected subnet or over a static route.  This IP address must exist in a subnet with a routed interface. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **interface_id**  string | Uniqiue identification number for layer 3 interface. |
| **interface_ip**  string | The IP address this switch will use for layer 3 routing on this VLAN or subnet.  This cannot be the same as the switch’s management IP. |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **multicast_routing**  string | Enable multicast support if multicast routing between VLANs is required.  **Choices:**   - `"disabled"` - `"enabled"` - `"IGMP snooping querier"` |
| **name**  string | A friendly name or description for the interface or VLAN. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **ospf_settings**  dictionary | The OSPF routing settings of the interface. |
| **area**  string | The OSPF area to which this interface should belong.  Can be either ‘disabled’ or the identifier of an existing OSPF area. |
| **cost**  integer | The path cost for this interface. |
| **is_passive_enabled**  boolean | When enabled, OSPF will not run on the interface, but the subnet will still be advertised.  **Choices:**   - `false` - `true` |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **serial**  string | Serial number of MS switch hosting the layer 3 interface. |
| **state**  string | Create or modify an organization.  **Choices:**   - `"present"` ← (default) - `"query"` - `"absent"` |
| **subnet**  string | The network that this routed interface is on, in CIDR notation. |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vlan_id**  integer | The VLAN this routed interface is on.  VLAN must be between 1 and 4094. |

## [Notes](meraki_ms_l3_interface_module.md#id4)

> **Note:**
>
> - Once a layer 3 interface is created, the API does not allow updating the interface and specifying `default_gateway`.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_ms_l3_interface_module.md#id5)

```yaml+jinja
- name: Query all l3 interfaces
  meraki_ms_l3_interface:
    auth_key: abc123
    state: query
    serial: aaa-bbb-ccc

- name: Query one l3 interface
  meraki_ms_l3_interface:
    auth_key: abc123
    state: query
    serial: aaa-bbb-ccc
    name: Test L3 interface

- name: Create l3 interface
  meraki_ms_l3_interface:
    auth_key: abc123
    state: present
    serial: aaa-bbb-ccc
    name: "Test L3 interface 2"
    subnet: "192.168.3.0/24"
    interface_ip: "192.168.3.2"
    multicast_routing: disabled
    vlan_id: 11
    ospf_settings:
      area: 0
      cost: 1
      is_passive_enabled: true

- name: Update l3 interface
  meraki_ms_l3_interface:
    auth_key: abc123
    state: present
    serial: aaa-bbb-ccc
    name: "Test L3 interface 2"
    subnet: "192.168.3.0/24"
    interface_ip: "192.168.3.2"
    multicast_routing: disabled
    vlan_id: 11
    ospf_settings:
      area: 0
      cost: 2
      is_passive_enabled: true

- name: Delete l3 interface
  meraki_ms_l3_interface:
    auth_key: abc123
    state: absent
    serial: aaa-bbb-ccc
    interface_id: abc123344566
```

## [Return Values](meraki_ms_l3_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the layer 3 interfaces.  **Returned:** success |
| **default_gateway**  string | The next hop for any traffic that isn’t going to a directly connected subnet or over a static route.  **Returned:** success  **Sample:** `"192.168.2.1"` |
| **interface_id**  string | Uniqiue identification number for layer 3 interface.  **Returned:** success  **Sample:** `"62487444811111120"` |
| **interface_ip**  string | The IP address this switch will use for layer 3 routing on this VLAN or subnet.  **Returned:** success  **Sample:** `"192.168.2.2"` |
| **multicast_routing**  string | Enable multicast support if multicast routing between VLANs is required.  **Returned:** success  **Sample:** `"disabled"` |
| **name**  string | A friendly name or description for the interface or VLAN.  **Returned:** success  **Sample:** `"L3 interface"` |
| **ospf_settings**  complex | The OSPF routing settings of the interface.  **Returned:** success |
| **area**  string | The OSPF area to which this interface should belong.  **Returned:** success  **Sample:** `"0"` |
| **cost**  integer | The path cost for this interface.  **Returned:** success  **Sample:** `1` |
| **is_passive_enabled**  boolean | When enabled, OSPF will not run on the interface, but the subnet will still be advertised.  **Returned:** success  **Sample:** `true` |
| **subnet**  string | The network that this routed interface is on, in CIDR notation.  **Returned:** success  **Sample:** `"192.168.2.0/24"` |
| **vlan_id**  integer | The VLAN this routed interface is on.  **Returned:** success  **Sample:** `10` |

## [Status](meraki_ms_l3_interface_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_ms_l3_interface_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
