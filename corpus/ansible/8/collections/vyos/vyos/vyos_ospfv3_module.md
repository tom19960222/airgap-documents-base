---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_ospfv3 module – OSPFV3 resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_ospfv3_module.html
fetched_at: 2026-07-28T02:59:22+00:00
---
# vyos.vyos.vyos_ospfv3 module – OSPFV3 resource module

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
> To use it in a playbook, specify: `vyos.vyos.vyos_ospfv3`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_ospfv3_module.md#synopsis)
- [Parameters](vyos_ospfv3_module.md#parameters)
- [Notes](vyos_ospfv3_module.md#notes)
- [Examples](vyos_ospfv3_module.md#examples)
- [Return Values](vyos_ospfv3_module.md#return-values)

## [Synopsis](vyos_ospfv3_module.md#id1)

- This resource module configures and manages attributes of OSPFv3 routes on VyOS network devices.

Aliases: ospfv3

## [Parameters](vyos_ospfv3_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A provided OSPFv3 route configuration. |
| **areas**  list / elements=dictionary | OSPFv3 area. |
| **area_id**  string | OSPFv3 Area name/identity. |
| **export_list**  string | Name of export-list. |
| **import_list**  string | Name of import-list. |
| **range**  list / elements=dictionary | Summarize routes matching prefix (border routers only). |
| **address**  string | border router IPv4 address. |
| **advertise**  boolean | Advertise this range.  **Choices:**   - `false` - `true` |
| **not_advertise**  boolean | Don’t advertise this range.  **Choices:**   - `false` - `true` |
| **parameters**  dictionary | OSPFv3 specific parameters. |
| **router_id**  string | Override the default router identifier. |
| **redistribute**  list / elements=dictionary | Redistribute information from another routing protocol. |
| **route_map**  string | Route map references. |
| **route_type**  string | Route type to redistribute.  **Choices:**   - `"bgp"` - `"connected"` - `"kernel"` - `"ripng"` - `"static"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VyOS device by executing the command **show configuration commands | grep ospfv3**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](vyos_ospfv3_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).

## [Examples](vyos_ospfv3_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos# run show  configuration commands | grep ospfv3
#
#
- name: Merge the provided configuration with the existing running configuration
  vyos.vyos.vyos_ospfv3:
    config:
      redistribute:
      - route_type: bgp
      parameters:
        router_id: 192.0.2.10
      areas:
      - area_id: '2'
        export_list: export1
        import_list: import1
        range:
        - address: 2001:db10::/32
        - address: 2001:db20::/32
        - address: 2001:db30::/32
      - area_id: '3'
        range:
        - address: 2001:db40::/32
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# before": {}
#
#    "commands": [
#       "set protocols ospfv3 redistribute bgp",
#       "set protocols ospfv3 parameters router-id '192.0.2.10'",
#       "set protocols ospfv3 area 2 range 2001:db10::/32",
#       "set protocols ospfv3 area 2 range 2001:db20::/32",
#       "set protocols ospfv3 area 2 range 2001:db30::/32",
#       "set protocols ospfv3 area '2'",
#       "set protocols ospfv3 area 2 export-list export1",
#       "set protocols ospfv3 area 2 import-list import1",
#       "set protocols ospfv3 area '3'",
#       "set protocols ospfv3 area 3 range 2001:db40::/32"
#    ]
#
# "after": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'

# Using replaced
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'
#
- name: Replace ospfv3 routes attributes configuration.
  vyos.vyos.vyos_ospfv3:
    config:
      redistribute:
      - route_type: bgp
      parameters:
        router_id: 192.0.2.10
      areas:
      - area_id: '2'
        export_list: export1
        import_list: import1
        range:
        - address: 2001:db10::/32
        - address: 2001:db30::/32
        - address: 2001:db50::/32
      - area_id: '4'
        range:
        - address: 2001:db60::/32
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# "commands": [
#     "delete protocols ospfv3 area 2 range 2001:db20::/32",
#     "delete protocols ospfv3 area 3",
#     "set protocols ospfv3 area 2 range 2001:db50::/32",
#     "set protocols ospfv3 area '4'",
#     "set protocols ospfv3 area 4 range 2001:db60::/32"
#    ]
#
#    "after": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    },
#                    {
#                        "address": "2001:db50::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "4",
#                "range": [
#                    {
#                        "address": "2001:db60::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 2 range '2001:db50::/32'
# set protocols ospfv3 area 4 range '2001:db60::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_ospfv3:
    config:
      redistribute:
      - route_type: bgp
      parameters:
        router_id: 192.0.2.10
      areas:
      - area_id: '2'
        export_list: export1
        import_list: import1
        range:
        - address: 2001:db10::/32
        - address: 2001:db20::/32
        - address: 2001:db30::/32
      - area_id: '3'
        range:
        - address: 2001:db40::/32
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        [
#       "set protocols ospfv3 redistribute bgp",
#       "set protocols ospfv3 parameters router-id '192.0.2.10'",
#       "set protocols ospfv3 area 2 range 2001:db10::/32",
#       "set protocols ospfv3 area 2 range 2001:db20::/32",
#       "set protocols ospfv3 area 2 range 2001:db30::/32",
#       "set protocols ospfv3 area '2'",
#       "set protocols ospfv3 area 2 export-list export1",
#       "set protocols ospfv3 area 2 import-list import1",
#       "set protocols ospfv3 area '3'",
#       "set protocols ospfv3 area 3 range 2001:db40::/32"
#    ]

# Using parsed
#
#
- name: Parse the commands to provide structured configuration.
  vyos.vyos.vyos_ospfv3:
    running_config:
      "set protocols ospfv3 area 2 export-list 'export1'
       set protocols ospfv3 area 2 import-list 'import1'
       set protocols ospfv3 area 2 range '2001:db10::/32'
       set protocols ospfv3 area 2 range '2001:db20::/32'
       set protocols ospfv3 area 2 range '2001:db30::/32'
       set protocols ospfv3 area 3 range '2001:db40::/32'
       set protocols ospfv3 parameters router-id '192.0.2.10'
       set protocols ospfv3 redistribute 'bgp'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }

# Using gathered
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'
#
- name: Gather ospfv3 routes config with provided configurations
  vyos.vyos.vyos_ospfv3:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'

# Using deleted
#
# Before state
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'
#
- name: Delete attributes of ospfv3 routes.
  vyos.vyos.vyos_ospfv3:
    config:
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
# "commands": [
#        "delete protocols ospfv3"
#    ]
#
# "after": {}
# After state
# ------------
# vyos@192# run show configuration commands | grep ospfv3
```

## [Return Values](vyos_ospfv3_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["set protocols ospf parameters router-id 192.0.1.1", "set protocols ospfv3 area 2 range '2001:db10::/32'"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
