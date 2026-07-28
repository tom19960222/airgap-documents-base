---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_interfaces module – Junos Interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_interfaces_module.html
fetched_at: 2026-07-27T17:54:17+00:00
---
# junipernetworks.junos.junos_interfaces module – Junos Interfaces resource module

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_interfaces_module.md#ansible-collections-junipernetworks-junos-junos-interfaces-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_interfaces`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_interfaces_module.md#synopsis)
- [Requirements](junos_interfaces_module.md#requirements)
- [Parameters](junos_interfaces_module.md#parameters)
- [Notes](junos_interfaces_module.md#notes)
- [Examples](junos_interfaces_module.md#examples)
- [Return Values](junos_interfaces_module.md#return-values)

## [Synopsis](junos_interfaces_module.md#id1)

- This module manages the interfaces on Juniper Junos OS network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_interfaces_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)

## [Parameters](junos_interfaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | The provided configuration |
| **description**  string | Interface description. |
| **duplex**  string | Interface link status. Applicable for Ethernet interfaces only, either in half duplex, full duplex or in automatic state which negotiates the duplex automatically.  Choices:   - `"automatic"` - `"full-duplex"` - `"half-duplex"` |
| **enabled**  boolean | Administrative state of the interface.  Set the value to `true` to administratively enabled the interface or `false` to disable it.  Choices:   - `false` - `true` ← (default) |
| **hold_time**  dictionary | The hold time for given interface name. |
| **down**  integer | The link down hold time in milliseconds. |
| **up**  integer | The link up hold time in milliseconds. |
| **mtu**  integer | MTU for a specific interface.  Applicable for Ethernet interfaces only. |
| **name**  string / required | Full name of interface, e.g. ge-0/0/0. |
| **speed**  string | Interface link speed. Applicable for Ethernet interfaces only. |
| **units**  list / elements=dictionary | Specify Logical interfaces units. |
| **description**  string | Specify logical interface description. |
| **name**  integer | Specify interface unit number. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show interfaces**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](junos_interfaces_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 18.4R1.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).

## [Examples](junos_interfaces_module.md#id5)

```yaml+jinja
# Using deleted

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Configured by Ansible-1";
#    speed 1g;
#    mtu 1800
#    unit 0 {
#     description "This is logical intf unit0";
# }
# ge-0/0/2 {
#    description "Configured by Ansible-2";
#    ether-options {
#        auto-negotiation;
#    }
# }

- name: "Delete given options for the interface (Note: This won't delete the interface itself if any other values are configured for interface)"
  junipernetworks.junos.junos_interfaces:
    config:
    - name: ge-0/0/1
      description: Configured by Ansible-1
      speed: 1g
      mtu: 1800
    - name: ge-0/0/2
      description: Configured by Ansible -2
    state: deleted

# After state:
# ------------
# user@junos01# show interfaces
# ge-0/0/2 {
#    ether-options {
#        auto-negotiation;
#    }
# }

# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "test interface";
#    speed 1g;
# }
# fe-0/0/2 {
#     vlan-tagging;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }

- name: Merge provided configuration with device configuration (default operation
    is merge)
  junipernetworks.junos.junos_interfaces:
    config:
    - name: ge-0/0/1
      description: Configured by Ansible-1
      enabled: true
      units:
        - name: 0
          description: "This is logical intf unit0"
      mtu: 1800
    - name: ge-0/0/2
      description: Configured by Ansible-2
      enabled: false
    state: merged

# After state:
# ------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Configured by Ansible-1";
#    speed 1g;
#    mtu 1800
#    unit 0 {
#     description "This is logical intf unit0";
#   }
# }
# ge-0/0/2 {
#    disable;
#    description "Configured by Ansible-2";
# }

# Using overridden

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Configured by Ansible-1";
#    speed 1g;
#    mtu 1800
# }
# ge-0/0/2 {
#    disable;
#    description "Configured by Ansible-2";
#    ether-options {
#        auto-negotiation;
#    }
# }
# ge-0/0/11 {
#    description "Configured by Ansible-11";
# }

- name: Override device configuration of all interfaces with provided configuration
  junipernetworks.junos.junos_interfaces:
    config:
    - name: ge-0/0/2
      description: Configured by Ansible-2
      enabled: false
      mtu: 2800
    - name: ge-0/0/3
      description: Configured by Ansible-3
    state: overridden

# After state:
# ------------
# user@junos01# show interfaces
# ge-0/0/2 {
#    disable;
#    description "Configured by Ansible-2";
#    mtu 2800
# }
# ge-0/0/3 {
#    description "Configured by Ansible-3";
# }

# Using replaced

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Configured by Ansible-1";
#    speed 1g;
#    mtu 1800
# }
# ge-0/0/2 {
#    disable;
#    mtu 1800;
#    speed 1g;
#    description "Configured by Ansible-2";
#    ether-options {
#        auto-negotiation;
#    }
# }
# ge-0/0/11 {
#    description "Configured by Ansible-11";
# }

- name: Replaces device configuration of listed interfaces with provided configuration
  junipernetworks.junos.junos_interfaces:
    config:
    - name: ge-0/0/2
      description: Configured by Ansible-2
      enabled: false
      mtu: 2800
    - name: ge-0/0/3
      description: Configured by Ansible-3
    state: replaced

# After state:
# ------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Configured by Ansible-1";
#    speed 1g;
#    mtu 1800
# }
# ge-0/0/2 {
#    disable;
#    description "Configured by Ansible-2";
#    mtu 2800
# }
# ge-0/0/3 {
#    description "Configured by Ansible-3";
# }
# ge-0/0/11 {
#    description "Configured by Ansible-11";
# }
# Using gathered
# Before state:
# ------------
#
# vagrant@vsrx# show interfaces
# fe-0/0/2 {
#     description "This is interface DESCRIPTION";
#     vlan-tagging;
#     unit 10 {
#         description "UNIT 10 DESCRIPTION";
#         vlan-id 10;
#     }
#     unit 11 {
#         description "UNIT 11 DESCRIPTION";
#         vlan-id 11;
#     }
# }
# fxp0 {
#     description OUTER;
#     unit 0 {
#         description "Sample config";
#         family inet {
#             dhcp;
#         }
#     }
# }
#
- name: Gather junos interfaces as in given arguments
  junipernetworks.junos.junos_interfaces:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "description": "This is interface DESCRIPTION",
#             "enabled": true,
#             "name": "fe-0/0/2",
#             "units": [
#                 {
#                     "description": "UNIT 10 DESCRIPTION",
#                     "name": 10
#                 },
#                 {
#                     "description": "UNIT 11 DESCRIPTION",
#                     "name": 11
#                 }
#             ]
#         },
#         {
#             "description": "OUTER",
#             "enabled": true,
#             "name": "fxp0",
#             "units": [
#                 {
#                     "description": "Sample config",
#                     "name": 0
#                 }
#             ]
#         }
#     ]
# After state:
# ------------
#
# vagrant@vsrx# show interfaces
# fe-0/0/2 {
#     description "This is interface DESCRIPTION";
#     vlan-tagging;
#     unit 10 {
#         description "UNIT 10 DESCRIPTION";
#         vlan-id 10;
#     }
#     unit 11 {
#         description "UNIT 11 DESCRIPTION";
#         vlan-id 11;
#     }
# }
# fxp0 {
#     description OUTER;
#     unit 0 {
#         description "Sample config";
#         family inet {
#             dhcp;
#         }
#     }
# }
#
# Using parsed
# parsed.cfg
# ------------
#
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <interfaces>
#             <interface>
#                 <name>ge-0/0/1</name>
#                 <description>Configured by Ansible</description>
#                 <disable/>
#                 <speed>100m</speed>
#                 <mtu>1024</mtu>
#                 <hold-time>
#                     <up>2000</up>
#                     <down>2200</down>
#                 </hold-time>
#                 <link-mode>full-duplex</link-mode>
#                 <unit>
#                     <name>0</name>
#                     <family>
#                         <ethernet-switching>
#                             <interface-mode>access</interface-mode>
#                             <vlan>
#                                 <members>vlan100</members>
#                             </vlan>
#                         </ethernet-switching>
#                     </family>
#                 </unit>
#             </interface>
#         </interfaces>
#     </configuration>
# </rpc-reply>
# - name: Convert interfaces config to argspec without connecting to the appliance
#   junipernetworks.junos.junos_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#         {
#             "description": "Configured by Ansible",
#             "duplex": "full-duplex",
#             "enabled": false,
#             "hold_time": {
#                 "down": 2200,
#                 "up": 2000
#             },
#             "mtu": 1024,
#             "name": "ge-0/0/1",
#             "speed": "100m"
#         }
#     ]
#
# Using rendered
- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_interfaces:
    config:
    - name: ge-0/0/2
      description: Configured by Ansibull
      mtu: 2048
      speed: 20m
      hold_time:
        up: 3200
        down: 3200
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": <nc:interfaces
#     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:interface>
#         <nc:name>ge-0/0/2</nc:name>
#         <nc:description>Configured by Ansibull</nc:description>
#         <nc:speed>20m</nc:speed>
#         <nc:mtu>2048</nc:mtu>
#         <nc:hold-time>
#             <nc:up>3200</nc:up>
#             <nc:down>3200</nc:down>
#         </nc:hold-time>
#     </nc:interface>
# </nc:interfaces>"
```

## [Return Values](junos_interfaces_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **xml**  list / elements=string | The set of xml rpc payload pushed to the remote device.  Returned: always  Sample: `["<?xml version=\"1.0\" encoding=\"UTF-8\"?> <rpc-reply message-id=\"urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f\"> <configuration changed-seconds=\"1590139550\" changed-localtime=\"2020-05-22 09:25:50 UTC\"> <interfaces> <interface> <name>ge-0/0/1</name> <description>Configured by Ansible</description> <disable/> <speed>100m</speed> <mtu>1024</mtu> <hold-time> <up>2000</up> <down>2200</down> </hold-time> <link-mode>full-duplex</link-mode> <unit> <name>0</name> <family> <ethernet-switching> <interface-mode>access</interface-mode> <vlan> <members>vlan100</members> </vlan> </ethernet-switching> </family> </unit> </interface> </interfaces> </configuration> </rpc-reply>", "xml 2", "xml 3"]` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
