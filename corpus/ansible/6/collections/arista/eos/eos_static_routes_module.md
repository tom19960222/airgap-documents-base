---
collection: ansible
version: "6"
title: "arista.eos.eos_static_routes module – Static routes resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_static_routes_module.html
fetched_at: 2026-07-27T16:45:19+00:00
---
# arista.eos.eos_static_routes module – Static routes resource module

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
> To use it in a playbook, specify: `arista.eos.eos_static_routes`.

New in arista.eos 1.0.0

- [Synopsis](eos_static_routes_module.md#synopsis)
- [Parameters](eos_static_routes_module.md#parameters)
- [Notes](eos_static_routes_module.md#notes)
- [Examples](eos_static_routes_module.md#examples)
- [Return Values](eos_static_routes_module.md#return-values)

## [Synopsis](eos_static_routes_module.md#id1)

- This module configures and manages the attributes of static routes on Arista EOS platforms.

## [Parameters](eos_static_routes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of configurations for static routes. |
| **address_families**  list / elements=dictionary | A dictionary specifying the address family to which the static route(s) belong. |
| **afi**  string / required | Specifies the top level address family indicator.  Choices:   - `"ipv4"` - `"ipv6"` |
| **routes**  list / elements=dictionary | A dictionary that specifies the static route configurations. |
| **dest**  string / required | Destination IPv4 subnet (CIDR or address-mask notation).  The address format is <v4/v6 address>/<mask> or <v4/v6 address> <mask>.  The mask is number in range 0-32 for IPv4 and in range 0-128 for IPv6. |
| **next_hops**  list / elements=dictionary | Details of route to be taken. |
| **admin_distance**  integer | Preference or administrative distance of route (range 1-255). |
| **description**  string | Name of the static route. |
| **forward_router_address**  string | Forwarding router’s address on destination interface. |
| **interface**  string | Outgoing interface to take. For anything except ‘null0’, then next hop IP address should also be configured.  IP address of the next hop router or  null0 Null0 interface or  ethernet e_num Ethernet interface or  loopback l_num Loopback interface or  management m_num Management interface or  port-channel p_num  vlan v_num  vxlan vx_num  Nexthop-Group Specify nexthop group name  Tunnel Tunnel interface  vtep Configure VXLAN Tunnel End Points |
| **mpls_label**  integer | MPLS label |
| **nexthop_grp**  string | Nexthop group |
| **tag**  integer | Route tag value (ranges from 0 to 4294967295). |
| **track**  string | Track value (range 1 - 512). Track must already be configured on the device before adding the route. |
| **vrf**  string | VRF of the destination. |
| **vrf**  string | The VRF to which the static route(s) belong. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | grep routes**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_static_routes_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_static_routes_module.md#id4)

```yaml+jinja
# Using deleted

# Before State:
# ------------

# veos(config)#show running-config | grep route
# ip route vrf testvrf 22.65.1.0/24 Null0 90 name testroute
# ipv6 route 5222:5::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Ethernet1 55
# ipv6 route vrf testvrf 2222:6::/64 Null0 90 name testroute1
# veos(config)#

- name: Delete afi
  arista.eos.eos_static_routes:
    config:
    - vrf: testvrf
      address_families:
      - afi: ipv4
    state: deleted

#    "after": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5222:5::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2222:6::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                },
#                                {
#                                    "admin_distance": 55,
#                                    "interface": "Ethernet1"
#                                },
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute1",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ],
#    "before": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5222:5::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "22.65.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2222:6::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                },
#                                {
#                                    "admin_distance": 55,
#                                    "interface": "Ethernet1"
#                                },
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute1",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ],
#    "changed": true,
#    "commands": [
#        "no ip route vrf testvrf 22.65.1.0/24 Null0 90 name testroute"
#    ],

# After State
# ___________

# veos(config)#show running-config | grep route
# ipv6 route 5222:5::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Ethernet1 55
# ipv6 route vrf testvrf 2222:6::/64 Null0 90 name testroute1

#
# Using merged

# Before : [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "165.10.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 100,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "172.17.252.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgroup"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5001::/64",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 50,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "130.1.122.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1",
#                                    "tag": 50
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ]
#
# Before State
# -------------
# veos(config)#show running-config | grep "route"
# ip route 165.10.1.0/24 Ethernet1 100
# ip route 172.17.252.0/24 Nexthop-Group testgroup
# ip route vrf testvrf 130.1.122.0/24 Ethernet1 tag 50
# ipv6 route 5001::/64 Ethernet1 50
# veos(config)#

- name: Merge new static route configuration
  arista.eos.eos_static_routes:
    config:
    - vrf: testvrf
      address_families:
      - afi: ipv6
        routes:
        - dest: 2211::0/64
          next_hop:
          - forward_router_address: 100:1::2
            interface: Ethernet1
    state: merged

# After State
# -----------

#After [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "165.10.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 100,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "172.17.252.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgroup"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5001::/64",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 50,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "130.1.122.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1",
#                                    "tag": 50
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2211::0/64",
#                            "next_hops": [
#                                {
#                                    "aforward_router_address": 100:1::2
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }

#            ],
#            "vrf": "testvrf"
#        }
#    ]
#
# veos(config)#show running-config | grep "route"
# ip route 165.10.1.0/24 Ethernet1 100
# ip route 172.17.252.0/24 Nexthop-Group testgroup
# ip route vrf testvrf 130.1.122.0/24 Ethernet1 tag 50
# ipv6 route 2211::/64 Ethernet1 100:1::2
# ipv6 route 5001::/64 Ethernet1 50
# veos(config)#

# Using overridden

# Before State
# -------------

#    "before": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "165.10.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 100,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "172.17.252.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgroup"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5001::/64",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 50,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "130.1.122.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1",
#                                    "tag": 50
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ]
# veos(config)#show running-config | grep "route"
# ip route 165.10.1.0/24 Ethernet1 100
# ip route 172.17.252.0/24 Nexthop-Group testgroup
# ip route vrf testvrf 130.1.122.0/24 Ethernet1 tag 50
# ipv6 route 5001::/64 Ethernet1 50
# veos(config)#

- name: Overridden static route configuration
  arista.eos.eos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 10.2.2.0/24
          next_hop:
          - interface: Ethernet1
    state: replaced

# After State
# -----------

# "after": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "10.2.2.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
# veos(config)#show running-config | grep "route"
# ip route 10.2.2.0/24 Ethernet1
# veos(config)#

# Using replaced

# Before State
# -------------

# ip route 10.2.2.0/24 Ethernet1
# ip route 10.2.2.0/24 64.1.1.1 label 17 33
# ip route 33.33.33.0/24 Nexthop-Group testgrp
# ip route vrf testvrf 22.65.1.0/24 Null0 90 name testroute
# ipv6 route 5222:5::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Ethernet1 55
# ipv6 route vrf testvrf 2222:6::/64 Null0 90 name testroute1

# [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "10.2.2.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1"
#                                },
#                                {
#                                    "admin_distance": 33,
#                                    "interface": "64.1.1.1",
#                                    "mpls_label": 17
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "33.33.33.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgrp"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5222:5::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "22.65.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2222:6::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                },
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute1",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ]

- name: Replace nexthop
  arista.eos.eos_static_routes:
    config:
    - vrf: testvrf
      address_families:
      - afi: ipv6
        routes:
        - dest: 2222:6::/64
          next_hops:
          - admin_distance: 55
            interface: Ethernet1
    state: replaced

# After State
# -----------

# veos(config)#show running-config | grep route
# ip route 10.2.2.0/24 Ethernet1
# ip route 10.2.2.0/24 64.1.1.1 label 17 33
# ip route 33.33.33.0/24 Nexthop-Group testgrp
# ip route vrf testvrf 22.65.1.0/24 Null0 90 name testroute
# ipv6 route 5222:5::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Ethernet1 55

# "after": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "10.2.2.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1"
#                                },
#                                {
#                                    "admin_distance": 33,
#                                    "interface": "64.1.1.1",
#                                    "mpls_label": 17
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "33.33.33.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgrp"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5222:5::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "22.65.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2222:6::/64",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 55,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ]

# Before State
# -------------
# veos(config)#show running-config | grep "route"
# ip route 165.10.1.0/24 Ethernet1 10.1.1.2 100
# ipv6 route 5001::/64 Ethernet1
# veos(config)#

- name: Gather the exisitng condiguration
  arista.eos.eos_static_routes:
    state: gathered

# returns :
#  arista.eos.eos_static_routes:
#    config:
#      - address_families:
#          - afi: ipv4
#            routes:
#              - dest: 165.10.1.0/24
#                next_hop:
#                  - forward_router_address: 10.1.1.2
#                    interface: "Ethernet1"
#                    admin_distance: 100
#          - afi: ipv6
#            routes:
#              - dest: 5001::/64
#                next_hop:
#                  - interface: "Ethernet1"

# Using rendered

#   arista.eos.eos_static_routes:
#    config:
#      - address_families:
#          - afi: ipv4
#            routes:
#              - dest: 165.10.1.0/24
#                next_hop:
#                  - forward_router_address: 10.1.1.2
#                    interface: "Ethernet1"
#                    admin_distance: 100
#         - afi: ipv6
#            routes:
#              - dest: 5001::/64
#                next_hop:
#                  - interface: "Ethernet1"

# returns:

# ip route 165.10.1.0/24 Ethernet1 10.1.1.2 100
# ipv6 route 5001::/64 Ethernet1
```

## [Return Values](eos_static_routes_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["ip route vrf vrf1 192.2.2.0/24 125.2.3.1 93"]` |
| **gathered**  list / elements=string | The configuration as structured data transformed for the running configuration fetched from remote host  Returned: When `state` is *gathered*  Sample: `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **parsed**  list / elements=string | The configuration as structured data transformed for the value of `running_config` option  Returned: When `state` is *parsed*  Sample: `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **rendered**  list / elements=string | The set of CLI commands generated from the value in `config` option  Returned: When `state` is *rendered*  Sample: `["\"address_families\": [\n                    {\n                        \"afi\": \"ipv4\"", "\n                        \"routes\": [\n                            {\n                                \"dest\": \"192.2.2.0/24\"", "\n                                \"next_hops\": [\n                                    {\n                                        \"admin_distance\": 93", "\n                                        \"description\": null", "\n                                        \"forward_router_address\": null", "\n                                        \"interface\": \"125.2.3.1\"", "\n                                        \"mpls_label\": null", "\n                                        \"nexthop_grp\": null", "\n                                        \"tag\": null", "\n                                        \"track\": null", "\n                                        \"vrf\": null\n                                    }\n                                ]\n                            }\n                        ]\n                    }\n                ]", "\n                \"vrf\": \"vrf1\"\n            }\n        ]", "\n        \"running_config\": null", "\n        \"state\": \"rendered\"\n    }\n"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
