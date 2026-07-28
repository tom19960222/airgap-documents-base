---
collection: ansible
version: "6"
title: "arista.eos.eos_interfaces module – Interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_interfaces_module.html
fetched_at: 2026-07-27T16:42:55+00:00
---
# arista.eos.eos_interfaces module – Interfaces resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_interfaces`.

New in arista.eos 1.0.0

- [Synopsis](eos_interfaces_module.md#synopsis)
- [Parameters](eos_interfaces_module.md#parameters)
- [Notes](eos_interfaces_module.md#notes)
- [Examples](eos_interfaces_module.md#examples)
- [Return Values](eos_interfaces_module.md#return-values)

## [Synopsis](eos_interfaces_module.md#id1)

- This module manages the interface attributes of Arista EOS interfaces.

## [Parameters](eos_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | The provided configuration |
| **description**  string | Interface description |
| **duplex**  string | Interface link status. Applicable for Ethernet interfaces only.  Values other than `auto` must also set *speed*.  Ignored when *speed* is set above `1000`. |
| **enabled**  boolean | Administrative state of the interface.  Set the value to `true` to administratively enable the interface or `false` to disable it.  Choices:   - `false` - `true` ← (default) |
| **mode**  string | Manage Layer2 or Layer3 state of the interface. Applicable for Ethernet and port channel interfaces only.  Choices:   - `"layer2"` - `"layer3"` |
| **mtu**  integer | MTU for a specific interface. Must be an even number between 576 and 9216. Applicable for Ethernet interfaces only. |
| **name**  string / required | Full name of the interface, e.g. GigabitEthernet1. |
| **speed**  string | Interface link speed. Applicable for Ethernet interfaces only. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Notes](eos_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    description "Interface 1"
# !
# interface Ethernet2
# !
# interface Management1
#    description "Management interface"
#    ip address dhcp
# !

- name: Merge provided configuration with device configuration
  arista.eos.eos_interfaces:
    config:
    - name: Ethernet1
      enabled: true
      mode: layer3
    - name: Ethernet2
      description: Configured by Ansible
      enabled: false
    state: merged

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    description "Interface 1"
#    no switchport
# !
# interface Ethernet2
#    description "Configured by Ansible"
#    shutdown
# !
# interface Management1
#    description "Management interface"
#    ip address dhcp
# !

# Using replaced

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    description "Interface 1"
# !
# interface Ethernet2
# !
# interface Management1
#    description "Management interface"
#    ip address dhcp
# !

- name: Replaces device configuration of listed interfaces with provided configuration
  arista.eos.eos_interfaces:
    config:
    - name: Ethernet1
      enabled: true
    - name: Ethernet2
      description: Configured by Ansible
      enabled: false
    state: replaced

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description "Configured by Ansible"
#    shutdown
# !
# interface Management1
#    description "Management interface"
#    ip address dhcp
# !

# Using overridden

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    description "Interface 1"
# !
# interface Ethernet2
# !
# interface Management1
#    description "Management interface"
#    ip address dhcp
# !

- name: Overrides all device configuration with provided configuration
  arista.eos.eos_interfaces:
    config:
    - name: Ethernet1
      enabled: true
    - name: Ethernet2
      description: Configured by Ansible
      enabled: false
    state: overridden

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description "Configured by Ansible"
#    shutdown
# !
# interface Management1
#    ip address dhcp
# !

# Using deleted

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    description "Interface 1"
#    no switchport
# !
# interface Ethernet2
# !
# interface Management1
#    description "Management interface"
#    ip address dhcp
# !

- name: Delete or return interface parameters to default settings
  arista.eos.eos_interfaces:
    config:
    - name: Ethernet1
    state: deleted

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
# !
# interface Management1
#    description "Management interface"
#    ip address dhcp
# !

# Using rendered

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_interfaces:
    config:
    - name: Ethernet1
      enabled: true
      mode: layer3
    - name: Ethernet2
      description: Configured by Ansible
      enabled: false
    state: merged

# Output:
# ------------

# - "interface Ethernet1"
# - "description "Interface 1""
# - "no swithcport"
# - "interface Ethernet2"
# - "description "Configured by Ansible""
# - "shutdown"
# - "interface Management1"
# - "description "Management interface""
# - "ip address dhcp"

# Using parsed
# parsed.cfg

# interface Ethernet1
#    description "Interface 1"
# !
# interface Ethernet2
#    description "Configured by Ansible"
#    shutdown
# !

- name: Use parsed to convert native configs to structured data
  arista.eos.interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Output
# parsed:
#     - name: Ethernet1
#       enabled: True
#       mode: layer2
#     - name: Ethernet2
#       description: 'Configured by Ansible'
#       enabled: False
#       mode: layer2

# Using gathered:

# Existing config on the device
# -----------------------------
# interface Ethernet1
#    description "Interface 1"
# !
# interface Ethernet2
#    description "Configured by Ansible"
#    shutdown
# !

- name: Gather interfaces facts from the device
  arista.eos.interfaces:
    state: gathered

# output
# gathered:
#      - name: Ethernet1
#        enabled: True
#        mode: layer2
#      - name: Ethernet2
#        description: 'Configured by Ansible'
#        enabled: False
#        mode: layer2
```

## [Return Values](eos_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  Returned: when changed  Sample: `"The configuration returned will always be in the same format of the parameters above."` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format of the parameters above."` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface Ethernet2", "shutdown", "speed 10full"]` |

### Authors

- Nathaniel Case (@qalthos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
