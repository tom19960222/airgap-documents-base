---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_lag_interfaces module – LAG interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_lag_interfaces_module.html
fetched_at: 2026-07-28T00:23:21+00:00
---
# vyos.vyos.vyos_lag_interfaces module – LAG interfaces resource module

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/vyos/vyos) (version 3.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_lag_interfaces`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_lag_interfaces_module.md#synopsis)
- [Parameters](vyos_lag_interfaces_module.md#parameters)
- [Notes](vyos_lag_interfaces_module.md#notes)
- [Examples](vyos_lag_interfaces_module.md#examples)
- [Return Values](vyos_lag_interfaces_module.md#return-values)

## [Synopsis](vyos_lag_interfaces_module.md#id1)

- This module manages attributes of link aggregation groups on VyOS network devices.

## [Parameters](vyos_lag_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of link aggregation group configurations. |
| **arp_monitor**  dictionary | ARP Link monitoring parameters. |
| **interval**  integer | ARP link monitoring frequency in milliseconds. |
| **target**  list / elements=string | IP address to use for ARP monitoring. |
| **hash_policy**  string | LAG or bonding transmit hash policy.  Choices:   - `"layer2"` - `"layer2+3"` - `"layer3+4"` |
| **members**  list / elements=dictionary | List of member interfaces for the LAG (bond). |
| **member**  string | Name of the member interface. |
| **mode**  string | LAG or bond mode.  Choices:   - `"802.3ad"` - `"active-backup"` - `"broadcast"` - `"round-robin"` - `"transmit-load-balance"` - `"adaptive-load-balance"` - `"xor-hash"` |
| **name**  string / required | Name of the link aggregation group (LAG) or bond. |
| **primary**  string | Primary device interfaces for the LAG (bond). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VyOS device by executing the command **show configuration commands | grep bond**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](vyos_lag_interfaces_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).

## [Examples](vyos_lag_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2
# set interfaces bonding bond3
#
- name: Merge provided configuration with device configuration
  vyos.vyos.vyos_lag_interfaces:
    config:
    - name: bond2
      mode: active-backup
      members:
      - member: eth2
      - member: eth1
      hash_policy: layer2
      primary: eth2

    - name: bond3
      mode: active-backup
      hash_policy: layer2+3
      members:
      - member: eth3
      primary: eth3
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "name": "bond2"
#        },
#        {
#            "name": "bond3"
#        }
#    ],
#
# "commands": [
#        "set interfaces bonding bond2 hash-policy 'layer2'",
#        "set interfaces bonding bond2 mode 'active-backup'",
#        "set interfaces ethernet eth2 bond-group bond2",
#        "set interfaces ethernet eth1 bond-group bond2",
#        "set interfaces bonding bond2 primary 'eth2'",
#        "set interfaces bonding bond3 hash-policy 'layer2+3'",
#        "set interfaces bonding bond3 mode 'active-backup'",
#        "set interfaces ethernet eth3 bond-group bond3",
#        "set interfaces bonding bond3 primary 'eth3'"
#    ]
#
#     "after": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2+3",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond3",
#            "primary": "eth3"
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2+3'
# set interfaces bonding bond3 mode 'active-backup'
# set interfaces bonding bond3 primary 'eth3'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'

# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2+3'
# set interfaces bonding bond3 mode 'active-backup'
# set interfaces bonding bond3 primary 'eth3'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'
#
- name: Replace device configurations of listed LAGs with provided configurations
  vyos.vyos.vyos_lag_interfaces:
    config:
    - name: bond3
      mode: 802.3ad
      hash_policy: layer2
      members:
      - member: eth3
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2+3",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond3",
#            "primary": "eth3"
#        }
#    ],
#
# "commands": [
#        "delete interfaces bonding bond3 primary",
#        "set interfaces bonding bond3 hash-policy 'layer2'",
#        "set interfaces bonding bond3 mode '802.3ad'"
#    ],
#
# "after": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "802.3ad",
#            "name": "bond3"
#        }
#    ],
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2'
# set interfaces bonding bond3 mode '802.3ad'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'

# Using overridden
#
# Before state
# --------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2'
# set interfaces bonding bond3 mode '802.3ad'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'
#
- name: Overrides all device configuration with provided configuration
  vyos.vyos.vyos_lag_interfaces:
    config:
    - name: bond3
      mode: active-backup
      members:
      - member: eth1
      - member: eth2
      - member: eth3
      primary: eth3
      hash_policy: layer2
    state: overridden
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "802.3ad",
#            "name": "bond3"
#        }
#    ],
#
#    "commands": [
#        "delete interfaces bonding bond2 hash-policy",
#        "delete interfaces ethernet eth1 bond-group bond2",
#        "delete interfaces ethernet eth2 bond-group bond2",
#        "delete interfaces bonding bond2 mode",
#        "delete interfaces bonding bond2 primary",
#        "set interfaces bonding bond3 mode 'active-backup'",
#        "set interfaces ethernet eth1 bond-group bond3",
#        "set interfaces ethernet eth2 bond-group bond3",
#        "set interfaces bonding bond3 primary 'eth3'"
#    ],
#
# "after": [
#        {
#            "name": "bond2"
#        },
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                },
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond3",
#            "primary": "eth3"
#        }
#    ],
#
#
# After state
# ------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2
# set interfaces bonding bond3 hash-policy 'layer2'
# set interfaces bonding bond3 mode 'active-backup'
# set interfaces bonding bond3 primary 'eth3'
# set interfaces ethernet eth1 bond-group 'bond3'
# set interfaces ethernet eth2 bond-group 'bond3'
# set interfaces ethernet eth3 bond-group 'bond3'

# Using deleted
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2+3'
# set interfaces bonding bond3 mode 'active-backup'
# set interfaces bonding bond3 primary 'eth3'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'
#
- name: Delete LAG attributes of given interfaces (Note This won't delete the interface
    itself)
  vyos.vyos.vyos_lag_interfaces:
    config:
    - name: bond2
    - name: bond3
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
# "before": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2+3",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond3",
#            "primary": "eth3"
#        }
#    ],
# "commands": [
#        "delete interfaces bonding bond2 hash-policy",
#        "delete interfaces ethernet eth1 bond-group bond2",
#        "delete interfaces ethernet eth2 bond-group bond2",
#        "delete interfaces bonding bond2 mode",
#        "delete interfaces bonding bond2 primary",
#        "delete interfaces bonding bond3 hash-policy",
#        "delete interfaces ethernet eth3 bond-group bond3",
#        "delete interfaces bonding bond3 mode",
#        "delete interfaces bonding bond3 primary"
#    ],
#
# "after": [
#        {
#            "name": "bond2"
#        },
#        {
#            "name": "bond3"
#        }
#    ],
#
# After state
# ------------
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2
# set interfaces bonding bond3

# Using gathered
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep bond
# set interfaces bonding bond0 hash-policy 'layer2'
# set interfaces bonding bond0 mode 'active-backup'
# set interfaces bonding bond0 primary 'eth1'
# set interfaces bonding bond1 hash-policy 'layer2+3'
# set interfaces bonding bond1 mode 'active-backup'
# set interfaces bonding bond1 primary 'eth2'
# set interfaces ethernet eth1 bond-group 'bond0'
# set interfaces ethernet eth2 bond-group 'bond1'
#
- name: Gather listed  lag interfaces with provided configurations
  vyos.vyos.vyos_lag_interfaces:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#        {
#            "afi": "ipv6",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "This is ipv6 specific rule-set",
#                    "name": "UPLINK",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 1 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 1
#                        },
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 2 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 2
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "INBOUND",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 101 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 101
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 102 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 102
#                        },
#                        {
#                            "action": "accept",
#                            "description": "Rule 103 is configured by Ansible",
#                            "destination": {
#                                "group": {
#                                    "address_group": "inbound"
#                                }
#                            },
#                            "number": 103,
#                            "source": {
#                                "address": "192.0.2.0"
#                            },
#                            "state": {
#                                "established": true,
#                                "invalid": false,
#                                "new": false,
#                                "related": true
#                            }
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep bond
# set interfaces bonding bond0 hash-policy 'layer2'
# set interfaces bonding bond0 mode 'active-backup'
# set interfaces bonding bond0 primary 'eth1'
# set interfaces bonding bond1 hash-policy 'layer2+3'
# set interfaces bonding bond1 mode 'active-backup'
# set interfaces bonding bond1 primary 'eth2'
# set interfaces ethernet eth1 bond-group 'bond0'
# set interfaces ethernet eth2 bond-group 'bond1'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_lag_interfaces:
    config:
    - name: bond0
      hash_policy: layer2
      members:
      - member: eth1
      mode: active-backup
      primary: eth1
    - name: bond1
      hash_policy: layer2+3
      members:
      - member: eth2
      mode: active-backup
      primary: eth2
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        "set interfaces bonding bond0 hash-policy 'layer2'",
#        "set interfaces ethernet eth1 bond-group 'bond0'",
#        "set interfaces bonding bond0 mode 'active-backup'",
#        "set interfaces bonding bond0 primary 'eth1'",
#        "set interfaces bonding bond1 hash-policy 'layer2+3'",
#        "set interfaces ethernet eth2 bond-group 'bond1'",
#        "set interfaces bonding bond1 mode 'active-backup'",
#        "set interfaces bonding bond1 primary 'eth2'"
#    ]

# Using parsed
#
#
- name: Parsed the commands for provided  configuration
  vyos.vyos.vyos_l3_interfaces:
    running_config:
      "set interfaces bonding bond0 hash-policy 'layer2'
       set interfaces bonding bond0 mode 'active-backup'
       set interfaces bonding bond0 primary 'eth1'
       set interfaces bonding bond1 hash-policy 'layer2+3'
       set interfaces bonding bond1 mode 'active-backup'
       set interfaces bonding bond1 primary 'eth2'
       set interfaces ethernet eth1 bond-group 'bond0'
       set interfaces ethernet eth2 bond-group 'bond1'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#         {
#             "hash_policy": "layer2",
#             "members": [
#                 {
#                     "member": "eth1"
#                 }
#             ],
#             "mode": "active-backup",
#             "name": "bond0",
#             "primary": "eth1"
#         },
#         {
#             "hash_policy": "layer2+3",
#             "members": [
#                 {
#                     "member": "eth2"
#                 }
#             ],
#             "mode": "active-backup",
#             "name": "bond1",
#             "primary": "eth2"
#         }
#     ]
```

## [Return Values](vyos_lag_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["set interfaces bonding bond2", "set interfaces bonding bond2 hash-policy layer2"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
