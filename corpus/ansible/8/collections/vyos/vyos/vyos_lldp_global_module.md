---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_lldp_global module – LLDP global resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_lldp_global_module.html
fetched_at: 2026-07-28T02:59:16+00:00
---
# vyos.vyos.vyos_lldp_global module – LLDP global resource module

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
> To use it in a playbook, specify: `vyos.vyos.vyos_lldp_global`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_lldp_global_module.md#synopsis)
- [Parameters](vyos_lldp_global_module.md#parameters)
- [Notes](vyos_lldp_global_module.md#notes)
- [Examples](vyos_lldp_global_module.md#examples)
- [Return Values](vyos_lldp_global_module.md#return-values)

## [Synopsis](vyos_lldp_global_module.md#id1)

- This module manages link layer discovery protocol (LLDP) attributes on VyOS devices.

Aliases: lldp_global

## [Parameters](vyos_lldp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | The provided link layer discovery protocol (LLDP) configuration. |
| **address**  string | This argument defines management-address. |
| **enable**  boolean | This argument is a boolean value to enable or disable LLDP.  **Choices:**   - `false` - `true` |
| **legacy_protocols**  list / elements=string | List of the supported legacy protocols.  **Choices:**   - `"cdp"` - `"edp"` - `"fdp"` - `"sonmp"` |
| **snmp**  string | This argument enable the SNMP queries to LLDP database. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VyOS device by executing the command **show configuration commands | grep lldp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](vyos_lldp_global_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).

## [Examples](vyos_lldp_global_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands|grep lldp
#
- name: Merge provided configuration with device configuration
  vyos.vyos.vyos_lldp_global:
    config:
      legacy_protocols:
      - fdp
      - cdp
      snmp: enable
      address: 192.0.2.11
    state: merged
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
# "before": []
#
# "commands": [
#        "set service lldp legacy-protocols fdp",
#        "set service lldp legacy-protocols cdp",
#        "set service lldp snmp enable",
#        "set service lldp management-address '192.0.2.11'"
#    ]
#
# "after": [
#        {
#            "snmp": "enable"
#        },
#        {
#            "address": "192.0.2.11"
#        },
#        {
#            "legacy_protocols": [
#                "cdp",
#                "fdp"
#            ]
#        }
#        {
#            "enable": true
#        }
#    ]
#
# After state:
# -------------
#
# set service lldp legacy-protocols cdp
# set service lldp legacy-protocols fdp
# set service lldp management-address '192.0.2.11'
# set service lldp snmp enable

# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp legacy-protocols cdp
# set service lldp legacy-protocols fdp
# set service lldp management-address '192.0.2.11'
# set service lldp snmp enable
#
- name: Replace device configurations with provided configurations
  vyos.vyos.vyos_lldp_global:
    config:
      legacy_protocols:
      - edp
      - sonmp
      - cdp
      address: 192.0.2.14
    state: replaced
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#
# "before": [
#        {
#            "snmp": "enable"
#        },
#        {
#            "address": "192.0.2.11"
#        },
#        {
#            "legacy_protocols": [
#                "cdp",
#                "fdp"
#            ]
#        }
#        {
#            "enable": true
#        }
#    ]
# "commands": [
#        "delete service lldp snmp",
#        "delete service lldp legacy-protocols fdp",
#        "set service lldp management-address '192.0.2.14'",
#        "set service lldp legacy-protocols edp",
#        "set service lldp legacy-protocols sonmp"
#    ]
#
# "after": [
#        {
#            "address": "192.0.2.14"
#        },
#        {
#            "legacy_protocols": [
#                "cdp",
#                "edp",
#                "sonmp"
#            ]
#        }
#        {
#            "enable": true
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands|grep lldp
# set service lldp legacy-protocols cdp
# set service lldp legacy-protocols edp
# set service lldp legacy-protocols sonmp
# set service lldp management-address '192.0.2.14'

# Using deleted
#
# Before state
# -------------
# vyos@vyos:~$ show configuration commands|grep lldp
# set service lldp legacy-protocols cdp
# set service lldp legacy-protocols edp
# set service lldp legacy-protocols sonmp
# set service lldp management-address '192.0.2.14'
#
- name: Delete attributes of given lldp service (This won't delete the LLDP service
    itself)
  vyos.vyos.vyos_lldp_global:
    config:
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
# "before": [
#        {
#            "address": "192.0.2.14"
#        },
#        {
#            "legacy_protocols": [
#                "cdp",
#                "edp",
#                "sonmp"
#            ]
#        }
#        {
#            "enable": true
#        }
#    ]
#
#  "commands": [
#       "delete service lldp management-address",
#        "delete service lldp legacy-protocols"
#    ]
#
# "after": [
#        {
#            "enable": true
#        }
#          ]
#
# After state
# ------------
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp

# Using gathered
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep lldp
# set service lldp legacy-protocols 'cdp'
# set service lldp management-address '192.0.2.17'
#
- name: Gather lldp global config with provided configurations
  vyos.vyos.vyos_lldp_global:
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
# vyos@192# run show configuration commands | grep lldp
# set service lldp legacy-protocols 'cdp'
# set service lldp management-address '192.0.2.17'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_lldp_global:
    config:
      address: 192.0.2.17
      enable: true
      legacy_protocols:
      - cdp
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#         "set service lldp legacy-protocols 'cdp'",
#         "set service lldp",
#         "set service lldp management-address '192.0.2.17'"
#     ]
#

# Using parsed
#
#
- name: Parse the provided commands to provide structured configuration
  vyos.vyos.vyos_lldp_global:
    running_config:
      "set service lldp legacy-protocols 'cdp'
       set service lldp legacy-protocols 'fdp'
       set service lldp management-address '192.0.2.11'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": {
#         "address": "192.0.2.11",
#         "enable": true,
#         "legacy_protocols": [
#             "cdp",
#             "fdp"
#         ]
#     }
#
```

## [Return Values](vyos_lldp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["set service lldp legacy-protocols sonmp", "set service lldp management-address '192.0.2.14'"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
