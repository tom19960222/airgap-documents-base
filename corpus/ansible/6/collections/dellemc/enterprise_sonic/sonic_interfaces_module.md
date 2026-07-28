---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_interfaces module – Configure Interface attributes on interfaces such as, Eth, LAG, VLAN, and loopback. (create a loopback interface if it does not exist.)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_interfaces_module.html
fetched_at: 2026-07-27T17:24:54+00:00
---
# dellemc.enterprise_sonic.sonic_interfaces module – Configure Interface attributes on interfaces such as, Eth, LAG, VLAN, and loopback. (create a loopback interface if it does not exist.)

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
| **description**  string | Description about the interface. |
| **enabled**  boolean | Administrative state of the interface.  Choices:   - `false` - `true` |
| **mtu**  integer | MTU of the interface. |
| **name**  string / required | The name of the interface, for example, ‘Eth1/15’. |
| **state**  string | The state the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"deleted"` |

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
#Name                Description         Admin          Oper           Speed          MTU
#------------------------------------------------------------------------------------------
#Eth1/1           -                   up                            100000         9100
#Eth1/2           -                   up                            100000         9100
#Eth1/3           -                   down                          100000         9100
#Eth1/3           -                   down                          1000           5000
#Eth1/5           -                   down                          100000         9100
#
- name: Configures interfaces
  dellemc.enterprise_sonic.sonic_interfaces:
    config:
      name: Eth1/3
    state: deleted
#
# After state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin          Oper           Speed          MTU
#------------------------------------------------------------------------------------------
#Eth1/1           -                   up                            100000         9100
#Eth1/2           -                   up                            100000         9100
#Eth1/3           -                   down                          100000         9100
#Eth1/3           -                   up                            100000         9100
#Eth1/5           -                   down                          100000         9100
#
#
# Using deleted
#
# Before state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin          Oper           Speed          MTU
#------------------------------------------------------------------------------------------
#Eth1/1           -                   up                            100000         9100
#Eth1/2           -                   up                            100000         9100
#Eth1/3           -                   down                          100000         9100
#Eth1/3           -                   down                          1000           9100
#Eth1/5           -                   down                          100000         9100
#

- name: Configures interfaces
  dellemc.enterprise_sonic.sonic_interfaces:
    config:
    state: deleted

#
# After state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin          Oper           Speed          MTU
#------------------------------------------------------------------------------------------
#Eth1/1           -                   up                            100000         9100
#Eth1/2           -                   up                            100000         9100
#Eth1/3           -                   up                            100000         9100
#Eth1/3           -                   up                            100000         9100
#Eth1/5           -                   up                            100000         9100
#
#
# Using merged
#
# Before state:
# -------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin          Oper           Speed          MTU
#------------------------------------------------------------------------------------------
#Eth1/1           -                   up                            100000         9100
#Eth1/2           -                   up                            100000         9100
#Eth1/3           -                   down                          100000         9100
#Eth1/3           -                   down                          1000           9100
#
- name: Configures interfaces
  dellemc.enterprise_sonic.sonic_interfaces:
    config:
     - name: Eth1/3
       description: 'Ethernet Twelve'
     - name: Eth1/5
       description: 'Ethernet Sixteen'
       enable: True
       mtu: 3500
    state: merged
#
#
# After state:
# ------------
#
# show interface status | no-more
#------------------------------------------------------------------------------------------
#Name                Description         Admin          Oper           Speed          MTU
#------------------------------------------------------------------------------------------
#Eth1/1           -                   up                            100000         9100
#Eth1/2           -                   up                            100000         9100
#Eth1/3           -                   down                          100000         9100
#Eth1/4           -                   down                          1000           9100
#Eth1/5           -                   down                          100000         3500
#
#
```

## [Return Values](sonic_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M(@niraimadaiselvamm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
