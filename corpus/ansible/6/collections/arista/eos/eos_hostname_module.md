---
collection: ansible
version: "6"
title: "arista.eos.eos_hostname module – Manages hostname resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_hostname_module.html
fetched_at: 2026-07-27T16:45:09+00:00
---
# arista.eos.eos_hostname module – Manages hostname resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_hostname`.

New in arista.eos 4.1.0

- [Synopsis](eos_hostname_module.md#synopsis)
- [Parameters](eos_hostname_module.md#parameters)
- [Notes](eos_hostname_module.md#notes)
- [Examples](eos_hostname_module.md#examples)
- [Return Values](eos_hostname_module.md#return-values)

## [Synopsis](eos_hostname_module.md#id1)

- This module configures and manages the attribute of hostname on Arista EOS platforms.

## [Parameters](eos_hostname_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of hostname options |
| **hostname**  string | The system’s hostname |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section hostname**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The states *merged*, *replaced* and *overridden* have identical behaviour for this module.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | section ^hostname* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_hostname_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.60M
> - This module works with connection `network_cli`. See the [EOS Platform Options](eos_platform_options.md).

## [Examples](eos_hostname_module.md#id4)

```yaml+jinja
# Using state: merged
# Before state:
# -------------
# test#show running-config | section ^hostname
# hostname eos
# Merged play:
# ------------
- name: Apply the provided configuration
  arista.eos.eos_hostname:
    config:
      hostname: eos
    state: merged
# Commands Fired:
# ---------------
# "commands": [
#         "hostname eos",
# ],
# After state:
# ------------
# test#show running-config | section ^hostname
# hostname eos

# Using state: deleted
# Before state:
# -------------
# test#show running-config | section ^hostname
# hostname eosTest
# Deleted play:
# -------------
- name: Remove all existing configuration
  arista.eos.eos_hostname:
    state: deleted
# Commands Fired:
# ---------------
# "commands": [
#     "no hostname eosTest",
# ],
# After state:
# ------------
# test#show running-config | section ^hostname
# hostname eos

# Using state: overridden
# Before state:
# -------------
# test#show running-config | section ^hostname
# hostname eos
# Overridden play:
# ----------------
- name: Override commands with provided configuration
  arista.eos.eos_hostname:
    config:
      hostname: eosTest
    state: overridden
# Commands Fired:
# ---------------
# "commands": [
#       "hostname eosTest",
#     ],
# After state:
# ------------
# test#show running-config | section ^hostname
# hostname eosTest

# Using state: replaced
# Before state:
# -------------
# test#show running-config | section ^hostname
# hostname eosTest
# Replaced play:
# --------------
- name: Replace commands with provided configuration
  arista.eos.eos_hostname:
    config:
      hostname: eosTest
    state: replaced
# Commands Fired:
# ---------------
# "commands": [],
# After state:
# ------------
# test#show running-config | section ^hostname
# hostname eosTest

# Using state: gathered
# Before state:
# -------------
#test#show running-config | section ^hostname
# hostname eosTest
# Gathered play:
# --------------
- name: Gather listed hostname config
  arista.eos.eos_hostname:
    state: gathered
# Module Execution Result:
# ------------------------
#   "gathered": {
#      "hostname": "eosTest"
#     },

# Using state: rendered
# Rendered play:
# --------------
- name: Render the commands for provided configuration
  arista.eos.eos_hostname:
    config:
      hostname: eosTest
    state: rendered
# Module Execution Result:
# ------------------------
# "rendered": [
#     "hostname eosTest",
# ]

# Using state: parsed
# File: parsed.cfg
# ----------------
# hostname eosTest
# Parsed play:
# ------------
- name: Parse the provided configuration with the existing running configuration
  arista.eos.eos_hostname:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed
# Module Execution Result:
# ------------------------
#  "parsed": {
#     "hostname": "eosTest"
# }
```

## [Return Values](eos_hostname_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  Returned: when changed  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `["hostname eost_test"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  Returned: when *state* is `gathered`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  Returned: when *state* is `parsed`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  Returned: when *state* is `rendered`  Sample: `["hostname eost_test"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
