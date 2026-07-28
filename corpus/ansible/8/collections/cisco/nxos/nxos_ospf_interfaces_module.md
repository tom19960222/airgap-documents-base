---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_ospf_interfaces module – OSPF Interfaces Resource Module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_ospf_interfaces_module.html
fetched_at: 2026-07-28T01:38:57+00:00
---
# cisco.nxos.nxos_ospf_interfaces module – OSPF Interfaces Resource Module.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_ospf_interfaces`.

New in cisco.nxos 1.3.0

- [Synopsis](nxos_ospf_interfaces_module.md#synopsis)
- [Parameters](nxos_ospf_interfaces_module.md#parameters)
- [Notes](nxos_ospf_interfaces_module.md#notes)
- [Examples](nxos_ospf_interfaces_module.md#examples)
- [Return Values](nxos_ospf_interfaces_module.md#return-values)

## [Synopsis](nxos_ospf_interfaces_module.md#id1)

- This module manages OSPF(v2/v3) configuration of interfaces on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ospf_interfaces

## [Parameters](nxos_ospf_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of OSPF configuration for interfaces. |
| **address_family**  list / elements=dictionary | OSPF settings on the interfaces in address-family context. |
| **afi**  string / required | Address Family Identifier (AFI) for OSPF settings on the interfaces.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **authentication**  dictionary | Authentication settings on the interface. |
| **enable**  boolean | Enable/disable authentication on the interface.  **Choices:**   - `false` - `true` |
| **key_chain**  string | Authentication password key-chain. |
| **message_digest**  boolean | Use message-digest authentication.  **Choices:**   - `false` - `true` |
| **null_auth**  boolean | Use null(disable) authentication.  **Choices:**   - `false` - `true` |
| **authentication_key**  dictionary | Configure the authentication key for the interface. |
| **encryption**  integer | 0 Specifies an UNENCRYPTED authentication key will follow.  3 Specifies an 3DES ENCRYPTED authentication key will follow.  7 Specifies a Cisco type 7 ENCRYPTED authentication key will follow. |
| **key**  string / required | Authentication key.  Valid values are Cisco type 7 ENCRYPTED password, 3DES ENCRYPTED password and UNENCRYPTED (cleartext) password based on the value of encryption key. |
| **cost**  integer | Cost associated with interface. |
| **dead_interval**  integer | Dead interval value (in seconds). |
| **default_passive_interface**  boolean | Set passive-interface attribute on this interface to default.  This option is mutually exclusive with *passive_interface*.  **Choices:**   - `false` - `true` |
| **hello_interval**  integer | Hello interval value (in seconds). |
| **instance**  integer | Instance identifier. |
| **message_digest_key**  dictionary | Message digest authentication password (key) settings. |
| **encryption**  integer | 0 Specifies an UNENCRYPTED ospf password (key) will follow.  3 Specifies an 3DES ENCRYPTED ospf password (key) will follow.  7 Specifies a Cisco type 7 ENCRYPTED the ospf password (key) will follow. |
| **key**  string / required | Authentication key.  Valid values are Cisco type 7 ENCRYPTED password, 3DES ENCRYPTED password and UNENCRYPTED (cleartext) password based on the value of encryption key. |
| **key_id**  integer / required | Key ID. |
| **mtu_ignore**  boolean | Enable/disable OSPF MTU mismatch detection.  **Choices:**   - `false` - `true` |
| **multi_areas**  list / elements=string | Multi-Areas associated with interface (not tied to OSPF process).  Valid values are Area Ids as an integer or IP address. |
| **network**  string | Network type.  **Choices:**   - `"broadcast"` - `"point-to-point"` |
| **passive_interface**  boolean | Suppress routing updates on the interface.  This option is mutually exclusive with *default_passive_interface*.  **Choices:**   - `false` - `true` |
| **priority**  integer | Router priority. |
| **processes**  list / elements=dictionary | Interfaces configuration for an OSPF process. |
| **area**  dictionary | Area associated with interface. |
| **area_id**  string / required | Area ID in IP address format. |
| **secondaries**  boolean | Do not include secondary IPv4/IPv6 addresses.  **Choices:**   - `false` - `true` |
| **multi_areas**  list / elements=string | Multi-Areas associated with interface.  Valid values are Area Ids as an integer or IP address. |
| **process_id**  string / required | OSPF process tag. |
| **retransmit_interval**  integer | Packet retransmission interval. |
| **shutdown**  boolean | Shutdown OSPF on this interface.  **Choices:**   - `false` - `true` |
| **transmit_delay**  integer | Packet transmission delay. |
| **name**  string / required | Name/Identifier of the interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section “^interface”**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](nxos_ospf_interfaces_module.md#id3)

> **Note:**
>
> - Unsupported for Cisco MDS

## [Examples](nxos_ospf_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
# interface Ethernet1/2
#   no switchport
# interface Ethernet1/3
#   no switchport

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_ospf_interfaces:
    config:
      - name: Ethernet1/1
        address_family:
        - afi: ipv4
          processes:
          - process_id: "100"
            area:
              area_id: 1.1.1.1
              secondaries: False
          multi_areas:
          - 11.11.11.11
        - afi: ipv6
          processes:
          - process_id: "200"
            area:
              area_id: 2.2.2.2
            multi_areas:
            - 21.0.0.0
          - process_id: "300"
            multi_areas:
            - 50.50.50.50
          multi_areas:
          - 16.10.10.10
      - name: Ethernet1/2
        address_family:
        - afi: ipv4
          authentication:
            enable: True
            key_chain: test-1
          message_digest_key:
            key_id: 10
            encryption: 3
            key: abc01d272be25d29
          cost: 100
        - afi: ipv6
          network: broadcast
          shutdown: True
      - name: Ethernet1/3
        address_family:
        - afi: ipv4
          authentication_key:
            encryption: 7
            key: 12090404011C03162E
    state: merged

# Task output
# -------------
# "before": [
#        {
#            "name": "Ethernet1/1"
#        },
#        {
#            "name": "Ethernet1/2"
#        },
#        {
#            "name": "Ethernet1/3"
#        },
# ]
#
# "commands": [
#        "interface Ethernet1/1",
#        "ip router ospf multi-area 11.11.11.11",
#        "ip router ospf 100 area 1.1.1.1 secondaries none",
#        "ipv6 router ospfv3 multi-area 16.10.10.10",
#        "ipv6 router ospfv3 200 area 2.2.2.2",
#        "ipv6 router ospfv3 200 multi-area 21.0.0.0",
#        "ipv6 router ospfv3 300 multi-area 50.50.50.50",
#        "interface Ethernet1/2",
#        "ip ospf authentication key-chain test-1",
#        "ip ospf authentication",
#        "ip ospf message-digest-key 10 md5 3 abc01d272be25d29",
#        "ip ospf cost 100",
#        "ospfv3 network broadcast",
#        "ospfv3 shutdown",
#        "interface Ethernet1/3",
#        "ip ospf authentication-key 7 12090404011C03162E"
# ]
#
# "after": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "multi_areas": [
#                        "11.11.11.11"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "1.1.1.1",
#                                "secondaries": false
#                            },
#                            "process_id": "100"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "multi_areas": [
#                        "16.10.10.10"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "2.2.2.2"
#                            },
#                            "multi_areas": [
#                                "21.0.0.0"
#                            ],
#                            "process_id": "200"
#                        },
#                        {
#                            "multi_areas": [
#                                "50.50.50.50"
#                            ],
#                            "process_id": "300"
#                        }
#                    ]
#                }
#            ],
#            "name": "Ethernet1/1"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                       "enable": true,
#                       "key_chain": "test-1"
#                    },
#                    "cost": 100,
#                    "message_digest_key": {
#                        "encryption": 3,
#                        "key": "abc01d272be25d29",
#                        "key_id": 10
#                    }
#                },
#                {
#                    "afi": "ipv6",
#                    "network": "broadcast",
#                    "shutdown": true
#                }
#            ],
#            "name": "Ethernet1/2"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication_key": {
#                        "encryption": 7,
#                        "key": "12090404011C03162E"
#                    }
#                }
#            ],
#            "name": "Ethernet1/3"
#        },
# ]

# After state:
# -------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
#   ip router ospf 100 area 1.1.1.1 secondaries none
#   ip router ospf multi-area 11.11.11.11
#   ipv6 router ospfv3 200 area 2.2.2.2
#   ipv6 router ospfv3 multi-area 16.10.10.10
#   ipv6 router ospfv3 200 multi-area 21.0.0.0
#   ipv6 router ospfv3 300 multi-area 50.50.50.50
# interface Ethernet1/2
#   no switchport
#   ip ospf authentication
#   ip ospf authentication key-chain test-1
#   ip ospf message-digest-key 10 md5 3 abc01d272be25d29
#   ip ospf cost 100
#   ospfv3 network broadcast
#   ospfv3 shutdown
# interface Ethernet1/3
#   no switchport
#   ip ospf authentication-key 7 12090404011C03162E

# Using replaced

# Before state:
# ------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
#   ip router ospf 100 area 1.1.1.1 secondaries none
#   ip router ospf multi-area 11.11.11.11
#   ipv6 router ospfv3 200 area 2.2.2.2
#   ipv6 router ospfv3 multi-area 16.10.10.10
#   ipv6 router ospfv3 200 multi-area 21.0.0.0
#   ipv6 router ospfv3 300 multi-area 50.50.50.50
# interface Ethernet1/2
#   no switchport
#   ip ospf authentication
#   ip ospf authentication key-chain test-1
#   ip ospf message-digest-key 10 md5 3 abc01d272be25d29
#   ip ospf cost 100
#   ospfv3 network broadcast
#   ospfv3 shutdown
# interface Ethernet1/3
#   no switchport
#   ip ospf authentication-key 7 12090404011C03162E

- name: Replace OSPF configurations of listed interfaces with provided configurations
  cisco.nxos.nxos_ospf_interfaces:
    config:
    - name: Ethernet1/1
      address_family:
      - afi: ipv4
        processes:
        - process_id: "100"
          area:
            area_id: 1.1.1.1
            secondaries: False
        multi_areas:
        - 11.11.11.12
    - name: Ethernet1/3
    state: replaced

# Task output
# -------------
# "before": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "multi_areas": [
#                        "11.11.11.11"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "1.1.1.1",
#                                "secondaries": false
#                            },
#                            "process_id": "100"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "multi_areas": [
#                        "16.10.10.10"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "2.2.2.2"
#                            },
#                            "multi_areas": [
#                                "21.0.0.0"
#                            ],
#                            "process_id": "200"
#                        },
#                        {
#                            "multi_areas": [
#                                "50.50.50.50"
#                            ],
#                            "process_id": "300"
#                        }
#                    ]
#                }
#            ],
#            "name": "Ethernet1/1"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                       "enable": true,
#                       "key_chain": "test-1"
#                    },
#                    "cost": 100,
#                    "message_digest_key": {
#                        "encryption": 3,
#                        "key": "abc01d272be25d29",
#                        "key_id": 10
#                    }
#                },
#                {
#                    "afi": "ipv6",
#                    "network": "broadcast",
#                    "shutdown": true
#                }
#            ],
#            "name": "Ethernet1/2"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication_key": {
#                        "encryption": 7,
#                        "key": "12090404011C03162E"
#                    }
#                }
#            ],
#            "name": "Ethernet1/3"
#        },
# ]
#
# "commands": [
#        "interface Ethernet1/1",
#        "ip router ospf multi-area 11.11.11.12",
#        "no ip router ospf multi-area 11.11.11.11",
#        "no ipv6 router ospfv3 multi-area 16.10.10.10",
#        "no ipv6 router ospfv3 200 area 2.2.2.2",
#        "no ipv6 router ospfv3 200 multi-area 21.0.0.0",
#        "no ipv6 router ospfv3 300 multi-area 50.50.50.50",
#        "interface Ethernet1/3",
#        "no ip ospf authentication-key 7 12090404011C03162E"
# ]
#
# "after": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "multi_areas": [
#                        "11.11.11.12"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "1.1.1.1",
#                                "secondaries": false
#                            },
#                            "process_id": "100"
#                        }
#                    ]
#                }
#            ],
#            "name": "Ethernet1/1"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                        "enable": true,
#                        "key_chain": "test-1"
#                    },
#                    "cost": 100,
#                    "message_digest_key": {
#                        "encryption": 3,
#                        "key": "abc01d272be25d29",
#                        "key_id": 10
#                    }
#                },
#                {
#                    "afi": "ipv6",
#                    "network": "broadcast",
#                    "shutdown": true
#                }
#            ],
#            "name": "Ethernet1/2"
#        },
#        {
#            "name": "Ethernet1/3"
#        },
#
# After state:
# -------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
#   ip router ospf 100 area 1.1.1.1 secondaries none
#   ip router ospf multi-area 11.11.11.12
# interface Ethernet1/2
#   no switchport
#   ip ospf authentication
#   ip ospf authentication key-chain test-1
#   ip ospf message-digest-key 10 md5 3 abc01d272be25d29
#   ip ospf cost 100
#   ospfv3 network broadcast
#   ospfv3 shutdown
# interface Ethernet1/3
#   no switchport

# Using overridden

# Before state:
# ------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
#   ip router ospf 100 area 1.1.1.1 secondaries none
#   ip router ospf multi-area 11.11.11.11
#   ipv6 router ospfv3 200 area 2.2.2.2
#   ipv6 router ospfv3 multi-area 16.10.10.10
#   ipv6 router ospfv3 200 multi-area 21.0.0.0
#   ipv6 router ospfv3 300 multi-area 50.50.50.50
# interface Ethernet1/2
#   no switchport
#   ip ospf authentication
#   ip ospf authentication key-chain test-1
#   ip ospf message-digest-key 10 md5 3 abc01d272be25d29
#   ip ospf cost 100
#   ospfv3 network broadcast
#   ospfv3 shutdown
# interface Ethernet1/3
#   no switchport
#   ip ospf authentication-key 7 12090404011C03162E

- name: Override all OSPF interfaces configuration with provided configuration
  cisco.nxos.nxos_ospf_interfaces:
    config:
    - name: Ethernet1/1
      address_family:
      - afi: ipv4
        processes:
        - process_id: "100"
          area:
            area_id: 1.1.1.1
            secondaries: False
        multi_areas:
        - 11.11.11.12
    state: overridden

# Task output
# -------------
# "before": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "multi_areas": [
#                        "11.11.11.11"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "1.1.1.1",
#                                "secondaries": false
#                            },
#                            "process_id": "100"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "multi_areas": [
#                        "16.10.10.10"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "2.2.2.2"
#                            },
#                            "multi_areas": [
#                                "21.0.0.0"
#                            ],
#                            "process_id": "200"
#                        },
#                        {
#                            "multi_areas": [
#                                "50.50.50.50"
#                            ],
#                            "process_id": "300"
#                        }
#                    ]
#                }
#            ],
#            "name": "Ethernet1/1"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                       "enable": true,
#                       "key_chain": "test-1"
#                    },
#                    "cost": 100,
#                    "message_digest_key": {
#                        "encryption": 3,
#                        "key": "abc01d272be25d29",
#                        "key_id": 10
#                    }
#                },
#                {
#                    "afi": "ipv6",
#                    "network": "broadcast",
#                    "shutdown": true
#                }
#            ],
#            "name": "Ethernet1/2"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication_key": {
#                        "encryption": 7,
#                        "key": "12090404011C03162E"
#                    }
#                }
#            ],
#            "name": "Ethernet1/3"
#        },
# ]
#
# "commands": [
#        "interface Ethernet1/2",
#        "no ip ospf authentication key-chain test-1",
#        "no ip ospf authentication",
#        "no ip ospf message-digest-key 10 md5 3 abc01d272be25d29",
#        "no ip ospf cost 100",
#        "no ospfv3 network broadcast",
#        "no ospfv3 shutdown",
#        "interface Ethernet1/3",
#        "no ip ospf authentication-key 7 12090404011C03162E",
#        "interface Ethernet1/1",
#        "ip router ospf multi-area 11.11.11.12",
#        "no ip router ospf multi-area 11.11.11.11",
#        "no ipv6 router ospfv3 multi-area 16.10.10.10",
#        "no ipv6 router ospfv3 200 area 2.2.2.2",
#        "no ipv6 router ospfv3 200 multi-area 21.0.0.0",
#        "no ipv6 router ospfv3 300 multi-area 50.50.50.50"
# ]
#
# "after": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "multi_areas": [
#                        "11.11.11.12"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "1.1.1.1",
#                                "secondaries": false
#                            },
#                            "process_id": "100"
#                        }
#                    ]
#                }
#            ],
#            "name": "Ethernet1/1"
#        },
#        {
#            "name": "Ethernet1/2"
#        },
#        {
#            "name": "Ethernet1/3"
#        },
# ]

# After state:
# -------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
#   ip router ospf 100 area 1.1.1.1 secondaries none
#   ip router ospf multi-area 11.11.11.12
# interface Ethernet1/2
#   no switchport
# interface Ethernet1/3
#   no switchport

# Using deleted to delete OSPF config of a single interface

# Before state:
# ------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
#   ip router ospf 100 area 1.1.1.1 secondaries none
#   ip router ospf multi-area 11.11.11.11
#   ipv6 router ospfv3 200 area 2.2.2.2
#   ipv6 router ospfv3 multi-area 16.10.10.10
#   ipv6 router ospfv3 200 multi-area 21.0.0.0
#   ipv6 router ospfv3 300 multi-area 50.50.50.50
# interface Ethernet1/2
#   no switchport
#   ip ospf authentication
#   ip ospf authentication key-chain test-1
#   ip ospf message-digest-key 10 md5 3 abc01d272be25d29
#   ip ospf cost 100
#   ospfv3 network broadcast
#   ospfv3 shutdown
# interface Ethernet1/3
#   no switchport
#   ip ospf authentication-key 7 12090404011C03162E

- name: Delete OSPF config from a single interface
  cisco.nxos.nxos_ospf_interfaces:
    config:
      - name: Ethernet1/1
    state: deleted

# Task output
# -------------
# "before": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "multi_areas": [
#                        "11.11.11.11"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "1.1.1.1",
#                                "secondaries": false
#                            },
#                            "process_id": "100"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "multi_areas": [
#                        "16.10.10.10"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "2.2.2.2"
#                            },
#                            "multi_areas": [
#                                "21.0.0.0"
#                            ],
#                            "process_id": "200"
#                        },
#                        {
#                            "multi_areas": [
#                                "50.50.50.50"
#                            ],
#                            "process_id": "300"
#                        }
#                    ]
#                }
#            ],
#            "name": "Ethernet1/1"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                       "enable": true,
#                       "key_chain": "test-1"
#                    },
#                    "cost": 100,
#                    "message_digest_key": {
#                        "encryption": 3,
#                        "key": "abc01d272be25d29",
#                        "key_id": 10
#                    }
#                },
#                {
#                    "afi": "ipv6",
#                    "network": "broadcast",
#                    "shutdown": true
#                }
#            ],
#            "name": "Ethernet1/2"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication_key": {
#                        "encryption": 7,
#                        "key": "12090404011C03162E"
#                    }
#                }
#            ],
#            "name": "Ethernet1/3"
#        },
# ]
#
# "commands": [
#        "interface Ethernet1/1",
#        "no ip router ospf multi-area 11.11.11.11",
#        "no ip router ospf 100 area 1.1.1.1 secondaries none",
#        "no ipv6 router ospfv3 multi-area 16.10.10.10",
#        "no ipv6 router ospfv3 200 area 2.2.2.2",
#        "no ipv6 router ospfv3 200 multi-area 21.0.0.0",
#        "no ipv6 router ospfv3 300 multi-area 50.50.50.50"
# ]
#
# "before": [
#        {
#            "name": "Ethernet1/1"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                       "enable": true,
#                       "key_chain": "test-1"
#                    },
#                    "cost": 100,
#                    "message_digest_key": {
#                        "encryption": 3,
#                        "key": "abc01d272be25d29",
#                        "key_id": 10
#                    }
#                },
#                {
#                    "afi": "ipv6",
#                    "network": "broadcast",
#                    "shutdown": true
#                }
#            ],
#            "name": "Ethernet1/2"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication_key": {
#                        "encryption": 7,
#                        "key": "12090404011C03162E"
#                    }
#                }
#            ],
#            "name": "Ethernet1/3"
#        },
# ]

# After state:
# ------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
# interface Ethernet1/2
#   no switchport
#   ip ospf authentication
#   ip ospf authentication key-chain test-1
#   ip ospf message-digest-key 10 md5 3 abc01d272be25d29
#   ip ospf cost 100
#   ospfv3 network broadcast
#   ospfv3 shutdown
# interface Ethernet1/3
#   no switchport
#   ip ospf authentication-key 7 12090404011C03162E

# Using deleted to delete OSPF config from all interfaces

# Before state:
# ------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
#   ip router ospf 100 area 1.1.1.1 secondaries none
#   ip router ospf multi-area 11.11.11.11
#   ipv6 router ospfv3 200 area 2.2.2.2
#   ipv6 router ospfv3 multi-area 16.10.10.10
#   ipv6 router ospfv3 200 multi-area 21.0.0.0
#   ipv6 router ospfv3 300 multi-area 50.50.50.50
# interface Ethernet1/2
#   no switchport
#   ip ospf authentication
#   ip ospf authentication key-chain test-1
#   ip ospf message-digest-key 10 md5 3 abc01d272be25d29
#   ip ospf cost 100
#   ospfv3 network broadcast
#   ospfv3 shutdown
# interface Ethernet1/3
#   no switchport
#   ip ospf authentication-key 7 12090404011C03162E

- name: Delete OSPF config from all interfaces
  cisco.nxos.nxos_ospf_interfaces:
    state: deleted

# Task output
# -------------
# "before": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "multi_areas": [
#                        "11.11.11.11"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "1.1.1.1",
#                                "secondaries": false
#                            },
#                            "process_id": "100"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "multi_areas": [
#                        "16.10.10.10"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "2.2.2.2"
#                            },
#                            "multi_areas": [
#                                "21.0.0.0"
#                            ],
#                            "process_id": "200"
#                        },
#                        {
#                            "multi_areas": [
#                                "50.50.50.50"
#                            ],
#                            "process_id": "300"
#                        }
#                    ]
#                }
#            ],
#            "name": "Ethernet1/1"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                       "enable": true,
#                       "key_chain": "test-1"
#                    },
#                    "cost": 100,
#                    "message_digest_key": {
#                        "encryption": 3,
#                        "key": "abc01d272be25d29",
#                        "key_id": 10
#                    }
#                },
#                {
#                    "afi": "ipv6",
#                    "network": "broadcast",
#                    "shutdown": true
#                }
#            ],
#            "name": "Ethernet1/2"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication_key": {
#                        "encryption": 7,
#                        "key": "12090404011C03162E"
#                    }
#                }
#            ],
#            "name": "Ethernet1/3"
#        },
# ]
#
# "commands": [
#        "interface Ethernet1/1",
#        "no ip router ospf multi-area 11.11.11.11",
#        "no ip router ospf 100 area 1.1.1.1 secondaries none",
#        "no ipv6 router ospfv3 multi-area 16.10.10.10",
#        "no ipv6 router ospfv3 200 area 2.2.2.2",
#        "no ipv6 router ospfv3 200 multi-area 21.0.0.0",
#        "no ipv6 router ospfv3 300 multi-area 50.50.50.50",
#        "interface Ethernet1/2",
#        "no ip ospf authentication key-chain test-1",
#        "no ip ospf authentication",
#        "no ip ospf message-digest-key 10 md5 3 abc01d272be25d29",
#        "no ip ospf cost 100",
#        "no ospfv3 network broadcast",
#        "no ospfv3 shutdown",
#        "interface Ethernet1/3",
#        "no ip ospf authentication-key 7 12090404011C03162E"
# ]
#
# "after": [
#        {
#            "name": "Ethernet1/1"
#        },
#        {
#            "name": "Ethernet1/2"
#        },
#        {
#            "name": "Ethernet1/3"
#        },
# ]

# After state:
# ------------
# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
# interface Ethernet1/2
#   no switchport
# interface Ethernet1/3
#   no switchport

# Using rendered

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.nxos.nxos_ospf_interfaces:
    config:
      - name: Ethernet1/1
        address_family:
        - afi: ipv4
          processes:
          - process_id: "100"
            area:
              area_id: 1.1.1.1
              secondaries: False
          multi_areas:
          - 11.11.11.11
        - afi: ipv6
          processes:
          - process_id: "200"
            area:
              area_id: 2.2.2.2
            multi_areas:
            - 21.0.0.0
          - process_id: "300"
            multi_areas:
            - 50.50.50.50
          multi_areas:
          - 16.10.10.10
      - name: Ethernet1/2
        address_family:
        - afi: ipv4
          authentication:
            enable: True
            key_chain: test-1
          message_digest_key:
            key_id: 10
            encryption: 3
            key: abc01d272be25d29
          cost: 100
        - afi: ipv6
          network: broadcast
          shutdown: True
      - name: Ethernet1/3
        address_family:
        - afi: ipv4
          authentication_key:
            encryption: 7
            key: 12090404011C03162E
    state: rendered

# Task Output (redacted)
# -----------------------
# "rendered": [
#        "interface Ethernet1/1",
#        "ip router ospf multi-area 11.11.11.11",
#        "ip router ospf 100 area 1.1.1.1 secondaries none",
#        "ipv6 router ospfv3 multi-area 16.10.10.10",
#        "ipv6 router ospfv3 200 area 2.2.2.2",
#        "ipv6 router ospfv3 200 multi-area 21.0.0.0",
#        "ipv6 router ospfv3 300 multi-area 50.50.50.50",
#        "interface Ethernet1/2",
#        "ip ospf authentication key-chain test-1",
#        "ip ospf authentication",
#        "ip ospf message-digest-key 10 md5 3 abc01d272be25d29",
#        "ip ospf cost 100",
#        "ospfv3 network broadcast",
#        "ospfv3 shutdown",
#        "interface Ethernet1/3",
#        "ip ospf authentication-key 7 12090404011C03162E"
# ]

# Using parsed

# parsed.cfg
# ------------
# interface Ethernet1/1
#   ip router ospf 100 area 1.1.1.1 secondaries none
#   ip router ospf multi-area 11.11.11.11
#   ipv6 router ospfv3 200 area 2.2.2.2
#   ipv6 router ospfv3 200 multi-area 21.0.0.0
#   ipv6 router ospfv3 300 multi-area 50.50.50.50
#   ipv6 router ospfv3 multi-area 16.10.10.10
# interface Ethernet1/2
#   ip ospf authentication
#   ip ospf authentication key-chain test-1
#   ip ospf message-digest-key 10 md5 3 abc01d272be25d29
#   ip ospf cost 100
#   ospfv3 network broadcast
#   ospfv3 shutdown
# interface Ethernet1/3
#   ip ospf authentication-key 7 12090404011C03162E

- name: arse externally provided OSPF interfaces config
  cisco.nxos.nxos_ospf_interfaces:
    running_config: "{{ lookup('file', 'ospf_interfaces.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# "parsed": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "multi_areas": [
#                        "11.11.11.11"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "1.1.1.1",
#                                "secondaries": false
#                            },
#                            "process_id": "100"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "multi_areas": [
#                        "16.10.10.10"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "2.2.2.2"
#                            },
#                            "multi_areas": [
#                                "21.0.0.0"
#                            ],
#                            "process_id": "200"
#                        },
#                        {
#                            "multi_areas": [
#                                "50.50.50.50"
#                            ],
#                            "process_id": "300"
#                        }
#                    ]
#                }
#            ],
#            "name": "Ethernet1/1"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                       "enable": true,
#                       "key_chain": "test-1"
#                    },
#                    "cost": 100,
#                    "message_digest_key": {
#                        "encryption": 3,
#                        "key": "abc01d272be25d29",
#                        "key_id": 10
#                    }
#                },
#                {
#                    "afi": "ipv6",
#                    "network": "broadcast",
#                    "shutdown": true
#                }
#            ],
#            "name": "Ethernet1/2"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication_key": {
#                        "encryption": 7,
#                        "key": "12090404011C03162E"
#                    }
#                }
#            ],
#            "name": "Ethernet1/3"
#        },
# ]

# Using gathered

# On-box config

# NXOS# show running-config | section ^interface
# interface Ethernet1/1
#   no switchport
#   ip router ospf 100 area 1.1.1.1 secondaries none
#   ip router ospf multi-area 11.11.11.12
# interface Ethernet1/2
#   no switchport
#   ip ospf authentication
#   ip ospf authentication key-chain test-1
#   ip ospf message-digest-key 10 md5 3 abc01d272be25d29
#   ip ospf cost 100
#   ospfv3 network broadcast
#   ospfv3 shutdown
# interface Ethernet1/3
#   no switchport

# Task output (redacted)
# -----------------------
# "gathered": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "multi_areas": [
#                        "11.11.11.12"
#                    ],
#                    "processes": [
#                        {
#                            "area": {
#                                "area_id": "1.1.1.1",
#                                "secondaries": false
#                            },
#                            "process_id": "100"
#                        }
#                    ]
#                }
#            ],
#            "name": "Ethernet1/1"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                        "enable": true,
#                        "key_chain": "test-1"
#                    },
#                    "cost": 100,
#                    "message_digest_key": {
#                        "encryption": 3,
#                        "key": "abc01d272be25d29",
#                        "key_id": 10
#                    }
#                },
#                {
#                    "afi": "ipv6",
#                    "network": "broadcast",
#                    "shutdown": true
#                }
#            ],
#            "name": "Ethernet1/2"
#        },
#        {
#            "name": "Ethernet1/3"
#        },
```

## [Return Values](nxos_ospf_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface Ethernet1/1", "ip router ospf multi-area 11.11.11.11", "ip router ospf 100 area 1.1.1.1 secondaries none", "no ipv6 router ospfv3 multi-area 16.10.10.10", "ipv6 router ospfv3 200 area 2.2.2.2", "ipv6 router ospfv3 200 multi-area 21.0.0.0", "ipv6 router ospfv3 300 multi-area 50.50.50.50", "interface Ethernet1/2", "no ip ospf authentication key-chain test-1", "ip ospf authentication"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
