---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_hostname module – Manages hostname resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_hostname_module.html
fetched_at: 2026-07-28T02:59:13+00:00
---
# vyos.vyos.vyos_hostname module – Manages hostname resource module

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_hostname`.

New in vyos.vyos 2.8.0

- [Synopsis](vyos_hostname_module.md#synopsis)
- [Parameters](vyos_hostname_module.md#parameters)
- [Notes](vyos_hostname_module.md#notes)
- [Examples](vyos_hostname_module.md#examples)
- [Return Values](vyos_hostname_module.md#return-values)

## [Synopsis](vyos_hostname_module.md#id1)

- This module manages the hostname attribute of Vyos network devices

Aliases: hostname

## [Parameters](vyos_hostname_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Hostname configuration. |
| **hostname**  string | set hostname for VYOS. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the vyos device by executing the command **“show configuration commands | grep host-name”**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The states *merged*, *replaced* and *overridden* have identical behaviour for this module.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show configuration commands | grep host-name* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](vyos_hostname_module.md#id3)

> **Note:**
>
> - Tested against vyos 1.1.8
> - This module works with connection `network_cli`.
> - The Configuration defaults of the Vyos network devices are supposed to hinder idempotent behavior of plays

## [Examples](vyos_hostname_module.md#id4)

```yaml+jinja
# Using state: merged
# Before state:
# -------------
# test#show configuration commands | grep host-name
# set system host-name 'vyostest'
# Merged play:
# ------------
- name: Apply the provided configuration
  vyos.vyos.vyos_hostname:
    config:
      hostname: vyos
    state: merged
# Commands Fired:
# ---------------
# "commands": [
#         "hostname vyos",
# ],
# After state:
# ------------
# test#show configuration commands | grep host-name
# set system host-name 'vyos'

# Using state: deleted
# Before state:
# -------------
# test#show configuration commands | grep host-name
# set system host-name 'vyos'
# Deleted play:
# -------------
- name: Remove all existing configuration
  vyos.vyos.vyos_hostname:
    state: deleted
# Commands Fired:
# ---------------
# "commands": [
#     "no hostname vyosTest",
# ],
# After state:
# ------------
# test#show configuration commands | grep host-name

# Using state: overridden
# Before state:
# -------------
# test#show configuration commands | grep host-name
# set system host-name 'vyos'
# Overridden play:
# ----------------
- name: Override commands with provided configuration
  vyos.vyos.vyos_hostname:
    config:
      hostname: vyosTest
    state: overridden
# Commands Fired:
# ---------------
# "commands": [
#       "hostname vyosTest",
#     ],
# After state:
# ------------
# test#show configuration commands | grep host-name
# set system host-name 'vyosTest'

# Using state: replaced
# Before state:
# -------------
# test#show configuration commands | grep host-name
# set system host-name 'vyosTest'
# Replaced play:
# --------------
- name: Replace commands with provided configuration
  vyos.vyos.vyos_hostname:
    config:
      hostname: vyos
    state: replaced
# After state:
# ------------
# test#show configuration commands | grep host-name
# set system host-name 'vyos'

# Using state: gathered
# Before state:
# -------------
#test#show configuration commands | grep host-name
# set system host-name 'vyos'
# Gathered play:
# --------------
- name: Gather listed hostname config
  vyos.vyos.vyos_hostname:
    state: gathered
# Module Execution Result:
# ------------------------
#   "gathered": {
#      "hostname": "vyos"
#     },

# Using state: rendered
# Rendered play:
# --------------
- name: Render the commands for provided configuration
  vyos.vyos.vyos_hostname:
    config:
      hostname: vyosTest
    state: rendered
# Module Execution Result:
# ------------------------
# "rendered": [
#     "set system host-name vyosTest",
# ]

# Using state: parsed
# File: parsed.cfg
# ----------------
# set system host-name 'vyos'
# Parsed play:
# ------------
- name: Parse the provided configuration with the existing running configuration
  vyos.vyos.vyos_hostname:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed
# Module Execution Result:
# ------------------------
#  "parsed": {
#     "hostname": "vyos"
# }
```

## [Return Values](vyos_hostname_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["sample command 1", "sample command 2", "sample command 3"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["sample command 1", "sample command 2", "sample command 3"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
