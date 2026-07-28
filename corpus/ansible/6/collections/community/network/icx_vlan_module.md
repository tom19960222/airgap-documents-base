---
collection: ansible
version: "6"
title: "community.network.icx_vlan module – Manage VLANs on Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/icx_vlan_module.html
fetched_at: 2026-07-27T17:18:50+00:00
---
# community.network.icx_vlan module – Manage VLANs on Ruckus ICX 7000 series switches

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.icx_vlan`.

- [Synopsis](icx_vlan_module.md#synopsis)
- [Parameters](icx_vlan_module.md#parameters)
- [Notes](icx_vlan_module.md#notes)
- [Examples](icx_vlan_module.md#examples)
- [Return Values](icx_vlan_module.md#return-values)

## [Synopsis](icx_vlan_module.md#id1)

- This module provides declarative management of VLANs on ICX network devices.

## [Parameters](icx_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=string | List of VLANs definitions. |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vlan `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vlan interfaces on device it will result in failure. |
| **associated_tagged**  list / elements=string | This is a intent option and checks the operational state of given vlan `name` for associated tagged ports and lags. If the value in the `associated_tagged` does not match with the operational state of vlan interfaces on device it will result in failure. |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  Choices:   - `false` - `true` |
| **delay**  integer | Delay the play should wait to check for declarative intent params values. |
| **interfaces**  dictionary | List of ethernet ports or LAGS to be added as access(untagged) ports to the vlan. To add a range of ports use ‘to’ keyword. See the example. |
| **name**  list / elements=string | Name of the interface or lag |
| **purge**  boolean | Purge interfaces not defined in the *name*  Choices:   - `false` - `true` |
| **ip_arp_inspection**  boolean | Enables dynamic ARP inspection on a VLAN.  Choices:   - `false` - `true` |
| **ip_dhcp_snooping**  boolean | Enables DHCP snooping on a VLAN.  Choices:   - `false` - `true` |
| **name**  string | Name of the VLAN. |
| **state**  string | State of the VLAN configuration.  Choices:   - `"present"` - `"absent"` |
| **stp**  dictionary | Enable spanning-tree 802-1w/rstp for this vlan. |
| **enabled**  boolean | Manage the state(Enable/Disable) of the spanning_tree_802_1w in the current vlan  Choices:   - `false` - `true` |
| **priority**  string | Configures the priority of the bridge. The value ranges from 0 through 65535. A lower numerical value means the bridge has a higher priority. Thus, the highest priority is 0. The default is 32768. |
| **type**  string | Specify the type of spanning-tree  Choices:   - `"802-1w"` ← (default) - `"rstp"` |
| **tagged**  dictionary | List of ethernet ports or LAGS to be added as trunk(tagged) ports to the vlan. To add a range of ports use ‘to’ keyword. See the example. |
| **name**  list / elements=string | Name of the interface or lag |
| **purge**  boolean | Purge interfaces not defined in the *name*  Choices:   - `false` - `true` |
| **vlan_id**  string / required | ID of the VLAN. Range 1-4094. |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vlan `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vlan interfaces on device it will result in failure. |
| **associated_tagged**  list / elements=string | This is a intent option and checks the operational state of given vlan `name` for associated tagged ports and lags. If the value in the `associated_tagged` does not match with the operational state of vlan interfaces on device it will result in failure. |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  Choices:   - `false` - `true` ← (default) |
| **delay**  integer | Delay the play should wait to check for declarative intent params values.  Default: `10` |
| **interfaces**  dictionary | List of ethernet ports or LAGS to be added as access(untagged) ports to the vlan. To add a range of ports use ‘to’ keyword. See the example. |
| **name**  list / elements=string | Name of the interface or lag |
| **purge**  boolean | Purge interfaces not defined in the *name*  Choices:   - `false` - `true` |
| **ip_arp_inspection**  boolean | Enables dynamic ARP inspection on a VLAN.  Choices:   - `false` - `true` |
| **ip_dhcp_snooping**  boolean | Enables DHCP snooping on a VLAN.  Choices:   - `false` - `true` |
| **name**  string | Name of the VLAN. |
| **purge**  boolean | Purge VLANs not defined in the *aggregate* parameter.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the VLAN configuration.  Choices:   - `"present"` ← (default) - `"absent"` |
| **stp**  dictionary | Enable spanning-tree 802-1w/rstp for this vlan. |
| **enabled**  boolean | Manage the state(Enable/Disable) of the spanning_tree_802_1w in the current vlan  Choices:   - `false` - `true` |
| **priority**  string | Configures the priority of the bridge. The value ranges from 0 through 65535. A lower numerical value means the bridge has a higher priority. Thus, the highest priority is 0. The default is 32768. |
| **type**  string | Specify the type of spanning-tree  Choices:   - `"802-1w"` ← (default) - `"rstp"` |
| **tagged**  dictionary | List of ethernet ports or LAGS to be added as trunk(tagged) ports to the vlan. To add a range of ports use ‘to’ keyword. See the example. |
| **name**  list / elements=string | Name of the interface or lag |
| **purge**  boolean | Purge interfaces not defined in the *name*  Choices:   - `false` - `true` |
| **vlan_id**  integer / required | ID of the VLAN. Range 1-4094. |

## [Notes](icx_vlan_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_vlan_module.md#id4)

```yaml+jinja
- name: Add a single ethernet 1/1/48 as access(untagged) port to vlan 20
  community.network.icx_vlan:
    name: test-vlan
    vlan_id: 20
    interfaces:
      name:
        - ethernet 1/1/48

- name: Add a single LAG 10 as access(untagged) port to vlan 20
  community.network.icx_vlan:
    vlan_id: 20
    interfaces:
      name:
        - lag 10

- name: Add a range of ethernet ports as trunk(tagged) ports to vlan 20 by port
  community.network.icx_vlan:
    vlan_id: 20
    tagged:
      name:
        - ethernet 1/1/40 to 1/1/48

- name: Add discontinuous lags, ethernet ports as access(untagged) and trunk(tagged) port to vlan 20.
  community.network.icx_vlan:
    vlan_id: 20
    interfaces:
      name:
        - ethernet 1/1/40 to 1/1/48
        - ethernet 2/1/1
        - lag 1
        - lag 3 to 5
    tagged:
      name:
        - ethernet 1/1/20 to 1/1/25
        - lag 1 to 3

- name: Remove an access and range of trunk ports from vlan
  community.network.icx_vlan:
    vlan_id: 20
    interfaces:
      name:
        - ethernet 1/1/40
    tagged:
      name:
        - ethernet 1/1/39 to 1/1/70

- name: Enable dhcp snooping, disable arp inspection in vlan
  community.network.icx_vlan:
    vlan_id: 20
    ip_dhcp_snooping: present
    ip_arp_inspection: absent

- name: Create vlan 20.  Enable  arp inspection in vlan. Purge all other vlans.
  community.network.icx_vlan:
    vlan_id: 20
    ip_arp_inspection: present
    purge: present

- name: Remove vlan 20.
  community.network.icx_vlan:
    vlan_id: 20
    state: absent
```

## [Return Values](icx_vlan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["vlan 100", "name test-vlan"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
