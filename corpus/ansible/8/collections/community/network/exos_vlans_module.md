---
collection: ansible
version: "8"
title: "community.network.exos_vlans module – Manage VLANs on Extreme Networks EXOS devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/exos_vlans_module.html
fetched_at: 2026-07-28T01:56:39+00:00
---
# community.network.exos_vlans module – Manage VLANs on Extreme Networks EXOS devices.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.exos_vlans`.

New in community.network 0.2.0

- [Synopsis](exos_vlans_module.md#synopsis)
- [Parameters](exos_vlans_module.md#parameters)
- [Notes](exos_vlans_module.md#notes)
- [Examples](exos_vlans_module.md#examples)
- [Return Values](exos_vlans_module.md#return-values)

## [Synopsis](exos_vlans_module.md#id1)

- This module provides declarative management of VLANs on Extreme Networks EXOS network devices.

Aliases: network.exos.exos_vlans

## [Parameters](exos_vlans_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of VLANs options |
| **name**  string | Ascii name of the VLAN. |
| **state**  string | Operational state of the VLAN  **Choices:**   - `"active"` ← (default) - `"suspend"` |
| **vlan_id**  integer / required | ID of the VLAN. Range 1-4094 |
| **state**  string | The state the configuration should be left in  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Notes](exos_vlans_module.md#id3)

> **Note:**
>
> - Tested against EXOS 30.2.1.8
> - This module works with connection `httpapi`. See [EXOS Platform Options](user_guide/platform_exos.md)

## [Examples](exos_vlans_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }

- name: Delete attributes of given VLANs
  community.network.exos_vlans:
    config:
      - vlan_id: 10
      - vlan_id: 20
      - vlan_id: 30
    state: deleted

# Module Execution Results:
# -------------------------
#
# "after": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     }
# ],
#
# "before": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "vlan_20",
#         "state": "active",
#         "vlan_id": 20
#     }
#     {
#         "name": "vlan_30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "requests": [
#     {
#        "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=10"
#     },
#     {
#    "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=20"
#     },
#     {
#    "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=30"
#     }
# ]
#
#
#  After state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       }
#     ]
#   }
# }

# Using merged

# Before state:
# -------------
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       }
#     ]
#   }
# }

- name: Merge provided configuration with device configuration
  community.network.exos_vlans:
    config:
      - name: vlan_10
        vlan_id: 10
        state: active
      - name: vlan_20
        vlan_id: 20
        state: active
      - name: vlan_30
        vlan_id: 30
        state: active
    state: merged

# Module Execution Results:
# -------------------------
#
# "after": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "vlan_20",
#         "state": "active",
#         "vlan_id": 20
#     },
#     {
#         "name": "vlan_30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "before": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     }
# ],
#
# "requests": [
#     {
#        "data": {
#          "openconfig-vlan:vlan": [
#            {
#              "config": {
#                "name": "vlan_10",
#                "status": "ACTIVE",
#                "tpid": "oc-vlan-types:TPID_0x8100",
#                "vlan-id": 10
#             }
#            }
#          ]
#        },
#        "method": "POST",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#      },
#      {
#        "data": {
#          "openconfig-vlan:vlan": [
#            {
#              "config": {
#                "name": "vlan_20",
#                "status": "ACTIVE",
#                "tpid": "oc-vlan-types:TPID_0x8100",
#                "vlan-id": 20
#              }
#            }
#          ]
#        },
#        "method": "POST",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#      },
#        "data": {
#          "openconfig-vlan:vlan": [
#            {
#              "config": {
#                "name": "vlan_30",
#                "status": "ACTIVE",
#                "tpid": "oc-vlan-types:TPID_0x8100",
#                "vlan-id": 30
#              }
#            }
#          ]
#        },
#        "method": "POST",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#      }
#    ]
#
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }

# Using overridden

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }

- name: Override device configuration of all VLANs with provided configuration
  community.network.exos_vlans:
    config:
      - name: TEST_VLAN10
        vlan_id: 10
    state: overridden

# Module Execution Results:
# -------------------------
#
# "after": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "TEST_VLAN10",
#         "state": "active",
#         "vlan_id": 10
#     },
# ],
#
# "before": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "vlan_20",
#         "state": "active",
#         "vlan_id": 20
#     },
#     {
#         "name": "vlan_30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "requests": [
#     {
#        "data": {
#          "openconfig-vlan:vlan": {
#        "vlan": [
#              {
#                "config": {
#                  "name": "TEST_VLAN10",
#                  "status": "ACTIVE",
#                  "tpid": "oc-vlan-types:TPID_0x8100",
#                  "vlan-id": 10
#                }
#              }
#            ]
#          }
#        }
#     },
#        "method": "PATCH",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#     },
#     {
#    "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=20"
#     },
#     {
#    "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=30"
#     }
#  ]
#
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "TEST_VLAN10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       }
#     ]
#   }
# }

# Using replaced

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }

- name: Replaces device configuration of listed VLANs with provided configuration
  community.network.exos_vlans:
    config:
      - name: Test_VLAN20
        vlan_id: 20
      - name: Test_VLAN30
        vlan_id: 30
    state: replaced

# Module Execution Results:
# -------------------------
#
# "after": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "TEST_VLAN20",
#         "state": "active",
#         "vlan_id": 20
#     },
#     {
#         "name": "TEST_VLAN30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "before": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "vlan_20",
#         "state": "active",
#         "vlan_id": 20
#     },
#     {
#         "name": "vlan_30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "requests": [
#    {
#       "data": {
#          "openconfig-vlan:vlan": {
#             "vlan": [
#                 {
#                   "config": {
#                      "name": "TEST_VLAN20",
#                      "status": "ACTIVE",
#                      "tpid": "oc-vlan-types:TPID_0x8100",
#                      "vlan-id": 20
#                   }
#                   "config": {
#                      "name": "TEST_VLAN30",
#                      "status": "ACTIVE",
#                      "tpid": "oc-vlan-types:TPID_0x8100",
#                      "vlan-id": 30
#                   }
#                }
#             ]
#          },
#       "method": "PATCH",
#       "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#    }
# ]
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "TEST_VLAN20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "TEST_VLAN30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }
```

## [Return Values](exos_vlans_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **requests**  list / elements=string | The set of requests pushed to the remote device.  **Returned:** always  **Sample:** `[{"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}]` |

### Authors

- Jayalakshmi Viswanathan (@jayalakshmiV)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
