---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_interfaces module – Configure Interface attributes on interfaces such as, Eth, LAG, VLAN, and loopback. (create a loopback interface if it does not exist.)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_interfaces_module.html
fetched_at: 2026-07-28T02:03:36+00:00
---
# dellemc.enterprise_sonic.sonic_interfaces module – Configure Interface attributes on interfaces such as, Eth, LAG, VLAN, and loopback. (create a loopback interface if it does not exist.)

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_interfaces`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_interfaces_module.md#synopsis)
- [Parameters](sonic_interfaces_module.md#parameters)
- [Notes](sonic_interfaces_module.md#notes)
- [Examples](sonic_interfaces_module.md#examples)
- [Return Values](sonic_interfaces_module.md#return-values)

## [Synopsis](sonic_interfaces_module.md#id1)

- Configure Interface attributes such as, MTU, admin statu, and so on, on interfaces such as, Eth, LAG, VLAN, and loopback. (create a loopback interface if it does not exist.)

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of interface configurations. |
| **advertised_speed**  list / elements=string | Advertised speeds of the interface.  Supported speeds are dependent on the type of switch.  Speeds may be 10, 100, 1000, 2500, 5000, 10000, 20000, 25000, 40000, 50000, 100000 or 400000. |
| **auto_negotiate**  boolean | auto-negotiate transmission parameters with peer interface.  **Choices:**   - `false` - `true` |
| **description**  string | Description about the interface. |
| **enabled**  boolean | Administrative state of the interface.  **Choices:**   - `false` - `true` |
| **fec**  string | Interface FEC (Forward Error Correction).  **Choices:**   - `"FEC_RS"` - `"FEC_FC"` - `"FEC_DISABLED"` - `"FEC_DEFAULT"` - `"FEC_AUTO"` |
| **mtu**  integer | MTU of the interface. |
| **name**  string / required | The name of the interface, for example, ‘Eth1/15’. |
| **speed**  string | Interface speed.  Supported speeds are dependent on the type of switch.  **Choices:**   - `"SPEED_10MB"` - `"SPEED_100MB"` - `"SPEED_1GB"` - `"SPEED_2500MB"` - `"SPEED_5GB"` - `"SPEED_10GB"` - `"SPEED_20GB"` - `"SPEED_25GB"` - `"SPEED_40GB"` - `"SPEED_50GB"` - `"SPEED_100GB"` - `"SPEED_400GB"` |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Notes](sonic_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_interfaces_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           -                   up                              100000       9100
#Ethernet4           -                   up                              100000       9100
#Ethernet8           Ethernet-8          down                            100000       9100
#Ethernet12          Ethernet-12         down                on          -            5000
#Ethernet16          -                   down                            40000        9100
#
# show running-configuration interface Ethernet 8
#!
#interface Ethernet8
# mtu 9100
# speed 100000
# fec AUTO
# shutdown
#
- name: Configure interfaces
  sonic_interfaces:
    config:
      - name: Ethernet8
      - name: Ethernet12
      - name: Ethernet16
    state: deleted
#
# After state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           -                   up                              100000       9100
#Ethernet4           -                   up                              100000       9100
#Ethernet8           -                   up                              100000       9100
#Ethernet12          -                   up                              100000       9100
#Ethernet16          -                   up                              100000       9100
#
# show running-configuration interface Ethernet 8
#!
#interface Ethernet8
# mtu 9100
# speed 100000
# shutdown
#
# Using deleted
#
# Before state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           -                   up                              100000       9100
#Ethernet4           -                   up                              100000       9100
#Ethernet8           -                   down                            100000       9100
#Ethernet12          -                   down                            1000         9100
#Ethernet16          -                   down                            100000       9100
#
- name: Configure interfaces
  sonic_interfaces:
    config:

    state: deleted
#
# After state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           -                   up                              100000       9100
#Ethernet4           -                   up                              100000       9100
#Ethernet8           -                   up                              100000       9100
#Ethernet12          -                   up                              100000       9100
#Ethernet16          -                   up                              100000       9100
#
#
#
# Using merged
#
# Before state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           -                   up                              100000       9100
#Ethernet4           -                   up                              100000       9100
#Ethernet8           -                   down                            100000       9100
#Ethernet12          -                   down                            100000       9100
#Ethernet16          -                   down                            100000       9100
#
# show running-configuration interface Ethernet 8
#!
#interface Ethernet8
# mtu 9100
# speed 100000
# shutdown
#
- name: Configure interfaces
  sonic_interfaces:
    config:
      - name: Ethernet8
        fec: FEC_AUTO
      - name: Ethernet12
        description: 'Ethernet Twelve'
        auto_negotiate: True
      - name: Ethernet16
        description: 'Ethernet Sixteen'
        enabled: True
        mtu: 3500
        speed: SPEED_40GB
    state: merged
#
# After state:
# ------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           -                   up                              100000       9100
#Ethernet4           -                   up                              100000       9100
#Ethernet8           -                   down                            100000       9100
#Ethernet12          Ethernet Twelve     down                on          100000       9100
#Ethernet16          Ethernet Sixteen    up                              40000        3500
#
# show running-configuration interface Ethernet 8
#!
#interface Ethernet8
# mtu 9100
# speed 100000
# fec AUTO
# shutdown
#
# Using overridden
#
# Before state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           E0                  up                              100000       9100
#Ethernet4           E4                  up                              100000       9100
#Ethernet8           E8                  down                            100000       9100
#Ethernet12          -                   down                            1000         9100
#Ethernet16          -                   down                            100000       9100
#
# show running-configuration interface Ethernet 8
#!
#interface Ethernet8
# mtu 9100
# speed 100000
# shutdown
#
- name: Configure interfaces
  sonic_interfaces:
    config:
      - name: Ethernet8
        fec: FEC_AUTO
      - name: Ethernet12
        description: 'Ethernet Twelve'
        mtu: 3500
        enable: True
        auto_negotiate: True
      - name: Ethernet16
        description: 'Ethernet Sixteen'
        mtu: 3000
        enable: False
        speed: SPEED_40GB
    state: overridden
#
# After state:
# ------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           -                   up                              100000       9100
#Ethernet4           -                   up                              100000       9100
#Ethernet8           -                   up                              100000       9100
#Ethernet12          Ethernet Twelve     up                  on          100000       3500
#Ethernet16          Ethernet Sixteen    down                            40000        3000
#
# show running-configuration interface Ethernet 8
#!
#interface Ethernet8
# mtu 9100
# speed 100000
# fec AUTO
# no shutdown
#
# Using replaced
#
# Before state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           -                   up                              100000       9100
#Ethernet4           -                   up                              100000       9100
#Ethernet8           -                   down                            100000       9100
#Ethernet12          -                   down                            1000         9100
#Ethernet16          -                   down                            100000       9100
#
# show running-configuration interface Ethernet 8
#!
#interface Ethernet8
# mtu 9100
# speed 100000
# shutdown
#
- name: Configure interfaces
  sonic_interfaces:
    config:
      - name: Ethernet8
        fec: FEC_AUTO
      - name: Ethernet12
        description: 'Ethernet Twelve'
        mtu: 3500
        enable: True
        auto_negotiate: True
      - name: Ethernet16
        description: 'Ethernet Sixteen'
        mtu: 3000
        enable: False
        speed: SPEED_40GB
    state: replaced
#
# After state:
# ------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin     Oper      AutoNeg     Speed        MTU
#------------------------------------------------------------------------------------------
#Ethernet0           -                   up                              100000       9100
#Ethernet4           -                   up                              100000       9100
#Ethernet8           -                   up                              100000       9100
#Ethernet12          Ethernet Twelve     up                  on          100000       3500
#Ethernet16          Ethernet Sixteen    down                            40000        3000
#
# show running-configuration interface Ethernet 8
#!
#interface Ethernet8
# mtu 9100
# speed 100000
# fec AUTO
# no shutdown
#
```

## [Return Values](sonic_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M(@niraimadaiselvamm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
