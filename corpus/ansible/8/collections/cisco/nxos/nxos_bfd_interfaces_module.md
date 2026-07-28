---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_bfd_interfaces module – BFD interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_bfd_interfaces_module.html
fetched_at: 2026-07-28T01:38:29+00:00
---
# cisco.nxos.nxos_bfd_interfaces module – BFD interfaces resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_bfd_interfaces`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_bfd_interfaces_module.md#synopsis)
- [Parameters](nxos_bfd_interfaces_module.md#parameters)
- [Notes](nxos_bfd_interfaces_module.md#notes)
- [Examples](nxos_bfd_interfaces_module.md#examples)
- [Return Values](nxos_bfd_interfaces_module.md#return-values)

## [Synopsis](nxos_bfd_interfaces_module.md#id1)

- Manages attributes of Bidirectional Forwarding Detection (BFD) on the interface.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: bfd_interfaces

## [Parameters](nxos_bfd_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | The provided configuration |
| **bfd**  string | Enable/Disable Bidirectional Forwarding Detection (BFD) on the interface.  **Choices:**   - `"enable"` - `"disable"` |
| **echo**  string | Enable/Disable BFD Echo functionality on the interface.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string | The name of the interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^interface|^feature bfd’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_bfd_interfaces_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 7.0(3)I5(1).
> - Unsupported for Cisco MDS
> - Feature bfd should be enabled for this module.

## [Examples](nxos_bfd_interfaces_module.md#id4)

```yaml+jinja
# Using deleted

- name: Configure interfaces
  cisco.nxos.nxos_bfd_interfaces:
    state: deleted

# Using merged

- name: Configure interfaces
  cisco.nxos.nxos_bfd_interfaces:
    config:
    - name: Ethernet1/1
      bfd: enable
      echo: enable
    - name: Ethernet1/2
      bfd: disable
      echo: disable
    state: merged

# Using overridden

- name: Configure interfaces
  cisco.nxos.nxos_bfd_interfaces:
    config:
    - name: Ethernet1/1
      bfd: enable
      echo: enable
    - name: Ethernet1/2
      bfd: disable
      echo: disable
    state: overridden

# Using replaced

- name: Configure interfaces
  cisco.nxos.nxos_bfd_interfaces:
    config:
    - name: Ethernet1/1
      bfd: enable
      echo: enable
    - name: Ethernet1/2
      bfd: disable
      echo: disable
    state: replaced

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_bfd_interfaces:
    config:
    - name: Ethernet1/800
      bfd: enable
      echo: enable
    - name: Ethernet1/801
      bfd: disable
      echo: disable
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#   - "interface Ethernet1/800"
#   - "bfd"
#   - "bfd echo"
#   - "interface Ethernet1/801"
#   - "no bfd"
#   - "no bfd echo"

# Using parsed

# parsed.cfg
# ------------

# feature bfd
# interface Ethernet1/800
#   no switchport
#   no bfd
#   no bfd echo
# interface Ethernet1/801
#   no switchport
#   no bfd
# interface Ethernet1/802
#   no switchport
#   no bfd echo
# interface mgmt0
#   ip address dhcp
#   vrf member management

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_bfd_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------

# parsed:
#   - bfd: disable
#     echo: disable
#     name: Ethernet1/800
#   - bfd: disable
#     echo: enable
#     name: Ethernet1/801
#   - bfd: enable
#     echo: disable
#     name: Ethernet1/802
#   - bfd: enable
#     echo: enable
#     name: mgmt0

# Using gathered

# Existing device config state
# -------------------------------

# feature bfd
# interface Ethernet1/1
#   no switchport
#   no bfd
# interface Ethernet1/2
#   no switchport
#   no bfd echo
# interface mgmt0
#   ip address dhcp
#   vrf member management

- name: Gather bfd_interfaces facts from the device using nxos_bfd_interfaces
  cisco.nxos.nxos_bfd_interfaces:
    state: gathered

# Task output (redacted)
# -----------------------
# gathered:
# - name: Ethernet1/1
#   bfd: disable
#   echo: enable
# - name: Ethernet1/3
#   echo: disable
#   bfd: enable
# - name: mgmt0
#   bfd: enable
#   echo: enable
```

## [Return Values](nxos_bfd_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface Ethernet1/1", "no bfd", "no bfd echo"]` |

### Authors

- Chris Van Heuveln (@chrisvanheuveln)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
