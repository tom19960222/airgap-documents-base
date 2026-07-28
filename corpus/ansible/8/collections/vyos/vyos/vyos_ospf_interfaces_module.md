---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_ospf_interfaces module – OSPF Interfaces Resource Module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_ospf_interfaces_module.html
fetched_at: 2026-07-28T02:59:20+00:00
---
# vyos.vyos.vyos_ospf_interfaces module – OSPF Interfaces Resource Module.

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_ospf_interfaces`.

New in vyos.vyos 1.2.0

- [Synopsis](vyos_ospf_interfaces_module.md#synopsis)
- [Parameters](vyos_ospf_interfaces_module.md#parameters)
- [Examples](vyos_ospf_interfaces_module.md#examples)

## [Synopsis](vyos_ospf_interfaces_module.md#id1)

- This module manages OSPF configuration of interfaces on devices running VYOS.

Aliases: ospf_interfaces

## [Parameters](vyos_ospf_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of OSPF configuration for interfaces. |
| **address_family**  list / elements=dictionary | OSPF settings on the interfaces in address-family context. |
| **afi**  string / required | Address Family Identifier (AFI) for OSPF settings on the interfaces.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **authentication**  dictionary | Authentication settings on the interface. |
| **md5_key**  dictionary | md5 parameters. |
| **key**  string | md5 key. |
| **key_id**  integer | key id. |
| **plaintext_password**  string | Plain Text password. |
| **bandwidth**  integer | Bandwidth of interface (kilobits/sec) |
| **cost**  integer | metric associated with interface. |
| **dead_interval**  integer | Time interval to detect a dead router. |
| **hello_interval**  integer | Timer interval between transmission of hello packets. |
| **ifmtu**  integer | interface MTU. |
| **instance**  string | Instance ID. |
| **mtu_ignore**  boolean | if True, Disable MTU check for Database Description packets.  **Choices:**   - `false` - `true` |
| **network**  string | Interface type. |
| **passive**  boolean | If True, disables forming adjacency.  **Choices:**   - `false` - `true` |
| **priority**  integer | Interface priority. |
| **retransmit_interval**  integer | LSA retransmission interval. |
| **transmit_delay**  integer | LSA transmission delay. |
| **name**  string | Name/Identifier of the interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VYOS device by executing the command **show configuration commands | match “set interfaces”**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Examples](vyos_ospf_interfaces_module.md#id3)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#

# @vyos:~$ show configuration commands | match "ospf"

  - name: Merge provided configuration with device configuration
    vyos.vyos.vyos_ospf_interfaces:
      config:
        - name: "eth1"
          address_family:
            - afi: "ipv4"
              transmit_delay: 50
              priority: 26
              network: "point-to-point"
            - afi: "ipv6"
              dead_interval: 39
        - name: "bond2"
          address_family:
            - afi: "ipv4"
              transmit_delay: 45
              bandwidth: 70
              authentication:
                md5_key:
                  key_id: 10
                  key: "1111111111232345"
            - afi: "ipv6"
              passive: True
      state: merged

# After State:
# --------------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set interfaces bonding bond2 ip ospf authentication md5 key-id 10 md5-key '1111111111232345'
# set interfaces bonding bond2 ip ospf bandwidth '70'
# set interfaces bonding bond2 ip ospf transmit-delay '45'
# set interfaces bonding bond2 ipv6 ospfv3 'passive'
# set interfaces ethernet eth1 ip ospf network 'point-to-point'
# set interfaces ethernet eth1 ip ospf priority '26'
# set interfaces ethernet eth1 ip ospf transmit-delay '50'
# set interfaces ethernet eth1 ipv6 ospfv3 dead-interval '39'

# "after": [
#        "
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                        "md5_key": {
#                            "key": "1111111111232345",
#                            "key_id": 10
#                        }
#                    },
#                    "bandwidth": 70,
#                    "transmit_delay": 45
#                },
#                {
#                    "afi": "ipv6",
#                    "passive": true
#                }
#            ],
#            "name": "bond2"
#        },
#        {
#            "name": "eth0"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "network": "point-to-point",
#                    "priority": 26,
#                    "transmit_delay": 50
#                },
#                {
#                    "afi": "ipv6",
#                    "dead_interval": 39
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
#    "before": [
#        {
#            "name": "eth0"
#        },
#        {
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
#    "changed": true,
#    "commands": [
#        "set interfaces ethernet eth1 ip ospf transmit-delay 50",
#        "set interfaces ethernet eth1 ip ospf priority 26",
#        "set interfaces ethernet eth1 ip ospf network point-to-point",
#        "set interfaces ethernet eth1 ipv6 ospfv3 dead-interval 39",
#        "set interfaces bonding bond2 ip ospf transmit-delay 45",
#        "set interfaces bonding bond2 ip ospf bandwidth 70",
#        "set interfaces bonding bond2 ip ospf authentication md5 key-id 10 md5-key 1111111111232345",
#        "set interfaces bonding bond2 ipv6 ospfv3 passive"
#    ],

# Using replaced:

# Before State:
# ------------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set interfaces bonding bond2 ip ospf authentication md5 key-id 10 md5-key '1111111111232345'
# set interfaces bonding bond2 ip ospf bandwidth '70'
# set interfaces bonding bond2 ip ospf transmit-delay '45'
# set interfaces bonding bond2 ipv6 ospfv3 'passive'
# set interfaces ethernet eth1 ip ospf network 'point-to-point'
# set interfaces ethernet eth1 ip ospf priority '26'
# set interfaces ethernet eth1 ip ospf transmit-delay '50'
# set interfaces ethernet eth1 ipv6 ospfv3 dead-interval '39'

  - name: Replace provided configuration with device configuration
    vyos.vyos.vyos_ospf_interfaces:
      config:
        - name: "eth1"
          address_family:
            - afi: "ipv4"
              cost: 100
            - afi: "ipv6"
              ifmtu: 33
        - name: "bond2"
          address_family:
            - afi: "ipv4"
              transmit_delay: 45
            - afi: "ipv6"
              passive: True
      state: replaced

# After State:
# -----------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set interfaces bonding bond2 ip ospf transmit-delay '45'
# set interfaces bonding bond2 ipv6 ospfv3 'passive'
# set interfaces ethernet eth1 ip ospf cost '100'
# set interfaces ethernet eth1 ipv6 ospfv3 ifmtu '33'
# vyos@vyos:~$

# Module Execution
# ----------------
#    "after": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "transmit_delay": 45
#                },
#                {
#                    "afi": "ipv6",
#                    "passive": true
#                }
#            ],
#            "name": "bond2"
#        },
#        {
#            "name": "eth0"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "cost": 100
#                },
#                {
#                    "afi": "ipv6",
#                    "ifmtu": 33
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
#    "before": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                        "md5_key": {
#                            "key": "1111111111232345",
#                            "key_id": 10
#                        }
#                    },
#                    "bandwidth": 70,
#                    "transmit_delay": 45
#                },
#                {
#                    "afi": "ipv6",
#                    "passive": true
#                }
#            ],
#            "name": "bond2"
#        },
#        {
#            "name": "eth0"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "network": "point-to-point",
#                    "priority": 26,
#                    "transmit_delay": 50
#                },
#                {
#                    "afi": "ipv6",
#                    "dead_interval": 39
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
#    "changed": true,
#    "commands": [
#        "set interfaces ethernet eth1 ip ospf cost 100",
#        "set interfaces ethernet eth1 ipv6 ospfv3 ifmtu 33",
#        "delete interfaces ethernet eth1 ip ospf network point-to-point",
#        "delete interfaces ethernet eth1 ip ospf priority 26",
#        "delete interfaces ethernet eth1 ip ospf transmit-delay 50",
#        "delete interfaces ethernet eth1 ipv6 ospfv3 dead-interval 39",
#        "delete interfaces bonding bond2 ip ospf authentication",
#        "delete interfaces bonding bond2 ip ospf bandwidth 70"
#    ],
#

# Using Overridden:
# -----------------

# Before State:
# ------------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set interfaces bonding bond2 ip ospf authentication md5 key-id 10 md5-key '1111111111232345'
# set interfaces bonding bond2 ip ospf bandwidth '70'
# set interfaces bonding bond2 ip ospf transmit-delay '45'
# set interfaces bonding bond2 ipv6 ospfv3 'passive'
# set interfaces ethernet eth1 ip ospf cost '100'
# set interfaces ethernet eth1 ip ospf network 'point-to-point'
# set interfaces ethernet eth1 ip ospf priority '26'
# set interfaces ethernet eth1 ip ospf transmit-delay '50'
# set interfaces ethernet eth1 ipv6 ospfv3 dead-interval '39'
# set interfaces ethernet eth1 ipv6 ospfv3 ifmtu '33'
# vyos@vyos:~$

  - name: Override device configuration with provided configuration
    vyos.vyos.vyos_ospf_interfaces:
      config:
        - name: "eth0"
          address_family:
            - afi: "ipv4"
              cost: 100
            - afi: "ipv6"
              ifmtu: 33
              passive: True
      state: overridden
# After State:
# -----------

# 200~vyos@vyos:~$ show configuration commands | match "ospf"
# set interfaces ethernet eth0 ip ospf cost '100'
# set interfaces ethernet eth0 ipv6 ospfv3 ifmtu '33'
# set interfaces ethernet eth0 ipv6 ospfv3 'passive'
# vyos@vyos:~$
#
#
#     "after": [
#         {
#             "name": "bond2"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "cost": 100
#                 },
#                 {
#                     "afi": "ipv6",
#                     "ifmtu": 33,
#                     "passive": true
#                 }
#             ],
#             "name": "eth0"
#         },
#         {
#             "name": "eth1"
#         },
#         {
#             "name": "eth2"
#         },
#         {
#             "name": "eth3"
#         }
#     ],
#     "before": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "md5_key": {
#                             "key": "1111111111232345",
#                             "key_id": 10
#                         }
#                     },
#                     "bandwidth": 70,
#                     "transmit_delay": 45
#                 },
#                 {
#                     "afi": "ipv6",
#                     "passive": true
#                 }
#             ],
#             "name": "bond2"
#         },
#         {
#             "name": "eth0"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "cost": 100,
#                     "network": "point-to-point",
#                     "priority": 26,
#                     "transmit_delay": 50
#                 },
#                 {
#                     "afi": "ipv6",
#                     "dead_interval": 39,
#                     "ifmtu": 33
#                 }
#             ],
#             "name": "eth1"
#         },
#         {
#             "name": "eth2"
#         },
#         {
#             "name": "eth3"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete interfaces bonding bond2 ip ospf",
#         "delete interfaces bonding bond2 ipv6 ospfv3",
#         "delete interfaces ethernet eth1 ip ospf",
#         "delete interfaces ethernet eth1 ipv6 ospfv3",
#         "set interfaces ethernet eth0 ip ospf cost 100",
#         "set interfaces ethernet eth0 ipv6 ospfv3 ifmtu 33",
#         "set interfaces ethernet eth0 ipv6 ospfv3 passive"
#     ],
#

# Using deleted:
# -------------

# before state:
# -------------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set interfaces bonding bond2 ip ospf authentication md5 key-id 10 md5-key '1111111111232345'
# set interfaces bonding bond2 ip ospf bandwidth '70'
# set interfaces bonding bond2 ip ospf transmit-delay '45'
# set interfaces bonding bond2 ipv6 ospfv3 'passive'
# set interfaces ethernet eth0 ip ospf cost '100'
# set interfaces ethernet eth0 ipv6 ospfv3 ifmtu '33'
# set interfaces ethernet eth0 ipv6 ospfv3 'passive'
# set interfaces ethernet eth1 ip ospf network 'point-to-point'
# set interfaces ethernet eth1 ip ospf priority '26'
# set interfaces ethernet eth1 ip ospf transmit-delay '50'
# set interfaces ethernet eth1 ipv6 ospfv3 dead-interval '39'
# vyos@vyos:~$

  - name: Delete device configuration
    vyos.vyos.vyos_ospf_interfaces:
      config:
        - name: "eth0"
      state: deleted

# After State:
# -----------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set interfaces bonding bond2 ip ospf authentication md5 key-id 10 md5-key '1111111111232345'
# set interfaces bonding bond2 ip ospf bandwidth '70'
# set interfaces bonding bond2 ip ospf transmit-delay '45'
# set interfaces bonding bond2 ipv6 ospfv3 'passive'
# set interfaces ethernet eth1 ip ospf network 'point-to-point'
# set interfaces ethernet eth1 ip ospf priority '26'
# set interfaces ethernet eth1 ip ospf transmit-delay '50'
# set interfaces ethernet eth1 ipv6 ospfv3 dead-interval '39'
# vyos@vyos:~$
#
#
# "after": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "md5_key": {
#                             "key": "1111111111232345",
#                             "key_id": 10
#                         }
#                     },
#                     "bandwidth": 70,
#                     "transmit_delay": 45
#                 },
#                 {
#                     "afi": "ipv6",
#                     "passive": true
#                 }
#             ],
#             "name": "bond2"
#         },
#         {
#             "name": "eth0"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "network": "point-to-point",
#                     "priority": 26,
#                     "transmit_delay": 50
#                 },
#                 {
#                     "afi": "ipv6",
#                     "dead_interval": 39
#                 }
#             ],
#             "name": "eth1"
#         },
#         {
#             "name": "eth2"
#         },
#         {
#             "name": "eth3"
#         }
#     ],
#     "before": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "md5_key": {
#                             "key": "1111111111232345",
#                             "key_id": 10
#                         }
#                     },
#                     "bandwidth": 70,
#                     "transmit_delay": 45
#                 },
#                 {
#                     "afi": "ipv6",
#                     "passive": true
#                 }
#             ],
#             "name": "bond2"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "cost": 100
#                 },
#                 {
#                     "afi": "ipv6",
#                     "ifmtu": 33,
#                     "passive": true
#                 }
#             ],
#             "name": "eth0"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "network": "point-to-point",
#                     "priority": 26,
#                     "transmit_delay": 50
#                 },
#                 {
#                     "afi": "ipv6",
#                     "dead_interval": 39
#                 }
#             ],
#             "name": "eth1"
#         },
#         {
#             "name": "eth2"
#         },
#         {
#             "name": "eth3"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete interfaces ethernet eth0 ip ospf",
#         "delete interfaces ethernet eth0 ipv6 ospfv3"
#     ],
#
# Using parsed:
# parsed.cfg:

# set interfaces bonding bond2 ip ospf authentication md5 key-id 10 md5-key '1111111111232345'
# set interfaces bonding bond2 ip ospf bandwidth '70'
# set interfaces bonding bond2 ip ospf transmit-delay '45'
# set interfaces bonding bond2 ipv6 ospfv3 'passive'
# set interfaces ethernet eth0 ip ospf cost '50'
# set interfaces ethernet eth0 ip ospf priority '26'
# set interfaces ethernet eth0 ipv6 ospfv3 instance-id '33'
# set interfaces ethernet eth0 ipv6 ospfv3 'mtu-ignore'
# set interfaces ethernet eth1 ip ospf network 'point-to-point'
# set interfaces ethernet eth1 ip ospf priority '26'
# set interfaces ethernet eth1 ip ospf transmit-delay '50'
# set interfaces ethernet eth1 ipv6 ospfv3 dead-interval '39'
#

  - name: parse configs
    vyos.vyos.vyos_ospf_interfaces:
      running_config: "{{ lookup('file', './parsed.cfg') }}"
      state: parsed

# Module Execution:
# ----------------

#  "parsed": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "md5_key": {
#                             "key": "1111111111232345",
#                             "key_id": 10
#                         }
#                     },
#                     "bandwidth": 70,
#                     "transmit_delay": 45
#                 },
#                 {
#                     "afi": "ipv6",
#                     "passive": true
#                 }
#             ],
#             "name": "bond2"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "cost": 50,
#                     "priority": 26
#                 },
#                 {
#                     "afi": "ipv6",
#                     "instance": "33",
#                     "mtu_ignore": true
#                 }
#             ],
#             "name": "eth0"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "network": "point-to-point",
#                     "priority": 26,
#                     "transmit_delay": 50
#                 },
#                 {
#                     "afi": "ipv6",
#                     "dead_interval": 39
#                 }
#             ],
#             "name": "eth1"
#         }
#     ]

# Using rendered:
# --------------

  - name: Render
    vyos.vyos.vyos_ospf_interfaces:
      config:
        - name: "eth1"
          address_family:
            - afi: "ipv4"
              transmit_delay: 50
              priority: 26
              network: "point-to-point"
            - afi: "ipv6"
              dead_interval: 39
        - name: "bond2"
          address_family:
            - afi: "ipv4"
              transmit_delay: 45
              bandwidth: 70
              authentication:
                md5_key:
                  key_id: 10
                  key: "1111111111232345"
            - afi: "ipv6"
              passive: True
      state: rendered

# Module Execution:
# ----------------

#    "rendered": [
#        "set interfaces ethernet eth1 ip ospf transmit-delay 50",
#        "set interfaces ethernet eth1 ip ospf priority 26",
#        "set interfaces ethernet eth1 ip ospf network point-to-point",
#        "set interfaces ethernet eth1 ipv6 ospfv3 dead-interval 39",
#        "set interfaces bonding bond2 ip ospf transmit-delay 45",
#        "set interfaces bonding bond2 ip ospf bandwidth 70",
#        "set interfaces bonding bond2 ip ospf authentication md5 key-id 10 md5-key 1111111111232345",
#        "set interfaces bonding bond2 ipv6 ospfv3 passive"
#    ]
#

# Using Gathered:
# --------------

# Native Config:

# vyos@vyos:~$ show configuration commands | match "ospf"
# set interfaces bonding bond2 ip ospf authentication md5 key-id 10 md5-key '1111111111232345'
# set interfaces bonding bond2 ip ospf bandwidth '70'
# set interfaces bonding bond2 ip ospf transmit-delay '45'
# set interfaces bonding bond2 ipv6 ospfv3 'passive'
# set interfaces ethernet eth1 ip ospf network 'point-to-point'
# set interfaces ethernet eth1 ip ospf priority '26'
# set interfaces ethernet eth1 ip ospf transmit-delay '50'
# set interfaces ethernet eth1 ipv6 ospfv3 dead-interval '39'
# vyos@vyos:~$

  - name: gather configs
    vyos.vyos.vyos_ospf_interfaces:
      state: gathered

# Module Execution:
# -----------------

#    "gathered": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                        "md5_key": {
#                            "key": "1111111111232345",
#                            "key_id": 10
#                        }
#                    },
#                    "bandwidth": 70,
#                    "transmit_delay": 45
#                },
#                {
#                    "afi": "ipv6",
#                    "passive": true
#                }
#            ],
#            "name": "bond2"
#        },
#        {
#            "name": "eth0"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "network": "point-to-point",
#                    "priority": 26,
#                    "transmit_delay": 50
#                },
#                {
#                    "afi": "ipv6",
#                    "dead_interval": 39
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
```

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
