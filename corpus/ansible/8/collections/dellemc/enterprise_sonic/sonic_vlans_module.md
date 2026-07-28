---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_vlans module – Manage VLAN and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_vlans_module.html
fetched_at: 2026-07-28T02:03:53+00:00
---
# dellemc.enterprise_sonic.sonic_vlans module – Manage VLAN and its parameters

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_vlans`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_vlans_module.md#synopsis)
- [Parameters](sonic_vlans_module.md#parameters)
- [Notes](sonic_vlans_module.md#notes)
- [Examples](sonic_vlans_module.md#examples)
- [Return Values](sonic_vlans_module.md#return-values)

## [Synopsis](sonic_vlans_module.md#id1)

- This module provides configuration management of VLANs parameters on devices running Enterprise SONiC Distribution by Dell Technologies.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_vlans_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of VLAN options. |
| **description**  string | Description about the VLAN. |
| **vlan_id**  integer / required | ID of the VLAN  Range is 1 to 4094 |
| **state**  string | The state that the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Notes](sonic_vlans_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_vlans_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#30         Inactive
#
#sonic#
#

- name: Merges given VLAN attributes with the device configuration
  dellemc.enterprise_sonic.sonic_vlans:
    config:
      - vlan_id: 10
        description: "Internal"
    state: merged

# After state:
# ------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#30         Inactive
#
#sonic#
#
#sonic# show interface Vlan 10
#Description: Internal
#Vlan10 is up
#Mode of IPV4 address assignment: not-set
#Mode of IPV6 address assignment: not-set
#IP MTU 6000 bytes
#sonic#
#

# Using replaced

# Before state:
# -------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#30         Inactive
#
#sonic#

- name: Replace all attributes of specified VLANs with provided configuration
  dellemc.enterprise_sonic.sonic_vlans:
    config:
      - vlan_id: 10
    state: replaced

# After state:
# ------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#30         Inactive
#
#sonic#

# Using overridden

# Before state:
# -------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#30         Inactive
#
#sonic#

- name: Override device configuration of all VLANs with provided configuration
  dellemc.enterprise_sonic.sonic_vlans:
    config:
      - vlan_id: 10
    state: overridden

# After state:
# ------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#
#sonic#

# Using deleted

# Before state:
# -------------
#
#sonic# show interface Vlan 70
#Description: Internal
#Vlan70 is up
#Mode of IPV4 address assignment: not-set
#Mode of IPV6 address assignment: not-set
#IP MTU 6000 bytes

- name: Deletes attributes of the given VLANs
  dellemc.enterprise_sonic.sonic_vlans:
    config:
      - vlan_id: 70
        description: "Internal"
    state: deleted

# After state:
# ------------
#
#sonic# show interface Vlan 70
#Vlan70 is up
#Mode of IPV4 address assignment: not-set
#Mode of IPV6 address assignment: not-set
#IP MTU 6000 bytes

# Before state:
# -------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#20         Inactive
#
#sonic#

- name: Deletes attributes of the given VLANs
  dellemc.enterprise_sonic.sonic_vlans:
    config:
      - vlan_id: 20
    state: deleted

# After state:
# ------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#
#sonic#

# Using deleted

# Before state:
# -------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#10         Inactive
#20         Inactive
#30         Inactive
#
#sonic#

- name: Deletes all the VLANs on the switch
  dellemc.enterprise_sonic.sonic_vlans:
    config:
    state: deleted

# After state:
# ------------
#
#sonic# show Vlan
#Q: A - Access (Untagged), T - Tagged
#NUM        Status      Q Ports
#
#sonic#
```

## [Return Values](sonic_vlans_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration that is returned is always in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Mohamed Javeed (@javeedf)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
