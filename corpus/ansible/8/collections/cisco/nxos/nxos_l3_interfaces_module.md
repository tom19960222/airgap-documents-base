---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_l3_interfaces module – L3 interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_l3_interfaces_module.html
fetched_at: 2026-07-28T01:38:48+00:00
---
# cisco.nxos.nxos_l3_interfaces module – L3 interfaces resource module

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_l3_interfaces`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_l3_interfaces_module.md#synopsis)
- [Parameters](nxos_l3_interfaces_module.md#parameters)
- [Notes](nxos_l3_interfaces_module.md#notes)
- [Examples](nxos_l3_interfaces_module.md#examples)
- [Return Values](nxos_l3_interfaces_module.md#return-values)

## [Synopsis](nxos_l3_interfaces_module.md#id1)

- This module manages Layer-3 interfaces attributes of NX-OS Interfaces.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: l3_interfaces

## [Parameters](nxos_l3_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer-3 interface options |
| **dot1q**  integer | Configures IEEE 802.1Q VLAN encapsulation on a subinterface. |
| **evpn_multisite_tracking**  string  *added in cisco.nxos 1.1.0* | VxLAN evpn multisite Interface tracking. Supported only on selected model.  **Choices:**   - `"fabric-tracking"` - `"dci-tracking"` |
| **ipv4**  list / elements=dictionary | IPv4 address and attributes of the L3 interface. |
| **address**  string | IPV4 address of the L3 interface. |
| **secondary**  boolean | A boolean attribute to manage addition of secondary IP address.  **Choices:**   - `false` - `true` |
| **tag**  integer | URIB route tag value for local/direct routes. |
| **ipv6**  list / elements=dictionary | IPv6 address and attributes of the L3 interface. |
| **address**  string | IPV6 address of the L3 interface. |
| **tag**  integer | URIB route tag value for local/direct routes. |
| **ipv6_redirects**  boolean | Enables/disables ipv6 redirects.  **Choices:**   - `false` - `true` |
| **name**  string / required | Full name of L3 interface, i.e. Ethernet1/1. |
| **redirects**  boolean | Enables/disables ipv4 redirects.  **Choices:**   - `false` - `true` |
| **unreachables**  boolean | Enables/disables ip redirects.  **Choices:**   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^interface’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  The state *overridden* would override the IP address configuration of all interfaces on the device with the provided configuration in the task. Use caution with this state as you may loose access to the device.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_l3_interfaces_module.md#id3)

> **Note:**
>
> - Tested against NXOS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS

## [Examples](nxos_l3_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# router# show running-config | section interface
# interface Ethernet1/6
#   description Configured by Ansible Network
#   no switchport
#   no shutdown
# interface Ethernet1/7
#   description Configured by Ansible
#   no switchport
#   no shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

- name: Merge provided configuration with device configuration.
  cisco.nxos.nxos_l3_interfaces:
    config:
    - name: Ethernet1/6
      ipv4:
      - address: 192.168.1.1/24
        tag: 5
      - address: 10.1.1.1/24
        secondary: true
        tag: 10
      ipv6:
      - address: fd5d:12c9:2201:2::1/64
        tag: 6
    - name: Ethernet1/7.42
      redirects: false
      unreachables: false
    state: merged

# Task Output
# -----------
#
# before:
# - name: Ethernet1/6
# - name: Ethernet1/7
# - ipv4:
#   - address: dhcp
#   name: mgmt0
# commands:
# - interface Ethernet1/6
# - ip address 192.168.1.1/24 tag 5
# - ip address 10.1.1.1/24 secondary tag 10
# - ipv6 address fd5d:12c9:2201:2::1/64 tag 6
# - interface Ethernet1/7
# - no ip redirects
# after:
# - ipv4:
#   - address: 192.168.1.1/24
#     tag: 5
#   - address: 10.1.1.1/24
#     secondary: true
#     tag: 10
#   ipv6:
#   - address: fd5d:12c9:2201:2::1/64
#     tag: 6
#   name: Ethernet1/6
#   redirects: false
# - name: Ethernet1/7
#   redirects: false
# - ipv4:
#   - address: dhcp
#   name: mgmt0

# After state:
# ------------
#
# router# show running-config | section interface
# interface Ethernet1/6
#   description Configured by Ansible Network
#   no switchport
#   no ip redirects
#   ip address 192.168.1.1/24 tag 5
#   ip address 10.1.1.1/24 secondary tag 10
#   ipv6 address fd5d:12c9:2201:2::1/64 tag 6
#   no shutdown
# interface Ethernet1/7
#   description Configured by Ansible
#   no switchport
#   no ip redirects
#   no shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

# Using replaced

# Before state:
# -------------
#
# router# show running-config | section interface
# interface Ethernet1/6
#   description Configured by Ansible Network
#   no switchport
#   no ip redirects
#   ip address 192.168.1.1/24 tag 5
#   ip address 10.1.1.1/24 secondary tag 10
#   ipv6 address fd5d:12c9:2201:2::1/64 tag 6
#   no shutdown
# interface Ethernet1/7
#   description Configured by Ansible
#   no switchport
#   no ip redirects
#   no shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

- name: Replace device configuration of specified L3 interfaces with provided configuration.
  cisco.nxos.nxos_l3_interfaces:
    config:
    - name: Ethernet1/6
      ipv4:
        - address: 192.168.22.3/24
    state: replaced

# Task Output
# -----------
#
# before:
# - ipv4:
#   - address: 192.168.1.1/24
#     tag: 5
#   - address: 10.1.1.1/24
#     secondary: true
#     tag: 10
#   ipv6:
#   - address: fd5d:12c9:2201:2::1/64
#     tag: 6
#   name: Ethernet1/6
#   redirects: false
# - name: Ethernet1/7
#   redirects: false
# - ipv4:
#   - address: dhcp
#   name: mgmt0
# commands:
# - interface Ethernet1/6
# - ip address 192.168.22.3/24
# - no ipv6 address fd5d:12c9:2201:2::1/64
# - ip redirects
# after:
# - ipv4:
#   - address: 192.168.22.3/24
#   - address: 10.1.1.1/24
#     secondary: true
#     tag: 10
#   name: Ethernet1/6
#   redirects: false
# - name: Ethernet1/7
#   redirects: false
# - ipv4:
#   - address: dhcp
#   name: mgmt0

# After state:
# ------------
#
# router# show running-config | section interface
# interface Ethernet1/6
#   description Configured by Ansible Network
#   no switchport
#   no ip redirects
#   ip address 192.168.22.3/24
#   ip address 10.1.1.1/24 secondary tag 10
#   no shutdown
# interface Ethernet1/7
#   description Configured by Ansible
#   no switchport
#   no ip redirects
#   no shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

# Using overridden

# Before state:
# -------------
#
# router# show running-config | section interface
# interface Ethernet1/6
#   description Configured by Ansible Network
#   no switchport
#   no ip redirects
#   ip address 192.168.1.1/24 tag 5
#   ip address 10.1.1.1/24 secondary tag 10
#   ipv6 address fd5d:12c9:2201:2::1/64 tag 6
#   no shutdown
# interface Ethernet1/7
#   description Configured by Ansible
#   no switchport
#   no ip redirects
#   no shutdown
# interface Ethernet1/7.42
#   no ip redirects
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

- name: Override device configuration with provided configuration.
  cisco.nxos.nxos_l3_interfaces:
    config:
    - ipv4:
      - address: dhcp
      name: mgmt0
    - name: Ethernet1/6
      ipv4:
      - address: 192.168.22.3/24
    state: overridden

# Task Output
# -----------
#
# before:
# - ipv4:
#   - address: 192.168.1.1/24
#     tag: 5
#   - address: 10.1.1.1/24
#     secondary: true
#     tag: 10
#   ipv6:
#   - address: fd5d:12c9:2201:2::1/64
#     tag: 6
#   name: Ethernet1/6
#   redirects: false
# - name: Ethernet1/7
#   redirects: false
# - name: Ethernet1/7.42
#   redirects: false
# - ipv4:
#   - address: dhcp
#   name: mgmt0
# commands:
# - interface Ethernet1/6
# - no ipv6 address fd5d:12c9:2201:2::1/64
# - no ip address 10.1.1.1/24 secondary
# - ip address 192.168.22.3/24
# - ip redirects
# - interface Ethernet1/7
# - ip redirects
# - interface Ethernet1/7.42
# - ip redirects
# after:
# - ipv4:
#   - address: 192.168.22.3/24
#   name: Ethernet1/6
# - name: Ethernet1/7
# - name: Ethernet1/7.42
# - ipv4:
#   - address: dhcp
#   name: mgmt0

# After state:
# ------------
#
# router# show running-config | section interface
# interface Ethernet1/6
#   description Configured by Ansible Network
#   no switchport
#   ip address 192.168.22.3/24
#   no shutdown
# interface Ethernet1/7
#   description Configured by Ansible
#   no switchport
#   no shutdown
# interface Ethernet1/7.42
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

# Using deleted

# Before state:
# -------------
#
# router# show running-config | section interface
# interface Ethernet1/6
#   description Configured by Ansible Network
#   no switchport
#   ip address 192.168.22.3/24
#   no shutdown
# interface Ethernet1/7
#   description Configured by Ansible
#   no switchport
#   no shutdown
# interface Ethernet1/7.42
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

- name: Delete L3 attributes of given interfaces (This won't delete the interface
    itself).
  cisco.nxos.nxos_l3_interfaces:
    config:
    - name: Ethernet1/6
    - name: Ethernet1/2
    state: deleted

# Task Output
# -----------
#
# before:
# - name: Ethernet1/2
# - ipv4:
#   - address: 192.168.22.3/24
#   name: Ethernet1/6
# - name: Ethernet1/7
# - name: Ethernet1/7.42
# - ipv4:
#   - address: dhcp
#   name: mgmt0
# commands:
# - interface Ethernet1/6
# - no ip address
# after:
# - name: Ethernet1/2
# - name: Ethernet1/7
# - name: Ethernet1/7.42
# - ipv4:
#   - address: dhcp
#   name: mgmt0

# After state:
# ------------
#
# router# show running-config | section interface
# interface Ethernet1/6
#   description Configured by Ansible Network
#   no switchport
#   no shutdown
# interface Ethernet1/7
#   description Configured by Ansible
#   no switchport
#   no shutdown
# interface Ethernet1/7.42
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_l3_interfaces:
    config:
    - name: Ethernet1/800
      ipv4:
      - address: 192.168.1.100/24
        tag: 5
      - address: 10.1.1.1/24
        secondary: true
        tag: 10
    - name: Ethernet1/800
      ipv6:
      - address: fd5d:12c9:2201:2::1/64
        tag: 6
    state: rendered

# Task Output
# -----------
#
# rendered:
#   - interface Ethernet1/800
#   - ip address 192.168.1.100/24 tag 5
#   - ip address 10.1.1.1/24 secondary tag 10
#   - interface Ethernet1/800
#   - ipv6 address fd5d:12c9:2201:2::1/64 tag 6

# Using parsed

# parsed.cfg
# ----------
#
# interface Ethernet1/800
#   ip address 192.168.1.100/24 tag 5
#   ip address 10.1.1.1/24 secondary tag 10
#   no ip redirects
# interface Ethernet1/801
#   ipv6 address fd5d:12c9:2201:2::1/64 tag 6
#   ip unreachables
# interface mgmt0
#   ip address dhcp
#   vrf member management

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_l3_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output
# -----------
#
# parsed:
#   - name: Ethernet1/800
#     ipv4:
#       - address: 192.168.1.100/24
#         tag: 5
#       - address: 10.1.1.1/24
#         secondary: True
#         tag: 10
#     redirects: False
#   - name: Ethernet1/801
#     ipv6:
#      - address: fd5d:12c9:2201:2::1/64
#        tag: 6
#     unreachables: True

# Using gathered

# Before state:
# -------------
#
# interface Ethernet1/1
#   ip address 192.0.2.100/24
# interface Ethernet1/2
#   no ip redirects
#   ip address 203.0.113.10/24
#   ip unreachables
#   ipv6 address 2001:db8::1/32

- name: Gather l3_interfaces facts from the device using nxos_l3_interfaces
  cisco.nxos.nxos_l3_interfaces:
    state: gathered

# Task output
# -----------
#
# gathered:
#   - name: Ethernet1/1
#     ipv4:
#       - address: 192.0.2.100/24
#   - name: Ethernet1/2
#     ipv4:
#       - address: 203.0.113.10/24
#     ipv6:
#       - address: 2001:db8::1/32
#     redirects: False
#     unreachables: True
```

## [Return Values](nxos_l3_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface Ethernet1/2", "ip address 192.168.0.1/2"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
