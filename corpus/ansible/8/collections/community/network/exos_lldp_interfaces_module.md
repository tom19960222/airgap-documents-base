---
collection: ansible
version: "8"
title: "community.network.exos_lldp_interfaces module – Manage link layer discovery protocol (LLDP) attributes of interfaces on EXOS platforms."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/exos_lldp_interfaces_module.html
fetched_at: 2026-07-28T01:56:38+00:00
---
# community.network.exos_lldp_interfaces module – Manage link layer discovery protocol (LLDP) attributes of interfaces on EXOS platforms.

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
> To use it in a playbook, specify: `community.network.exos_lldp_interfaces`.

New in community.network 0.2.0

- [Synopsis](exos_lldp_interfaces_module.md#synopsis)
- [Parameters](exos_lldp_interfaces_module.md#parameters)
- [Examples](exos_lldp_interfaces_module.md#examples)
- [Return Values](exos_lldp_interfaces_module.md#return-values)

## [Synopsis](exos_lldp_interfaces_module.md#id1)

- This module manages link layer discovery protocol (LLDP) attributes of interfaces on Extreme Networks EXOS platforms.

Aliases: network.exos.exos_lldp_interfaces

## [Parameters](exos_lldp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | The list of link layer discovery protocol interface attribute configurations |
| **enabled**  boolean | This is a boolean value to control disabling of LLDP on the interface `name`  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the interface LLDP needs to be configured on. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Examples](exos_lldp_interfaces_module.md#id3)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }

- name: Merge provided configuration with device configuration
  community.network.exos_lldp_interfaces:
    config:
      - name: '2'
        enabled: false
      - name: '5'
        enabled: true
    state: merged

# Module Execution Results:
# -------------------------
#
# "before":
#    - name: '1'
#      enabled: true
#    - name: '2'
#      enabled: true
#    - name: '3'
#      enabled: false
#    - name: '4'
#      enabled: true
#    - name: '5'
#      enabled: false
#
# "requests": [
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": false,
#             "name": "2"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=2/config"
#     },
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "5"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=5/config"
#     }
# ]
#
# "after":
#    - name: '1'
#      enabled: true
#    - name: '2'
#      enabled: false
#    - name: '3'
#      enabled: false
#    - name: '4'
#      enabled: true
#    - name: '5'
#      enabled: true

# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }

# Using replaced

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }

- name: Replaces device configuration of listed lldp_interfaces with provided configuration
  community.network.exos_lldp_interfaces:
    config:
      - name: '1'
        enabled: false
      - name: '3'
        enabled: true
    state: merged

# Module Execution Results:
# -------------------------
#
# "before":
#    - name: '1'
#      enabled: true
#    - name: '2'
#      enabled: true
#    - name: '3'
#      enabled: false
#    - name: '4'
#      enabled: true
#    - name: '5'
#      enabled: false
#
# "requests": [
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": false,
#             "name": "1"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=1/config"
#     },
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "3"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=3/config"
#     }
# ]
#
# "after":
#    - name: '1'
#      enabled: false
#    - name: '2'
#      enabled: true
#    - name: '3'
#      enabled: true
#    - name: '4'
#      enabled: true
#    - name: '5'
#      enabled: false

# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": false,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }

# Using deleted

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": false,
#           "name": "1"
#         },
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "2"
#         },
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         },
#       }
#     ]
#   }
# }

- name: Delete lldp interface configuration (this will not delete other lldp configuration)
  community.network.exos_lldp_interfaces:
    config:
      - name: '1'
      - name: '3'
    state: deleted

# Module Execution Results:
# -------------------------
#
# "before":
#    - name: '1'
#      enabled: false
#    - name: '2'
#      enabled: false
#    - name: '3'
#      enabled: false
#
# "requests": [
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "1"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=1/config"
#     },
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "3"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=3/config"
#     }
# ]
#
# "after":
#    - name: '1'
#      enabled: true
#    - name: '2'
#      enabled: false
#    - name: '3'
#      enabled: true
#
#  After state:
# -------------
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         },
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "2"
#         },
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "3"
#         },
#       }
#     ]
#   }
# }

# Using overridden

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }

- name: Override device configuration of all lldp_interfaces with provided configuration
  community.network.exos_lldp_interfaces:
    config:
      - name: '3'
        enabled: true
    state: overridden

# Module Execution Results:
# -------------------------
#
# "before":
#    - name: '1'
#      enabled: true
#    - name: '2'
#      enabled: true
#    - name: '3'
#      enabled: false
#    - name: '4'
#      enabled: true
#    - name: '5'
#      enabled: false
#
# "requests": [
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "5"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=5/config"
#     },
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "3"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=3/config"
#     }
# ]
#
# "after":
#    - name: '1'
#      enabled: true
#    - name: '2'
#      enabled: true
#    - name: '3'
#      enabled: true
#    - name: '4'
#      enabled: true
#    - name: '5'
#      enabled: true

# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }
```

## [Return Values](exos_lldp_interfaces_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **requests**  list / elements=string | The set of requests pushed to the remote device.  **Returned:** always  **Sample:** `[{"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}]` |

### Authors

- Jayalakshmi Viswanathan (@JayalakshmiV)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
