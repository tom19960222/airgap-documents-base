---
collection: ansible
version: "8"
title: "cisco.ios.ios_lag_interfaces module – Resource module to configure LAG interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_lag_interfaces_module.html
fetched_at: 2026-07-28T01:26:13+00:00
---
# cisco.ios.ios_lag_interfaces module – Resource module to configure LAG interfaces.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_lag_interfaces`.

New in cisco.ios 1.0.0

- [Synopsis](ios_lag_interfaces_module.md#synopsis)
- [Parameters](ios_lag_interfaces_module.md#parameters)
- [Notes](ios_lag_interfaces_module.md#notes)
- [Examples](ios_lag_interfaces_module.md#examples)
- [Return Values](ios_lag_interfaces_module.md#return-values)

## [Synopsis](ios_lag_interfaces_module.md#id1)

- This module manages properties of Link Aggregation Group on Cisco IOS devices.

Aliases: lag_interfaces

## [Parameters](ios_lag_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of link aggregation group configurations. |
| **members**  list / elements=dictionary | Interface options for the link aggregation group. |
| **link**  integer | Assign a link identifier used for load-balancing.  Refer to vendor documentation for valid values.  NOTE, parameter only supported on Cisco IOS XE platform. |
| **member**  string | Interface member of the link aggregation group. |
| **mode**  string | Etherchannel Mode of the interface for link aggregation.  On mode has to be quoted as ‘on’ or else pyyaml will convert to True before it gets to Ansible.  **Choices:**   - `"auto"` - `"on"` - `"desirable"` - `"active"` - `"passive"` |
| **name**  string / required | ID of Ethernet Channel of interfaces.  Refer to vendor documentation for valid port values. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"parsed"` - `"gathered"` |

## [Notes](ios_lag_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_lag_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface GigabitEthernet0/1
#  shutdown
# interface GigabitEthernet0/2
#  shutdown
# interface GigabitEthernet0/3
#  shutdown
# interface GigabitEthernet0/4
#  shutdown

- name: Merge provided configuration with device configuration
  cisco.ios.ios_lag_interfaces:
    config:
      - name: Port-channel10
        members:
          - member: GigabitEthernet0/1
            mode: auto
          - member: GigabitEthernet0/2
            mode: auto
      - name: Port-channel20
        members:
          - member: GigabitEthernet0/3
            mode: on
      - name: Port-channel30
        members:
          - member: GigabitEthernet0/4
            mode: active
    state: merged

# Task Output:
# ---------------

# commands:
# - interface GigabitEthernet0/1
# - channel-group 10 mode auto
# - interface GigabitEthernet0/2
# - channel-group 10 mode auto
# - interface GigabitEthernet0/3
# - channel-group 20 mode on
# - interface GigabitEthernet0/4
# - channel-group 30 mode active

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/2
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/3
#  shutdown
#  channel-group 20 mode on
# interface GigabitEthernet0/4
#  shutdown
#  channel-group 30 mode active

# Using overridden
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/2
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/3
#  shutdown
#  channel-group 20 mode on
# interface GigabitEthernet0/4
#  shutdown
#  channel-group 30 mode active

- name: Override device configuration of all interfaces with provided configuration
  cisco.ios.ios_lag_interfaces:
    config:
      - name: Port-channel20
        members:
          - member: GigabitEthernet0/2
            mode: auto
          - member: GigabitEthernet0/3
            mode: auto
    state: overridden

# Task Output:
# ---------------

# commands:
# - interface GigabitEthernet0/1
# - no channel-group 10 mode auto
# - interface GigabitEthernet0/2
# - no channel-group 10 mode auto
# - interface GigabitEthernet0/4
# - no channel-group 30 mode active
# - interface GigabitEthernet0/2
# - channel-group 20 mode auto
# - interface GigabitEthernet0/3
# - channel-group 20 mode auto

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
# interface GigabitEthernet0/2
#  shutdown
#  channel-group 20 mode auto
# interface GigabitEthernet0/3
#  shutdown
#  channel-group 20 mode auto
# interface GigabitEthernet0/4
#  shutdown

# Using replaced
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/2
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/3
#  shutdown
#  channel-group 20 mode on
# interface GigabitEthernet0/4
#  shutdown
#  channel-group 30 mode active

- name: Replaces device configuration of listed interfaces with provided configuration
  cisco.ios.ios_lag_interfaces:
    config:
      - name: Port-channel30
        members:
          - member: GigabitEthernet0/3
            mode: auto
    state: replaced

# Task Output:
# ---------------

# commands:
# - interface GigabitEthernet0/3
# - channel-group 30 mode auto
# - interface GigabitEthernet0/4
# - no channel-group 30 mode active

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/2
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/3
#  shutdown
#  channel-group 30 mode auto
# interface GigabitEthernet0/4
#  shutdown

# Using Deleted
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/2
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/3
#  shutdown
#  channel-group 20 mode on
# interface GigabitEthernet0/4
#  shutdown
#  channel-group 30 mode active

- name: "Delete LAG attributes of given interfaces (Note: This won't delete the interface itself)"
  cisco.ios.ios_lag_interfaces:
    config:
      - name: Port-channel10
      - name: Port-channel20
    state: deleted

# Task Output:
# ---------------

# commands:
# - interface GigabitEthernet0/1
# - no channel-group 10 mode auto
# - interface GigabitEthernet0/2
# - no channel-group 10 mode auto
# - interface GigabitEthernet0/3
# - no channel-group 20 mode on

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
# interface GigabitEthernet0/2
#  shutdown
# interface GigabitEthernet0/3
#  shutdown
# interface GigabitEthernet0/4
#  shutdown
#  channel-group 30 mode active

# Using Deleted without any config passed
#"(NOTE: This will delete all of configured LLDP module attributes)"

#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/2
#  shutdown
#  channel-group 10 mode auto
# interface GigabitEthernet0/3
#  shutdown
#  channel-group 20 mode on
# interface GigabitEthernet0/4
#  shutdown
#  channel-group 30 mode active

- name: "Delete all configured LAG attributes for interfaces (Note: This won't delete the interface itself)"
  cisco.ios.ios_lag_interfaces:
    state: deleted

# Task Output:
# ---------------

# commands:
# - interface GigabitEthernet0/1
# - no channel-group 10 mode auto
# - interface GigabitEthernet0/2
# - no channel-group 10 mode auto
# - interface GigabitEthernet0/3
# - no channel-group 20 mode on
# - interface GigabitEthernet0/4
# - no channel-group 30 mode active

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
# interface GigabitEthernet0/2
#  shutdown
# interface GigabitEthernet0/3
#  shutdown
# interface GigabitEthernet0/4
#  shutdown

# Using Gathered

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#   shutdown
#   channel-group 10 mode auto
# interface GigabitEthernet0/2
#   shutdown
#   channel-group 10 mode auto
# interface GigabitEthernet0/3
#   shutdown
#   channel-group 20 mode on
# interface GigabitEthernet0/4
#   shutdown
#   channel-group 30 mode active

- name: Gather listed LAG interfaces with provided configurations
  cisco.ios.ios_lag_interfaces:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
# {
#     "members": [
#         {
#             "member": "GigabitEthernet0/1",
#             "mode": "auto"
#         },
#         {
#             "member": "GigabitEthernet0/2",
#             "mode": "auto"
#         }
#     ],
#     "name": "Port-channel10"
# },
# {
#     "members": [
#         {
#             "member": "GigabitEthernet0/3",
#             "mode": "on"
#         }
#     ],
#     "name": "Port-channel20"
# },
# {
#     "members": [
#         {
#             "member": "GigabitEthernet0/4",
#             "mode": "active"
#         }
#     ],
#     "name": "Port-channel30"
# }
# ]

# After state:
# ------------
#
# vios#sh running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#   shutdown
#   channel-group 10 mode auto
# interface GigabitEthernet0/2
#   shutdown
#   channel-group 10 mode auto
# interface GigabitEthernet0/3
#   shutdown
#   channel-group 20 mode on
# interface GigabitEthernet0/4
#   shutdown
#   channel-group 30 mode active

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_lag_interfaces:
    config:
      - name: Port-channel11
        members:
          - member: GigabitEthernet0/1
            mode: active
      - name: Port-channel22
        members:
          - member: GigabitEthernet0/2
            mode: passive
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "interface GigabitEthernet0/1",
#         "channel-group 11 mode active",
#         "interface GigabitEthernet0/2",
#         "channel-group 22 mode passive",
#     ]

# Using Parsed

#  File: parsed.cfg
# ----------------
#
# interface GigabitEthernet0/1
# channel-group 11 mode active
# interface GigabitEthernet0/2
# channel-group 22 mode passive

- name: Parse the commands for provided configuration
  cisco.ios.ios_lag_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#     {
#         "members": [
#             {
#                 "member": "GigabitEthernet0/1",
#                 "mode": "active"
#             }
#         ],
#         "name": "Port-channel11"
#     },
#     {
#         "members": [
#             {
#                 "member": "GigabitEthernet0/2",
#                 "mode": "passive"
#             }
#         ],
#         "name": "Port-channel22"
#     }
# ]
```

## [Return Values](ios_lag_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["interface GigabitEthernet0/1", "channel-group 10 mode auto", "channel-group 10 mode active link 20"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["interface GigabitEthernet0/2", "channel-group 20 mode auto", "channel-group 20 mode active link 60"]` |

### Authors

- Sagar Paul (@KB-perByte)
- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
