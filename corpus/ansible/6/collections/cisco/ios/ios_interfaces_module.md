---
collection: ansible
version: "6"
title: "cisco.ios.ios_interfaces module – Resource module to configure interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_interfaces_module.html
fetched_at: 2026-07-27T16:55:12+00:00
---
# cisco.ios.ios_interfaces module – Resource module to configure interfaces.

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
> To use it in a playbook, specify: `cisco.ios.ios_interfaces`.

New in cisco.ios 1.0.0

- [Synopsis](ios_interfaces_module.md#synopsis)
- [Parameters](ios_interfaces_module.md#parameters)
- [Notes](ios_interfaces_module.md#notes)
- [Examples](ios_interfaces_module.md#examples)
- [Return Values](ios_interfaces_module.md#return-values)

## [Synopsis](ios_interfaces_module.md#id1)

- This module manages the interface attributes of Cisco IOS network devices.

## [Parameters](ios_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of interface options |
| **description**  string | Interface description. |
| **duplex**  string | Interface link status. Applicable for Ethernet interfaces only, either in half duplex, full duplex or in automatic state which negotiates the duplex automatically.  Choices:   - `"full"` - `"half"` - `"auto"` |
| **enabled**  boolean | Administrative state of the interface.  Set the value to `true` to administratively enable the interface or `false` to disable it.  Choices:   - `false` - `true` ← (default) |
| **mtu**  integer | MTU for a specific interface. Applicable for Ethernet interfaces only.  Refer to vendor documentation for valid values. |
| **name**  string / required | Full name of interface, e.g. GigabitEthernet0/2, loopback999. |
| **speed**  string | Interface link speed. Applicable for Ethernet interfaces only. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  The state *purged* negates virtual/logical interfaces that are specified in task from running-config.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"purged"` - `"parsed"` |

## [Notes](ios_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.2 on VIRL
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description This is test
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  no ip address
#  duplex auto
#  speed auto

- name: Merge provided configuration with device configuration
  cisco.ios.ios_interfaces:
    config:
    - name: GigabitEthernet0/2
      description: Configured and Merged by Ansible Network
      enabled: true
    - name: GigabitEthernet0/3
      description: Configured and Merged by Ansible Network
      mtu: 2800
      enabled: false
      speed: 100
      duplex: full
    state: merged

# Commands Fired:
# ---------------

# "commands": [
#       "interface GigabitEthernet0/2",
#       "description Configured and Merged by Ansible Network",
#       "no shutdown",
#       "interface GigabitEthernet0/3",
#       "description Configured and Merged by Ansible Network",
#       "mtu 2800",
#       "duplex full",
#       "shutdown",
#     ],

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured and Merged by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured and Merged by Ansible Network
#  mtu 2800
#  no ip address
#  shutdown
#  duplex full
#  speed 100

# Using replaced

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  mtu 2000
#  no ip address
#  shutdown
#  duplex full
#  speed 100

- name: Replaces device configuration of listed interfaces with provided configuration
  cisco.ios.ios_interfaces:
    config:
    - name: GigabitEthernet0/3
      description: Configured and Replaced by Ansible Network
      enabled: false
      duplex: auto
      mtu: 2500
      speed: 1000
    state: replaced

# Commands Fired:
# ---------------

# "commands": [
#       "interface GigabitEthernet0/3",
#       "description Configured and Replaced by Ansible Network",
#       "mtu 2500",
#       "duplex auto",
#       "speed 1000",
#     ],

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured and Replaced by Ansible Network
#  mtu 2500
#  no ip address
#  shutdown
#  duplex auto
#  speed 1000

# Using overridden

# Before state:
# -------------
#
# vios#show running-config | section ^interface#
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description This is test
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured by Ansible
#  mtu 2800
#  no ip address
#  shutdown
#  duplex full
#  speed 100

- name: Override device configuration of all interfaces with provided configuration
  cisco.ios.ios_interfaces:
    config:
    - name: GigabitEthernet0/2
      description: Configured and Overridden by Ansible Network
      speed: 1000
    - name: GigabitEthernet0/3
      description: Configured and Overridden by Ansible Network
      enabled: false
      duplex: full
      mtu: 2000
    state: overridden

# "commands": [
#       "interface GigabitEthernet0/1",
#       "no description description Configured by Ansible",
#       "no duplex auto",
#       "no speed auto",
#       "interface GigabitEthernet0/2",
#       "description Configured and Overridden by Ansible Network",
#       "interface GigabitEthernet0/3",
#       "description Configured and Overridden by Ansible Network",
#       "mtu 2000",
#     ],

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured and Overridden by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured and Overridden by Ansible Network
#  mtu 2000
#  no ip address
#  shutdown
#  duplex full
#  speed auto

# Using Deleted

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured by Ansible Network
#  mtu 2500
#  no ip address
#  shutdown
#  duplex full
#  speed 1000

- name: "Delete module attributes of given interfaces (Note: This won't delete the interface itself)"
  cisco.ios.ios_interfaces:
    config:
    - name: GigabitEthernet0/2
    state: deleted

# "commands": [
#       "interface GigabitEthernet0/2",
#       "no description description Configured by Ansible Network",
#       "no duplex auto",
#       "no speed 1000",
#     ],

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/3
#  description Configured by Ansible Network
#  mtu 2500
#  no ip address
#  shutdown
#  duplex full
#  speed 1000

# Using Purged

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Loopback888
# interface Port-channel10
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured by Ansible Network
#  mtu 2500
#  no ip address
#  shutdown
#  duplex full
#  speed 1000

- name: "Purge given interfaces (Note: This will delete the interface itself)"
  cisco.ios.ios_interfaces:
    config:
    - name: Loopback888
    - name: Port-channel10
    state: purged

# "commands": [
#       "no interface Loopback888",
#       "no interface Port-channel10",
#     ],

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured by Ansible Network
#  mtu 2500
#  no ip address
#  shutdown
#  duplex full
#  speed 1000

# Using Gathered

# Before state:
# -------------
#
# vios#sh running-config | section ^interface
# interface GigabitEthernet0/1
#  description this is interface1
#  mtu 65
#  duplex auto
#  speed 10
# interface GigabitEthernet0/2
#  description this is interface2
#  mtu 110
#  shutdown
#  duplex auto
#  speed 100

- name: Gather listed interfaces with provided configurations
  cisco.ios.ios_interfaces:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "description": "this is interface1",
#             "duplex": "auto",
#             "enabled": true,
#             "mtu": 65,
#             "name": "GigabitEthernet0/1",
#             "speed": "10"
#         },
#         {
#             "description": "this is interface2",
#             "duplex": "auto",
#             "enabled": false,
#             "mtu": 110,
#             "name": "GigabitEthernet0/2",
#             "speed": "100"
#         }
#     ]

# After state:
# ------------
#
# vios#sh running-config | section ^interface
# interface GigabitEthernet0/1
#  description this is interface1
#  mtu 65
#  duplex auto
#  speed 10
# interface GigabitEthernet0/2
#  description this is interface2
#  mtu 110
#  shutdown
#  duplex auto
#  speed 100

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_interfaces:
    config:
    - name: GigabitEthernet0/1
      description: Configured by Ansible-Network
      mtu: 110
      enabled: true
      duplex: half
    - name: GigabitEthernet0/2
      description: Configured by Ansible-Network
      mtu: 2800
      enabled: false
      speed: 100
      duplex: full
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "interface GigabitEthernet0/1",
#         "description Configured by Ansible-Network",
#         "mtu 110",
#         "duplex half",
#         "no shutdown",
#         "interface GigabitEthernet0/2",
#         "description Configured by Ansible-Network",
#         "mtu 2800",
#         "speed 100",
#         "duplex full",
#         "shutdown"
#         ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# interface GigabitEthernet0/1
# description interfaces 0/1
# mtu 110
# duplex half
# no shutdown
# interface GigabitEthernet0/2
# description interfaces 0/2
# mtu 2800
# speed 100
# duplex full
# shutdown

- name: Parse the commands for provided configuration
  cisco.ios.ios_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "description": "interfaces 0/1",
#             "duplex": "half",
#             "enabled": true,
#             "mtu": 110,
#             "name": "GigabitEthernet0/1"
#         },
#         {
#             "description": "interfaces 0/2",
#             "duplex": "full",
#             "enabled": true,
#             "mtu": 2800,
#             "name": "GigabitEthernet0/2",
#             "speed": "100"
#         }
#     ]
```

## [Return Values](ios_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  Returned: when changed  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `["interface GigabitEthernet2", "speed 1200", "mtu 1800"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  Returned: when *state* is `gathered`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  Returned: when *state* is `parsed`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  Returned: when *state* is `rendered`  Sample: `["interface GigabitEthernet1", "description Interface description", "shutdown"]` |

### Authors

- Sumit Jaiswal (@justjais)
- Sagar Paul (@KB-perByte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
