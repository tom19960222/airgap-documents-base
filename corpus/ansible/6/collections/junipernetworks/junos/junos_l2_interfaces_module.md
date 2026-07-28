---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_l2_interfaces module – L2 interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_l2_interfaces_module.html
fetched_at: 2026-07-27T17:54:18+00:00
---
# junipernetworks.junos.junos_l2_interfaces module – L2 interfaces resource module

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
> see [Requirements](junos_l2_interfaces_module.md#ansible-collections-junipernetworks-junos-junos-l2-interfaces-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_l2_interfaces`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_l2_interfaces_module.md#synopsis)
- [Requirements](junos_l2_interfaces_module.md#requirements)
- [Parameters](junos_l2_interfaces_module.md#parameters)
- [Notes](junos_l2_interfaces_module.md#notes)
- [Examples](junos_l2_interfaces_module.md#examples)
- [Return Values](junos_l2_interfaces_module.md#return-values)

## [Synopsis](junos_l2_interfaces_module.md#id1)

- This module provides declarative management of a Layer-2 interface on Juniper JUNOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_l2_interfaces_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)

## [Parameters](junos_l2_interfaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer-2 interface options |
| **access**  dictionary | Configure the interface as a Layer 2 access mode. |
| **vlan**  string | Configure the access VLAN ID. |
| **enhanced_layer**  boolean | True if your device has Enhanced Layer 2 Software (ELS). If the l2 configuration is under `interface-mode` the value is True else if the l2 configuration is under `port-mode` value is False  Choices:   - `false` - `true` |
| **name**  string / required | Full name of interface, e.g. ge-0/0/1. |
| **trunk**  dictionary | Configure the interface as a Layer 2 trunk mode. |
| **allowed_vlans**  list / elements=string | List of VLANs to be configured in trunk port. It’s used as the VLAN range to ADD or REMOVE from the trunk. |
| **native_vlan**  string | Native VLAN to be configured in trunk port. It is used as the trunk native VLAN ID. |
| **unit**  integer | Logical interface number. Value of `unit` should be of type integer. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show interfaces**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](junos_l2_interfaces_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 18.4R1.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).

## [Examples](junos_l2_interfaces_module.md#id5)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# ansible@junos01# show interfaces
# ge-0/0/1 {
#    description "L2 interface";
#    speed 1g;
#    unit 0 {
#        family ethernet-switching {
#            interface-mode access;
#            vlan {
#                members vlan30;
#            }
#        }
#    }
#}
#ge-0/0/2 {
#    description "non L2 interface";
#    unit 0 {
#        family inet {
#            address 192.168.56.14/24;
#        }
#    }

- name: "Delete L2 attributes of given interfaces (Note: This won't delete the
    interface itself)."
  junipernetworks.junos.junos_l2_interfaces:
    config:
    - name: ge-0/0/1
    - name: ge-0/0/2
    state: deleted

# After state:
# ------------
#
# ansible@junos01# show interfaces
# ge-0/0/1 {
#    description "L2 interface";
#    speed 1g;
# }
#ge-0/0/2 {
#    description "non L2 interface";
#    unit 0 {
#        family inet {
#            address 192.168.56.14/24;
#        }
#    }

# Using merged

# Before state:
# -------------
# ansible@junos01# show interfaces
# ge-0/0/3 {
#    description "test interface";
#    speed 1g;
#}
# ge-0/0/4 {
#    description interface-trunk;
#    native-vlan-id 100;
#    unit 0 {
#        family ethernet-switching {
#            interface-mode trunk;
#            vlan {
#                members [ vlan40 ];
#            }
#        }
#    }
# }

- name: Merge provided configuration with device configuration (default operation
    is merge)
  junipernetworks.junos.junos_l2_interfaces:
    config:
    - name: ge-0/0/3
      access:
        vlan: v101
    - name: ge-0/0/4
      trunk:
        allowed_vlans:
        - vlan30
        native_vlan: 50
    state: merged

# After state:
# ------------
# user@junos01# show interfaces
# ge-0/0/3 {
#    description "test interface";
#    speed 1g;
#    unit 0 {
#        family ethernet-switching {
#            interface-mode access;
#            vlan {
#                members v101;
#            }
#        }
#    }
# }
# ge-0/0/4 {
#    description interface-trunk;
#    native-vlan-id 50;
#    unit 0 {
#        family ethernet-switching {
#            interface-mode trunk;
#            vlan {
#                members [ vlan40 vlan30 ];
#            }
#        }
#    }
# }

# Using overridden

# Before state:
# -------------
# ansible@junos01# show interfaces
# ge-0/0/3 {
#    description "test interface";
#    speed 1g;
#}
# ge-0/0/4 {
#    description interface-trunk;
#    native-vlan-id 100;
#    unit 0 {
#        family ethernet-switching {
#            interface-mode trunk;
#            vlan {
#                members [ vlan40 ];
#            }
#        }
#    }
# }
# ge-0/0/5 {
#    description "Configured by Ansible-11";
#    unit 0 {
#        family ethernet-switching {
#            interface-mode access;
#            vlan {
#                members v101;
#            }
#        }
#    }
# }

- name: Override provided configuration with device configuration
  junipernetworks.junos.junos_l2_interfaces:
    config:
    - name: ge-0/0/3
      access:
        vlan: v101
    - name: ge-0/0/4
      trunk:
        allowed_vlans:
        - vlan30
        native_vlan: 50
    state: overridden

# After state:
# ------------
# user@junos01# show interfaces
# ge-0/0/3 {
#    unit 0 {
#        family ethernet-switching {
#            interface-mode access;
#            vlan {
#                members v101;
#            }
#        }
#    }
# }
# ge-0/0/4 {
#    description interface-trunk;
#    native-vlan-id 50;
#    unit 0 {
#        family ethernet-switching {
#            interface-mode trunk;
#            vlan {
#                members [ vlan30 ];
#            }
#        }
#    }
# }

# Using replaced

# Before state:
# -------------
# ansible@junos01# show interfaces
# ge-0/0/3 {
#    description "test interface";
#    speed 1g;
#}
# ge-0/0/4 {
#    description interface-trunk;
#    native-vlan-id 100;
#    unit 0 {
#        family ethernet-switching {
#            interface-mode trunk;
#            vlan {
#                members [ vlan40 ];
#            }
#        }
#    }
# }

- name: Replace provided configuration with device configuration
  junipernetworks.junos.junos_l2_interfaces:
    config:
    - name: ge-0/0/3
      access:
        vlan: v101
    - name: ge-0/0/4
      trunk:
        allowed_vlans:
        - vlan30
        native_vlan: 50
    state: replaced

# After state:
# ------------
# user@junos01# show interfaces
# ge-0/0/3 {
#    unit 0 {
#        family ethernet-switching {
#            interface-mode access;
#            vlan {
#                members v101;
#            }
#        }
#    }
# }
# ge-0/0/4 {
#    description interface-trunk;
#    native-vlan-id 50;
#    unit 0 {
#        family ethernet-switching {
#            interface-mode trunk;
#            vlan {
#                members [ vlan30 ];
#            }
#        }
#    }
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
- name: Gather junos layer 2 interfaces as in given arguments
  junipernetworks.junos.junos_l2_interfaces:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "access": {
#                 "vlan": "vlan100"
#             },
#             "enhanced_layer": true,
#             "name": "ge-0/0/1",
#             "unit": 0
#         },
#         {
#             "enhanced_layer": true,
#             "name": "ge-0/0/2",
#             "trunk": {
#                 "allowed_vlans": [
#                     "vlan200",
#                     "vlan300"
#                 ],
#                 "native_vlan": "400"
#             },
#             "unit": 0
#         }
#     ]
# After state:
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
#   junipernetworks.junos.junos_l2_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#         {
#             "access": {
#                 "vlan": "vlan100"
#             },
#             "enhanced_layer": true,
#             "name": "ge-0/0/1",
#             "unit": 0
#         },
#         {
#             "enhanced_layer": true,
#             "name": "ge-0/0/2",
#             "trunk": {
#                 "allowed_vlans": [
#                     "vlan200",
#                     "vlan300"
#                 ],
#                 "native_vlan": "400"
#             },
#             "unit": 0
#         }
#     ]
#
# Using rendered
- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_l2_interfaces:
    config:
      - name: ge-0/0/1
        access:
          vlan: vlan100
      - name: ge-0/0/2
        trunk:
          allowed_vlans:
            - vlan200
            - vlan300
          native_vlan: '400'
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": "<nc:interfaces
#     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:interface>
#         <nc:name>ge-0/0/1</nc:name>
#         <nc:unit>
#             <nc:name>0</nc:name>
#             <nc:family>
#                 <nc:ethernet-switching>
#                     <nc:interface-mode>access</nc:interface-mode>
#                     <nc:vlan>
#                         <nc:members>vlan100</nc:members>
#                     </nc:vlan>
#                 </nc:ethernet-switching>
#             </nc:family>
#         </nc:unit>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/2</nc:name>
#         <nc:unit>
#             <nc:name>0</nc:name>
#             <nc:family>
#                 <nc:ethernet-switching>
#                     <nc:interface-mode>trunk</nc:interface-mode>
#                     <nc:vlan>
#                         <nc:members>vlan200</nc:members>
#                         <nc:members>vlan300</nc:members>
#                     </nc:vlan>
#                 </nc:ethernet-switching>
#             </nc:family>
#         </nc:unit>
#         <nc:native-vlan-id>400</nc:native-vlan-id>
#     </nc:interface>
# </nc:interfaces>"
```

## [Return Values](junos_l2_interfaces_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["<nc:interfaces xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:interface> <nc:name>ge-0/0/1</nc:name> <nc:unit> <nc:name>0</nc:name> <nc:family> <nc:ethernet-switching> <nc:interface-mode>access</nc:interface-mode> <nc:vlan> <nc:members>vlan100</nc:members> </nc:vlan> </nc:ethernet-switching> </nc:family> </nc:unit> </nc:interface> <nc:interface> <nc:name>ge-0/0/2</nc:name> <nc:unit> <nc:name>0</nc:name> <nc:family> <nc:ethernet-switching> <nc:interface-mode>trunk</nc:interface-mode> <nc:vlan> <nc:members>vlan200</nc:members> <nc:members>vlan300</nc:members> </nc:vlan> </nc:ethernet-switching> </nc:family> </nc:unit> <nc:native-vlan-id>400</nc:native-vlan-id> </nc:interface> </nc:interfaces>", "xml 2", "xml 3"]` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
