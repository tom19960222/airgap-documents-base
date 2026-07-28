---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_port_breakout module – Configure port breakout settings on physical interfaces"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_port_breakout_module.html
fetched_at: 2026-07-27T17:24:57+00:00
---
# dellemc.enterprise_sonic.sonic_port_breakout module – Configure port breakout settings on physical interfaces

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/dellemc/enterprise_sonic) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_port_breakout`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_port_breakout_module.md#synopsis)
- [Parameters](sonic_port_breakout_module.md#parameters)
- [Notes](sonic_port_breakout_module.md#notes)
- [Examples](sonic_port_breakout_module.md#examples)
- [Return Values](sonic_port_breakout_module.md#return-values)

## [Synopsis](sonic_port_breakout_module.md#id1)

- This module provides configuration management of port breakout parameters on devices running Enterprise SONiC.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_port_breakout_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies the port breakout related configuration. |
| **mode**  string | Specifies the mode of the port breakout.  Choices:   - `"1x100G"` - `"1x400G"` - `"1x40G"` - `"2x100G"` - `"2x200G"` - `"2x50G"` - `"4x100G"` - `"4x10G"` - `"4x25G"` - `"4x50G"` |
| **name**  string / required | Specifies the name of the port breakout. |
| **state**  string | Specifies the operation to be performed on the port breakout configured on the device.  In case of merged, the input mode configuration will be merged with the existing port breakout configuration on the device.  In case of deleted the existing port breakout mode configuration will be removed from the device.  Choices:   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_port_breakout_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_port_breakout_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#do show interface breakout
#-----------------------------------------------
#Port  Breakout Mode  Status        Interfaces
#-----------------------------------------------
#1/1   4x10G          Completed     Eth1/1/1
#                                   Eth1/1/2
#                                   Eth1/1/3
#                                   Eth1/1/4
#1/11  1x100G         Completed     Eth1/11
#

- name: Merge users configurations
  dellemc.enterprise_sonic.sonic_port_breakout:
    config:
      - name: 1/11
        mode: 1x100G
    state: deleted

# After state:
# ------------
#
#do show interface breakout
#-----------------------------------------------
#Port  Breakout Mode  Status        Interfaces
#-----------------------------------------------
#1/1   4x10G          Completed     Eth1/1/1
#                                   Eth1/1/2
#                                   Eth1/1/3
#                                   Eth1/1/4
#1/11  Default        Completed     Ethernet40

# Using deleted
#
# Before state:
# -------------
#
#do show interface breakout
#-----------------------------------------------
#Port  Breakout Mode  Status        Interfaces
#-----------------------------------------------
#1/1   4x10G          Completed     Eth1/1/1
#                                   Eth1/1/2
#                                   Eth1/1/3
#                                   Eth1/1/4
#1/11  1x100G         Completed     Eth1/11
#
- name: Merge users configurations
  dellemc.enterprise_sonic.sonic_port_breakout:
    config:
    state: deleted

# After state:
# ------------
#
#do show interface breakout
#-----------------------------------------------
#Port  Breakout Mode  Status        Interfaces
#-----------------------------------------------
#1/1   Default        Completed     Ethernet0
#1/11  Default        Completed     Ethernet40

# Using merged
#
# Before state:
# -------------
#
#do show interface breakout
#-----------------------------------------------
#Port  Breakout Mode  Status        Interfaces
#-----------------------------------------------
#1/1   4x10G          Completed     Eth1/1/1
#                                   Eth1/1/2
#                                   Eth1/1/3
#                                   Eth1/1/4
#
- name: Merge users configurations
  dellemc.enterprise_sonic.sonic_port_breakout:
    config:
      - name: 1/11
        mode: 1x100G
    state: merged

# After state:
# ------------
#
#do show interface breakout
#-----------------------------------------------
#Port  Breakout Mode  Status        Interfaces
#-----------------------------------------------
#1/1   4x10G          Completed     Eth1/1/1
#                                   Eth1/1/2
#                                   Eth1/1/3
#                                   Eth1/1/4
#1/11  1x100G         Completed     Eth1/11
```

## [Return Values](sonic_port_breakout_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M (@niraimadaiselvamm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
