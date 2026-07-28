---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_lldp_interfaces module – LLDP interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_lldp_interfaces_module.html
fetched_at: 2026-07-28T02:59:17+00:00
---
# vyos.vyos.vyos_lldp_interfaces module – LLDP interfaces resource module

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
> To use it in a playbook, specify: `vyos.vyos.vyos_lldp_interfaces`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_lldp_interfaces_module.md#synopsis)
- [Parameters](vyos_lldp_interfaces_module.md#parameters)
- [Notes](vyos_lldp_interfaces_module.md#notes)
- [Examples](vyos_lldp_interfaces_module.md#examples)
- [Return Values](vyos_lldp_interfaces_module.md#return-values)

## [Synopsis](vyos_lldp_interfaces_module.md#id1)

- This module manages attributes of lldp interfaces on VyOS network devices.

Aliases: lldp_interfaces

## [Parameters](vyos_lldp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of lldp interfaces configurations. |
| **enable**  boolean | to disable lldp on the interface.  **Choices:**   - `false` - `true` ← (default) |
| **location**  dictionary | LLDP-MED location data. |
| **civic_based**  dictionary | Civic-based location data. |
| **ca_info**  list / elements=dictionary | LLDP-MED address info |
| **ca_type**  integer | LLDP-MED Civic Address type. |
| **ca_value**  string | LLDP-MED Civic Address value. |
| **country_code**  string / required | Country Code |
| **coordinate_based**  dictionary | Coordinate-based location. |
| **altitude**  integer | Altitude in meters. |
| **datum**  string | Coordinate datum type.  **Choices:**   - `"WGS84"` - `"NAD83"` - `"MLLW"` |
| **latitude**  string / required | Latitude. |
| **longitude**  string / required | Longitude. |
| **elin**  string | Emergency Call Service ELIN number (between 10-25 numbers). |
| **name**  string / required | Name of the lldp interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VyOS device by executing the command **show configuration commands | grep lldp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"parsed"` - `"gathered"` |

## [Notes](vyos_lldp_interfaces_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).

## [Examples](vyos_lldp_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep lldp
#
- name: Merge provided configuration with device configuration
  vyos.vyos.vyos_lldp_interfaces:
    config:
    - name: eth1
      location:
        civic_based:
          country_code: US
          ca_info:
          - ca_type: 0
            ca_value: ENGLISH

    - name: eth2
      location:
        coordinate_based:
          altitude: 2200
          datum: WGS84
          longitude: 222.267255W
          latitude: 33.524449N
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
#        "set service lldp interface eth1 location civic-based country-code 'US'",
#        "set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'",
#        "set service lldp interface eth1",
#        "set service lldp interface eth2 location coordinate-based latitude '33.524449N'",
#        "set service lldp interface eth2 location coordinate-based altitude '2200'",
#        "set service lldp interface eth2 location coordinate-based datum 'WGS84'",
#        "set service lldp interface eth2 location coordinate-based longitude '222.267255W'",
#        "set service lldp interface eth2 location coordinate-based latitude '33.524449N'",
#        "set service lldp interface eth2 location coordinate-based altitude '2200'",
#        "set service lldp interface eth2 location coordinate-based datum 'WGS84'",
#        "set service lldp interface eth2 location coordinate-based longitude '222.267255W'",
#        "set service lldp interface eth2"
#
# "after": [
#        {
#            "location": {
#                "coordinate_based": {
#                    "altitude": 2200,
#                    "datum": "WGS84",
#                    "latitude": "33.524449N",
#                    "longitude": "222.267255W"
#                }
#            },
#            "name": "eth2"
#        },
#        {
#            "location": {
#                "civic_based": {
#                    "ca_info": [
#                        {
#                            "ca_type": 0,
#                            "ca_value": "ENGLISH"
#                        }
#                    ],
#                    "country_code": "US"
#                }
#            },
#            "name": "eth1"
#        }
#    ],
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth1 location civic-based country-code 'US'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'

# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth1 location civic-based country-code 'US'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'
#
- name: Replace device configurations of listed LLDP interfaces with provided configurations
  vyos.vyos.vyos_lldp_interfaces:
    config:
    - name: eth2
      location:
        civic_based:
          country_code: US
          ca_info:
          - ca_type: 0
            ca_value: ENGLISH

    - name: eth1
      location:
        coordinate_based:
          altitude: 2200
          datum: WGS84
          longitude: 222.267255W
          latitude: 33.524449N
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "location": {
#                "coordinate_based": {
#                    "altitude": 2200,
#                    "datum": "WGS84",
#                    "latitude": "33.524449N",
#                    "longitude": "222.267255W"
#                }
#            },
#            "name": "eth2"
#        },
#        {
#            "location": {
#                "civic_based": {
#                    "ca_info": [
#                        {
#                            "ca_type": 0,
#                            "ca_value": "ENGLISH"
#                        }
#                    ],
#                    "country_code": "US"
#                }
#            },
#            "name": "eth1"
#        }
#    ]
#
#    "commands": [
#        "delete service lldp interface eth2 location",
#        "set service lldp interface eth2 'disable'",
#        "set service lldp interface eth2 location civic-based country-code 'US'",
#        "set service lldp interface eth2 location civic-based ca-type 0 ca-value 'ENGLISH'",
#        "delete service lldp interface eth1 location",
#        "set service lldp interface eth1 'disable'",
#        "set service lldp interface eth1 location coordinate-based latitude '33.524449N'",
#        "set service lldp interface eth1 location coordinate-based altitude '2200'",
#        "set service lldp interface eth1 location coordinate-based datum 'WGS84'",
#        "set service lldp interface eth1 location coordinate-based longitude '222.267255W'"
#    ]
#
#    "after": [
#        {
#            "location": {
#                "civic_based": {
#                    "ca_info": [
#                        {
#                            "ca_type": 0,
#                            "ca_value": "ENGLISH"
#                        }
#                    ],
#                    "country_code": "US"
#                }
#            },
#            "name": "eth2"
#        },
#        {
#            "location": {
#                "coordinate_based": {
#                    "altitude": 2200,
#                    "datum": "WGS84",
#                    "latitude": "33.524449N",
#                    "longitude": "222.267255W"
#                }
#            },
#            "name": "eth1"
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 'disable'
# set service lldp interface eth1 location coordinate-based altitude '2200'
# set service lldp interface eth1 location coordinate-based datum 'WGS84'
# set service lldp interface eth1 location coordinate-based latitude '33.524449N'
# set service lldp interface eth1 location coordinate-based longitude '222.267255W'
# set service lldp interface eth2 'disable'
# set service lldp interface eth2 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth2 location civic-based country-code 'US'

# Using overridden
#
# Before state
# --------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 'disable'
# set service lldp interface eth1 location coordinate-based altitude '2200'
# set service lldp interface eth1 location coordinate-based datum 'WGS84'
# set service lldp interface eth1 location coordinate-based latitude '33.524449N'
# set service lldp interface eth1 location coordinate-based longitude '222.267255W'
# set service lldp interface eth2 'disable'
# set service lldp interface eth2 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth2 location civic-based country-code 'US'
#
- name: Overrides all device configuration with provided configuration
  vyos.vyos.vyos_lldp_interfaces:
    config:
    - name: eth2
      location:
        elin: 0000000911

    state: overridden
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# "before": [
#        {
#            "enable": false,
#            "location": {
#                "civic_based": {
#                    "ca_info": [
#                        {
#                            "ca_type": 0,
#                            "ca_value": "ENGLISH"
#                        }
#                    ],
#                    "country_code": "US"
#                }
#            },
#            "name": "eth2"
#        },
#        {
#            "enable": false,
#            "location": {
#                "coordinate_based": {
#                    "altitude": 2200,
#                    "datum": "WGS84",
#                    "latitude": "33.524449N",
#                    "longitude": "222.267255W"
#                }
#            },
#            "name": "eth1"
#        }
#    ]
#
#    "commands": [
#        "delete service lldp interface eth2 location",
#        "delete service lldp interface eth2 disable",
#        "set service lldp interface eth2 location elin 0000000911"
#
#
#    "after": [
#        {
#            "location": {
#                "elin": 0000000911
#            },
#            "name": "eth2"
#        }
#    ]
#
#
# After state
# ------------
#
# vyos@vyos# run show configuration commands | grep lldp
# set service lldp interface eth2 location elin '0000000911'

# Using deleted
#
# Before state
# -------------
#
# vyos@vyos# run show configuration commands | grep lldp
# set service lldp interface eth2 location elin '0000000911'
#
- name: Delete lldp  interface attributes of given interfaces.
  vyos.vyos.vyos_lldp_interfaces:
    config:
    - name: eth2
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
    before: [{location: {elin: 0000000911}, name: eth2}]
# "commands": [
#    "commands": [
#        "delete service lldp interface eth2"
#    ]
#
# "after": []
# After state
# ------------
# vyos@vyos# run show configuration commands | grep lldp
# set service 'lldp'

# Using gathered
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep lldp
# set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth1 location civic-based country-code 'US'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'
#
- name: Gather listed lldp interfaces from running configuration
  vyos.vyos.vyos_lldp_interfaces:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#         {
#             "location": {
#                 "coordinate_based": {
#                     "altitude": 2200,
#                     "datum": "WGS84",
#                     "latitude": "33.524449N",
#                     "longitude": "222.267255W"
#                 }
#             },
#             "name": "eth2"
#         },
#         {
#             "location": {
#                 "civic_based": {
#                     "ca_info": [
#                         {
#                             "ca_type": 0,
#                             "ca_value": "ENGLISH"
#                         }
#                     ],
#                     "country_code": "US"
#                 }
#             },
#             "name": "eth1"
#         }
#     ]
#
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep lldp
# set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth1 location civic-based country-code 'US'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_lldp_interfaces:
    config:
    - name: eth1
      location:
        civic_based:
          country_code: US
          ca_info:
          - ca_type: 0
            ca_value: ENGLISH
    - name: eth2
      location:
        coordinate_based:
          altitude: 2200
          datum: WGS84
          longitude: 222.267255W
          latitude: 33.524449N
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#         "set service lldp interface eth1 location civic-based country-code 'US'",
#         "set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'",
#         "set service lldp interface eth1",
#         "set service lldp interface eth2 location coordinate-based latitude '33.524449N'",
#         "set service lldp interface eth2 location coordinate-based altitude '2200'",
#         "set service lldp interface eth2 location coordinate-based datum 'WGS84'",
#         "set service lldp interface eth2 location coordinate-based longitude '222.267255W'",
#         "set service lldp interface eth2"
#     ]

# Using parsed
#
#
- name: Parsed the commands to provide structured configuration.
  vyos.vyos.vyos_lldp_interfaces:
    running_config:
      "set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'
       set service lldp interface eth1 location civic-based country-code 'US'
       set service lldp interface eth2 location coordinate-based altitude '2200'
       set service lldp interface eth2 location coordinate-based datum 'WGS84'
       set service lldp interface eth2 location coordinate-based latitude '33.524449N'
       set service lldp interface eth2 location coordinate-based longitude '222.267255W'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#         {
#             "location": {
#                 "coordinate_based": {
#                     "altitude": 2200,
#                     "datum": "WGS84",
#                     "latitude": "33.524449N",
#                     "longitude": "222.267255W"
#                 }
#             },
#             "name": "eth2"
#         },
#         {
#             "location": {
#                 "civic_based": {
#                     "ca_info": [
#                         {
#                             "ca_type": 0,
#                             "ca_value": "ENGLISH"
#                         }
#                     ],
#                     "country_code": "US"
#                 }
#             },
#             "name": "eth1"
#         }
#     ]
```

## [Return Values](vyos_lldp_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["set service lldp interface eth2 'disable'", "delete service lldp interface eth1 location"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
