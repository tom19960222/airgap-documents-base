---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_firewall_global module – FIREWALL global resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_firewall_global_module.html
fetched_at: 2026-07-28T02:59:11+00:00
---
# vyos.vyos.vyos_firewall_global module – FIREWALL global resource module

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
> To use it in a playbook, specify: `vyos.vyos.vyos_firewall_global`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_firewall_global_module.md#synopsis)
- [Parameters](vyos_firewall_global_module.md#parameters)
- [Notes](vyos_firewall_global_module.md#notes)
- [Examples](vyos_firewall_global_module.md#examples)
- [Return Values](vyos_firewall_global_module.md#return-values)

## [Synopsis](vyos_firewall_global_module.md#id1)

- This module manage global policies or configurations for firewall on VyOS devices.

Aliases: firewall_global

## [Parameters](vyos_firewall_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of Firewall global configuration options. |
| **config_trap**  boolean | SNMP trap generation on firewall configuration changes.  **Choices:**   - `false` - `true` |
| **group**  dictionary | Defines a group of objects for referencing in firewall rules. |
| **address_group**  list / elements=dictionary | Defines a group of IP addresses for referencing in firewall rules. |
| **afi**  string | Specifies IP address type  **Choices:**   - `"ipv4"` ← (default) - `"ipv6"` |
| **description**  string | Allows you to specify a brief description for the address group. |
| **members**  list / elements=dictionary | Address-group members.  IPv4 address to match.  IPv4 range to match. |
| **address**  string | IP address. |
| **name**  string / required | Name of the firewall address group. |
| **network_group**  list / elements=dictionary | Defines a group of networks for referencing in firewall rules. |
| **afi**  string | Specifies network address type  **Choices:**   - `"ipv4"` ← (default) - `"ipv6"` |
| **description**  string | Allows you to specify a brief description for the network group. |
| **members**  list / elements=dictionary | Adds an IPv4 network to the specified network group.  The format is ip-address/prefix. |
| **address**  string | IP address. |
| **name**  string / required | Name of the firewall network group. |
| **port_group**  list / elements=dictionary | Defines a group of ports for referencing in firewall rules. |
| **description**  string | Allows you to specify a brief description for the port group. |
| **members**  list / elements=dictionary | Port-group member. |
| **port**  string | Defines the number. |
| **name**  string / required | Name of the firewall port group. |
| **log_martians**  boolean | Specifies whether or not to record packets with invalid addresses in the log.  (True) Logs packets with invalid addresses.  (False) Does not log packets with invalid addresses.  **Choices:**   - `false` - `true` |
| **ping**  dictionary | Policy for handling of all IPv4 ICMP echo requests. |
| **all**  boolean | Enables or disables response to all IPv4 ICMP Echo Request (ping) messages.  The system responds to IPv4 ICMP Echo Request messages.  **Choices:**   - `false` - `true` |
| **broadcast**  boolean | Enables or disables response to broadcast IPv4 ICMP Echo Request and Timestamp Request messages.  IPv4 ICMP Echo and Timestamp Request messages are not processed.  **Choices:**   - `false` - `true` |
| **route_redirects**  list / elements=dictionary | -A dictionary of Firewall icmp redirect and source route global configuration options. |
| **afi**  string / required | Specifies IP address type  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **icmp_redirects**  dictionary | Specifies whether to allow sending/receiving of IPv4/v6 ICMP redirect messages. |
| **receive**  boolean | Permits or denies receiving packets ICMP redirect messages.  **Choices:**   - `false` - `true` |
| **send**  boolean | Permits or denies transmitting packets ICMP redirect messages.  **Choices:**   - `false` - `true` |
| **ip_src_route**  boolean | Specifies whether or not to process source route IP options.  **Choices:**   - `false` - `true` |
| **state_policy**  list / elements=dictionary | Specifies global firewall state-policy. |
| **action**  string | Action for packets part of an established connection.  **Choices:**   - `"accept"` - `"drop"` - `"reject"` |
| **connection_type**  string | Specifies connection type.  **Choices:**   - `"established"` - `"invalid"` - `"related"` |
| **log**  boolean | Enable logging of packets part of an established connection.  **Choices:**   - `false` - `true` |
| **syn_cookies**  boolean | Specifies policy for using TCP SYN cookies with IPv4.  (True) Enables TCP SYN cookies with IPv4.  (False) Disables TCP SYN cookies with IPv4.  **Choices:**   - `false` - `true` |
| **twa_hazards_protection**  boolean | RFC1337 TCP TIME-WAIT assassination hazards protection.  **Choices:**   - `false` - `true` |
| **validation**  string | Specifies a policy for source validation by reversed path, as defined in RFC 3704.  (disable) No source validation is performed.  (loose) Enable Loose Reverse Path Forwarding as defined in RFC3704.  (strict) Enable Strict Reverse Path Forwarding as defined in RFC3704.  **Choices:**   - `"strict"` - `"loose"` - `"disable"` |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command `show configuration commands | grep 'firewall'` |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](vyos_firewall_global_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).

## [Examples](vyos_firewall_global_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos# run show  configuration commands | grep firewall
#
#
- name: Merge the provided configuration with the existing running configuration
  vyos.vyos.vyos_firewall_global:
    config:
      validation: strict
      config_trap: true
      log_martians: true
      syn_cookies: true
      twa_hazards_protection: true
      ping:
        all: true
        broadcast: true
      state_policy:
      - connection_type: established
        action: accept
        log: true
      - connection_type: invalid
        action: reject
      route_redirects:
      - afi: ipv4
        ip_src_route: true
        icmp_redirects:
          send: true
          receive: false
      group:
        address_group:
        - name: MGMT-HOSTS
          description: This group has the Management hosts address list
          members:
          - address: 192.0.1.1
          - address: 192.0.1.3
          - address: 192.0.1.5
        network_group:
        - name: MGMT
          description: This group has the Management network addresses
          members:
          - address: 192.0.1.0/24
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
#        "set firewall group address-group MGMT-HOSTS address 192.0.1.1",
#        "set firewall group address-group MGMT-HOSTS address 192.0.1.3",
#        "set firewall group address-group MGMT-HOSTS address 192.0.1.5",
#        "set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address list'",
#        "set firewall group address-group MGMT-HOSTS",
#        "set firewall group network-group MGMT network 192.0.1.0/24",
#        "set firewall group network-group MGMT description 'This group has the Management network addresses'",
#        "set firewall group network-group MGMT",
#        "set firewall ip-src-route 'enable'",
#        "set firewall receive-redirects 'disable'",
#        "set firewall send-redirects 'enable'",
#        "set firewall config-trap 'enable'",
#        "set firewall state-policy established action 'accept'",
#        "set firewall state-policy established log 'enable'",
#        "set firewall state-policy invalid action 'reject'",
#        "set firewall broadcast-ping 'enable'",
#        "set firewall all-ping 'enable'",
#        "set firewall log-martians 'enable'",
#        "set firewall twa-hazards-protection 'enable'",
#        "set firewall syn-cookies 'enable'",
#        "set firewall source-validation 'strict'"
#    ]
#
# "after": {
#        "config_trap": true,
#        "group": {
#            "address_group": [
#                {
#                    "description": "This group has the Management hosts address list",
#                    "members": [
#                        {
#                            "address": "192.0.1.1"
#                        },
#                        {
#                            "address": "192.0.1.3"
#                        },
#                        {
#                            "address": "192.0.1.5"
#                        }
#                    ],
#                    "name": "MGMT-HOSTS"
#                }
#            ],
#            "network_group": [
#                {
#                    "description": "This group has the Management network addresses",
#                    "members": [
#                        {
#                            "address": "192.0.1.0/24"
#                        }
#                    ],
#                    "name": "MGMT"
#                }
#            ]
#        },
#        "log_martians": true,
#        "ping": {
#            "all": true,
#            "broadcast": true
#        },
#        "route_redirects": [
#            {
#                "afi": "ipv4",
#                "icmp_redirects": {
#                    "receive": false,
#                    "send": true
#                },
#                "ip_src_route": true
#            }
#        ],
#        "state_policy": [
#            {
#                "action": "accept",
#                "connection_type": "established",
#                "log": true
#            },
#            {
#                "action": "reject",
#                "connection_type": "invalid"
#            }
#        ],
#        "syn_cookies": true,
#        "twa_hazards_protection": true,
#        "validation": "strict"
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep firewall
# set firewall all-ping 'enable'
# set firewall broadcast-ping 'enable'
# set firewall config-trap 'enable'
# set firewall group address-group MGMT-HOSTS address '192.0.1.1'
# set firewall group address-group MGMT-HOSTS address '192.0.1.3'
# set firewall group address-group MGMT-HOSTS address '192.0.1.5'
# set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address list'
# set firewall group network-group MGMT description 'This group has the Management network addresses'
# set firewall group network-group MGMT network '192.0.1.0/24'
# set firewall ip-src-route 'enable'
# set firewall log-martians 'enable'
# set firewall receive-redirects 'disable'
# set firewall send-redirects 'enable'
# set firewall source-validation 'strict'
# set firewall state-policy established action 'accept'
# set firewall state-policy established log 'enable'
# set firewall state-policy invalid action 'reject'
# set firewall syn-cookies 'enable'
# set firewall twa-hazards-protection 'enable'
#
#
# Using parsed
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_firewall_global:
    running_config:
      "set firewall all-ping 'enable'
       set firewall broadcast-ping 'enable'
       set firewall config-trap 'enable'
       set firewall group address-group ENG-HOSTS address '192.0.3.1'
       set firewall group address-group ENG-HOSTS address '192.0.3.2'
       set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'
       set firewall group address-group SALES-HOSTS address '192.0.2.1'
       set firewall group address-group SALES-HOSTS address '192.0.2.2'
       set firewall group address-group SALES-HOSTS address '192.0.2.3'
       set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'
       set firewall group network-group MGMT description 'This group has the Management network addresses'
       set firewall group network-group MGMT network '192.0.1.0/24'
       set firewall ip-src-route 'enable'
       set firewall log-martians 'enable'
       set firewall receive-redirects 'disable'
       set firewall send-redirects 'enable'
       set firewall source-validation 'strict'
       set firewall state-policy established action 'accept'
       set firewall state-policy established log 'enable'
       set firewall state-policy invalid action 'reject'
       set firewall syn-cookies 'enable'
       set firewall twa-hazards-protection 'enable'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": {
#        "config_trap": true,
#        "group": {
#            "address_group": [
#                {
#                    "description": "Sales office hosts address list",
#                    "members": [
#                        {
#                            "address": "192.0.3.1"
#                        },
#                        {
#                            "address": "192.0.3.2"
#                        }
#                    ],
#                    "name": "ENG-HOSTS"
#                },
#                {
#                    "description": "Sales office hosts address list",
#                    "members": [
#                        {
#                            "address": "192.0.2.1"
#                        },
#                        {
#                            "address": "192.0.2.2"
#                        },
#                        {
#                            "address": "192.0.2.3"
#                        }
#                    ],
#                    "name": "SALES-HOSTS"
#                }
#            ],
#            "network_group": [
#                {
#                    "description": "This group has the Management network addresses",
#                    "members": [
#                        {
#                            "address": "192.0.1.0/24"
#                        }
#                    ],
#                    "name": "MGMT"
#                }
#            ]
#        },
#        "log_martians": true,
#        "ping": {
#            "all": true,
#            "broadcast": true
#        },
#        "route_redirects": [
#            {
#                "afi": "ipv4",
#                "icmp_redirects": {
#                    "receive": false,
#                    "send": true
#                },
#                "ip_src_route": true
#            }
#        ],
#        "state_policy": [
#            {
#                "action": "accept",
#                "connection_type": "established",
#                "log": true
#            },
#            {
#                "action": "reject",
#                "connection_type": "invalid"
#            }
#        ],
#        "syn_cookies": true,
#        "twa_hazards_protection": true,
#        "validation": "strict"
#    }
# }
#
#
# Using deleted
#
# Before state
# -------------
#
# vyos@192# run show configuration commands | grep firewall
# set firewall all-ping 'enable'
# set firewall broadcast-ping 'enable'
# set firewall config-trap 'enable'
# set firewall group address-group MGMT-HOSTS address '192.0.1.1'
# set firewall group address-group MGMT-HOSTS address '192.0.1.3'
# set firewall group address-group MGMT-HOSTS address '192.0.1.5'
# set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address list'
# set firewall group network-group MGMT description 'This group has the Management network addresses'
# set firewall group network-group MGMT network '192.0.1.0/24'
# set firewall ip-src-route 'enable'
# set firewall log-martians 'enable'
# set firewall receive-redirects 'disable'
# set firewall send-redirects 'enable'
# set firewall source-validation 'strict'
# set firewall state-policy established action 'accept'
# set firewall state-policy established log 'enable'
# set firewall state-policy invalid action 'reject'
# set firewall syn-cookies 'enable'
# set firewall twa-hazards-protection 'enable'
- name: Delete attributes of firewall.
  vyos.vyos.vyos_firewall_global:
    config:
      state_policy:
      config_trap:
      log_martians:
      syn_cookies:
      twa_hazards_protection:
      route_redirects:
      ping:
      group:
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": {
#        "config_trap": true,
#        "group": {
#            "address_group": [
#                {
#                    "description": "This group has the Management hosts address list",
#                    "members": [
#                        {
#                            "address": "192.0.1.1"
#                        },
#                        {
#                            "address": "192.0.1.3"
#                        },
#                        {
#                            "address": "192.0.1.5"
#                        }
#                    ],
#                    "name": "MGMT-HOSTS"
#                }
#            ],
#            "network_group": [
#                {
#                    "description": "This group has the Management network addresses",
#                    "members": [
#                        {
#                            "address": "192.0.1.0/24"
#                        }
#                    ],
#                    "name": "MGMT"
#                }
#            ]
#        },
#        "log_martians": true,
#        "ping": {
#            "all": true,
#            "broadcast": true
#        },
#        "route_redirects": [
#            {
#                "afi": "ipv4",
#                "icmp_redirects": {
#                    "receive": false,
#                    "send": true
#                },
#                "ip_src_route": true
#            }
#        ],
#        "state_policy": [
#            {
#                "action": "accept",
#                "connection_type": "established",
#                "log": true
#            },
#            {
#                "action": "reject",
#                "connection_type": "invalid"
#            }
#        ],
#        "syn_cookies": true,
#        "twa_hazards_protection": true,
#        "validation": "strict"
#    }
# "commands": [
#        "delete firewall source-validation",
#        "delete firewall group",
#        "delete firewall log-martians",
#        "delete firewall ip-src-route",
#        "delete firewall receive-redirects",
#        "delete firewall send-redirects",
#        "delete firewall config-trap",
#        "delete firewall state-policy",
#        "delete firewall syn-cookies",
#        "delete firewall broadcast-ping",
#        "delete firewall all-ping",
#        "delete firewall twa-hazards-protection"
#    ]
#
# "after": []
# After state
# ------------
# vyos@192# run show configuration commands | grep firewall
# set  'firewall'
#
#
# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall all-ping 'enable'
# set firewall broadcast-ping 'enable'
# set firewall config-trap 'enable'
# set firewall group address-group MGMT-HOSTS address '192.0.1.1'
# set firewall group address-group MGMT-HOSTS address '192.0.1.3'
# set firewall group address-group MGMT-HOSTS address '192.0.1.5'
# set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address list'
# set firewall group network-group MGMT description 'This group has the Management network addresses'
# set firewall group network-group MGMT network '192.0.1.0/24'
# set firewall ip-src-route 'enable'
# set firewall log-martians 'enable'
# set firewall receive-redirects 'disable'
# set firewall send-redirects 'enable'
# set firewall source-validation 'strict'
# set firewall state-policy established action 'accept'
# set firewall state-policy established log 'enable'
# set firewall state-policy invalid action 'reject'
# set firewall syn-cookies 'enable'
# set firewall twa-hazards-protection 'enable'
#
- name: Replace firewall global attributes configuration.
  vyos.vyos.vyos_firewall_global:
    config:
      validation: strict
      config_trap: true
      log_martians: true
      syn_cookies: true
      twa_hazards_protection: true
      ping:
      all: true
      broadcast: true
      state_policy:
      - connection_type: established
        action: accept
        log: true
      - connection_type: invalid
        action: reject
      route_redirects:
      - afi: ipv4
        ip_src_route: true
        icmp_redirects:
          send: true
          receive: false
      group:
        address_group:
        - name: SALES-HOSTS
          description: Sales office hosts address list
          members:
          - address: 192.0.2.1
          - address: 192.0.2.2
          - address: 192.0.2.3
        - name: ENG-HOSTS
          description: Sales office hosts address list
          members:
          - address: 192.0.3.1
          - address: 192.0.3.2
        network_group:
        - name: MGMT
          description: This group has the Management network addresses
          members:
          - address: 192.0.1.0/24
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": {
#        "config_trap": true,
#        "group": {
#            "address_group": [
#                {
#                    "description": "This group has the Management hosts address list",
#                    "members": [
#                        {
#                            "address": "192.0.1.1"
#                        },
#                        {
#                            "address": "192.0.1.3"
#                        },
#                        {
#                            "address": "192.0.1.5"
#                        }
#                    ],
#                    "name": "MGMT-HOSTS"
#                }
#            ],
#            "network_group": [
#                {
#                    "description": "This group has the Management network addresses",
#                    "members": [
#                        {
#                            "address": "192.0.1.0/24"
#                        }
#                    ],
#                    "name": "MGMT"
#                }
#            ]
#        },
#        "log_martians": true,
#        "ping": {
#            "all": true,
#            "broadcast": true
#        },
#        "route_redirects": [
#            {
#                "afi": "ipv4",
#                "icmp_redirects": {
#                    "receive": false,
#                    "send": true
#                },
#                "ip_src_route": true
#            }
#        ],
#        "state_policy": [
#            {
#                "action": "accept",
#                "connection_type": "established",
#                "log": true
#            },
#            {
#                "action": "reject",
#                "connection_type": "invalid"
#            }
#        ],
#        "syn_cookies": true,
#        "twa_hazards_protection": true,
#        "validation": "strict"
#    }
#
# "commands": [
#        "delete firewall group address-group MGMT-HOSTS",
#        "set firewall group address-group SALES-HOSTS address 192.0.2.1",
#        "set firewall group address-group SALES-HOSTS address 192.0.2.2",
#        "set firewall group address-group SALES-HOSTS address 192.0.2.3",
#        "set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'",
#        "set firewall group address-group SALES-HOSTS",
#        "set firewall group address-group ENG-HOSTS address 192.0.3.1",
#        "set firewall group address-group ENG-HOSTS address 192.0.3.2",
#        "set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'",
#        "set firewall group address-group ENG-HOSTS"
#    ]
#
#    "after": {
#        "config_trap": true,
#        "group": {
#            "address_group": [
#                {
#                    "description": "Sales office hosts address list",
#                    "members": [
#                        {
#                            "address": "192.0.3.1"
#                        },
#                        {
#                            "address": "192.0.3.2"
#                        }
#                    ],
#                    "name": "ENG-HOSTS"
#                },
#                {
#                    "description": "Sales office hosts address list",
#                    "members": [
#                        {
#                            "address": "192.0.2.1"
#                        },
#                        {
#                            "address": "192.0.2.2"
#                        },
#                        {
#                            "address": "192.0.2.3"
#                        }
#                    ],
#                   "name": "SALES-HOSTS"
#                }
#            ],
#            "network_group": [
#                {
#                    "description": "This group has the Management network addresses",
#                    "members": [
#                        {
#                            "address": "192.0.1.0/24"
#                        }
#                    ],
#                    "name": "MGMT"
#                }
#            ]
#        },
#        "log_martians": true,
#        "ping": {
#            "all": true,
#            "broadcast": true
#        },
#        "route_redirects": [
#            {
#                "afi": "ipv4",
#                "icmp_redirects": {
#                    "receive": false,
#                    "send": true
#                },
#                "ip_src_route": true
#            }
#        ],
#        "state_policy": [
#            {
#                "action": "accept",
#                "connection_type": "established",
#                "log": true
#            },
#            {
#                "action": "reject",
#                "connection_type": "invalid"
#            }
#        ],
#        "syn_cookies": true,
#        "twa_hazards_protection": true,
#        "validation": "strict"
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep firewall
# set firewall all-ping 'enable'
# set firewall broadcast-ping 'enable'
# set firewall config-trap 'enable'
# set firewall group address-group ENG-HOSTS address '192.0.3.1'
# set firewall group address-group ENG-HOSTS address '192.0.3.2'
# set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'
# set firewall group address-group SALES-HOSTS address '192.0.2.1'
# set firewall group address-group SALES-HOSTS address '192.0.2.2'
# set firewall group address-group SALES-HOSTS address '192.0.2.3'
# set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'
# set firewall group network-group MGMT description 'This group has the Management network addresses'
# set firewall group network-group MGMT network '192.0.1.0/24'
# set firewall ip-src-route 'enable'
# set firewall log-martians 'enable'
# set firewall receive-redirects 'disable'
# set firewall send-redirects 'enable'
# set firewall source-validation 'strict'
# set firewall state-policy established action 'accept'
# set firewall state-policy established log 'enable'
# set firewall state-policy invalid action 'reject'
# set firewall syn-cookies 'enable'
# set firewall twa-hazards-protection 'enable'
#
#
# Using gathered
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep firewall
# set firewall all-ping 'enable'
# set firewall broadcast-ping 'enable'
# set firewall config-trap 'enable'
# set firewall group address-group ENG-HOSTS address '192.0.3.1'
# set firewall group address-group ENG-HOSTS address '192.0.3.2'
# set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'
# set firewall group address-group SALES-HOSTS address '192.0.2.1'
# set firewall group address-group SALES-HOSTS address '192.0.2.2'
# set firewall group address-group SALES-HOSTS address '192.0.2.3'
# set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'
# set firewall group network-group MGMT description 'This group has the Management network addresses'
# set firewall group network-group MGMT network '192.0.1.0/24'
# set firewall ip-src-route 'enable'
# set firewall log-martians 'enable'
# set firewall receive-redirects 'disable'
# set firewall send-redirects 'enable'
# set firewall source-validation 'strict'
# set firewall state-policy established action 'accept'
# set firewall state-policy established log 'enable'
# set firewall state-policy invalid action 'reject'
# set firewall syn-cookies 'enable'
# set firewall twa-hazards-protection 'enable'
#
- name: Gather firewall global config with provided configurations
  vyos.vyos.vyos_firewall_global:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
# {
#        "config_trap": true,
#        "group": {
#            "address_group": [
#                {
#                    "description": "Sales office hosts address list",
#                    "members": [
#                        {
#                            "address": "192.0.3.1"
#                        },
#                        {
#                            "address": "192.0.3.2"
#                        }
#                    ],
#                    "name": "ENG-HOSTS"
#                },
#                {
#                    "description": "Sales office hosts address list",
#                    "members": [
#                        {
#                            "address": "192.0.2.1"
#                        },
#                        {
#                            "address": "192.0.2.2"
#                        },
#                        {
#                            "address": "192.0.2.3"
#                        }
#                    ],
#                    "name": "SALES-HOSTS"
#                }
#            ],
#            "network_group": [
#                {
#                    "description": "This group has the Management network addresses",
#                    "members": [
#                        {
#                            "address": "192.0.1.0/24"
#                        }
#                    ],
#                    "name": "MGMT"
#                }
#            ]
#        },
#        "log_martians": true,
#        "ping": {
#            "all": true,
#            "broadcast": true
#        },
#        "route_redirects": [
#            {
#                "afi": "ipv4",
#                "icmp_redirects": {
#                    "receive": false,
#                    "send": true
#                },
#                "ip_src_route": true
#            }
#        ],
#        "state_policy": [
#            {
#                "action": "accept",
#                "connection_type": "established",
#                "log": true
#            },
#            {
#                "action": "reject",
#                "connection_type": "invalid"
#            }
#        ],
#        "syn_cookies": true,
#        "twa_hazards_protection": true,
#        "validation": "strict"
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep firewall
# set firewall all-ping 'enable'
# set firewall broadcast-ping 'enable'
# set firewall config-trap 'enable'
# set firewall group address-group ENG-HOSTS address '192.0.3.1'
# set firewall group address-group ENG-HOSTS address '192.0.3.2'
# set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'
# set firewall group address-group SALES-HOSTS address '192.0.2.1'
# set firewall group address-group SALES-HOSTS address '192.0.2.2'
# set firewall group address-group SALES-HOSTS address '192.0.2.3'
# set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'
# set firewall group network-group MGMT description 'This group has the Management network addresses'
# set firewall group network-group MGMT network '192.0.1.0/24'
# set firewall ip-src-route 'enable'
# set firewall log-martians 'enable'
# set firewall receive-redirects 'disable'
# set firewall send-redirects 'enable'
# set firewall source-validation 'strict'
# set firewall state-policy established action 'accept'
# set firewall state-policy established log 'enable'
# set firewall state-policy invalid action 'reject'
# set firewall syn-cookies 'enable'
# set firewall twa-hazards-protection 'enable'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_firewall_global:
    config:
      validation: strict
      config_trap: true
      log_martians: true
      syn_cookies: true
      twa_hazards_protection: true
      ping:
      all: true
      broadcast: true
      state_policy:
      - connection_type: established
        action: accept
        log: true
      - connection_type: invalid
        action: reject
      route_redirects:
      - afi: ipv4
        ip_src_route: true
        icmp_redirects:
        send: true
        receive: false
      group:
        address_group:
        - name: SALES-HOSTS
          description: Sales office hosts address list
          members:
          - address: 192.0.2.1
          - address: 192.0.2.2
          - address: 192.0.2.3
        - name: ENG-HOSTS
          description: Sales office hosts address list
          members:
          - address: 192.0.3.1
          - address: 192.0.3.2
        network_group:
        - name: MGMT
          description: This group has the Management network addresses
          members:
          - address: 192.0.1.0/24
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        "set firewall group address-group SALES-HOSTS address 192.0.2.1",
#        "set firewall group address-group SALES-HOSTS address 192.0.2.2",
#        "set firewall group address-group SALES-HOSTS address 192.0.2.3",
#        "set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'",
#        "set firewall group address-group SALES-HOSTS",
#        "set firewall group address-group ENG-HOSTS address 192.0.3.1",
#        "set firewall group address-group ENG-HOSTS address 192.0.3.2",
#        "set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'",
#        "set firewall group address-group ENG-HOSTS",
#        "set firewall group network-group MGMT network 192.0.1.0/24",
#        "set firewall group network-group MGMT description 'This group has the Management network addresses'",
#        "set firewall group network-group MGMT",
#        "set firewall ip-src-route 'enable'",
#        "set firewall receive-redirects 'disable'",
#        "set firewall send-redirects 'enable'",
#        "set firewall config-trap 'enable'",
#        "set firewall state-policy established action 'accept'",
#        "set firewall state-policy established log 'enable'",
#        "set firewall state-policy invalid action 'reject'",
#        "set firewall broadcast-ping 'enable'",
#        "set firewall all-ping 'enable'",
#        "set firewall log-martians 'enable'",
#        "set firewall twa-hazards-protection 'enable'",
#        "set firewall syn-cookies 'enable'",
#        "set firewall source-validation 'strict'"
#    ]
#
#
```

## [Return Values](vyos_firewall_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["set firewall group address-group ENG-HOSTS", "set firewall group address-group ENG-HOSTS address 192.0.3.1"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
