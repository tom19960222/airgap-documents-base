---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_port_group module – Manages port group configuration on SONiC."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_port_group_module.html
fetched_at: 2026-07-28T02:03:46+00:00
---
# dellemc.enterprise_sonic.sonic_port_group module – Manages port group configuration on SONiC.

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_port_group`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_port_group_module.md#synopsis)
- [Parameters](sonic_port_group_module.md#parameters)
- [Examples](sonic_port_group_module.md#examples)
- [Return Values](sonic_port_group_module.md#return-values)

## [Synopsis](sonic_port_group_module.md#id1)

- This module provides configuration management of port group for devices running SONiC.

## [Parameters](sonic_port_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of port group configurations. |
| **id**  string / required | The index of the port group. |
| **speed**  string | Speed for the port group.  This configures the speed for all the memebr ports of the prot group.  Supported speeds are dependent on the type of switch.  **Choices:**   - `"SPEED_10MB"` - `"SPEED_100MB"` - `"SPEED_1GB"` - `"SPEED_2500MB"` - `"SPEED_5GB"` - `"SPEED_10GB"` - `"SPEED_20GB"` - `"SPEED_25GB"` - `"SPEED_40GB"` - `"SPEED_50GB"` - `"SPEED_100GB"` - `"SPEED_400GB"` |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Examples](sonic_port_group_module.md#id3)

```yaml+jinja
#
# Using deleted
#
# Before state:
# -------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
#
- name: Configure port group speed
  sonic_port_group:
    config:
      - id: 1
      - id: 10
    state: deleted
#
#
# After state:
# ------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
#
# Using deleted
#
# Before state:
# -------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
#
- name: Configure port group speed
  sonic_port_group:
    config:
      - id:
    state: deleted
#
#
# After state:
# ------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           25G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
#
# Using merged
#
# Before state:
# -------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           25G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
#
- name: Configure port group speed
  sonic_port_group:
    config:
      - id: 1
        speed: SPEED_10GB
      - id: 9
        speed: SPEED_10GB
    state: merged
#
#
# After state:
# ------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
#
# Using replaced
#
# Before state:
# -------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           10G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           25G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
#
- name: Replace port group speed
  sonic_port_group:
    config:
      - id: 1
        speed: SPEED_10GB
      - id: 9
        speed: SPEED_10GB
    state: replaced
#
# After state:
# ------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           10G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
#
# Using overridden
#
# Before state:
# -------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           10G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           10G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           10G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           10G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           10G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           10G
#
- name: Override port group speed
  sonic_port_group:
    config:
      - id: 1
        speed: SPEED_10GB
      - id: 9
        speed: SPEED_10GB
    state: overridden
#
# After state:
# ------------
#
#sonic# show port-group
#-------------------------------------------------------------------------------------
#Port-group  Interface range            Valid speeds      Default Speed Current Speed
#-------------------------------------------------------------------------------------
#1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
#2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
#3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
#4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
#5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
#6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
#7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
#8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
#9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
#10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
#
```

## [Return Values](sonic_port_group_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- 13. Zhang (@mingjunzhang2019)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
