---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_lldp_interfaces module – LLDP interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_lldp_interfaces_module.html
fetched_at: 2026-07-28T01:38:51+00:00
---
# cisco.nxos.nxos_lldp_interfaces module – LLDP interfaces resource module

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_lldp_interfaces`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_lldp_interfaces_module.md#synopsis)
- [Parameters](nxos_lldp_interfaces_module.md#parameters)
- [Notes](nxos_lldp_interfaces_module.md#notes)
- [Examples](nxos_lldp_interfaces_module.md#examples)
- [Return Values](nxos_lldp_interfaces_module.md#return-values)

## [Synopsis](nxos_lldp_interfaces_module.md#id1)

- This module manages interfaces’ configuration for Link Layer Discovery Protocol (LLDP) on NX-OS platforms.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: lldp_interfaces

## [Parameters](nxos_lldp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of link layer discovery configurations for interfaces. |
| **name**  string / required | Name of the interface |
| **receive**  boolean | Used to enable or disable the reception of LLDP packets on that interface. By default, this is enabled after LLDP is enabled globally.  **Choices:**   - `false` - `true` |
| **tlv_set**  dictionary | Used to configure TLV parameters on the interface |
| **management_address**  string | Used to mention the IPv4 or IPv6 management address for the interface |
| **vlan**  integer | Used to mention the VLAN for the interface |
| **transmit**  boolean | Used to enable or disable the transmission of LLDP packets on that interface. By default, this is enabled after LLDP is enabled globally.  **Choices:**   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_lldp_interfaces_module.md#id3)

> **Note:**
>
> - Tested against NXOS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - The LLDP feature needs to be enabled before using this module

## [Examples](nxos_lldp_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#

- name: Merge provided configuration with device configuration
  cisco.nxos.nxos_lldp_interfaces:
    config:
    - name: Ethernet1/4
      receive: false
      transmit: true
      tlv_set:
        management_address: 192.168.122.64
      vlan: 12
    state: merged

# After state:
# -------------
#
# interface Ethernet1/4
#   no lldp receive
#   lldp tlv-set management-address 192.168.122.64
#   lldp tlv-set vlan 12

# Using replaced

# Before state:
# ------------
#
# interface Ethernet1/4
#   no lldp receive
#   lldp tlv-set management-address 192.168.122.64
# interface Ethernet1/5
#   no lldp transmit
#   lldp tlv-set vlan 10

- name: Replace LLDP configuration on interfaces with given configuration
  cisco.nxos.nxos_lldp_interfaces:
    config:
    - name: Ethernet1/4
      transmit: false
      tlv_set:
        vlan: 2
    state: replaced

# After state:
# -----------
#
# interface Ethernet1/4
#   no lldp transmit
#   lldp tlv_set vlan 2
# interface Ethernet1/5
#   no lldp transmit
#   lldp tlv-set vlan 10

# Using overridden

# Before state:
# ------------
#
# interface Ethernet1/4
#   no lldp receive
#   lldp tlv-set management-address 192.168.122.64
# interface Ethernet1/5
#   no lldp transmit
#   lldp tlv-set vlan 10

- name: Override LLDP configuration on all interfaces with given configuration
  cisco.nxos.nxos_lldp_interfaces:
    config:
    - name: Ethernet1/7
      receive: false
      tlv_set:
        vlan: 12
    state: overridden

# After state:
# -----------
#
# interface Ethernet1/7
#   no lldp receive
#   lldp tlv_set vlan 12

# Using deleted

# Before state:
# ------------
#
# interface Ethernet1/4
#   lldp tlv-set management vlan 24
#   no lldp transmit
# interface mgmt0
#   no lldp receive

- name: Delete LLDP interfaces configuration
  cisco.nxos.nxos_lldp_interfaces:
    state: deleted

# After state:
# ------------
#
```

## [Return Values](nxos_lldp_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface Ethernet1/2", "lldp receive", "lldp tlv-set vlan 12"]` |

### Authors

- Adharsh Srivats Rangarajan (@adharshsrivatsr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
