---
collection: ansible
version: "6"
title: "cisco.ios.ios_hostname module – Resource module to configure hostname."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_hostname_module.html
fetched_at: 2026-07-27T16:55:11+00:00
---
# cisco.ios.ios_hostname module – Resource module to configure hostname.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_hostname`.

New in cisco.ios 2.7.0

- [Synopsis](ios_hostname_module.md#synopsis)
- [Parameters](ios_hostname_module.md#parameters)
- [Notes](ios_hostname_module.md#notes)
- [Examples](ios_hostname_module.md#examples)
- [Return Values](ios_hostname_module.md#return-values)

## [Synopsis](ios_hostname_module.md#id1)

- This module provides declarative management of hostname on Cisco IOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_hostname_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of hostname options |
| **hostname**  string | set hostname for IOS |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^hostname**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The states *merged*, *replaced* and *overridden* have identical behaviour for this module.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | section ^hostname* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](ios_hostname_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.6.
> - This module works with connection `network_cli`.

## [Examples](ios_hostname_module.md#id4)

```yaml+jinja
# Using state: merged

# Before state:
# -------------

# router-ios#show running-config | section ^hostname
# hostname Router

# Merged play:
# ------------

- name: Apply the provided configuration
  cisco.ios.ios_hostname:
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

# router-ios#show running-config | section ^hostname
# hostname Router1

# Using state: deleted

# Before state:
# -------------

# router-ios#show running-config | section ^hostname
# hostname RouterTest

# Deleted play:
# -------------

- name: Remove all existing configuration
  cisco.ios.ios_hostname:
    state: deleted

# Commands Fired:
# ---------------

# "commands": [
#     "no hostname RouterTest",
# ],

# After state:
# ------------

# router-ios#show running-config | section ^hostname
# hostname Router

# Using state: overridden

# Before state:
# -------------

# router-ios#show running-config | section ^hostname
# hostname Router

# Overridden play:
# ----------------

- name: Override commands with provided configuration
  cisco.ios.ios_hostname:
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

# router-ios#show running-config | section ^hostname
# hostname RouterTest

# Using state: replaced

# Before state:
# -------------

# router-ios#show running-config | section ^hostname
# hostname RouterTest

# Replaced play:
# --------------

- name: Replace commands with provided configuration
  cisco.ios.ios_hostname:
    config:
      hostname: RouterTest
    state: replaced

# Commands Fired:
# ---------------

# "commands": [],

# After state:
# ------------

# router-ios#show running-config | section ^hostname
# hostname RouterTest

# Using state: gathered

# Before state:
# -------------

#router-ios#show running-config | section ^hostname
# hostname RouterTest

# Gathered play:
# --------------

- name: Gather listed hostname config
  cisco.ios.ios_hostname:
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
  cisco.ios.ios_hostname:
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
  cisco.ios.ios_hostname:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------

#  "parsed": {
#     "hostname": "RouterTest"
# }
```

## [Return Values](ios_hostname_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  Returned: when changed  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `["hostname Router1"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  Returned: when *state* is `gathered`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  Returned: when *state* is `parsed`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  Returned: when *state* is `rendered`  Sample: `["hostname Switch1"]` |

### Authors

- Sagar Paul (@KB-perByte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
