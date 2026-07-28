---
collection: ansible
version: "6"
title: "cisco.ios.ios_lacp module – Resource module to configure LACP."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_lacp_module.html
fetched_at: 2026-07-27T16:55:16+00:00
---
# cisco.ios.ios_lacp module – Resource module to configure LACP.

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
> To use it in a playbook, specify: `cisco.ios.ios_lacp`.

New in cisco.ios 1.0.0

- [Synopsis](ios_lacp_module.md#synopsis)
- [Parameters](ios_lacp_module.md#parameters)
- [Notes](ios_lacp_module.md#notes)
- [Examples](ios_lacp_module.md#examples)
- [Return Values](ios_lacp_module.md#return-values)

## [Synopsis](ios_lacp_module.md#id1)

- This module provides declarative management of Global LACP on Cisco IOS network devices.

## [Parameters](ios_lacp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | The provided configurations. |
| **system**  dictionary | This option sets the default system parameters for LACP. |
| **priority**  integer / required | LACP priority for the system.  Refer to vendor documentation for valid values. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show lacp sys-id**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"rendered"` - `"parsed"` - `"gathered"` |

## [Notes](ios_lacp_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.2 on VIRL.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_lacp_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vios#show lacp sys-id
# 32768, 5e00.0000.8000

- name: Merge provided configuration with device configuration
  cisco.ios.ios_lacp:
    config:
      system:
        priority: 123
    state: merged

# After state:
# ------------
#
# vios#show lacp sys-id
# 123, 5e00.0000.8000

# Using replaced
#
# Before state:
# -------------
#
# vios#show lacp sys-id
# 500, 5e00.0000.8000

- name: Replaces Global LACP configuration
  cisco.ios.ios_lacp:
    config:
      system:
        priority: 123
    state: replaced

# After state:
# ------------
#
# vios#show lacp sys-id
# 123, 5e00.0000.8000

# Using Deleted
#
# Before state:
# -------------
#
# vios#show lacp sys-id
# 500, 5e00.0000.8000

- name: Delete Global LACP attribute
  cisco.ios.ios_lacp:
    state: deleted

# After state:
# -------------
#
# vios#show lacp sys-id
# 32768, 5e00.0000.8000

# Using Gathered

# Before state:
# -------------
#
# vios#show lacp sys-id
# 123, 5e00.0000.8000

- name: Gather listed LACP with provided configurations
  cisco.ios.ios_lacp:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": {
#         "system": {
#             "priority": 500
#         }
#     }

# After state:
# ------------
#
# vios#show lacp sys-id
# 123, 5e00.0000.8000

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_lacp:
    config:
      system:
        priority: 123
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "lacp system-priority 10"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# lacp system-priority 123

- name: Parse the commands for provided configuration
  cisco.ios.ios_lacp:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": {
#         "system": {
#             "priority": 123
#         }
#     }
```

## [Return Values](ios_lacp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["lacp system-priority 10"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
