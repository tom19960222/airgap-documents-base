---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_hsrp_interfaces module – HSRP interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_hsrp_interfaces_module.html
fetched_at: 2026-07-27T17:01:51+00:00
---
# cisco.nxos.nxos_hsrp_interfaces module – HSRP interfaces resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_hsrp_interfaces`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_hsrp_interfaces_module.md#synopsis)
- [Parameters](nxos_hsrp_interfaces_module.md#parameters)
- [Notes](nxos_hsrp_interfaces_module.md#notes)
- [Examples](nxos_hsrp_interfaces_module.md#examples)
- [Return Values](nxos_hsrp_interfaces_module.md#return-values)

## [Synopsis](nxos_hsrp_interfaces_module.md#id1)

- Manages Hot Standby Router Protocol (HSRP) interface attributes.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_hsrp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | The provided configuration |
| **bfd**  string | Enable/Disable HSRP Bidirectional Forwarding Detection (BFD) on the interface.  Choices:   - `"enable"` - `"disable"` |
| **name**  string | The name of the interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^interface’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_hsrp_interfaces_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 7.0(3)I5(1).
> - Feature bfd should be enabled for this module.
> - Unsupported for Cisco MDS

## [Examples](nxos_hsrp_interfaces_module.md#id4)

```yaml+jinja
# Using deleted

- name: Configure hsrp attributes on interfaces
  cisco.nxos.nxos_hsrp_interfaces:
    config:
    - name: Ethernet1/1
    - name: Ethernet1/2
    operation: deleted

# Using merged

- name: Configure hsrp attributes on interfaces
  cisco.nxos.nxos_hsrp_interfaces:
    config:
    - name: Ethernet1/1
      bfd: enable
    - name: Ethernet1/2
      bfd: disable
    operation: merged

# Using overridden

- name: Configure hsrp attributes on interfaces
  cisco.nxos.nxos_hsrp_interfaces:
    config:
    - name: Ethernet1/1
      bfd: enable
    - name: Ethernet1/2
      bfd: disable
    operation: overridden

# Using replaced

- name: Configure hsrp attributes on interfaces
  cisco.nxos.nxos_hsrp_interfaces:
    config:
    - name: Ethernet1/1
      bfd: enable
    - name: Ethernet1/2
      bfd: disable
    operation: replaced

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_hsrp_interfaces:
    config:
    - name: Ethernet1/800
      bfd: enable
    - name: Ethernet1/801
      bfd: enable
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#   - "interface Ethernet1/800"
#   - "hsrp bfd"
#   - "interface Ethernet1/801"
#   - "hsrp bfd"

# Using parsed

# parsed.cfg
# ------------
# interface Ethernet1/800
#   no switchport
#   hsrp bfd
# interface Ethernet1/801
#   no switchport
#   hsrp bfd

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_hsrp_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------

# parsed:
#   - name: Ethernet1/800
#     bfd: enable
#   - name: Ethernet1/801
#     bfd: enable

# Using gathered

# Existing device config state
# -------------------------------

# interface Ethernet1/1
#   no switchport
#   hsrp bfd
# interface Ethernet1/2
#   no switchport
#   hsrp bfd
# interface Ethernet1/3
#   no switchport

- name: Gather hsrp_interfaces facts from the device using nxos_hsrp_interfaces
  cisco.nxos.nxos_hsrp_interfaces:
    state: gathered

# Task output (redacted)
# -----------------------

# gathered:
#   - name: Ethernet1/1
#     bfd: enable
#   - name: Ethernet1/2
#     bfd: enable
```

## [Return Values](nxos_hsrp_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface Ethernet1/1", "hsrp bfd"]` |

### Authors

- Chris Van Heuveln (@chrisvanheuveln)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
