---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_lag_interfaces module – Link Aggregation Juniper JUNOS resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_lag_interfaces_module.html
fetched_at: 2026-07-28T02:39:40+00:00
---
# junipernetworks.junos.junos_lag_interfaces module – Link Aggregation Juniper JUNOS resource module

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
> see [Requirements](junos_lag_interfaces_module.md#ansible-collections-junipernetworks-junos-junos-lag-interfaces-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_lag_interfaces`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_lag_interfaces_module.md#synopsis)
- [Requirements](junos_lag_interfaces_module.md#requirements)
- [Parameters](junos_lag_interfaces_module.md#parameters)
- [Notes](junos_lag_interfaces_module.md#notes)
- [Examples](junos_lag_interfaces_module.md#examples)
- [Return Values](junos_lag_interfaces_module.md#return-values)

## [Synopsis](junos_lag_interfaces_module.md#id1)

- This module manages properties of Link Aggregation Group on Juniper JUNOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: lag_interfaces

## [Requirements](junos_lag_interfaces_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)

## [Parameters](junos_lag_interfaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of link aggregation group configurations. |
| **link_protection**  boolean | This boolean option indicates if link protection should be enabled for the LAG interface. If value is `True` link protection is enabled on LAG and if value is `False` link protection is disabled.  **Choices:**   - `false` - `true` |
| **members**  list / elements=dictionary | List of member interfaces of the link aggregation group. The value can be single interface or list of interfaces. |
| **link_type**  string | The value of this options configures the member link as either `primary` or `backup`. Value `primary` configures primary interface for link-protection mode and `backup` configures backup interface for link-protection mode.  **Choices:**   - `"primary"` - `"backup"` |
| **member**  string | Name of the member interface. |
| **mode**  string | LAG mode. A value of `passive` will enable LACP in `passive` mode that is it will respond to LACP packets and `active` configures the link to initiate transmission of LACP packets.  **Choices:**   - `"active"` - `"passive"` |
| **name**  string / required | Name of the link aggregation group (LAG). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show interfaces**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state of the configuration after module completion  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](junos_lag_interfaces_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 18.4R1.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).

## [Examples](junos_lag_interfaces_module.md#id5)

```yaml+jinja
# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ae0 {
#     description "lag interface";
# }
# ae1 {
#     description "lag interface 1";
# }

- name: "Delete LAG attributes of given interfaces (Note: This won't delete the interface itself)"
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae0
      - name: ae1
    state: deleted

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }

# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }

- name: Merge provided configuration with device configuration
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae0
        members:
          - member: ge-0/0/1
            link_type: primary
          - member: ge-0/0/2
            link_type: backup
    state: merged

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad {
#            ae0;
#            primary;
#        }
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad {
#            ae0;
#            backup;
#        }
#    }
# }

# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ae0 {
#     description "lag interface";
# }
# ae3 {
#     description "lag interface 3";
# }

- name: Overrides all device LAG configuration with provided configuration
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae0
        members:
          - member: ge-0/0/2
      - name: ae1
        members:
          - member: ge-0/0/1
        mode: passive
    state: overridden

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae1;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ae0 {
#     description "lag interface";
# }
# ae1 {
#    aggregated-ether-options {
#        lacp {
#            active;
#        }
#    }
# }

# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }
# ge-0/0/3 {
#    description "Ansible configured interface 3";
# }

- name: Replace device LAG configuration with provided configuration
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae0
        members:
          - member: ge-0/0/1
        mode: active
    state: replaced

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }
# ae0 {
#    aggregated-ether-options {
#        lacp {
#            active;
#        }
#    }
# }
# ge-0/0/3 {
#    description "Ansible configured interface 3";
# }
# Using gathered
# Before state:
# ------------
#
# ansible@cm123456tr21# show interfaces
# ge-0/0/1 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             ae2;
#             primary;
#         }
#     }
# }
# ge-0/0/4 {
#     ether-options {
#         802.3ad {
#             ae2;
#             backup;
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
# ae1 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         lacp {
#             active;
#         }
#     }
# }
# ae2 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         link-protection;
#         lacp {
#             passive;
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
- name: Gather junos lag interfaces as in given arguments
  junipernetworks.junos.junos_lag_interfaces:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "members": [
#                 {
#                     "member": "ge-0/0/1"
#                 },
#                 {
#                     "member": "ge-0/0/2"
#                 }
#             ],
#             "mode": "active",
#             "name": "ae1"
#         },
#         {
#             "link_protection": true,
#             "members": [
#                 {
#                     "link_type": "primary",
#                     "member": "ge-0/0/3"
#                 },
#                 {
#                     "link_type": "backup",
#                     "member": "ge-0/0/4"
#                 }
#             ],
#             "mode": "passive",
#             "name": "ae2"
#         }
#     ]
# After state:
# ------------
#
# ansible@cm123456tr21# show interfaces
# ge-0/0/1 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             ae2;
#             primary;
#         }
#     }
# }
# ge-0/0/4 {
#     ether-options {
#         802.3ad {
#             ae2;
#             backup;
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
# ae1 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         lacp {
#             active;
#         }
#     }
# }
# ae2 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         link-protection;
#         lacp {
#             passive;
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
# <interfaces>
#         <interface>
#             <name>ge-0/0/1</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae1</bundle>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-0/0/2</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae1</bundle>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-0/0/3</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae2</bundle>
#                     <primary/>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-0/0/4</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae2</bundle>
#                     <backup/>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-1/0/0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>192.168.100.1/24</name>
#                         </address>
#                         <address>
#                             <name>10.200.16.20/24</name>
#                         </address>
#                     </inet>
#                     <inet6>
#                     </inet6>
#                 </family>
#             </unit>
#         </interface>
#         <interface>
#             <name>ge-2/0/0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>192.168.100.2/24</name>
#                         </address>
#                         <address>
#                             <name>10.200.16.21/24</name>
#                         </address>
#                     </inet>
#                     <inet6>
#                     </inet6>
#                 </family>
#             </unit>
#         </interface>
#         <interface>
#             <name>ge-3/0/0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>192.168.100.3/24</name>
#                         </address>
#                         <address>
#                             <name>10.200.16.22/24</name>
#                         </address>
#                     </inet>
#                     <inet6>
#                     </inet6>
#                 </family>
#             </unit>
#         </interface>
#         <interface>
#             <name>ae1</name>
#             <description>Configured by Ansible</description>
#             <aggregated-ether-options>
#                 <lacp>
#                     <active/>
#                 </lacp>
#             </aggregated-ether-options>
#         </interface>
#         <interface>
#             <name>ae2</name>
#             <description>Configured by Ansible</description>
#             <aggregated-ether-options>
#                 <link-protection>
#                 </link-protection>
#                 <lacp>
#                     <passive/>
#                 </lacp>
#             </aggregated-ether-options>
#         </interface>
#         <interface>
#             <name>em1</name>
#             <description>TEST</description>
#         </interface>
#         <interface>
#             <name>fxp0</name>
#             <description>ANSIBLE</description>
#             <speed>1g</speed>
#             <link-mode>automatic</link-mode>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>10.8.38.38/24</name>
#                         </address>
#                     </inet>
#                 </family>
#             </unit>
#         </interface>
#     </interfaces>
#     </configuration>
# </rpc-reply>
# - name: Convert interfaces config to argspec without connecting to the appliance
#   junipernetworks.junos.junos_lag_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#         {
#             "members": [
#                 {
#                     "member": "ge-0/0/1"
#                 },
#                 {
#                     "member": "ge-0/0/2"
#                 }
#             ],
#             "mode": "active",
#             "name": "ae1"
#         },
#         {
#             "link_protection": true,
#             "members": [
#                 {
#                     "link_type": "primary",
#                     "member": "ge-0/0/3"
#                 },
#                 {
#                     "link_type": "backup",
#                     "member": "ge-0/0/4"
#                 }
#             ],
#             "mode": "passive",
#             "name": "ae2"
#         }
#     ]
# Using rendered
- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae1
        members:
          - member: ge-0/0/1
          - member: ge-0/0/2
        mode: active

      - name: ae2
        link_protection: true
        members:
          - member: ge-0/0/3
            link_type: primary
          - member: ge-0/0/4
            link_type: backup
        mode: passive
# Task Output (redacted)
# -----------------------
# "rendered": "<nc:interfaces
#     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:interface>
#         <nc:name>ae1</nc:name>
#         <nc:aggregated-ether-options>
#             <nc:lacp>
#                 <nc:active/>
#             </nc:lacp>
#         </nc:aggregated-ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/1</nc:name>
#         <nc:ether-options>
#             <nc:ieee-802.3ad>
#                 <nc:bundle>ae1</nc:bundle>
#             </nc:ieee-802.3ad>
#         </nc:ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/2</nc:name>
#         <nc:ether-options>
#             <nc:ieee-802.3ad>
#                 <nc:bundle>ae1</nc:bundle>
#             </nc:ieee-802.3ad>
#         </nc:ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ae2</nc:name>
#         <nc:aggregated-ether-options>
#             <nc:lacp>
#                 <nc:passive/>
#             </nc:lacp>
#             <nc:link-protection/>
#         </nc:aggregated-ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/3</nc:name>
#         <nc:ether-options>
#             <nc:ieee-802.3ad>
#                 <nc:bundle>ae2</nc:bundle>
#                 <nc:primary/>
#             </nc:ieee-802.3ad>
#         </nc:ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/4</nc:name>
#         <nc:ether-options>
#             <nc:ieee-802.3ad>
#                 <nc:bundle>ae2</nc:bundle>
#                 <nc:backup/>
#             </nc:ieee-802.3ad>
#         </nc:ether-options>
#     </nc:interface>
# </nc:interfaces>"
```

## [Return Values](junos_lag_interfaces_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **xml**  list / elements=string | The set of xml rpc payload pushed to the remote device.  **Returned:** always  **Sample:** `["<nc:interfaces xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:interface> <nc:name>ae1</nc:name> <nc:aggregated-ether-options> <nc:lacp> <nc:active/> </nc:lacp> </nc:aggregated-ether-options> </nc:interface> <nc:interface> <nc:name>ge-0/0/1</nc:name> <nc:ether-options> <nc:ieee-802.3ad> <nc:bundle>ae1</nc:bundle> </nc:ieee-802.3ad> </nc:ether-options> </nc:interface> <nc:interface> <nc:name>ge-0/0/2</nc:name> <nc:ether-options> <nc:ieee-802.3ad> <nc:bundle>ae1</nc:bundle> </nc:ieee-802.3ad> </nc:ether-options> </nc:interface> <nc:interface> <nc:name>ae2</nc:name> <nc:aggregated-ether-options> <nc:lacp> <nc:passive/> </nc:lacp> <nc:link-protection/> </nc:aggregated-ether-options> </nc:interface> <nc:interface> <nc:name>ge-0/0/3</nc:name> <nc:ether-options> <nc:ieee-802.3ad> <nc:bundle>ae2</nc:bundle> <nc:primary/> </nc:ieee-802.3ad> </nc:ether-options> </nc:interface> <nc:interface> <nc:name>ge-0/0/4</nc:name> <nc:ether-options> <nc:ieee-802.3ad> <nc:bundle>ae2</nc:bundle> <nc:backup/> </nc:ieee-802.3ad> </nc:ether-options> </nc:interface> </nc:interfaces>", "xml 2", "xml 3"]` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
