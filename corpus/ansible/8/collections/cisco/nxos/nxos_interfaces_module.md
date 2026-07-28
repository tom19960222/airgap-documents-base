---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_interfaces module – Interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_interfaces_module.html
fetched_at: 2026-07-28T01:38:46+00:00
---
# cisco.nxos.nxos_interfaces module – Interfaces resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_interfaces`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_interfaces_module.md#synopsis)
- [Parameters](nxos_interfaces_module.md#parameters)
- [Notes](nxos_interfaces_module.md#notes)
- [Examples](nxos_interfaces_module.md#examples)
- [Return Values](nxos_interfaces_module.md#return-values)

## [Synopsis](nxos_interfaces_module.md#id1)

- This module manages the interface attributes of NX-OS interfaces.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: interfaces

## [Parameters](nxos_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of interface options |
| **description**  string | Interface description. |
| **duplex**  string | Interface link status. Applicable for Ethernet interfaces only.  **Choices:**   - `"full"` - `"half"` - `"auto"` |
| **enabled**  boolean | Administrative state of the interface. Set the value to `true` to administratively enable the interface or `false` to disable it  **Choices:**   - `false` - `true` |
| **fabric_forwarding_anycast_gateway**  boolean | Associate SVI with anycast gateway under VLAN configuration mode. Applicable for SVI interfaces only.  **Choices:**   - `false` - `true` |
| **ip_forward**  boolean | Enable or disable IP forward feature on SVIs. Set the value to `true` to enable or `false` to disable.  **Choices:**   - `false` - `true` |
| **mode**  string | Manage Layer2 or Layer3 state of the interface. Applicable for Ethernet and port channel interfaces only.  **Choices:**   - `"layer2"` - `"layer3"` |
| **mtu**  string | MTU for a specific interface. Must be an even number between 576 and 9216. Applicable for Ethernet interfaces only. |
| **name**  string / required | Full name of interface, e.g. Ethernet1/1, port-channel10. |
| **speed**  string | Interface link speed. Applicable for Ethernet interfaces only. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ^interface**  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  The state *rendered* considers the system default mode for interfaces to be “Layer 3” and the system default state for interfaces to be shutdown.  The state *purged* negates virtual interfaces that are specified in task from running-config.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` - `"purged"` |

## [Notes](nxos_interfaces_module.md#id3)

> **Note:**
>
> - Tested against NXOS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS

## [Examples](nxos_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   description testing
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

- name: Merge provided configuration with device configuration
  cisco.nxos.nxos_interfaces:
    config:
    - name: Ethernet1/1
      description: Configured by Ansible
      enabled: true
    - name: Ethernet1/2
      description: Configured by Ansible Network
      enabled: false
    state: merged

# Task Output
# -----------
#
# before:
# - description: testing
#   name: Ethernet1/1
# - description: mgmt interface
#   name: mgmt0
# commands:
# - interface Ethernet1/1
# - description Configured by Ansible
# - interface Ethernet1/2
# - description Configured by Ansible Network
# - shutdown
# after:
# - description: Configured by Ansible
#   name: Ethernet1/1
# - description: Configured by Ansible Network
#   enabled: false
#   name: Ethernet1/2
# - description: mgmt interface
#   name: mgmt0

# After state:
# ------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   description Configured by Ansible
# interface Ethernet1/2
#   description Configured by Ansible Network
#   shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

# Using replaced

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   description Updated by Ansible
# interface Ethernet1/2
#   description Configured by Ansible Network
#   shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

- name: Replaces device configuration of listed interfaces with provided configuration
  cisco.nxos.nxos_interfaces:
    config:
    - name: Ethernet1/1
      description: Configured by Ansible
      enabled: true
      mtu: 9000
    - name: Ethernet1/2
      description: Configured by Ansible Network
      enabled: false
      mode: layer2
    state: replaced

# Task Output
# -----------
#
# before:
# - description: Updated by Ansible
#   name: Ethernet1/1
# - description: Configured by Ansible Network
#   enabled: false
#   name: Ethernet1/2
# - description: mgmt interface
#   name: mgmt0
# commands:
# - interface Ethernet1/1
# - mtu 1500
# - interface Ethernet1/2
# - description Updated by Ansible
# after:
# - description: Updated by Ansible
#   name: Ethernet1/1
# - description: Updated by Ansible
#   enabled: false
#   name: Ethernet1/2
# - description: mgmt interface
#   name: mgmt0

# After state:
# ------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   description Updated by Ansible
# interface Ethernet1/2
#   description Updated by Ansible
#   shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

# Using overridden

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   description Updated by Ansible
# interface Ethernet1/2
#   description Updated by Ansible
#   shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

- name: Override device configuration of all interfaces with provided configuration
  cisco.nxos.nxos_interfaces:
    config:
    - name: Ethernet1/1
      enabled: true
    - name: Ethernet1/2
      description: Configured by Ansible Network
      enabled: false
    - description: mgmt interface
      name: mgmt0
    state: overridden

# Task Output
# -----------
#
# before:
# - description: Updated by Ansible
#   name: Ethernet1/1
# - description: Updated by Ansible
#   enabled: false
#   name: Ethernet1/2
# - description: mgmt interface
#   name: mgmt0
# commands:
# - interface Ethernet1/1
# - no description
# - interface Ethernet1/2
# - description Configured by Ansible Network
# after:
# - name: Ethernet1/1
# - description: Configured by Ansible Network
#   enabled: false
#   name: Ethernet1/2
# - description: mgmt interface
#   name: mgmt0

# After state:
# ------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
# interface Ethernet1/2
#   description Configured by Ansible Network
#   shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

# Using deleted

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
# interface Ethernet1/2
#   description Configured by Ansible Network
#   shutdown
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

- name: Delete or return interface parameters to default settings
  cisco.nxos.nxos_interfaces:
    config:
    - name: Ethernet1/2
    state: deleted

# Task Output
# -----------
#
# before:
# - name: Ethernet1/1
# - description: Configured by Ansible Network
#   enabled: false
#   name: Ethernet1/2
# - description: mgmt interface
#   name: mgmt0
# commands:
# - interface Ethernet1/2
# - no description
# - no shutdown
# after:
# - name: Ethernet1/1
# - name: Ethernet1/2
# - description: mgmt interface
#   name: mgmt0

# After state:
# ------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
# interface Ethernet1/2
# interface mgmt0
#   description mgmt interface
#   ip address dhcp
#   vrf member management

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_interfaces:
    config:
    - name: Ethernet1/1
      description: outbound-intf
      mode: layer3
      speed: 100
    - name: Ethernet1/2
      mode: layer2
      enabled: true
      duplex: full
    state: rendered

# Task Output
# -----------
#
# rendered:
#   - "interface Ethernet1/1"
#   - "description outbound-intf"
#   - "speed 100"
#   - "interface Ethernet1/2"
#   - "switchport"
#   - "duplex full"
#   - "no shutdown"

# Using parsed

# parsed.cfg
# ------------
#
# interface Ethernet1/800
#   description test-1
#   speed 1000
#   shutdown
#   no switchport
#   duplex half
# interface Ethernet1/801
#   description test-2
#   switchport
#   no shutdown
#   mtu 1800

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output
# -----------
#
#  parsed:
#    - description: "test-1"
#      duplex: "half"
#      enabled: false
#      mode: "layer3"
#      name: "Ethernet1/800"
#      speed: "1000"
#    - description: "test-2"
#      enabled: true
#      mode: "layer2"
#      mtu: "1800"
#      name: "Ethernet1/801"

# Using gathered

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   description outbound-intf
#   switchport
#   no shutdown
# interface Ethernet1/2
#   description intf-l3
#   speed 1000
# interface Ethernet1/3
# interface Ethernet1/4
# interface Ethernet1/5

- name: Gather interfaces facts from the device using nxos_interfaces
  cisco.nxos.nxos_interfaces:
    state: gathered

# Task output
# -----------
#
# - name: Ethernet1/1
#   description: outbound-intf
#   mode: layer2
#   enabled: True
# - name: Ethernet1/2
#   description: intf-l3
#   speed: "1000"

# Using purged

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Vlan1
# interface Vlan42
#   mtu 1800
# interface port-channel10
# interface port-channel11
# interface Ethernet1/1
# interface Ethernet1/2
# interface Ethernet1/2.100
#   description sub-intf

- name: Purge virtual interfaces from running-config
  cisco.nxos.nxos_interfaces:
    config:
      - name: Vlan42
      - name: port-channel10
      - name: Ethernet1/2.100
    state: purged

# Task output
# ------------
#
# before:
#   - name: Vlan1
#   - mtu: '1800'
#     name: Vlan42
#   - name: port-channel10
#   - name: port-channel11
#   - name: Ethernet1/1
#   - name: Ethernet1/2
#   - description: sub-intf
#     name: Ethernet1/2.100
# commands:
#   - no interface port-channel10
#   - no interface Ethernet1/2.100
#   - no interface Vlan42
# after:
#   - name: Vlan1
#   - name: port-channel11
#   - name: Ethernet1/1
#   - name: Ethernet1/2

# After state:
# -------------
#
# switch# show running-config | section interface
# interface Vlan1
# interface port-channel11
# interface Ethernet1/1
# interface Ethernet1/2
```

## [Return Values](nxos_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface Ethernet1/1", "mtu 1800"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
