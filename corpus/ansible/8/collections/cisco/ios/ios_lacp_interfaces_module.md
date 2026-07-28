---
collection: ansible
version: "8"
title: "cisco.ios.ios_lacp_interfaces module – Resource module to configure LACP interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_lacp_interfaces_module.html
fetched_at: 2026-07-28T01:26:13+00:00
---
# cisco.ios.ios_lacp_interfaces module – Resource module to configure LACP interfaces.

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
> To use it in a playbook, specify: `cisco.ios.ios_lacp_interfaces`.

New in cisco.ios 1.0.0

- [Synopsis](ios_lacp_interfaces_module.md#synopsis)
- [Parameters](ios_lacp_interfaces_module.md#parameters)
- [Notes](ios_lacp_interfaces_module.md#notes)
- [Examples](ios_lacp_interfaces_module.md#examples)
- [Return Values](ios_lacp_interfaces_module.md#return-values)

## [Synopsis](ios_lacp_interfaces_module.md#id1)

- This module provides declarative management of LACP on Cisco IOS network devices lacp_interfaces.

Aliases: lacp_interfaces

## [Parameters](ios_lacp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of LACP lacp_interfaces option |
| **fast_switchover**  boolean | LACP fast switchover supported on this port channel.  **Choices:**   - `false` - `true` |
| **max_bundle**  integer | LACP maximum number of ports to bundle in this port channel.  Refer to vendor documentation for valid port values. |
| **name**  string / required | Name of the Interface for configuring LACP. |
| **port_priority**  integer | LACP priority on this interface.  Refer to vendor documentation for valid port values. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](ios_lacp_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_lacp_interfaces_module.md#id4)

```yaml+jinja
# Using merged
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
# interface GigabitEthernet0/2
#  shutdown
# interface GigabitEthernet0/3
#  shutdown

- name: Merge provided configuration with device configuration
  cisco.ios.ios_lacp_interfaces:
    config:
      - name: GigabitEthernet0/1
        port_priority: 10
      - name: GigabitEthernet0/2
        port_priority: 20
      - name: GigabitEthernet0/3
        port_priority: 30
      - name: Port-channel10
        fast_switchover: true
        max_bundle: 5
    state: merged

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
#  lacp max-bundle 5
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

# Using overridden
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

- name: Override device configuration of all lacp_interfaces with provided configuration
  cisco.ios.ios_lacp_interfaces:
    config:
      - name: GigabitEthernet0/1
        port_priority: 20
      - name: Port-channel10
        max_bundle: 2
    state: overridden

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp max-bundle 2
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/2
#  shutdown
# interface GigabitEthernet0/3
#  shutdown

# Using replaced
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp max-bundle 5
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

- name: Replaces device configuration of listed lacp_interfaces with provided configuration
  cisco.ios.ios_lacp_interfaces:
    config:
      - name: GigabitEthernet0/3
        port_priority: 40
      - name: Port-channel10
        fast_switchover: true
        max_bundle: 2
    state: replaced

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
#  lacp max-bundle 2
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 40

# Using Deleted
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  flowcontrol receive on
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

- name: "Delete LACP attributes of given interfaces (Note: This won't delete the interface itself)"
  cisco.ios.ios_lacp_interfaces:
    config:
      - name: GigabitEthernet0/1
    state: deleted

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
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

# Using Deleted without any config passed
# "(NOTE: This will delete all of configured LLDP module attributes)"
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
# interface Port-channel20
#  lacp max-bundle 2
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

- name: "Delete LACP attributes for all configured interfaces (Note: This won't delete the interface itself)"
  cisco.ios.ios_lacp_interfaces:
    state: deleted

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

# Using Gathered

# Before state:
# -------------
#
# vios#sh running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
#  lacp max-bundle 2
# interface Port-channel40
#  lacp max-bundle 5
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  lacp port-priority 30
# interface GigabitEthernet0/2
#  lacp port-priority 20

- name: Gather listed LACP interfaces with provided configurations
  cisco.ios.ios_lacp_interfaces:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "fast_switchover": true,
#             "max_bundle": 2,
#             "name": "Port-channel10"
#         },
#         {
#             "max_bundle": 5,
#             "name": "Port-channel40"
#         },
#         {
#             "name": "GigabitEthernet0/0"
#         },
#         {
#             "name": "GigabitEthernet0/1",
#             "port_priority": 30
#         },
#         {
#             "name": "GigabitEthernet0/2",
#             "port_priority": 20
#         }
#     ]

# After state:
# ------------
#
# vios#sh running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
#  lacp max-bundle 2
# interface Port-channel40
#  lacp max-bundle 5
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  lacp port-priority 30
# interface GigabitEthernet0/2
#  lacp port-priority 20

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_lacp_interfaces:
    config:
      - name: GigabitEthernet0/1
        port_priority: 10
      - name: GigabitEthernet0/2
        port_priority: 20
      - name: Port-channel10
        fast_switchover: true
        max_bundle: 2
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "interface GigabitEthernet0/1",
#         "lacp port-priority 10",
#         "interface GigabitEthernet0/2",
#         "lacp port-priority 20",
#         "interface Port-channel10",
#         "lacp max-bundle 2",
#         "lacp fast-switchover"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# interface GigabitEthernet0/1
# lacp port-priority 10
# interface GigabitEthernet0/2
# lacp port-priority 20
# interface Port-channel10
# lacp max-bundle 2 fast-switchover

- name: Parse the commands for provided configuration
  cisco.ios.ios_lacp_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "name": "GigabitEthernet0/1",
#             "port_priority": 10
#         },
#         {
#             "name": "GigabitEthernet0/2",
#             "port_priority": 20
#         },
#         {
#             "fast_switchover": true,
#             "max_bundle": 2,
#             "name": "Port-channel10"
#         }
#     ]
```

## [Return Values](ios_lacp_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface GigabitEthernet 0/1", "lacp port-priority 30"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
