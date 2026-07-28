---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_l3_interfaces module – L3 interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_l3_interfaces_module.html
fetched_at: 2026-07-28T02:39:38+00:00
---
# junipernetworks.junos.junos_l3_interfaces module – L3 interfaces resource module

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_l3_interfaces_module.md#ansible-collections-junipernetworks-junos-junos-l3-interfaces-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_l3_interfaces`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_l3_interfaces_module.md#synopsis)
- [Requirements](junos_l3_interfaces_module.md#requirements)
- [Parameters](junos_l3_interfaces_module.md#parameters)
- [Notes](junos_l3_interfaces_module.md#notes)
- [Examples](junos_l3_interfaces_module.md#examples)
- [Return Values](junos_l3_interfaces_module.md#return-values)

## [Synopsis](junos_l3_interfaces_module.md#id1)

- This module provides declarative management of a Layer 3 interface on Juniper JUNOS devices

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: l3_interfaces

## [Requirements](junos_l3_interfaces_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)

## [Parameters](junos_l3_interfaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer 3 interface options |
| **ipv4**  list / elements=dictionary | IPv4 addresses to be set for the Layer 3 logical interface mentioned in *name* option. The address format is <ipv4 address>/<mask>. The mask is number in range 0-32 for example, 192.0.2.1/24, or `dhcp` to query DHCP for an IP address |
| **address**  string | IPv4 address to be set for the specific interface |
| **ipv6**  list / elements=dictionary | IPv6 addresses to be set for the Layer 3 logical interface mentioned in *name* option. The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 for example, 2001:db8:2201:1::1/64 or `auto-config` to use SLAAC |
| **address**  string | IPv6 address to be set for the specific interface |
| **name**  string / required | Full name of interface, e.g. ge-0/0/1 |
| **unit**  integer | Logical interface number. Value of `unit` should be of type integer  **Default:** `0` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show interfaces**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state of the configuration after module completion  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](junos_l3_interfaces_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - Tested against JunOS v18.4R1
> - This module works with connection `netconf`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html>
> - The module examples uses callback plugin (stdout_callback = yaml) to generate task output in yaml format.

## [Examples](junos_l3_interfaces_module.md#id5)

```yaml+jinja
# Using merged

# Before state
# ------------
#
# admin# show interfaces
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }

- name: Merge provided configuration with device configuration
  junipernetworks.junos.junos_l3_interfaces:
    config:
    - name: ge-0/0/1
      ipv4:
      - address: 192.168.1.10/24
      ipv6:
      - address: 8d8d:8d01::1/64
    - name: ge-0/0/2
      ipv4:
      - address: dhcp
    state: merged

# Task Output
# -----------
#
# before:
# - ipv4:
#   - address: dhcp
#   name: fxp0
#   unit: '0'
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:interface>
#       <nc:name>ge-0/0/1</nc:name>
#       <nc:unit>
#         <nc:name>0</nc:name>
#         <nc:family>
#           <nc:inet>
#             <nc:address>
#               <nc:name>192.168.1.10/24</nc:name>
#             </nc:address>
#           </nc:inet>
#         </nc:family>
#         <nc:family>
#           <nc:inet6>
#             <nc:address>
#               <nc:name>8d8d:8d01::1/64</nc:name>
#             </nc:address>
#           </nc:inet6>
#         </nc:family>
#       </nc:unit>
#     </nc:interface>
#     <nc:interface>
#       <nc:name>ge-0/0/2</nc:name>
#       <nc:unit>
#         <nc:name>0</nc:name>
#         <nc:family>
#           <nc:inet>
#             <nc:dhcp/>
#           </nc:inet>
#         </nc:family>
#       </nc:unit>
#     </nc:interface>
#   </nc:interfaces>
# after:
# - ipv4:
#   - address: 192.168.1.10/24
#   ipv6:
#   - address: 8d8d:8d01::1/64
#   name: ge-0/0/1
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: ge-0/0/2
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: fxp0
#   unit: '0'

# After state:
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#         family inet6 {
#             address 8d8d:8d01::1/64;
#         }
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }

# Using overridden

# Before state
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#         family inet6 {
#             address 8d8d:8d01::1/64;
#         }
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }

- name: Override provided configuration with device configuration
  junipernetworks.junos.junos_l3_interfaces:
    config:
    - name: ge-0/0/1
      ipv4:
      - address: 192.168.1.10/24
    - ipv4:
      - address: dhcp
      name: fxp0
      unit: '0'
    state: overridden

# Task Output
# -----------
#
# before:
# - ipv4:
#   - address: 192.168.1.10/24
#   ipv6:
#   - address: 8d8d:8d01::1/64
#   name: ge-0/0/1
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: ge-0/0/2
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: fxp0
#   unit: '0'
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:interface>
#     <nc:name>ge-0/0/1</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:inet>
#           <nc:address delete="delete"/>
#         </nc:inet>
#         <nc:inet6>
#           <nc:address delete="delete"/>
#         </nc:inet6>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>ge-0/0/2</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:inet>
#           <nc:dhcp delete="delete"/>
#         </nc:inet>
#         <nc:inet6>
#           <nc:address delete="delete"/>
#         </nc:inet6>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>fxp0</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:inet>
#           <nc:dhcp delete="delete"/>
#         </nc:inet>
#         <nc:inet6>
#           <nc:address delete="delete"/>
#         </nc:inet6>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>ge-0/0/1</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:inet>
#           <nc:address>
#             <nc:name>192.168.1.10/24</nc:name>
#           </nc:address>
#         </nc:inet>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>fxp0</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:inet>
#           <nc:dhcp/>
#         </nc:inet>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
# </nc:interfaces>
# after:
# - ipv4:
#   - address: 192.168.1.10/24
#   name: ge-0/0/1
#   unit: '0'
# - name: ge-0/0/2
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: fxp0
#   unit: '0'

# After state:
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

# Using replaced

# Before state
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

- name: Replace provided configuration with device configuration
  junipernetworks.junos.junos_l3_interfaces:
    config:
    - name: ge-0/0/1
      ipv4:
      - address: 192.168.1.10/24
      ipv6:
      - address: 8d8d:8d01::1/64
    - name: ge-0/0/2
      ipv4:
      - address: dhcp
    state: replaced

# Task Output
# -----------
#
# before:
# - ipv4:
#   - address: 192.168.1.10/24
#   name: ge-0/0/1
#   unit: '0'
# - name: ge-0/0/2
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: fxp0
#   unit: '0'
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:interface>
#     <nc:name>ge-0/0/1</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:inet>
#           <nc:address delete="delete"/>
#         </nc:inet>
#         <nc:inet6>
#           <nc:address delete="delete"/>
#         </nc:inet6>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>ge-0/0/2</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:inet/>
#         <nc:inet6>
#           <nc:address delete="delete"/>
#         </nc:inet6>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>ge-0/0/1</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:inet>
#           <nc:address>
#             <nc:name>192.168.1.10/24</nc:name>
#           </nc:address>
#         </nc:inet>
#       </nc:family>
#       <nc:family>
#         <nc:inet6>
#           <nc:address>
#             <nc:name>8d8d:8d01::1/64</nc:name>
#           </nc:address>
#         </nc:inet6>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>ge-0/0/2</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:inet>
#           <nc:dhcp/>
#         </nc:inet>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
# </nc:interfaces>
# after:
# - ipv4:
#   - address: 192.168.1.10/24
#   ipv6:
#   - address: 8d8d:8d01::1/64
#   name: ge-0/0/1
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: ge-0/0/2
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: fxp0
#   unit: '0'

# After state:
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#         family inet6 {
#             address 8d8d:8d01::1/64;
#         }
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

# Using deleted

# Before state:
# -------------
#
# admin# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#         family inet6 {
#             address 8d8d:8d01::1/64;
#         }
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

- name: Delete L3 logical interface
  junipernetworks.junos.junos_l3_interfaces:
    config:
    - name: ge-0/0/1
    - name: ge-0/0/2
    state: deleted

# Task Output
# -----------
#
# before:
# - ipv4:
#   - address: 192.168.1.10/24
#   ipv6:
#   - address: 8d8d:8d01::1/64
#   name: ge-0/0/1
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: ge-0/0/2
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: fxp0
#   unit: '0'
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:interface>
#       <nc:name>ge-0/0/1</nc:name>
#       <nc:unit>
#         <nc:name>0</nc:name>
#         <nc:family>
#           <nc:inet>
#             <nc:address delete="delete"/>
#           </nc:inet>
#           <nc:inet6>
#             <nc:address delete="delete"/>
#           </nc:inet6>
#         </nc:family>
#       </nc:unit>
#     </nc:interface>
#     <nc:interface>
#       <nc:name>ge-0/0/2</nc:name>
#       <nc:unit>
#         <nc:name>0</nc:name>
#         <nc:family>
#           <nc:inet>
#             <nc:dhcp delete="delete"/>
#           </nc:inet>
#           <nc:inet6>
#             <nc:address delete="delete"/>
#           </nc:inet6>
#         </nc:family>
#       </nc:unit>
#     </nc:interface>
#   </nc:interfaces>
# after:
# - name: ge-0/0/1
#   unit: '0'
# - name: ge-0/0/2
#   unit: '0'
# - ipv4:
#   - address: dhcp
#   name: fxp0
#   unit: '0'

# After state:
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

# Using gathered

# Before state:
# ------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     description "Configured by Ansible";
#     disable;
#     speed 100m;
#     mtu 1024;
#     hold-time up 2000 down 2200;
#     link-mode full-duplex;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#             vlan {
#                 members vlan100;
#             }
#         }
#     }
# }
# ge-0/0/2 {
#     description "Configured by Ansible";
#     native-vlan-id 400;
#     speed 10m;
#     mtu 2048;
#     hold-time up 3000 down 3200;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode trunk;
#             vlan {
#                 members [ vlan200 vlan300 ];
#             }
#         }
#     }
# }
# ge-1/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.1/24;
#             address 10.200.16.20/24;
#         }
#         family inet6;
#     }
# }
# ge-2/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.2/24;
#             address 10.200.16.21/24;
#         }
#         family inet6;
#     }
# }
# ge-3/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.3/24;
#             address 10.200.16.22/24;
#         }
#         family inet6;
#     }
# }
# em1 {
#     description TEST;
# }
# fxp0 {
#     description ANSIBLE;
#     speed 1g;
#     link-mode automatic;
#     unit 0 {
#         family inet {
#             address 10.8.38.38/24;
#         }
#     }
# }

- name: Gather layer3 interfaces facts
  junipernetworks.junos.junos_l3_interfaces:
    state: gathered

# Task Output
# -----------
#
# gathered:
# - ipv4:
#   - address: 192.168.100.1/24
#   - address: 10.200.16.20/24
#   name: ge-1/0/0
#   unit: '0'
# - ipv4:
#   - address: 192.168.100.2/24
#   - address: 10.200.16.21/24
#   name: ge-2/0/0
#   unit: '0'
# - ipv4:
#   - address: 192.168.100.3/24
#   - address: 10.200.16.22/24
#   name: ge-3/0/0
#   unit: '0'
# - ipv4:
#   - address: 10.8.38.38/24
#   name: fxp0
#   unit: '0'

# Using parsed

# parsed.cfg
# ------------
#
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <interfaces>
#             <interface>
#                 <name>ge-1/0/0</name>
#                 <unit>
#                     <name>0</name>
#                     <family>
#                         <inet>
#                             <address>
#                                 <name>192.168.100.1/24</name>
#                             </address>
#                             <address>
#                                 <name>10.200.16.20/24</name>
#                             </address>
#                         </inet>
#                         <inet6></inet6>
#                     </family>
#                 </unit>
#             </interface>
#             <interface>
#                 <name>ge-2/0/0</name>
#                 <unit>
#                     <name>0</name>
#                     <family>
#                         <inet>
#                             <address>
#                                 <name>192.168.100.2/24</name>
#                             </address>
#                             <address>
#                                 <name>10.200.16.21/24</name>
#                             </address>
#                         </inet>
#                         <inet6></inet6>
#                     </family>
#                 </unit>
#             </interface>
#         </interfaces>
#     </configuration>
# </rpc-reply>

# - name: Convert interfaces config to argspec without connecting to the appliance
#   junipernetworks.junos.junos_l3_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed

# Task Output
# -----------
#
# parsed:
# - ipv4:
#   - address: 192.168.100.1/24
#   - address: 10.200.16.20/24
#   name: ge-1/0/0
#   unit: '0'
# - ipv4:
#   - address: 192.168.100.2/24
#   - address: 10.200.16.21/24
#   name: ge-2/0/0
#   unit: '0'

# Using rendered

- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_l3_interfaces:
    config:
      - name: ge-1/0/0
        ipv4:
          - address: 192.168.100.1/24
          - address: 10.200.16.20/24
        unit: 0
      - name: ge-2/0/0
        ipv4:
          - address: 192.168.100.2/24
          - address: 10.200.16.21/24
        unit: 0
    state: rendered

# Task Output
# -----------
#
# "rendered": "<nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:interface>
#         <nc:name>ge-1/0/0</nc:name>
#         <nc:unit>
#             <nc:name>0</nc:name>
#             <nc:family>
#                 <nc:inet>
#                     <nc:address>
#                         <nc:name>192.168.100.1/24</nc:name>
#                     </nc:address>
#                     <nc:address>
#                         <nc:name>10.200.16.20/24</nc:name>
#                     </nc:address>
#                 </nc:inet>
#             </nc:family>
#         </nc:unit>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-2/0/0</nc:name>
#         <nc:unit>
#             <nc:name>0</nc:name>
#             <nc:family>
#                 <nc:inet>
#                     <nc:address>
#                         <nc:name>192.168.100.2/24</nc:name>
#                     </nc:address>
#                     <nc:address>
#                         <nc:name>10.200.16.21/24</nc:name>
#                     </nc:address>
#                 </nc:inet>
#             </nc:family>
#         </nc:unit>
#     </nc:interface>
# </nc:interfaces>"
```

## [Return Values](junos_l3_interfaces_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["<nc:interfaces xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:interface> <nc:name>ge-1/0/0</nc:name> <nc:unit> <nc:name>0</nc:name> <nc:family> <nc:inet> <nc:address> <nc:name>192.168.100.1/24</nc:name> </nc:address> <nc:address> <nc:name>10.200.16.20/24</nc:name> </nc:address> </nc:inet> </nc:family> </nc:unit> </nc:interfaces>", "xml 2", "xml 3"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">"]` |

### Authors

- Daniel Mellado (@dmellado)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
