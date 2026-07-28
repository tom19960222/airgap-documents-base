---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_lacp_interfaces module – LACP interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_lacp_interfaces_module.html
fetched_at: 2026-07-28T01:38:49+00:00
---
# cisco.nxos.nxos_lacp_interfaces module – LACP interfaces resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_lacp_interfaces`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_lacp_interfaces_module.md#synopsis)
- [Parameters](nxos_lacp_interfaces_module.md#parameters)
- [Notes](nxos_lacp_interfaces_module.md#notes)
- [Examples](nxos_lacp_interfaces_module.md#examples)
- [Return Values](nxos_lacp_interfaces_module.md#return-values)

## [Synopsis](nxos_lacp_interfaces_module.md#id1)

- This module manages Link Aggregation Control Protocol (LACP) attributes of NX-OS Interfaces.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: lacp_interfaces

## [Parameters](nxos_lacp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of LACP interfaces options. |
| **convergence**  dictionary | This dict contains configurable options related to convergence. Applicable only for Port-channel. |
| **graceful**  boolean | port-channel lacp graceful convergence. Disable this only with lacp ports connected to Non-Nexus peer. Disabling this with Nexus peer can lead to port suspension.  **Choices:**   - `false` - `true` |
| **vpc**  boolean | Enable lacp convergence for vPC port channels.  **Choices:**   - `false` - `true` |
| **links**  dictionary | This dict contains configurable options related to max and min port-channel links. Applicable only for Port-channel. |
| **max**  integer | Port-channel max bundle. |
| **min**  integer | Port-channel min links. |
| **mode**  string | LACP mode. Applicable only for Port-channel.  **Choices:**   - `"delay"` |
| **name**  string / required | Name of the interface. |
| **port_priority**  integer | LACP port priority for the interface. Range 1-65535. Applicable only for Ethernet. |
| **rate**  string | Rate at which PDUs are sent by LACP. Applicable only for Ethernet. At fast rate LACP is transmitted once every 1 second. At normal rate LACP is transmitted every 30 seconds after the link is bundled.  **Choices:**   - `"fast"` - `"normal"` |
| **suspend_individual**  boolean | port-channel lacp state. Disabling this will cause lacp to put the port to individual state and not suspend the port in case it does not get LACP BPDU from the peer ports in the port-channel.  **Choices:**   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_lacp_interfaces_module.md#id3)

> **Note:**
>
> - Tested against NXOS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS

## [Examples](nxos_lacp_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#

- name: Merge provided configuration with device configuration.
  cisco.nxos.nxos_lacp_interfaces:
    config:
    - name: Ethernet1/3
      port_priority: 5
      rate: fast
    state: merged

# After state:
# ------------
#
# interface Ethernet1/3
# lacp port-priority 5
# lacp rate fast

# Using replaced

# Before state:
# -------------
#
# interface Ethernet1/3
#   lacp port-priority 5
# interface port-channel11
#   lacp mode delay

- name: Replace device lacp interfaces configuration with the given configuration.
  cisco.nxos.nxos_lacp_interfaces:
    config:
    - name: port-channel11
      links:
        min: 4
    state: replaced

# After state:
# ------------
#
# interface Ethernet1/3
#   lacp port-priority 5
# interface port-channel11
#   lacp min-links 4

# Using overridden

# Before state:
# -------------
#
# interface Ethernet1/3
#   lacp port-priority 5
# interface port-channel11
#   lacp mode delay

- name: Override device configuration of all LACP interfaces attributes of given interfaces
    on device with provided configuration.
  cisco.nxos.nxos_lacp_interfaces:
    config:
    - name: port-channel11
      links:
        min: 4
    state: overridden

# After state:
# ------------
#
# interface port-channel11
# lacp min-links 4

# Using deleted

# Before state:
# -------------
#
# interface Ethernet1/3
#   lacp port-priority 5
# interface port-channel11
#   lacp mode delay

- name: Delete LACP interfaces configurations.
  cisco.nxos.nxos_lacp_interfaces:
    state: deleted

# After state:
# ------------
#

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_lacp_interfaces:
    config:
    - name: Ethernet1/800
      rate: fast
    - name: Ethernet1/801
      rate: fast
      port_priority: 32
    - name: port-channel10
      links:
        max: 15
        min: 2
      convergence:
        graceful: true
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#  - "interface Ethernet1/800"
#  - "lacp rate fast"
#  - "interface Ethernet1/801"
#  - "lacp port-priority 32"
#  - "lacp rate fast"
#  - "interface port-channel10"
#  - "lacp min-links 2"
#  - "lacp max-bundle 15"
#  - "lacp graceful-convergence"

# Using parsed

# parsed.cfg
# ------------

# interface port-channel10
#   lacp min-links 10
#   lacp max-bundle 15
# interface Ethernet1/800
#   lacp port-priority 100
#   lacp rate fast

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_lacp_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------

# parsed:
#   - name: port-channel10
#     links:
#       max: 15
#       min: 10
#   - name: Ethernet1/800
#     port_priority: 100
#     rate: fast

# Using gathered

# Existing device config state
# -------------------------------
# interface Ethernet1/1
#   lacp port-priority 5
#   lacp rate fast
# interface port-channel10
#   lacp mode delay
# interface port-channel11
#   lacp max-bundle 10
#   lacp min-links 5

- name: Gather lacp_interfaces facts from the device using nxos_lacp_interfaces
  cisco.nxos.nxos_lacp_interfaces:
    state: gathered

# Task output (redacted)
# -----------------------
# gathered:
#  - name: Ethernet1/1
#    port_priority: 5
#    rate: fast
#  - name: port-channel10
#    mode: delay
#  - name: port-channel11
#    links:
#      max: 10
#      min: 5
```

## [Return Values](nxos_lacp_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface port-channel10", "lacp min-links 5", "lacp mode delay"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
