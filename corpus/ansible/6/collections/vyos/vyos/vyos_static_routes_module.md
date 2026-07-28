---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_static_routes module – Static routes resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_static_routes_module.html
fetched_at: 2026-07-28T00:23:33+00:00
---
# vyos.vyos.vyos_static_routes module – Static routes resource module

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
> To use it in a playbook, specify: `vyos.vyos.vyos_static_routes`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_static_routes_module.md#synopsis)
- [Parameters](vyos_static_routes_module.md#parameters)
- [Notes](vyos_static_routes_module.md#notes)
- [Examples](vyos_static_routes_module.md#examples)
- [Return Values](vyos_static_routes_module.md#return-values)

## [Synopsis](vyos_static_routes_module.md#id1)

- This module manages attributes of static routes on VyOS network devices.

## [Parameters](vyos_static_routes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A provided static route configuration. |
| **address_families**  list / elements=dictionary | A dictionary specifying the address family to which the static route(s) belong. |
| **afi**  string / required | Specifies the type of route.  Choices:   - `"ipv4"` - `"ipv6"` |
| **routes**  list / elements=dictionary | A dictionary that specify the static route configurations. |
| **blackhole_config**  dictionary | Configured to silently discard packets. |
| **distance**  integer | Distance for the route. |
| **type**  string | This is to configure only blackhole. |
| **dest**  string / required | An IPv4/v6 address in CIDR notation that specifies the destination network for the static route. |
| **next_hops**  list / elements=dictionary | Next hops to the specified destination. |
| **admin_distance**  integer | Distance value for the route. |
| **enabled**  boolean | Disable IPv4/v6 next-hop static route.  Choices:   - `false` - `true` |
| **forward_router_address**  string / required | The IP address of the next hop that can be used to reach the destination network. |
| **interface**  string | Name of the outgoing interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VyOS device by executing the command **show configuration commands | grep static route**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](vyos_static_routes_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).

## [Examples](vyos_static_routes_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep static
#
- name: Merge the provided configuration with the existing running configuration
  vyos.vyos.vyos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 192.0.2.32/28
          blackhole_config:
            type: blackhole
          next_hops:
          - forward_router_address: 192.0.2.6
          - forward_router_address: 192.0.2.7
    - address_families:
      - afi: ipv6
        routes:
        - dest: 2001:db8:1000::/36
          blackhole_config:
            distance: 2
          next_hops:
          - forward_router_address: 2001:db8:2000:2::1
          - forward_router_address: 2001:db8:2000:2::2
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# before": []
#
#    "commands": [
#        "set protocols static route 192.0.2.32/28",
#        "set protocols static route 192.0.2.32/28 blackhole",
#        "set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'",
#        "set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'",
#        "set protocols static route6 2001:db8:1000::/36",
#        "set protocols static route6 2001:db8:1000::/36 blackhole distance '2'",
#        "set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'",
#        "set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'"
#    ]
#
# "after": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "type": "blackhole"
#                            },
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "192.0.2.6"
#                                },
#                                {
#                                    "forward_router_address": "192.0.2.7"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::1"
#                                },
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::2"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep static
# set protocols static route 192.0.2.32/28 'blackhole'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'
# set protocols static route6 2001:db8:1000::/36 blackhole distance '2'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'

# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep static
# set protocols static route 192.0.2.32/28 'blackhole'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'
# set protocols static route 192.0.2.33/28 'blackhole'
# set protocols static route 192.0.2.33/28 next-hop '192.0.2.3'
# set protocols static route 192.0.2.33/28 next-hop '192.0.2.4'
# set protocols static route6 2001:db8:1000::/36 blackhole distance '2'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'
#
- name: Replace device configurations of listed static routes with provided configurations
  vyos.vyos.vyos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 192.0.2.32/28
          blackhole_config:
            distance: 2
          next_hops:
          - forward_router_address: 192.0.2.7
            enabled: false
          - forward_router_address: 192.0.2.9
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "type": "blackhole"
#                            },
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "192.0.2.6"
#                                },
#                                {
#                                    "forward_router_address": "192.0.2.7"
#                                }
#                            ]
#                        },
#                        {
#                            "blackhole_config": {
#                                "type": "blackhole"
#                            },
#                            "dest": "192.0.2.33/28",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "192.0.2.3"
#                                },
#                                {
#                                    "forward_router_address": "192.0.2.4"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::1"
#                                },
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::2"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
# "commands": [
#        "delete protocols static route 192.0.2.32/28 next-hop '192.0.2.6'",
#        "delete protocols static route 192.0.2.32/28 next-hop '192.0.2.7'",
#        "set protocols static route 192.0.2.32/28 next-hop 192.0.2.7 'disable'",
#        "set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'",
#        "set protocols static route 192.0.2.32/28 next-hop '192.0.2.9'",
#        "set protocols static route 192.0.2.32/28 blackhole distance '2'"
#    ]
#
#    "after": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "enabled": false,
#                                    "forward_router_address": "192.0.2.7"
#                                },
#                                {
#                                    "forward_router_address": "192.0.2.9"
#                                }
#                            ]
#                        },
#                        {
#                            "blackhole_config": {
#                                "type": "blackhole"
#                            },
#                            "dest": "192.0.2.33/28",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "192.0.2.3"
#                                },
#                                {
#                                    "forward_router_address": "192.0.2.4"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::1"
#                                },
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::2"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep static
# set protocols static route 192.0.2.32/28 blackhole distance '2'
# set protocols static route 192.0.2.32/28 next-hop 192.0.2.7 'disable'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.9'
# set protocols static route 192.0.2.33/28 'blackhole'
# set protocols static route 192.0.2.33/28 next-hop '192.0.2.3'
# set protocols static route 192.0.2.33/28 next-hop '192.0.2.4'
# set protocols static route6 2001:db8:1000::/36 blackhole distance '2'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'

# Using overridden
#
# Before state
# --------------
#
# vyos@vyos:~$ show configuration commands| grep static
# set protocols static route 192.0.2.32/28 blackhole distance '2'
# set protocols static route 192.0.2.32/28 next-hop 192.0.2.7 'disable'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.9'
# set protocols static route6 2001:db8:1000::/36 blackhole distance '2'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'
#
- name: Overrides all device configuration with provided configuration
  vyos.vyos.vyos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 198.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.18
    state: overridden
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# "before": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "enabled": false,
#                                    "forward_router_address": "192.0.2.7"
#                                },
#                                {
#                                    "forward_router_address": "192.0.2.9"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::1"
#                                },
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::2"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
#    "commands": [
#        "delete protocols static route 192.0.2.32/28",
#        "delete protocols static route6 2001:db8:1000::/36",
#        "set protocols static route 198.0.2.48/28",
#        "set protocols static route 198.0.2.48/28 next-hop '192.0.2.18'"
#
#
#    "after": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "198.0.2.48/28",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "192.0.2.18"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
#
# After state
# ------------
#
# vyos@vyos:~$ show configuration commands| grep static
# set protocols static route 198.0.2.48/28 next-hop '192.0.2.18'

# Using deleted to delete static route based on afi
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands| grep static
# set protocols static route 192.0.2.32/28 'blackhole'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'
# set protocols static route6 2001:db8:1000::/36 blackhole distance '2'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'
#
- name: Delete static route based on afi.
  vyos.vyos.vyos_static_routes:
    config:
    - address_families:
      - afi: ipv4
      - afi: ipv6
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "type": "blackhole"
#                            },
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "192.0.2.6"
#                                },
#                                {
#                                    "forward_router_address": "192.0.2.7"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::1"
#                                },
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::2"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#    "commands": [
#       "delete protocols static route",
#       "delete protocols static route6"
#    ]
#
# "after": []
# After state
# ------------
# vyos@vyos# run show configuration commands | grep static
# set protocols 'static'

# Using deleted to delete all the static routes when passes config is empty
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands| grep static
# set protocols static route 192.0.2.32/28 'blackhole'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'
# set protocols static route6 2001:db8:1000::/36 blackhole distance '2'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'
#
- name: Delete all the static routes.
  vyos.vyos.vyos_static_routes:
    config:
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "type": "blackhole"
#                            },
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "192.0.2.6"
#                                },
#                                {
#                                    "forward_router_address": "192.0.2.7"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::1"
#                                },
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::2"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#    "commands": [
#       "delete protocols static route",
#       "delete protocols static route6"
#    ]
#
# "after": []
# After state
# ------------
# vyos@vyos# run show configuration commands | grep static
# set protocols 'static'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 192.0.2.32/28
          blackhole_config:
            type: blackhole
          next_hops:
          - forward_router_address: 192.0.2.6
          - forward_router_address: 192.0.2.7
    - address_families:
      - afi: ipv6
        routes:
        - dest: 2001:db8:1000::/36
          blackhole_config:
            distance: 2
          next_hops:
          - forward_router_address: 2001:db8:2000:2::1
          - forward_router_address: 2001:db8:2000:2::2
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        "set protocols static route 192.0.2.32/28",
#        "set protocols static route 192.0.2.32/28 blackhole",
#        "set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'",
#        "set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'",
#        "set protocols static route6 2001:db8:1000::/36",
#        "set protocols static route6 2001:db8:1000::/36 blackhole distance '2'",
#        "set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'",
#        "set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'"
#    ]

# Using parsed
#
#
- name: Parse the provided running configuration
  vyos.vyos.vyos_static_routes:
    running_config:
      "set protocols static route 192.0.2.32/28 'blackhole'
       set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'
       set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'
       set protocols static route6 2001:db8:1000::/36 blackhole distance '2'
       set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'
       set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::2"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::2"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]

# Using gathered
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep static
# set protocols static route 192.0.2.32/28 'blackhole'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'
# set protocols static route6 2001:db8:1000::/36 blackhole distance '2'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'
#
- name: Gather listed static routes with provided configurations
  vyos.vyos.vyos_static_routes:
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
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "type": "blackhole"
#                            },
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "192.0.2.6"
#                                },
#                                {
#                                    "forward_router_address": "192.0.2.7"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "blackhole_config": {
#                                "distance": 2
#                            },
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::1"
#                                },
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::2"
#                                }
#                            ]
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
# vyos@vyos:~$ show configuration commands| grep static
# set protocols static route 192.0.2.32/28 'blackhole'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'
# set protocols static route 192.0.2.32/28 next-hop '192.0.2.7'
# set protocols static route6 2001:db8:1000::/36 blackhole distance '2'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::1'
# set protocols static route6 2001:db8:1000::/36 next-hop '2001:db8:2000:2::2'
```

## [Return Values](vyos_static_routes_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["set protocols static route 192.0.2.32/28 next-hop '192.0.2.6'", "set protocols static route 192.0.2.32/28 'blackhole'"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
