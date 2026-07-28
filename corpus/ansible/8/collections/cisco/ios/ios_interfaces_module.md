---
collection: ansible
version: "8"
title: "cisco.ios.ios_interfaces module – Resource module to configure interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_interfaces_module.html
fetched_at: 2026-07-28T01:26:09+00:00
---
# cisco.ios.ios_interfaces module – Resource module to configure interfaces.

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
> To use it in a playbook, specify: `cisco.ios.ios_interfaces`.

New in cisco.ios 1.0.0

- [Synopsis](ios_interfaces_module.md#synopsis)
- [Parameters](ios_interfaces_module.md#parameters)
- [Notes](ios_interfaces_module.md#notes)
- [Examples](ios_interfaces_module.md#examples)
- [Return Values](ios_interfaces_module.md#return-values)

## [Synopsis](ios_interfaces_module.md#id1)

- This module manages the interface attributes of Cisco IOS network devices.

Aliases: interfaces

## [Parameters](ios_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of interface options |
| **description**  string | Interface description. |
| **duplex**  string | Interface link status. Applicable for Ethernet interfaces only, either in half duplex, full duplex or in automatic state which negotiates the duplex automatically.  **Choices:**   - `"full"` - `"half"` - `"auto"` |
| **enabled**  boolean | Administrative state of the interface.  Set the value to `true` to administratively enable the interface or `false` to disable it.  **Choices:**   - `false` - `true` ← (default) |
| **mode**  string | Manage Layer2 or Layer3 state of the interface.  For a Layer 2 appliance mode Layer2 adds switchport command ( default impacts idempotency).  For a Layer 2 appliance mode Layer3 adds no switchport command.  For a Layer 3 appliance mode Layer3/2 has no impact rather command fails on apply.  **Choices:**   - `"layer2"` - `"layer3"` |
| **mtu**  integer | MTU for a specific interface. Applicable for Ethernet interfaces only.  Refer to vendor documentation for valid values. |
| **name**  string / required | Full name of interface, e.g. GigabitEthernet0/2, loopback999. |
| **speed**  string | Interface link speed. Applicable for Ethernet interfaces only. |
| **template**  string | IOS template name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  The state *purged* negates virtual/logical interfaces that are specified in task from running-config.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"purged"` - `"parsed"` |

## [Notes](ios_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - The module examples uses callback plugin (stdout_callback = yaml) to generate task output in yaml format.

## [Examples](ios_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# Router#sh running-config | section interface
# interface Loopback888
#  no ip address
# interface Loopback999
#  no ip address
# interface GigabitEthernet1
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  description Configured and Merged by Ansible Network
#  ip address dhcp
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  no ip address
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

- name: Merge provided configuration with device configuration
  cisco.ios.ios_interfaces:
    config:
      - name: GigabitEthernet2
        description: Configured and Merged by Ansible Network
        enabled: true
      - name: GigabitEthernet3
        description: Configured and Merged by Ansible Network
        mtu: 3800
        enabled: false
        speed: 100
        duplex: full
    state: merged

# Task Output
# -----------
#
# before:
# - enabled: true
#   name: GigabitEthernet1
# - description: Configured and Merged by Ansible Network
#   enabled: true
#   name: GigabitEthernet2
#   speed: '1000'
# - description: Configured and Merged by Ansible Network
#   enabled: false
#   mtu: 3800
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: true
#   name: Loopback888
# - enabled: true
#   name: Loopback999
# commands:
# - interface GigabitEthernet3
# - description Configured and Merged by Ansible Network
# - speed 100
# - mtu 3800
# - duplex full
# - shutdown
# after:
# - enabled: true
#   name: GigabitEthernet1
# - description: Configured and Merged by Ansible Network
#   enabled: true
#   name: GigabitEthernet2
#   speed: '1000'
# - description: Configured and Merged by Ansible Network
#   enabled: true
#   mtu: 2800
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: true
#   name: Loopback888
# - enabled: true
#   name: Loopback999

# After state:
# ------------
#
# Router#show running-config | section ^interface
# interface Loopback888
#  no ip address
# interface Loopback999
#  no ip address
# interface GigabitEthernet1
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  description Configured and Merged by Ansible Network
#  ip address dhcp
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Merged by Ansible Network
#  mtu 3800
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

# Using merged - with mode attribute

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet1
#  description Configured by Ansible
# interface GigabitEthernet2
#  description This is test
# interface GigabitEthernet3
#  description This is test
#  no switchport

- name: Merge provided configuration with device configuration
  cisco.ios.ios_interfaces:
    config:
      - name: GigabitEthernet2
        description: Configured and Merged by Ansible Network
        enabled: true
        mode: layer2
      - name: GigabitEthernet3
        description: Configured and Merged by Ansible Network
        mode: layer3
    state: merged

# Task Output
# -----------
#
# before:
# - enabled: true
#   name: GigabitEthernet1
# - description: Configured and Merged by Ansible Network
#   name: GigabitEthernet2
# - description: Configured and Merged by Ansible Network
#   name: GigabitEthernet3
# commands:
# - interface GigabitEthernet2
# - description Configured and Merged by Ansible Network
# - switchport
# - interface GigabitEthernet3
# - description Configured and Merged by Ansible Network
# after:
# - enabled: true
#   name: GigabitEthernet1
# - description: Configured and Merged by Ansible Network
#   enabled: true
#   name: GigabitEthernet2
# - description: Configured and Merged by Ansible Network
#   name: GigabitEthernet3
#   mode: layer3

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet1
#  description Configured by Ansible
# interface GigabitEthernet2
#  description Configured and Merged by Ansible Network
# interface GigabitEthernet3
#  description Configured and Merged by Ansible Network
#  no switchport

# Using replaced

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Loopback888
#  no ip address
# interface Loopback999
#  no ip address
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address dhcp
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  no ip address
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto
# interface Vlan50
#  ip address dhcp hostname testHostname

- name: Replaces device configuration of listed interfaces with provided configuration
  cisco.ios.ios_interfaces:
    config:
      - name: GigabitEthernet3
        description: Configured and Replaced by Ansible Network
        enabled: false
        speed: 1000
    state: replaced

# Task Output
# -----------
#
# before:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - enabled: true
#   name: GigabitEthernet2
#   speed: '1000'
# - enabled: true
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: true
#   name: Loopback888
# - enabled: true
#   name: Loopback999
# - enabled: true
#   name: Vlan50
# commands:
# - interface GigabitEthernet3
# - description Configured and Replaced by Ansible Network
# - shutdown
# after:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - enabled: true
#   name: GigabitEthernet2
#   speed: '1000'
# - description: Configured and Replaced by Ansible Network
#   enabled: false
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: true
#   name: Loopback888
# - enabled: true
#   name: Loopback999
# - enabled: true
#   name: Vlan50

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface Loopback888
#  no ip address
# interface Loopback999
#  no ip address
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address dhcp
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Replaced by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto
# interface Vlan50
#  ip address dhcp hostname testHostname

# Using overridden

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Loopback888
#  no ip address
# interface Loopback999
#  no ip address
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address dhcp
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Replaced by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto
# interface Vlan50
#  ip address dhcp hostname testHostname

- name: Override device configuration of all interfaces with provided configuration
  cisco.ios.ios_interfaces:
    config:
      - description: Management interface do not change
        enabled: true
        name: GigabitEthernet1
      - name: GigabitEthernet2
        description: Configured and Overridden by Ansible Network
        speed: 10000
      - name: GigabitEthernet3
        description: Configured and Overridden by Ansible Network
        enabled: false
    state: overridden

# Task Output
# -----------
#
# before:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - enabled: true
#   name: GigabitEthernet2
#   speed: '1000'
# - description: Configured and Replaced by Ansible Network
#   enabled: false
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: true
#   name: Loopback888
# - enabled: true
#   name: Loopback999
# - enabled: true
#   name: Vlan50
# commands:
# - interface loopback888
# - shutdown
# - interface loopback999
# - shutdown
# - interface Vlan50
# - shutdown
# - interface GigabitEthernet2
# - description Configured and Overridden by Ansible Network
# - speed 10000
# - interface GigabitEthernet3
# - description Configured and Overridden by Ansible Network
# - no speed 1000
# after:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - description: Configured and Overridden by Ansible Network
#   enabled: true
#   name: GigabitEthernet2
#   speed: '10000'
# - description: Configured and Overridden by Ansible Network
#   enabled: false
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: false
#   name: Loopback888
# - enabled: false
#   name: Loopback999
# - enabled: false
#   name: Vlan50

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface Loopback888
#  no ip address
#  shutdown
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  description Configured and Overridden by Ansible Network
#  ip address dhcp
#  speed 10000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto
# interface Vlan50
#  ip address dhcp hostname testHostname
#  shutdown

# Using Deleted

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Loopback888
#  no ip address
#  shutdown
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  description Configured and Overridden by Ansible Network
#  ip address dhcp
#  speed 10000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto
# interface Vlan50
#  ip address dhcp hostname testHostname
#  shutdown

- name: "Delete interface attributes (Note: This won't delete the interface itself)"
  cisco.ios.ios_interfaces:
    config:
      - name: GigabitEthernet2
    state: deleted

# Task Output
# -----------
#
# before:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - description: Configured and Overridden by Ansible Network
#   enabled: true
#   name: GigabitEthernet2
#   speed: '10000'
# - description: Configured and Overridden by Ansible Network
#   enabled: false
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: false
#   name: Loopback888
# - enabled: false
#   name: Loopback999
# - enabled: false
#   name: Vlan50
# commands:
# - interface GigabitEthernet2
# - no description Configured and Overridden by Ansible Network
# - no speed 10000
# - shutdown
# after:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - enabled: false
#   name: GigabitEthernet2
#   speed: '1000'
# - description: Configured and Overridden by Ansible Network
#   enabled: false
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: false
#   name: Loopback888
# - enabled: false
#   name: Loopback999
# - enabled: false
#   name: Vlan50

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface Loopback888
#  no ip address
#  shutdown
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address dhcp
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto
# interface Vlan50
#  ip address dhcp hostname testHostname
#  shutdown

# Using Purged

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Loopback888
#  no ip address
#  shutdown
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address dhcp
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto
# interface Vlan50
#  ip address dhcp hostname testHostname
#  shutdown

- name: "Purge given interfaces (Note: This will delete the interface itself)"
  cisco.ios.ios_interfaces:
    config:
      - name: Loopback888
      - name: Vlan50
    state: purged

# Task Output
# -----------
#
# before:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - enabled: false
#   name: GigabitEthernet2
#   speed: '1000'
# - description: Configured and Overridden by Ansible Network
#   enabled: false
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: false
#   name: Loopback888
# - enabled: false
#   name: Loopback999
# - enabled: false
#   name: Vlan50
# commands:
# - no interface loopback888
# - no interface Vlan50
# after:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - enabled: false
#   name: GigabitEthernet2
#   speed: '1000'
# - description: Configured and Overridden by Ansible Network
#   enabled: false
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: false
#   name: Loopback999

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address dhcp
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

# Using gathered

# Before state:
# -------------
#
# vios#sh running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address dhcp
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

- name: Gather facts of interfaces
  cisco.ios.ios_interfaces:
    config:
    state: gathered

# Task Output
# -----------
#
# gathered:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - enabled: false
#   name: GigabitEthernet2
#   speed: '1000'
# - description: Configured and Overridden by Ansible Network
#   enabled: false
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: false
#   name: Loopback999

# Using rendered

- name: Render the commands for provided configuration
  cisco.ios.ios_interfaces:
    config:
      - name: GigabitEthernet1
        description: Configured by Ansible-Network
        mtu: 110
        enabled: true
        duplex: half
      - name: GigabitEthernet2
        description: Configured by Ansible-Network
        mtu: 2800
        enabled: false
        speed: 100
        duplex: full
    state: rendered

# Task Output
# -----------
#
# rendered:
# - interface GigabitEthernet1
# - description Configured by Ansible-Network
# - mtu 110
# - duplex half
# - no shutdown
# - interface GigabitEthernet2
# - description Configured by Ansible-Network
# - speed 100
# - mtu 2800
# - duplex full
# - shutdown

# Using parsed

# File: parsed.cfg
# ----------------
#
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address dhcp
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

- name: Parse the provided configuration
  cisco.ios.ios_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task Output
# -----------
#
# parsed:
# - description: Management interface do not change
#   enabled: true
#   name: GigabitEthernet1
# - enabled: false
#   name: GigabitEthernet2
#   speed: '1000'
# - description: Configured and Overridden by Ansible Network
#   enabled: false
#   name: GigabitEthernet3
#   speed: '1000'
# - enabled: false
#   name: GigabitEthernet4
# - enabled: false
#   name: Loopback999
```

## [Return Values](ios_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["interface GigabitEthernet2", "speed 1200", "mtu 1800"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["interface GigabitEthernet1", "description Interface description", "shutdown"]` |

### Authors

- Sumit Jaiswal (@justjais)
- Sagar Paul (@KB-perByte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
