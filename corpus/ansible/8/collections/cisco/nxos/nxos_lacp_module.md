---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_lacp module – LACP resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_lacp_module.html
fetched_at: 2026-07-28T01:38:48+00:00
---
# cisco.nxos.nxos_lacp module – LACP resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_lacp`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_lacp_module.md#synopsis)
- [Parameters](nxos_lacp_module.md#parameters)
- [Notes](nxos_lacp_module.md#notes)
- [Examples](nxos_lacp_module.md#examples)
- [Return Values](nxos_lacp_module.md#return-values)

## [Synopsis](nxos_lacp_module.md#id1)

- This module manages Global Link Aggregation Control Protocol (LACP) on NX-OS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: lacp

## [Parameters](nxos_lacp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | LACP global options. |
| **system**  dictionary | LACP system options |
| **mac**  dictionary | MAC address to be used for the LACP Protocol exchanges |
| **address**  string | MAC-address (FORMAT :xxxx.xxxx.xxxx). |
| **role**  string | The role for the Switch.  **Choices:**   - `"primary"` - `"secondary"` |
| **priority**  integer | The system priority to use in LACP negotiations. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | include lacp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_lacp_module.md#id3)

> **Note:**
>
> - Tested against NXOS 7.3.(0)D1(1) on VIRL.
> - Unsupported for Cisco MDS
> - Feature lacp should be enabled for this module.

## [Examples](nxos_lacp_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#

- name: Merge provided configuration with device configuration.
  cisco.nxos.nxos_lacp:
    config:
      system:
        priority: 10
        mac:
          address: 00c1.4c00.bd15
    state: merged

# After state:
# ------------
#
# lacp system-priority 10
# lacp system-mac 00c1.4c00.bd15

# Using replaced

# Before state:
# -------------
#
# lacp system-priority 10

- name: Replace device global lacp configuration with the given configuration.
  cisco.nxos.nxos_lacp:
    config:
      system:
        mac:
          address: 00c1.4c00.bd15
    state: replaced

# After state:
# ------------
#
# lacp system-mac 00c1.4c00.bd15

# Using deleted

# Before state:
# -------------
#
# lacp system-priority 10

- name: Delete global LACP configurations.
  cisco.nxos.nxos_lacp:
    state: deleted

# After state:
# ------------
#

# Using rendered

- name: Render platform specific configuration lines (without connecting to the device)
  cisco.nxos.nxos_lacp:
    config:
      system:
        priority: 10
        mac:
          address: 00c1.4c00.bd15
          role: secondary
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#   - "lacp system-priority 10"
#   - "lacp system-mac 00c1.4c00.bd15 role secondary"

# Using parsed

# parsed.cfg
# ------------
# lacp system-priority 10
# lacp system-mac 00c1.4c00.bd15 role secondary

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_lacp:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# parsed:
#  system:
#    priority: 10
#    mac:
#      address: 00c1.4c00.bd15
#      role: secondary

# Using gathered

# Existing device config state
# -------------------------------
# Nexus9000v# show running-config | include lacp
# lacp system-priority 11
# lacp system-mac 00c1.4c00.bd15 role primary

- name: Gather lacp facts from the device using nxos_lacp
  cisco.nxos.nxos_lacp:
    state: gathered

# Task output (redacted)
# -----------------------
# gathered:
#  system:
#    priority: 11
#    mac:
#      address: 00c1.4c00.bd15
#      role: primary
```

## [Return Values](nxos_lacp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["lacp system-priority 15", "lacp system-mac 00c1.4c00.bd15 role primary"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
