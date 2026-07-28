---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_hostname module – Resource module to configure hostname."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_hostname_module.html
fetched_at: 2026-07-28T01:26:41+00:00
---
# cisco.iosxr.iosxr_hostname module – Resource module to configure hostname.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_hostname`.

New in cisco.iosxr 2.7.0

- [Synopsis](iosxr_hostname_module.md#synopsis)
- [Parameters](iosxr_hostname_module.md#parameters)
- [Notes](iosxr_hostname_module.md#notes)
- [Examples](iosxr_hostname_module.md#examples)
- [Return Values](iosxr_hostname_module.md#return-values)

## [Synopsis](iosxr_hostname_module.md#id1)

- This module configures and manages the attributes of hostname on Cisco IOSXR platforms.

Aliases: hostname

## [Parameters](iosxr_hostname_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Hostname configuration. |
| **hostname**  string | hostname of iosxr box. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOSXR device by executing the command **show running-config hostname**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The states *merged*, *replaced* and *overridden* have identical behaviour for this module.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config hostname* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](iosxr_hostname_module.md#id3)

> **Note:**
>
> - Tested against Cisco Iosxr 7.0.2
> - This module works with connection `network_cli`.

## [Examples](iosxr_hostname_module.md#id4)

```yaml+jinja
# Using state: merged
# Before state:
# -------------

#RP/0/RP0/CPU0:ios#show running-config hostname
#Thu Jan 20 19:48:56.011 UTC
#hostname ios

# Merged play:
# ------------

- name: Apply the provided configuration
  cisco.iosxr.iosxr_hostname:
    config:
      hostname: Router1
    state: merged

# Commands Fired:
# ---------------
# "commands": [
#         "hostname Router1",
# ],

# After state:
# ------------

# RP/0/0/CPU0:Router1#show running-config hostname
#Thu Jan 20 19:48:56.011 UTC
# hostname Router1

# Using state: deleted
# Before state:
# -------------

# RP/0/0/CPU0:Router1#show running-config hostname
#Thu Jan 20 19:48:56.011 UTC
# hostname Router1

# Deleted play:
# -------------

- name: Remove all existing configuration
  cisco.iosxr.iosxr_hostname:
    state: deleted

# Commands Fired:
# ---------------

# "commands": [
#     "no hostname Router1",
# ],

# After state:
# ------------
#RP/0/RP0/CPU0:ios#show running-config hostname
#Thu Jan 20 19:55:12.971 UTC
#hostname ios

# Using state: overridden
# Before state:
# -------------

# RP/0/0/CPU0:ios#show running-config hostname
# hostname ios

# Overridden play:
# ----------------

- name: Override commands with provided configuration
  cisco.iosxr.iosxr_hostname:
    config:
      hostname: RouterTest
    state: overridden

# Commands Fired:
# ---------------
# "commands": [
#       "hostname RouterTest",
#     ],

# After state:
# ------------

#RP/0/RP0/CPU0:RouterTest#show running-config hostname
#Thu Jan 20 19:48:56.011 UTC
#hostname RouterTest

# Using state: replaced
# Before state:
# -------------

#RP/0/RP0/CPU0:RouterTest#show running-config hostname
#Thu Jan 20 19:48:56.011 UTC
#hostname RouterTest

# Replaced play:
# --------------

- name: Replace commands with provided configuration
  cisco.iosxr.iosxr_hostname:
    config:
      hostname: RouterTest
    state: replaced

# Commands Fired:
# ---------------
# "commands": [],

# After state:
# ------------
# RP/0/0/CPU0:RouterTest#show running-config hostname
# hostname RouterTest

# Using state: gathered
# Before state:
# -------------

#RP/0/RP0/CPU0:RouterTest#show running-config hostname
#Thu Jan 20 19:48:56.011 UTC
#hostname RouterTest

# Gathered play:
# --------------

- name: Gather listed hostname config
  cisco.iosxr.iosxr_hostname:
    state: gathered

# Module Execution Result:
# ------------------------
#   "gathered": {
#      "hostname": "RouterTest"
#     },

# Using state: rendered
# Rendered play:
# --------------

- name: Render the commands for provided configuration
  cisco.iosxr.iosxr_hostname:
    config:
      hostname: RouterTest
    state: rendered

# Module Execution Result:
# ------------------------
# "rendered": [
#     "hostname RouterTest",
# ]

# Using state: parsed
# File: parsed.cfg
# ----------------

# hostname RouterTest
# Parsed play:
# ------------

- name: Parse the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_hostname:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#  "parsed": {
#     "hostname": "RouterTest"
# }
```

## [Return Values](iosxr_hostname_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["hostname Router1"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["hostname Router1"]` |

### Authors

- Ashwini Mhatre (@amhatre)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
