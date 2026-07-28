---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_l2_interfaces module – Configure interface-to-VLAN association that is based on access or trunk mode"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_l2_interfaces_module.html
fetched_at: 2026-07-28T02:03:39+00:00
---
# dellemc.enterprise_sonic.sonic_l2_interfaces module – Configure interface-to-VLAN association that is based on access or trunk mode

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_l2_interfaces`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_l2_interfaces_module.md#synopsis)
- [Parameters](sonic_l2_interfaces_module.md#parameters)
- [Notes](sonic_l2_interfaces_module.md#notes)
- [Examples](sonic_l2_interfaces_module.md#examples)
- [Return Values](sonic_l2_interfaces_module.md#return-values)

## [Synopsis](sonic_l2_interfaces_module.md#id1)

- Manages Layer 2 interface attributes of Enterprise SONiC Distribution by Dell Technologies.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_l2_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of Layer 2 interface configurations. |
| **access**  dictionary | Configures access mode characteristics of the interface. |
| **vlan**  integer | Configures the specified VLAN in access mode. |
| **name**  string / required | Full name of the interface, for example, ‘Eth1/26’. |
| **trunk**  dictionary | Configures trunking parameters on an interface. |
| **allowed_vlans**  list / elements=dictionary | Specifies a list of allowed trunk mode VLANs and VLAN ranges for the interface. |
| **vlan**  string | Configures the specified trunk mode VLAN or VLAN range. |
| **state**  string | The state that the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Notes](sonic_l2_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_l2_interfaces_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive    A  Eth1/3
#11         Inactive    T  Eth1/3
#12         Inactive    A  Eth1/4
#13         Inactive    T  Eth1/4
#14         Inactive    A  Eth1/5
#15         Inactive    T  Eth1/5
#
- name: Configures switch port of interfaces
  dellemc.enterprise_sonic.sonic_l2_interfaces:
   config:
     - name: Eth1/3
     - name: Eth1/4
   state: deleted
#
# After state:
# ------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#11         Inactive
#12         Inactive
#13         Inactive
#14         Inactive    A  Eth1/5
#15         Inactive    T  Eth1/5
#
#
# Using deleted
#
# Before state:
# -------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive    A  Eth1/3
#11         Inactive    T  Eth1/3
#12         Inactive    A  Eth1/4
#13         Inactive    T  Eth1/4
#14         Inactive    A  Eth1/5
#15         Inactive    T  Eth1/5
#
- name: Configures switch port of interfaces
  dellemc.enterprise_sonic.sonic_l2_interfaces:
    config:
    state: deleted
#
# After state:
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#11         Inactive
#12         Inactive
#13         Inactive
#14         Inactive
#15         Inactive
#
#
# Using deleted
#
# Before state:
# -------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#11         Inactive    T  Ethernet12
#12         Inactive    A  Ethernet12
#13         Inactive    T  Ethernet12
#14         Inactive    T  Ethernet12
#15         Inactive    T  Ethernet12
#16         Inactive    T  Ethernet12

- name: Delete the access vlan and a range of trunk vlans for an interface
  sonic_l2_interfaces:
    config:
      - name: Ethernet12
        access:
          vlan: 12
        trunk:
          allowed_vlans:
             - vlan: 13-16
    state: deleted

# After state:
# ------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#11         Inactive    T  Ethernet12
#12         Inactive
#13         Inactive
#14         Inactive
#15         Inactive
#16         Inactive
#
#
#
# Using merged
#
# Before state:
# -------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#11         Inactive    T  Eth1/7
#12         Inactive    T  Eth1/7
#
- name: Configures an access vlan for an interface
  dellemc.enterprise_sonic.sonic_l2_interfaces:
    config:
     - name: Eth1/3
       access:
         vlan: 10
    state: merged
#
# After state:
# ------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive    A  Eth1/3
#11         Inactive    T  Eth1/7
#12         Inactive    T  Eth1/7
#
#
# Using merged
#
# Before state:
# -------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive    A  Eth1/3
#12         Inactive
#13         Inactive
#14         Inactive
#15         Inactive
#16         Inactive
#18         Inactive
#
- name: Modify the access vlan, add a range of trunk vlans and a single trunk vlan for an interface
  dellemc.enterprise_sonic.sonic_l2_interfaces:
    config:
     - name: Eth1/3
       access:
         vlan: 12
       trunk:
         allowed_vlans:
            - vlan: 13-16
            - vlan: 18
    state: merged
#
# After state:
# ------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#12         Inactive    A  Eth1/3
#13         Inactive    T  Eth1/3
#14         Inactive    T  Eth1/3
#15         Inactive    T  Eth1/3
#16         Inactive    T  Eth1/3
#18         Inactive    T  Eth1/3
#
#
# Using merged
#
# Before state:
# -------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#11         Inactive
#12         Inactive    A  Eth1/4
#13         Inactive    T  Eth1/4
#14         Inactive    A  Eth1/5
#15         Inactive    T  Eth1/5
#
- name: Configures switch port of interfaces
  dellemc.enterprise_sonic.sonic_l2_interfaces:
    config:
     - name: Eth1/3
       access:
         vlan: 12
       trunk:
         allowed_vlans:
            - vlan: 13
            - vlan: 14
    state: merged
#
# After state:
# ------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#11         Inactive
#12         Inactive    A  Eth1/3
#                       A  Eth1/4
#13         Inactive    T  Eth1/3
#                       T  Eth1/4
#14         Inactive    A  Eth1/3
#                       A  Eth1/5
#15         Inactive    T  Eth1/5
#
#
# Using replaced
#
# Before state:
# -------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive    A  Ethernet12
#                       A  Ethernet13
#11         Inactive    T  Ethernet12
#                       T  Ethernet13

- name: Replace access vlan and trunk vlans for specified interfaces
  sonic_l2_interfaces:
    config:
      - name: Ethernet12
        access:
          vlan: 12
        trunk:
          allowed_vlans:
             - vlan: 13-14
      - name: Ethernet14
        access:
          vlan: 10
        trunk:
          allowed_vlans:
             - vlan: 11
             - vlan: 13-14
    state: replaced

# After state:
# ------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive    A  Ethernet13
#                       A  Ethernet14
#11         Inactive    T  Ethernet13
#                       T  Ethernet14
#12         Inactive    A  Ethernet12
#13         Inactive    T  Ethernet12
#                       T  Ethernet14
#14         Inactive    T  Ethernet12
#                       T  Ethernet14
#
#
# Using overridden
#
# Before state:
# -------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive    A  Ethernet11
#11         Inactive    T  Ethernet11
#12         Inactive    A  Ethernet12
#13         Inactive    T  Ethernet12

- name: Override L2 interfaces configuration in device with provided configuration
  sonic_l2_interfaces:
    config:
      - name: Ethernet13
        access:
          vlan: 12
        trunk:
          allowed_vlans:
             - vlan: 13-14
    state: overridden

# After state:
# ------------
#
#do show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#12         Inactive    A  Ethernet13
#13         Inactive    T  Ethernet13
#14         Inactive    T  Ethernet13
#
#
```

## [Return Values](sonic_l2_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned always in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M(@niraimadaiselvamm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
