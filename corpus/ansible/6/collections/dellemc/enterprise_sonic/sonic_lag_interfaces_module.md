---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_lag_interfaces module – Manage link aggregation group (LAG) interface parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_lag_interfaces_module.html
fetched_at: 2026-07-27T17:24:56+00:00
---
# dellemc.enterprise_sonic.sonic_lag_interfaces module – Manage link aggregation group (LAG) interface parameters

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_lag_interfaces`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_lag_interfaces_module.md#synopsis)
- [Parameters](sonic_lag_interfaces_module.md#parameters)
- [Notes](sonic_lag_interfaces_module.md#notes)
- [Examples](sonic_lag_interfaces_module.md#examples)
- [Return Values](sonic_lag_interfaces_module.md#return-values)

## [Synopsis](sonic_lag_interfaces_module.md#id1)

- This module manages attributes of link aggregation group (LAG) interfaces of devices running Enterprise SONiC Distribution by Dell Technologies.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_lag_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of LAG configurations. |
| **members**  dictionary | The list of interfaces that are part of the group. |
| **interfaces**  list / elements=dictionary | The list of interfaces that are part of the group. |
| **member**  string | The interface name. |
| **mode**  string | Specifies mode of the port-channel while creation.  Choices:   - `"static"` - `"lacp"` |
| **name**  string / required | ID of the LAG. |
| **state**  string | The state that the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_lag_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_lag_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# interface Eth1/10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  channel-group 12
#  mtu 9100
#  speed 100000
#  no shutdown
#
- name: Merges provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
     - name: PortChannel10
       members:
         interfaces:
           - member: Eth1/10
    state: merged
#
# After state:
# ------------
#
# interface Eth1/10
#  channel-group 10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  channel-group 12
#  mtu 9100
#  speed 100000
#  no shutdown
#
# Using deleted
#
# Before state:
# -------------
# interface PortChannel10
# !
# interface Eth1/10
#  channel-group 10
#  mtu 9100
#  speed 100000
#  no shutdown
#
- name: Deletes LAG attributes of a given interface, This does not delete the port-channel itself
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
     - name: PortChannel10
       members:
         interfaces:
    state: deleted
#
# After state:
# ------------
# interface PortChannel10
# !
# interface Eth1/10
#  mtu 9100
#  speed 100000
#  no shutdown
#
# Using deleted
#
# Before state:
# -------------
# interface PortChannel 10
# !
# interface PortChannel 12
# !
# interface Eth1/10
#  channel-group 10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  channel-group 12
#  mtu 9100
#  speed 100000
#  no shutdown
#
- name: Deletes all LAGs and LAG attributes of all interfaces
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
    state: deleted
#
# After state:
# -------------
#
# interface Eth1/10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  mtu 9100
#  speed 100000
#  no shutdown
#
#
```

## [Return Values](sonic_lag_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration that is returned is always in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
