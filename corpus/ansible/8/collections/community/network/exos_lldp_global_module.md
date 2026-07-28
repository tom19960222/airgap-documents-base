---
collection: ansible
version: "8"
title: "community.network.exos_lldp_global module – Configure and manage Link Layer Discovery Protocol(LLDP) attributes on EXOS platforms."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/exos_lldp_global_module.html
fetched_at: 2026-07-28T01:56:37+00:00
---
# community.network.exos_lldp_global module – Configure and manage Link Layer Discovery Protocol(LLDP) attributes on EXOS platforms.

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
> To use it in a playbook, specify: `community.network.exos_lldp_global`.

- [Synopsis](exos_lldp_global_module.md#synopsis)
- [Parameters](exos_lldp_global_module.md#parameters)
- [Notes](exos_lldp_global_module.md#notes)
- [Examples](exos_lldp_global_module.md#examples)
- [Return Values](exos_lldp_global_module.md#return-values)

## [Synopsis](exos_lldp_global_module.md#id1)

- This module configures and manages the Link Layer Discovery Protocol(LLDP) attributes on Extreme Networks EXOS platforms.

Aliases: network.exos.exos_lldp_global

## [Parameters](exos_lldp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of LLDP options |
| **interval**  integer | Frequency at which LLDP advertisements are sent (in seconds). By default - 30 seconds.  **Default:** `30` |
| **tlv_select**  dictionary | This attribute can be used to specify the TLVs that need to be sent in the LLDP packets. By default, only system name and system description is sent |
| **management_address**  boolean | Used to specify the management address in TLV messages  **Choices:**   - `false` - `true` |
| **port_description**  boolean | Used to specify the port description TLV  **Choices:**   - `false` - `true` |
| **system_capabilities**  boolean | Used to specify the system capabilities TLV  **Choices:**   - `false` - `true` |
| **system_description**  boolean | Used to specify the system description TLV  **Choices:**   - `false` - `true` ← (default) |
| **system_name**  boolean | Used to specify the system name TLV  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` |

## [Notes](exos_lldp_global_module.md#id3)

> **Note:**
>
> - Tested against Extreme Networks EXOS version 30.2.1.8 on x460g2.
> - This module works with connection `httpapi`. See [EXOS Platform Options](user_guide/platform_exos.md)

## [Examples](exos_lldp_global_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# path: /rest/restconf/data/openconfig_lldp:lldp/config
# method: GET
# data:
# {
#   "openconfig_lldp:config": {
#     "enabled": true,
#     "hello-timer": 30,
#     "suppress-tlv-advertisement": [
#       "PORT_DESCRIPTION",
#       "SYSTEM_CAPABILITIES",
#       "MANAGEMENT_ADDRESS"
#     ],
#     "system-description": "ExtremeXOS (X460G2-24t-10G4) version 30.2.1.8"
#     "system-name": "X460G2-24t-10G4"
#   }
# }

- name: Merge provided LLDP configuration with device configuration
  community.network.exos_lldp_global:
    config:
      interval: 10000
      tlv_select:
        system_capabilities: true
    state: merged

# Module Execution Results:
# -------------------------
#
# "before": [
#   {
#     "interval": 30,
#     "tlv_select": {
#       "system_name": true,
#       "system_description": true
#       "port_description": false,
#       "management_address": false,
#       "system_capabilities": false
#     }
#   }
# ]
#
# "requests": [
#     {
#        "data": {
#           "openconfig_lldp:config": {
#             "hello-timer": 10000,
#             "suppress-tlv-advertisement": [
#               "PORT_DESCRIPTION",
#               "MANAGEMENT_ADDRESS"
#             ]
#           }
#         },
#        "method": "PATCH",
#        "path": "/rest/restconf/data/openconfig_lldp:lldp/config"
#     }
# ]
#
# "after": [
#   {
#     "interval": 10000,
#     "tlv_select": {
#       "system_name": true,
#       "system_description": true,
#       "port_description": false,
#       "management_address": false,
#       "system_capabilities": true
#     }
#   }
# ]

# After state:
# -------------
# path: /rest/restconf/data/openconfig_lldp:lldp/config
# method: GET
# data:
# {
#   "openconfig_lldp:config": {
#     "enabled": true,
#     "hello-timer": 10000,
#     "suppress-tlv-advertisement": [
#       "PORT_DESCRIPTION",
#       "MANAGEMENT_ADDRESS"
#     ],
#     "system-description": "ExtremeXOS (X460G2-24t-10G4) version 30.2.1.8"
#     "system-name": "X460G2-24t-10G4"
#   }
# }

# Using replaced

# Before state:
# -------------
# path: /rest/restconf/data/openconfig_lldp:lldp/config
# method: GET
# data:
# {
#   "openconfig_lldp:config": {
#     "enabled": true,
#     "hello-timer": 30,
#     "suppress-tlv-advertisement": [
#       "PORT_DESCRIPTION",
#       "SYSTEM_CAPABILITIES",
#       "MANAGEMENT_ADDRESS"
#     ],
#     "system-description": "ExtremeXOS (X460G2-24t-10G4) version 30.2.1.8"
#     "system-name": "X460G2-24t-10G4"
#   }
# }

- name: Replace device configuration with provided LLDP configuration
  community.network.exos_lldp_global:
    config:
      interval: 10000
      tlv_select:
        system_capabilities: true
    state: replaced

# Module Execution Results:
# -------------------------
#
# "before": [
#   {
#     "interval": 30,
#     "tlv_select": {
#       "system_name": true,
#       "system_description": true
#       "port_description": false,
#       "management_address": false,
#       "system_capabilities": false
#     }
#   }
# ]
#
# "requests": [
#     {
#        "data": {
#           "openconfig_lldp:config": {
#             "hello-timer": 10000,
#             "suppress-tlv-advertisement": [
#               "SYSTEM_NAME",
#               "SYSTEM_DESCRIPTION",
#               "PORT_DESCRIPTION",
#               "MANAGEMENT_ADDRESS"
#             ]
#           }
#         },
#        "method": "PATCH",
#        "path": "/rest/restconf/data/openconfig_lldp:lldp/config"
#     }
# ]
#
# "after": [
#   {
#     "interval": 10000,
#     "tlv_select": {
#       "system_name": false,
#       "system_description": false,
#       "port_description": false,
#       "management_address": false,
#       "system_capabilities": true
#     }
#   }
# ]

# After state:
# -------------
# path: /rest/restconf/data/openconfig_lldp:lldp/config
# method: GET
# data:
# {
#   "openconfig_lldp:config": {
#     "enabled": true,
#     "hello-timer": 10000,
#     "suppress-tlv-advertisement": [
#       "SYSTEM_NAME",
#       "SYSTEM_DESCRIPTION",
#       "PORT_DESCRIPTION",
#       "MANAGEMENT_ADDRESS"
#     ],
#     "system-description": "ExtremeXOS (X460G2-24t-10G4) version 30.2.1.8"
#     "system-name": "X460G2-24t-10G4"
#   }
# }

# Using deleted

# Before state:
# -------------
# path: /rest/restconf/data/openconfig_lldp:lldp/config
# method: GET
# data:
# {
#   "openconfig_lldp:config": {
#     "enabled": true,
#     "hello-timer": 10000,
#     "suppress-tlv-advertisement": [
#       "SYSTEM_CAPABILITIES",
#       "MANAGEMENT_ADDRESS"
#     ],
#     "system-description": "ExtremeXOS (X460G2-24t-10G4) version 30.2.1.8"
#     "system-name": "X460G2-24t-10G4"
#   }
# }

- name: Delete attributes of given LLDP service (This won't delete the LLDP service itself)
  community.network.exos_lldp_global:
    config:
    state: deleted

# Module Execution Results:
# -------------------------
#
# "before": [
#   {
#     "interval": 10000,
#     "tlv_select": {
#       "system_name": true,
#       "system_description": true,
#       "port_description": true,
#       "management_address": false,
#       "system_capabilities": false
#     }
#   }
# ]
#
# "requests": [
#     {
#        "data": {
#           "openconfig_lldp:config": {
#             "hello-timer": 30,
#             "suppress-tlv-advertisement": [
#               "SYSTEM_CAPABILITIES",
#               "PORT_DESCRIPTION",
#               "MANAGEMENT_ADDRESS"
#             ]
#           }
#         },
#        "method": "PATCH",
#        "path": "/rest/restconf/data/openconfig_lldp:lldp/config"
#     }
# ]
#
# "after": [
#   {
#     "interval": 30,
#     "tlv_select": {
#       "system_name": true,
#       "system_description": true,
#       "port_description": false,
#       "management_address": false,
#       "system_capabilities": false
#     }
#   }
# ]

# After state:
# -------------
# path: /rest/restconf/data/openconfig_lldp:lldp/config
# method: GET
# data:
# {
#   "openconfig_lldp:config": {
#     "enabled": true,
#     "hello-timer": 30,
#     "suppress-tlv-advertisement": [
#       "SYSTEM_CAPABILITIES",
#       "PORT_DESCRIPTION",
#       "MANAGEMENT_ADDRESS"
#     ],
#     "system-description": "ExtremeXOS (X460G2-24t-10G4) version 30.2.1.8"
#     "system-name": "X460G2-24t-10G4"
#   }
# }
```

## [Return Values](exos_lldp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **requests**  list / elements=string | The set of requests pushed to the remote device.  **Returned:** always  **Sample:** `[{"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}]` |

### Authors

- Ujwal Komarla (@ujwalkomarla)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
