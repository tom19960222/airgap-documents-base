---
collection: ansible
version: "8"
title: "cisco.ios.ios_l3_interfaces module – Resource module to configure L3 interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_l3_interfaces_module.html
fetched_at: 2026-07-28T01:26:11+00:00
---
# cisco.ios.ios_l3_interfaces module – Resource module to configure L3 interfaces.

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
> To use it in a playbook, specify: `cisco.ios.ios_l3_interfaces`.

New in cisco.ios 1.0.0

- [Synopsis](ios_l3_interfaces_module.md#synopsis)
- [Parameters](ios_l3_interfaces_module.md#parameters)
- [Notes](ios_l3_interfaces_module.md#notes)
- [Examples](ios_l3_interfaces_module.md#examples)
- [Return Values](ios_l3_interfaces_module.md#return-values)

## [Synopsis](ios_l3_interfaces_module.md#id2)

- This module provides declarative management of Layer-3 interface on Cisco IOS devices.

Aliases: l3_interfaces

## [Parameters](ios_l3_interfaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer-3 interface options |
| **ipv4**  list / elements=dictionary | IPv4 address to be set for the Layer-3 interface mentioned in *name* option. The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 192.168.0.1/24. |
| **address**  string | Configures the IPv4 address for Interface. |
| **dhcp**  dictionary | IP Address negotiated via DHCP. |
| **client_id**  string | Specify client-id to use. |
| **enable**  boolean | Enable dhcp.  **Choices:**   - `false` - `true` |
| **hostname**  string | Specify value for hostname option. |
| **dhcp_client**  string | Configures and specifies client-id to use over DHCP ip. Note, This option shall work only when dhcp is configured as IP.  GigabitEthernet interface number  This option is DEPRECATED and is replaced with dhcp which accepts dict as input this attribute will be removed after 2023-08-01. |
| **dhcp_hostname**  string | Configures and specifies value for hostname option over DHCP ip. Note, This option shall work only when dhcp is configured as IP.  This option is DEPRECATED and is replaced with dhcp which accepts dict as input this attribute will be removed after 2023-08-01. |
| **pool**  string | IP Address auto-configured from a local DHCP pool. |
| **secondary**  boolean | Configures the IP address as a secondary address.  **Choices:**   - `false` - `true` |
| **ipv6**  list / elements=dictionary | IPv6 address to be set for the Layer-3 interface mentioned in *name* option.  The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64 |
| **address**  string | Configures the IPv6 address for Interface. |
| **anycast**  boolean | Configure as an anycast  **Choices:**   - `false` - `true` |
| **autoconfig**  dictionary | Obtain address using auto-configuration. |
| **default**  boolean | Insert default route.  **Choices:**   - `false` - `true` |
| **enable**  boolean | enable auto-configuration.  **Choices:**   - `false` - `true` |
| **cga**  boolean | Use CGA interface identifier  **Choices:**   - `false` - `true` |
| **dhcp**  dictionary | Obtain a ipv6 address using DHCP. |
| **enable**  boolean | Enable dhcp.  **Choices:**   - `false` - `true` |
| **rapid_commit**  boolean | Enable Rapid-Commit.  **Choices:**   - `false` - `true` |
| **eui**  boolean | Use eui-64 interface identifier  **Choices:**   - `false` - `true` |
| **link_local**  boolean | Use link-local address  **Choices:**   - `false` - `true` |
| **segment_routing**  dictionary | Segment Routing submode |
| **default**  boolean | Set a command to its defaults.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable segmented routing.  **Choices:**   - `false` - `true` |
| **ipv6_sr**  boolean | Set ipv6_sr.  **Choices:**   - `false` - `true` |
| **name**  string / required | Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | section ^interface* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](ios_l3_interfaces_module.md#id4)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - Using deleted state without config will delete all l3 attributes from all the interfaces.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - The module examples uses callback plugin (stdout_callback = yaml) to generate task output in yaml format.

## [Examples](ios_l3_interfaces_module.md#id5)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# Router#show running-config | section ^interface
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

- name: Merge provided configuration with device configuration
  cisco.ios.ios_l3_interfaces:
    config:
      - name: GigabitEthernet0/1
        ipv4:
          - address: 192.168.0.1/24
            secondary: true
      - name: GigabitEthernet2
        ipv4:
          - address: 192.168.0.2/24
      - name: GigabitEthernet3
        ipv6:
          - address: fd5d:12c9:2201:1::1/64
      - name: GigabitEthernet3.100
        ipv4:
          - address: 192.168.0.3/24
    state: merged

# Task Output
# -----------
#
# before:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet2
# - name: GigabitEthernet3
# - name: GigabitEthernet4
# - name: Loopback999
# commands:
# - interface GigabitEthernet2
# - ip address 192.168.0.2 255.255.255.0
# - interface GigabitEthernet3
# - ipv6 address fd5d:12c9:2201:1::1/64
# - interface GigabitEthernet3.100
# - ip address 192.168.0.3 255.255.255.0
# after:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - ipv4:
#   - address: 192.168.0.2/24
#   name: GigabitEthernet2
# - ipv6:
#   - address: FD5D:12C9:2201:1::1/64
#   name: GigabitEthernet3
# - name: GigabitEthernet3.100
#   ipv4:
#   - address: 192.168.0.3/24
# - name: GigabitEthernet4
# - name: Loopback999

# After state:
# ------------
#
# Router#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address 192.168.0.2 255.255.255.0
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
#  ipv6 address FD5D:12C9:2201:1::1/64
# interface GigabitEthernet3.100
#  ip address 192.168.0.3 255.255.255.0
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

# Using replaced

# Before state:
# -------------
#
# Router#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address 192.168.0.2 255.255.255.0
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
#  ipv6 address FD5D:12C9:2201:1::1/64
# interface GigabitEthernet3.100
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

- name: Replaces device configuration of listed interfaces with provided configuration
  cisco.ios.ios_l3_interfaces:
    config:
      - name: GigabitEthernet2
        ipv4:
          - address: 192.168.2.0/24
      - name: GigabitEthernet3
        ipv4:
          - dhcp:
              client_id: GigabitEthernet2
              hostname: test.com
    state: replaced

# Task Output
# -----------
#
# before:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - ipv4:
#   - address: 192.168.0.2/24
#   name: GigabitEthernet2
# - ipv6:
#   - address: FD5D:12C9:2201:1::1/64
#   name: GigabitEthernet3
# - name: GigabitEthernet3.100
# - name: GigabitEthernet4
# - name: Loopback999
# commands:
# - interface GigabitEthernet2
# - ip address 192.168.0.3 255.255.255.0
# - no ip address 192.168.0.2 255.255.255.0
# - interface GigabitEthernet3
# - ip address dhcp client-id GigabitEthernet2 hostname test.com
# - no ipv6 address fd5d:12c9:2201:1::1/64
# after:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - ipv4:
#   - address: 192.168.0.3/24
#   name: GigabitEthernet2
# - ipv4:
#   - dhcp:
#       client_id: GigabitEthernet2
#       enable: true
#       hostname: test.com
#   name: GigabitEthernet3
# - name: GigabitEthernet3.100
# - name: GigabitEthernet4
# - name: Loopback999

# After state:
# ------------
#
# router-ios#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address 192.168.0.3 255.255.255.0
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  ip address dhcp client-id GigabitEthernet2 hostname test.com
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3.100
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

# Using overridden

# Before state:
# -------------
#
# router-ios#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address 192.168.0.3 255.255.255.0
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  ip address dhcp client-id GigabitEthernet2 hostname test.com
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3.100
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

- name: Override device configuration of all interfaces with provided configuration
  cisco.ios.ios_l3_interfaces:
    config:
      - ipv4:
          - dhcp:
              enable: true
        name: GigabitEthernet1
      - name: GigabitEthernet2
        ipv4:
          - address: 192.168.0.1/24
      - name: GigabitEthernet3
    state: overridden

# Task Output
# -----------
# before:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - ipv4:
#   - address: 192.168.0.3/24
#   name: GigabitEthernet2
# - ipv4:
#   - dhcp:
#       client_id: GigabitEthernet2
#       enable: true
#       hostname: test.com
#   name: GigabitEthernet3
# - name: GigabitEthernet3.100
# - name: GigabitEthernet4
# - name: Loopback999
# commands:
# - interface GigabitEthernet2
# - ip address 192.168.0.1 255.255.255.0
# - no ip address 192.168.0.3 255.255.255.0
# - interface GigabitEthernet3
# - no ip address dhcp client-id GigabitEthernet2 hostname test.com
# after:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - ipv4:
#   - address: 192.168.0.1/24
#   name: GigabitEthernet2
# - name: GigabitEthernet3
# - name: GigabitEthernet3.100
# - name: GigabitEthernet4
# - name: Loopback999

# After state:
# ------------
#
# router-ios#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address 192.168.0.1 255.255.255.0
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3.100
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

# Using deleted

# Before state:
# -------------
#
# router-ios#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address 192.168.0.1 255.255.255.0
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3.100
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

- name: "Delete attributes of given interfaces (NOTE: This won't delete the interfaces)"
  cisco.ios.ios_l3_interfaces:
    config:
      - name: GigabitEthernet2
      - name: GigabitEthernet3.100
    state: deleted

# Task Output
# -----------
#
# before:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - ipv4:
#   - address: 192.168.0.1/24
#   name: GigabitEthernet2
# - name: GigabitEthernet3
# - name: GigabitEthernet3.100
# - name: GigabitEthernet4
# - name: Loopback999
# commands:
# - interface GigabitEthernet2
# - no ip address 192.168.0.1 255.255.255.0
# after:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - name: GigabitEthernet2
# - name: GigabitEthernet3
# - name: GigabitEthernet3.100
# - name: GigabitEthernet4
# - name: Loopback999

# After state:
# -------------
#
# router-ios#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3.100
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

# Using deleted without config passed, only interface's configuration will be negated

# Before state:
# -------------

# router-ios#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address 192.168.0.2 255.255.255.0
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
#  ipv6 address FD5D:12C9:2201:1::1/64
# interface GigabitEthernet3.100
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

- name: "Delete L3 config of all interfaces"
  cisco.ios.ios_l3_interfaces:
    state: deleted

# Task Output
# -----------
#
# before:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - ipv4:
#   - address: 192.168.0.2/24
#   name: GigabitEthernet2
# - ipv6:
#   - address: FD5D:12C9:2201:1::1/64
#   name: GigabitEthernet3
# - name: GigabitEthernet3.100
# - name: GigabitEthernet4
# - name: Loopback999
# commands:
# - interface GigabitEthernet1
# - no ip address dhcp
# - interface GigabitEthernet2
# - no ip address 192.168.0.2 255.255.255.0
# - interface GigabitEthernet3
# - no ipv6 address fd5d:12c9:2201:1::1/64
# after:
# - name: GigabitEthernet1
# - name: GigabitEthernet2
# - name: GigabitEthernet3
# - name: GigabitEthernet3.100
# - name: GigabitEthernet4
# - name: Loopback999

# After state:
# -------------
#
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  negotiation auto
# interface GigabitEthernet2
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  no ip address
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3.100
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

# Using gathered

# Before state:
# -------------
#
# Router#show running-config | section ^interface
# interface Loopback999
#  no ip address
#  shutdown
# interface GigabitEthernet1
#  description Management interface do not change
#  ip address dhcp
#  negotiation auto
# interface GigabitEthernet2
#  ip address 192.168.0.3 255.255.255.0
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3
#  description Configured and Overridden by Ansible Network
#  ip address dhcp client-id GigabitEthernet2 hostname test.com
#  shutdown
#  speed 1000
#  no negotiation auto
# interface GigabitEthernet3.100
# interface GigabitEthernet4
#  no ip address
#  shutdown
#  negotiation auto

- name: Gather facts for l3 interfaces
  cisco.ios.ios_l3_interfaces:
    state: gathered

# Task Output
# -----------
#
# gathered:
# - ipv4:
#   - dhcp:
#       enable: true
#   name: GigabitEthernet1
# - ipv4:
#   - address: 192.168.0.3/24
#   name: GigabitEthernet2
# - ipv4:
#   - dhcp:
#       client_id: GigabitEthernet2
#       enable: true
#       hostname: test.com
#   name: GigabitEthernet3
# - name: GigabitEthernet3.100
# - name: GigabitEthernet4
# - name: Loopback999

# Using rendered

- name: Render the commands for provided configuration
  cisco.ios.ios_l3_interfaces:
    config:
      - name: GigabitEthernet1
        ipv4:
          - dhcp:
              client_id: GigabitEthernet0/0
              hostname: test.com
      - name: GigabitEthernet2
        ipv4:
          - address: 198.51.100.1/24
            secondary: true
          - address: 198.51.100.2/24
        ipv6:
          - address: 2001:db8:0:3::/64
    state: rendered

# Task Output
# -----------
#
# rendered:
# - interface GigabitEthernet1
# - ip address dhcp client-id GigabitEthernet0/0 hostname test.com
# - interface GigabitEthernet2
# - ip address 198.51.100.1 255.255.255.0 secondary
# - ip address 198.51.100.2 255.255.255.0
# - ipv6 address 2001:db8:0:3::/64

# Using parsed

# File: parsed.cfg
# ----------------
#
# interface GigabitEthernet0/1
#  ip address dhcp client-id GigabitEthernet 0/0 hostname test.com
# interface GigabitEthernet0/2
#  ip address 198.51.100.1 255.255.255.0
#  ip address 198.51.100.2 255.255.255.0 secondary
#  ipv6 address 2001:db8:0:3::/64

- name: Parse the provided configuration
  cisco.ios.ios_l3_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task Output
# -----------
#
# parsed:
# - ipv4:
#   - dhcp:
#       client_id: GigabitEthernet0/0
#       hostname: test.com
#   name: GigabitEthernet0/1
# - ipv4:
#   - address: 198.51.100.1/24
#     secondary: true
#   - address: 198.51.100.2/24
#   ipv6:
#   - address: 2001:db8:0:3::/64
#   name: GigabitEthernet0/2
```

## [Return Values](ios_l3_interfaces_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `["ip address 192.168.0.3 255.255.255.0", "ipv6 address dhcp rapid-commit", "ipv6 address fd5d:12c9:2201:1::1/64 anycast"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when state is *parsed*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when state is *rendered*  **Sample:** `["ipv6 address FD5D:12C9:2201:1::1/64", "ip address 192.168.0.3 255.255.255.0", "ip address autoconfig"]` |

### Authors

- Sagar Paul (@KB-perByte)
- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
