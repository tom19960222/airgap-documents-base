---
collection: ansible
version: "6"
title: "community.network.exos_l2_interfaces module – Manage L2 interfaces on Extreme Networks EXOS devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/exos_l2_interfaces_module.html
fetched_at: 2026-07-27T17:18:33+00:00
---
# community.network.exos_l2_interfaces module – Manage L2 interfaces on Extreme Networks EXOS devices.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.exos_l2_interfaces`.

New in community.network 0.2.0

- [Synopsis](exos_l2_interfaces_module.md#synopsis)
- [Parameters](exos_l2_interfaces_module.md#parameters)
- [Notes](exos_l2_interfaces_module.md#notes)
- [Examples](exos_l2_interfaces_module.md#examples)
- [Return Values](exos_l2_interfaces_module.md#return-values)

## [Synopsis](exos_l2_interfaces_module.md#id1)

- This module provides declarative management of L2 interfaces on Extreme Networks EXOS network devices.

## [Parameters](exos_l2_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of L2 interfaces options |
| **access**  dictionary | Switchport mode access command to configure the interface as a layer 2 access. |
| **vlan**  integer | Configure given VLAN in access port. It’s used as the access VLAN ID. |
| **name**  string / required | Name of the interface |
| **trunk**  dictionary | Switchport mode trunk command to configure the interface as a Layer 2 trunk. |
| **native_vlan**  integer | Native VLAN to be configured in trunk port. It’s used as the trunk native VLAN ID. |
| **trunk_allowed_vlans**  list / elements=string | List of allowed VLANs in a given trunk port. These are the only VLANs that will be configured on the trunk. |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Notes](exos_l2_interfaces_module.md#id3)

> **Note:**
>
> - Tested against EXOS 30.2.1.8
> - This module works with connection `httpapi`. See [EXOS Platform Options](user_guide/platform_exos.md)

## [Examples](exos_l2_interfaces_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 10
#             }
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "native-vlan": 1,
#               "trunk-vlans": [
#                 10
#               ]
#             }
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "native-vlan": 10,
#               "trunk-vlans": [
#                 20,
#                 30
#               ]
#             }
#           }
#         }
#       }
#     ]
#   }
# }

- name: Delete L2 interface configuration for the given arguments
  community.network.exos_l2_interfaces:
    config:
      - name: '3'
    state: deleted

# Module Execution Results:
# -------------------------
#
# "before": [
#     {
#         "access": {
#             "vlan": 10
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": null,
#         "name": "2",
#         "trunk": {
#             "native_vlan": 1,
#             "trunk_allowed_vlans": [
#                 10
#             ]
#         }
#     },
#     {
#         "access": null,
#         "name": "3",
#         "trunk": {
#             "native_vlan": 10,
#             "trunk_allowed_vlans": [
#                 20,
#                 30
#             ]
#         }
#     }
# ],
#
# "requests": [
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "access-vlan": 1,
#            "interface-mode": "ACCESS"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=3/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     }
# ],
#
# "after": [
#     {
#         "access": {
#             "vlan": 10
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": null,
#         "name": "2",
#         "trunk": {
#             "native_vlan": 1,
#             "trunk_allowed_vlans": [
#                 10
#             ]
#         }
#     },
#     {
#         "access": {
#             "vlan": 1
#         },
#         "name": "3",
#         "trunk": null
#     }
# ]
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 10
#             }
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "native-vlan": 1,
#               "trunk-vlans": [
#                 10
#               ]
#             }
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 1
#             }
#           }
#         }
#       }
#     ]
#   }
# }

# Using deleted without any config passed
#"(NOTE: This will delete all of configured resource module attributes from each configured interface)"

# Before state:
# -------------
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 10
#             }
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "native-vlan": 1,
#               "trunk-vlans": [
#                 10
#               ]
#             }
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "native-vlan": 10,
#               "trunk-vlans": [
#                 20,
#                 30
#               ]
#             }
#           }
#         }
#       }
#     ]
#   }
# }

- name: Delete L2 interface configuration for the given arguments
  community.network.exos_l2_interfaces:
    state: deleted

# Module Execution Results:
# -------------------------
#
# "before": [
#     {
#         "access": {
#             "vlan": 10
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": null,
#         "name": "2",
#         "trunk": {
#             "native_vlan": 1,
#             "trunk_allowed_vlans": [
#                 10
#             ]
#         }
#     },
#     {
#         "access": null,
#         "name": "3",
#         "trunk": {
#             "native_vlan": 10,
#             "trunk_allowed_vlans": [
#                 20,
#                 30
#             ]
#         }
#     }
# ],
#
# "requests": [
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "access-vlan": 1,
#            "interface-mode": "ACCESS"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=1/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     },
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "access-vlan": 1,
#            "interface-mode": "ACCESS"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=2/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     },
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "access-vlan": 1,
#            "interface-mode": "ACCESS"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=3/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     }
# ],
#
# "after": [
#     {
#         "access": {
#             "vlan": 1
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": {
#             "vlan": 1
#         },
#         "name": "2",
#         "trunk": null
#     },
#     {
#         "access": {
#             "vlan": 1
#         },
#         "name": "3",
#         "trunk": null
#     }
# ]
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 1
#             }
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 1
#             }
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 1
#             }
#           }
#         }
#       }
#     ]
#   }
# }

# Using merged

# Before state:
# -------------
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#     "openconfig-if-ethernet:ethernet": {
#       "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 1
#             },
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 1
#             },
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 1
#             },
#           }
#         }
#       },
#     ]
#   }
# }

- name: Merge provided configuration with device configuration
  community.network.exos_l2_interfaces:
    config:
      - access:
          vlan: 10
        name: '1'
      - name: '2'
        trunk:
          trunk_allowed_vlans: 10
      - name: '3'
        trunk:
          native_vlan: 10
          trunk_allowed_vlans: 20
    state: merged

# Module Execution Results:
# -------------------------
#
# "before": [
#     {
#         "access": {
#             "vlan": 1
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": {
#             "vlan": 1
#         },
#         "name": "2",
#         "trunk": null
#     },
#     {
#         "access": {
#             "vlan": 1
#         },
#         "name": "3",
#         "trunk": null
#     }
# ],
#
# "requests": [
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "access-vlan": 10,
#            "interface-mode": "ACCESS"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=1/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     },
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "trunk-vlans": [10],
#            "interface-mode": "TRUNK"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=2/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     },
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "native-vlan": 10,
#        "trunk-vlans": [20],
#            "interface-mode": "TRUNK"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=3/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     }
# ],
#
# "after": [
#     {
#         "access": {
#             "vlan": 10
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": null,
#         "name": "2",
#         "trunk": {
#             "native_vlan": 1,
#             "trunk_allowed_vlans": [
#                 10
#             ]
#         }
#     },
#     {
#         "access": null,
#         "name": "3",
#         "trunk": {
#             "native_vlan": 10,
#             "trunk_allowed_vlans": [
#                 20
#             ]
#         }
#     }
# ]
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#     "openconfig-if-ethernet:ethernet": {
#       "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 10
#             }
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#           "native-vlan": 1,
#               "trunk-vlans": [
#                 10
#               ]
#             }
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#           "native-vlan": 10,
#               "trunk-vlans": [
#             20
#               ]
#             }
#           }
#         }
#       },
#     ]
#   }
# }

# Using overridden

# Before state:
# -------------
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 10
#             }
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "native-vlan": 1,
#               "trunk-vlans": [
#                 10
#               ]
#             }
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "native-vlan": 10,
#               "trunk-vlans": [
#                 20,
#             30
#               ]
#             }
#           }
#         }
#       }
#     ]
#   }
# }

- name: Overrride device configuration of all L2 interfaces with provided configuration
  community.network.exos_l2_interfaces:
    config:
      - access:
          vlan: 10
        name: '2'
    state: overridden

# Module Execution Results:
# -------------------------
#
# "before": [
#     {
#         "access": {
#             "vlan": 10
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": null,
#         "name": "2",
#         "trunk": {
#             "native_vlan": 1,
#             "trunk_allowed_vlans": [
#                 10
#             ]
#         }
#     },
#     {
#         "access": null,
#         "name": "3",
#         "trunk": {
#             "native_vlan": 10,
#             "trunk_allowed_vlans": [
#                 20,
#                 30
#             ]
#         }
#     }
# ],
#
# "requests": [
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "access-vlan": 1,
#            "interface-mode": "ACCESS"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=1/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     },
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "access-vlan": 10,
#            "interface-mode": "ACCESS"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=2/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     }
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "access-vlan": 1,
#            "interface-mode": "ACCESS"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=3/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     }
# ],
#
# "after": [
#     {
#         "access": {
#             "vlan": 1
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": {
#             "vlan": 10
#         },
#         "name": "2",
#         "trunk": null
#     },
#     {
#         "access": {
#             "vlan": 1
#         },
#         "name": "3",
#         "trunk": null
#     }
# ]
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 1
#             }
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 10
#             }
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 1
#             }
#           }
#         }
#       }
#     ]
#   }
# }

# Using replaced

# Before state:
# -------------
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 10
#             }
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 20
#             }
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "native-vlan": 1,
#           "trunk-vlans": [
#             10
#           ]
#             }
#           }
#         }
#       }
#     ]
#   }
# }

- name: Replace device configuration of listed L2 interfaces with provided configuration
  community.network.exos_l2_interfaces:
    config:
      - access:
          vlan: 20
        name: '1'
      - name: '2'
        trunk:
          trunk_allowed_vlans: 10
      - name: '3'
        trunk:
          native_vlan: 10
          trunk_allowed_vlan: 20,30
    state: replaced

# Module Execution Results:
# -------------------------
#
# "before": [
#     {
#         "access": {
#             "vlan": 10
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": {
#             "vlan": 20
#         },
#         "name": "2",
#         "trunk": null
#     },
#     {
#         "access": null,
#         "name": "3",
#         "trunk": {
#             "native_vlan": 1,
#             "trunk_allowed_vlans": [
#                 10
#             ]
#         }
#     }
# ],
#
# "requests": [
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "access-vlan": 20,
#            "interface-mode": "ACCESS"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=1/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     },
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "trunk-vlans": [10],
#            "interface-mode": "TRUNK"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=2/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     },
#     {
#        "data": {
#          "openconfig-vlan:config": {
#            "native-vlan": 10,
#            "trunk-vlans": [20, 30]
#            "interface-mode": "TRUNK"
#          }
#        }
#        "method": "PATCH",
#        "path": "rest/restconf/data/openconfig-interfaces:interfaces/interface=3/openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
#     }
# ],
#
# "after": [
#     {
#         "access": {
#             "vlan": 20
#         },
#         "name": "1",
#         "trunk": null
#     },
#     {
#         "access": null,
#         "name": "2",
#         "trunk": {
#             "native_vlan": null,
#             "trunk_allowed_vlans": [
#                 10
#             ]
#         }
#     },
#     {
#         "access": null,
#         "name": "3",
#         "trunk": {
#             "native_vlan": 10,
#             "trunk_allowed_vlans": [
#                 20,
#                 30
#             ]
#         }
#     }
# ]
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-interfaces:interfaces/
# method: GET
# data:
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "1",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "ACCESS",
#               "access-vlan": 20
#             }
#           }
#         }
#       },
#       {
#         "name": "2",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "trunk-vlans": [
#             10
#           ]
#             }
#           }
#         }
#       },
#       {
#         "name": "3",
#         "openconfig-if-ethernet:ethernet": {
#           "openconfig-vlan:switched-vlan": {
#             "config": {
#               "interface-mode": "TRUNK",
#               "native-vlan": 10,
#               "trunk-vlans": [
#             20,
#             30
#           ]
#             }
#           }
#         }
#       }
#     ]
#   }
# }
```

## [Return Values](exos_l2_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **requests**  list / elements=string | The set of requests pushed to the remote device.  Returned: always  Sample: `[{"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}]` |

### Authors

- Jayalakshmi Viswanathan (@jayalakshmiV)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
