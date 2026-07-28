---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_lag_interfaces module – LAG interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_lag_interfaces_module.html
fetched_at: 2026-07-27T17:02:01+00:00
---
# cisco.nxos.nxos_lag_interfaces module – LAG interfaces resource module

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_lag_interfaces`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_lag_interfaces_module.md#synopsis)
- [Parameters](nxos_lag_interfaces_module.md#parameters)
- [Notes](nxos_lag_interfaces_module.md#notes)
- [Examples](nxos_lag_interfaces_module.md#examples)
- [Return Values](nxos_lag_interfaces_module.md#return-values)

## [Synopsis](nxos_lag_interfaces_module.md#id1)

- This module manages attributes of link aggregation groups of NX-OS Interfaces.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_lag_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of link aggregation group configurations. |
| **members**  list / elements=dictionary | The list of interfaces that are part of the group. |
| **force**  boolean | When true it forces link aggregation group members to match what is declared in the members param. This can be used to remove members.  Choices:   - `false` - `true` |
| **member**  string | The interface name. |
| **mode**  string | Link aggregation group (LAG).  Choices:   - `"active"` - `"on"` - `"passive"` |
| **name**  string / required | Name of the link aggregation group (LAG). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_lag_interfaces_module.md#id3)

> **Note:**
>
> - Tested against NXOS 7.3.(0)D1(1) on VIRL.
> - Unsupported for Cisco MDS
> - This module works with connection `network_cli`.

## [Examples](nxos_lag_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# interface Ethernet1/4

- name: Merge provided configuration with device configuration.
  cisco.nxos.nxos_lag_interfaces:
    config:
    - name: port-channel99
      members:
      - member: Ethernet1/4
    state: merged

# After state:
# ------------
#
# interface Ethernet1/4
#   channel-group 99

# Using replaced

# Before state:
# -------------
#
# interface Ethernet1/4
#   channel-group 99 mode active

- name: Replace device configuration of specified LAG attributes of given interfaces
    with provided configuration.
  cisco.nxos.nxos_lag_interfaces:
    config:
    - name: port-channel10
      members:
      - member: Ethernet1/4
    state: replaced

# After state:
# ------------
#
# interface Ethernet1/4
#   channel-group 10

# Using overridden

# Before state:
# -------------
#
# interface Ethernet1/4
#   channel-group 10
# interface Ethernet1/2
#   channel-group 99 mode passive

- name: Override device configuration of all LAG attributes of given interfaces on
    device with provided configuration.
  cisco.nxos.nxos_lag_interfaces:
    config:
    - name: port-channel20
      members:
      - member: Ethernet1/6
        force: true
    state: overridden

# After state:
# ------------
# interface Ethernet1/2
# interface Ethernet1/4
# interface Ethernet1/6
#   channel-group 20 force

# Using deleted

# Before state:
# -------------
#
# interface Ethernet1/4
#   channel-group 99 mode active

- name: Delete LAG attributes of given interface (This won't delete the port-channel
    itself).
  cisco.nxos.nxos_lag_interfaces:
    config:
    - port-channel: port-channel99
    state: deleted

- name: Delete LAG attributes of all the interfaces
  cisco.nxos.nxos_lag_interfaces:
    state: deleted

# After state:
# ------------
#
# interface Ethernet1/4
#   no channel-group 99

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_lag_interfaces:
    config:
    - name: port-channel10
      members:
      - member: Ethernet1/800
        mode: active
      - member: Ethernet1/801
    - name: port-channel11
      members:
      - member: Ethernet1/802
        mode: passive
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#  - "interface Ethernet1/800"
#  - "channel-group 10 mode active"
#  - "interface Ethernet1/801"
#  - "channel-group 10"
#  - "interface Ethernet1/802"
#  - "channel-group 11 mode passive"

# Using parsed

# parsed.cfg
# ------------

# interface port-channel10
# interface port-channel11
# interface port-channel12
# interface Ethernet1/800
#   channel-group 10 mode active
# interface Ethernet1/801
#   channel-group 10 mode active
# interface Ethernet1/802
#   channel-group 11 mode passive
# interface Ethernet1/803
#   channel-group 11 mode passive

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_lag_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------

# parsed:
#  - members:
#      - member: Ethernet1/800
#        mode: active
#      - member: Ethernet1/801
#        mode: active
#    name: port-channel10
#
#  - members:
#      - member: Ethernet1/802
#        mode: passive
#      - member: Ethernet1/803
#        mode: passive
#    name: port-channel11
#
#  - name: port-channel12

# Using gathered

# Existing device config state
# -------------------------------
# interface port-channel10
# interface port-channel11
# interface Ethernet1/1
#   channel-group 10 mode active
# interface Ethernet1/2
#   channel-group 11 mode passive
#

- name: Gather lag_interfaces facts from the device using nxos_lag_interfaces
  cisco.nxos.nxos_lag_interfaces:
    state: gathered

# Task output (redacted)
# -----------------------
# gathered:
#  - name: port-channel10
#    members:
#      - member: Ethernet1/1
#        mode: active
#  - name: port-channel11
#    members:
#      - member: Ethernet1/2
#        mode: passive
```

## [Return Values](nxos_lag_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface Ethernet1/800", "channel-group 10 mode active", "interface Ethernet1/801", "channel-group 10", "interface Ethernet1/802", "channel-group 11 mode passive"]` |

### Authors

- Trishna Guha (@trishnaguha)
- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
