---
collection: ansible
version: "6"
title: "arista.eos.eos_ntp_global module – Manages ntp resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_ntp_global_module.html
fetched_at: 2026-07-27T16:45:15+00:00
---
# arista.eos.eos_ntp_global module – Manages ntp resource module

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
> To use it in a playbook, specify: `arista.eos.eos_ntp_global`.

New in arista.eos 3.1.0

- [Synopsis](eos_ntp_global_module.md#synopsis)
- [Parameters](eos_ntp_global_module.md#parameters)
- [Notes](eos_ntp_global_module.md#notes)
- [Examples](eos_ntp_global_module.md#examples)
- [Return Values](eos_ntp_global_module.md#return-values)

## [Synopsis](eos_ntp_global_module.md#id1)

- This module configures and manages the attributes of ntp on Arista EOS platforms.

## [Parameters](eos_ntp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of ntp options |
| **authenticate**  dictionary | Require authentication for NTP synchronization. |
| **enable**  boolean | Enable authentication for NTP synchronization.  Choices:   - `false` - `true` |
| **servers**  boolean | Authentication required only for incoming NTP server responses.  Choices:   - `false` - `true` |
| **authentication_keys**  list / elements=dictionary | Define a key to use for authentication. |
| **algorithm**  string | hash algorithm,  Choices:   - `"md5"` - `"sha1"` |
| **encryption**  integer | key type  Choices:   - `0` - `7` |
| **id**  integer | key identifier. |
| **key**  string | Unobfuscated key string. |
| **local_interface**  string | Configure the interface from which the IP source address is taken. |
| **qos_dscp**  integer | Set DSCP value in IP header |
| **serve**  dictionary | Configure the switch as an NTP server. |
| **access_lists**  list / elements=dictionary | Configure access control list. |
| **acls**  list / elements=dictionary | Access lists to be configured under the afi |
| **acl_name**  string | Name of the access list. |
| **direction**  string | direction for the packets.  Choices:   - `"in"` - `"out"` |
| **vrf**  string | VRF in which to apply the access control list. |
| **afi**  string | ip/ipv6 config commands. |
| **all**  boolean | Service NTP requests received on any interface.  Choices:   - `false` - `true` |
| **servers**  list / elements=dictionary | Configure NTP server to synchronize to. |
| **burst**  boolean | Send a burst of packets instead of the usual one.  Choices:   - `false` - `true` |
| **iburst**  boolean | Send bursts of packets until the server is reached  Choices:   - `false` - `true` |
| **key_id**  integer | Set a key to use for authentication. |
| **local_interface**  string | Configure the interface from which the IP source address is taken. |
| **maxpoll**  integer | Maximum poll interval. |
| **minpoll**  integer | Minimum poll interval. |
| **prefer**  boolean | Mark this server as preferred.  Choices:   - `false` - `true` |
| **server**  string / required | Hostname or A.B.C.D or A:B:C:D:E:F:G:H. |
| **source**  string | Configure the interface from which the IP source address is taken. |
| **version**  integer | NTP version. |
| **vrf**  string | vrf name. |
| **trusted_key**  string | Configure the set of keys that are accepted for incoming messages |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ntp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states *replaced* and *overridden* have identical behaviour for this module.  Please refer to examples for more details.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_ntp_global_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.60M
> - This module works with connection `network_cli`. See the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_eos.html>.

## [Examples](eos_ntp_global_module.md#id4)

```yaml+jinja
# Using merged

# Before state

# localhost(config)#show running-config | section ntp
# localhost(config)#

  - name: Merge provided configuration with device configuration
    arista.eos.eos_ntp_global:
      config:
        authenticate:
          enable: true
        authentication_keys:
          - id: 2
            algorithm: "sha1"
            encryption: 7
            key: "123456"
          - id: 23
            algorithm: "md5"
            encryption: 7
            key: "123456"
        local_interface: "Ethernet1"
        qos_dscp: 10
        trusted_key: 23
        servers:
          - server: "10.1.1.1"
            vrf: "vrf01"
            burst: True
            prefer: True
          - server: "25.1.1.1"
            vrf: "vrf01"
            maxpoll: 15
            key_id: 2
        serve:
          access_lists:
            - afi: "ip"
              acls:
                - acl_name: "acl01"
                  direction: "in"
            - afi: "ipv6"
              acls:
                 - acl_name: "acl02"
                   direction: "in"

# After State

# localhost(config)#show running-config | section ntp
# ntp authentication-key 2 sha1 7 123456
# ntp authentication-key 23 md5 7 123456
# ntp trusted-key 23
# ntp authenticate
# ntp local-interface Ethernet1
# ntp qos dscp 10
# ntp server vrf vrf01 10.1.1.1 prefer burst
# ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
# ntp serve ip access-group acl01 in
# ntp serve ipv6 access-group acl02 in
# localhost(config)#
#
#
# Module Execution:
# "after": {
#         "authenticate": {
#             "enable": true
#         },
#         "authentication_keys": [
#             {
#                 "algorithm": "sha1",
#                 "encryption": 7,
#                 "id": 2,
#                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#             },
#             {
#                 "algorithm": "md5",
#                 "encryption": 7,
#                 "id": 23,
#                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#             }
#         ],
#         "local_interface": "Ethernet1",
#         "qos_dscp": 10,
#         "serve": {
#             "access_lists": [
#                 {
#                     "acls": [
#                         {
#                             "acl_name": "acl01",
#                             "direction": "in"
#                         }
#                     ],
#                     "afi": "ip"
#                 },
#                 {
#                     "acls": [
#                         {
#                             "acl_name": "acl02",
#                             "direction": "in"
#                         }
#                     ],
#                     "afi": "ipv6"
#                 }
#             ]
#         },
#         "servers": [
#             {
#                 "burst": true,
#                 "prefer": true,
#                 "server": "10.1.1.1",
#                 "vrf": "vrf01"
#             },
#             {
#                 "key_id": 2,
#                 "maxpoll": 15,
#                 "server": "25.1.1.1",
#                 "vrf": "vrf01"
#             }
#         ],
#         "trusted_key": "23"
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "ntp serve ip access-group acl01 in",
#         "ntp serve ipv6 access-group acl02 in",
#         "ntp authentication-key 2 sha1 7 ********",
#         "ntp authentication-key 23 md5 7 ********",
#         "ntp server vrf vrf01 10.1.1.1 burst prefer",
#         "ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
#         "ntp authenticate",
#         "ntp local-interface Ethernet1",
#         "ntp qos dscp 10",
#         "ntp trusted-key 23"
#     ],

# Using Replaced

# Before State

# localhost(config)#show running-config | section ntp
# ntp authentication-key 2 sha1 7 123456
# ntp authentication-key 23 md5 7 123456
# ntp trusted-key 23
# ntp authenticate
# ntp local-interface Ethernet1
# ntp qos dscp 10
# ntp server vrf vrf01 10.1.1.1 prefer burst
# ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
# ntp serve ip access-group acl01 in
# ntp serve ipv6 access-group acl02 in
# localhost(config)#

  - name: Replace
    arista.eos.eos_ntp_global:
      config:
        qos_dscp: 15
        authentication_keys:
          - id: 2
            algorithm: "md5"
            encryption: 7
            key: "123456"
        servers:
          - server: "11.21.1.1"
            vrf: "vrf01"
            burst: True
            prefer: True
            minpoll: 13
        serve:
          access_lists:
            - afi: "ip"
              acls:
                - acl_name: "acl03"
                  direction: "in"
      state: replaced
# After State:
# localhost(config)#show running-config | section ntp
# ntp authentication-key 2 md5 7 123456
# ntp qos dscp 15
# ntp server vrf vrf01 11.21.1.1 prefer burst minpoll 13
# ntp serve ip access-group acl03 in
# localhost(config)#
#
#
# Module Execution:
# "after": {
#        "authentication_keys": [
#            {
#                "algorithm": "md5",
#                "encryption": 7,
#                "id": 2,
#                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#            }
#        ],
#        "qos_dscp": 15,
#        "serve": {
#            "access_lists": [
#                {
#                    "acls": [
#                        {
#                            "acl_name": "acl03",
#                            "direction": "in"
#                        }
#                    ],
#                    "afi": "ip"
#                }
#            ]
#        },
#        "servers": [
#            {
#                "burst": true,
#                "minpoll": 13,
#                "prefer": true,
#                "server": "11.21.1.1",
#                "vrf": "vrf01"
#            }
#        ]
#    },
#    "before": {
#        "authenticate": {
#            "enable": true
#        },
#        "authentication_keys": [
#            {
#                "algorithm": "sha1",
#                "encryption": 7,
#                "id": 2,
#                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#            },
#            {
#                "algorithm": "md5",
#                "encryption": 7,
#                "id": 23,
#                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#            }
#        ],
#        "local_interface": "Ethernet1",
#        "qos_dscp": 10,
#        "serve": {
#            "access_lists": [
#                {
#                    "acls": [
#                        {
#                            "acl_name": "acl01",
#                            "direction": "in"
#                        }
#                    ],
#                    "afi": "ip"
#                },
#                {
#                    "acls": [
#                        {
#                            "acl_name": "acl02",
#                            "direction": "in"
#                        }
#                    ],
#                    "afi": "ipv6"
#                }
#            ]
#        },
#        "servers": [
#            {
#                "burst": true,
#                "prefer": true,
#                "server": "10.1.1.1",
#                "vrf": "vrf01"
#            },
#            {
#                "key_id": 2,
#                "maxpoll": 15,
#                "server": "25.1.1.1",
#                "vrf": "vrf01"
#            }
#        ],
#        "trusted_key": "23"
#    },
#    "changed": true,
#    "commands": [
#        "no ntp serve ip access-group acl01 in",
#        "no ntp serve ipv6 access-group acl02 in",
#        "no ntp authentication-key 23 md5 7 ********",
#        "no ntp server vrf vrf01 10.1.1.1 burst prefer",
#        "no ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
#        "no ntp authenticate",
#        "no ntp local-interface Ethernet1",
#        "no ntp trusted-key 23",
#        "ntp serve ip access-group acl03 in",
#        "ntp authentication-key 2 md5 7 ********",
#        "ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
#        "ntp qos dscp 15"
#    ],
#
# Using Overridden

# Before State

# localhost(config)#show running-config | section ntp
# ntp authentication-key 2 sha1 7 123456
# ntp authentication-key 23 md5 7 123456
# ntp trusted-key 23
# ntp authenticate
# ntp local-interface Ethernet1
# ntp qos dscp 10
# ntp server vrf vrf01 10.1.1.1 prefer burst
# ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
# ntp serve ip access-group acl01 in
# ntp serve ipv6 access-group acl02 in
# localhost(config)#

  - name: Replace
    arista.eos.eos_ntp_global:
      config:
        qos_dscp: 15
        authentication_keys:
          - id: 2
            algorithm: "md5"
            encryption: 7
            key: "123456"
        servers:
          - server: "11.21.1.1"
            vrf: "vrf01"
            burst: True
            prefer: True
            minpoll: 13
        serve:
          access_lists:
            - afi: "ip"
              acls:
                - acl_name: "acl03"
                  direction: "in"
      state: overridden
# After State:
# localhost(config)#show running-config | section ntp
# ntp authentication-key 2 md5 7 123456
# ntp qos dscp 15
# ntp server vrf vrf01 11.21.1.1 prefer burst minpoll 13
# ntp serve ip access-group acl03 in
# localhost(config)#
#
#
# Module Execution:
# "after": {
#        "authentication_keys": [
#            {
#                "algorithm": "md5",
#                "encryption": 7,
#                "id": 2,
#                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#            }
#        ],
#        "qos_dscp": 15,
#        "serve": {
#            "access_lists": [
#                {
#                    "acls": [
#                        {
#                            "acl_name": "acl03",
#                            "direction": "in"
#                        }
#                    ],
#                    "afi": "ip"
#                }
#            ]
#        },
#        "servers": [
#            {
#                "burst": true,
#                "minpoll": 13,
#                "prefer": true,
#                "server": "11.21.1.1",
#                "vrf": "vrf01"
#            }
#        ]
#    },
#    "before": {
#        "authenticate": {
#            "enable": true
#        },
#        "authentication_keys": [
#            {
#                "algorithm": "sha1",
#                "encryption": 7,
#                "id": 2,
#                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#            },
#            {
#                "algorithm": "md5",
#                "encryption": 7,
#                "id": 23,
#                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#            }
#        ],
#        "local_interface": "Ethernet1",
#        "qos_dscp": 10,
#        "serve": {
#            "access_lists": [
#                {
#                    "acls": [
#                        {
#                            "acl_name": "acl01",
#                            "direction": "in"
#                        }
#                    ],
#                    "afi": "ip"
#                },
#                {
#                    "acls": [
#                        {
#                            "acl_name": "acl02",
#                            "direction": "in"
#                        }
#                    ],
#                    "afi": "ipv6"
#                }
#            ]
#        },
#        "servers": [
#            {
#                "burst": true,
#                "prefer": true,
#                "server": "10.1.1.1",
#                "vrf": "vrf01"
#            },
#            {
#                "key_id": 2,
#                "maxpoll": 15,
#                "server": "25.1.1.1",
#                "vrf": "vrf01"
#            }
#        ],
#        "trusted_key": "23"
#    },
#    "changed": true,
#    "commands": [
#        "no ntp serve ip access-group acl01 in",
#        "no ntp serve ipv6 access-group acl02 in",
#        "no ntp authentication-key 23 md5 7 ********",
#        "no ntp server vrf vrf01 10.1.1.1 burst prefer",
#        "no ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
#        "no ntp authenticate",
#        "no ntp local-interface Ethernet1",
#        "no ntp trusted-key 23",
#        "ntp serve ip access-group acl03 in",
#        "ntp authentication-key 2 md5 7 ********",
#        "ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
#        "ntp qos dscp 15"
#    ],
#

# using deleted:
# Before State

# localhost(config)#show running-config | section ntp
# ntp authentication-key 2 sha1 7 123456
# ntp authentication-key 23 md5 7 123456
# ntp trusted-key 23
# ntp authenticate
# ntp local-interface Ethernet1
# ntp qos dscp 10
# ntp server vrf vrf01 10.1.1.1 prefer burst
# ntp server vrf vrf01 11.21.1.1 prefer burst minpoll 13
# ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
# ntp serve ip access-group acl01 in
# ntp serve ipv6 access-group acl02 in
# localhost(config)#

  - name: Delete  ntp-global
    arista.eos.eos_ntp_global:
      state: deleted

# After State:
#  localhost(config)#show running-config | section ntp
# localhost(config)#
#
#
# # Module Execution
# "after": {},
#     "before": {
#         "authenticate": {
#             "enable": true
#         },
#         "authentication_keys": [
#             {
#                 "algorithm": "sha1",
#                 "encryption": 7,
#                 "id": 2,
#                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#             },
#             {
#                 "algorithm": "md5",
#                 "encryption": 7,
#                 "id": 23,
#                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#             }
#         ],
#         "local_interface": "Ethernet1",
#         "qos_dscp": 10,
#         "serve": {
#             "access_lists": [
#                 {
#                     "acls": [
#                         {
#                             "acl_name": "acl01",
#                             "direction": "in"
#                         }
#                     ],
#                     "afi": "ip"
#                 },
#                 {
#                     "acls": [
#                         {
#                             "acl_name": "acl02",
#                             "direction": "in"
#                         }
#                     ],
#                     "afi": "ipv6"
#                 }
#             ]
#         },
#         "servers": [
#             {
#                 "burst": true,
#                 "prefer": true,
#                 "server": "10.1.1.1",
#                 "vrf": "vrf01"
#             },
#             {
#                 "burst": true,
#                 "minpoll": 13,
#                 "prefer": true,
#                 "server": "11.21.1.1",
#                 "vrf": "vrf01"
#             },
#             {
#                 "key": 2,
#                 "maxpoll": 15,
#                 "server": "25.1.1.1",
#                 "vrf": "vrf01"
#             }
#         ],
#         "trusted_key": "23"
#     },
#     "changed": true,
#     "commands": [
#         "no ntp serve ip access-group acl01 in",
#         "no ntp serve ipv6 access-group acl02 in",
#         "no ntp authentication-key 2 sha1 7 ********",
#         "no ntp authentication-key 23 md5 7 ********",
#         "no ntp server vrf vrf01 10.1.1.1 burst prefer",
#         "no ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
#         "no ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
#         "no ntp authenticate",
#         "no ntp local-interface Ethernet1",
#         "no ntp qos dscp 10",
#         "no ntp trusted-key 23"
#     ],
#

# Using parsed:
# parsed.cfg
# ntp authentication-key 2 sha1 7 123456
# ntp authentication-key 23 md5 7 123456
# ntp trusted-key 23
# ntp authenticate
# ntp local-interface Ethernet1
# ntp qos dscp 10
# ntp server vrf vrf01 10.1.1.1 prefer burst
# ntp server vrf vrf01 11.21.1.1 prefer burst minpoll 13
# ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
# ntp serve ip access-group acl01 in
# ntp serve ipv6 access-group acl02 in

  - name: parse configs
    arista.eos.eos_ntp_global:
      running_config: "{{ lookup('file', './parsed_ntp_global.cfg') }}"
      state: parsed
    tags:
      - parsed
# Module Execution
# "parsed": {
#         "authenticate": {
#             "enable": true
#         },
#         "authentication_keys": [
#             {
#                 "algorithm": "sha1",
#                 "encryption": 7,
#                 "id": 2,
#                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#             },
#             {
#                 "algorithm": "md5",
#                 "encryption": 7,
#                 "id": 23,
#                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#             }
#         ],
#         "local_interface": "Ethernet1",
#         "qos_dscp": 10,
#         "serve": {
#             "access_lists": [
#                 {
#                     "acls": [
#                         {
#                             "acl_name": "acl01",
#                             "direction": "in"
#                         }
#                     ],
#                     "afi": "ip"
#                 },
#                 {
#                     "acls": [
#                         {
#                             "acl_name": "acl02",
#                             "direction": "in"
#                         }
#                     ],
#                     "afi": "ipv6"
#                 }
#             ]
#         },
#         "servers": [
#             {
#                 "burst": true,
#                 "prefer": true,
#                 "server": "10.1.1.1",
#                 "vrf": "vrf01"
#             },
#             {
#                 "burst": true,
#                 "minpoll": 13,
#                 "prefer": true,
#                 "server": "11.21.1.1",
#                 "vrf": "vrf01"
#             },
#             {
#                 "key": 2,
#                 "maxpoll": 15,
#                 "server": "25.1.1.1",
#                 "vrf": "vrf01"
#             }
#         ],
#         "trusted_key": "23"
#     }
# }

# using Gathered
# Device config:
# localhost(config)#show running-config | section ntp
# ntp authentication-key 2 sha1 7 123456
# ntp authentication-key 23 md5 7 123456
# ntp trusted-key 23
# ntp authenticate
# ntp local-interface Ethernet1
# ntp qos dscp 10
# ntp server vrf vrf01 10.1.1.1 prefer burst
# ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
# ntp serve ip access-group acl01 in
# ntp serve ipv6 access-group acl02 in
# localhost(config)#

  - name: gather configs
    arista.eos.eos_ntp_global:
      state: gathered
    tags:
      - gathered
# Module Execution
#   "gathered": {
#         "authenticate": {
#             "enable": true
#         },
#         "authentication_keys": [
#             {
#                 "algorithm": "sha1",
#                 "encryption": 7,
#                 "id": 2,
#                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#             },
#             {
#                 "algorithm": "md5",
#                 "encryption": 7,
#                 "id": 23,
#                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
#             }
#         ],
#         "local_interface": "Ethernet1",
#         "qos_dscp": 10,
#         "serve": {
#             "access_lists": [
#                 {
#                     "acls": [
#                         {
#                             "acl_name": "acl01",
#                             "direction": "in"
#                         }
#                     ],
#                     "afi": "ip"
#                 },
#                 {
#                     "acls": [
#                         {
#                             "acl_name": "acl02",
#                             "direction": "in"
#                         }
#                     ],
#                     "afi": "ipv6"
#                 }
#             ]
#         },
#         "servers": [
#             {
#                 "burst": true,
#                 "prefer": true,
#                 "server": "10.1.1.1",
#                 "vrf": "vrf01"
#             },
#             {
#                 "key_id": 2,
#                 "maxpoll": 15,
#                 "server": "25.1.1.1",
#                 "vrf": "vrf01"
#             }
#         ],
#         "trusted_key": "23"
#     },
#     "invocation": {
#         "module_args": {
#             "config": null,
#             "running_config": null,
#             "state": "gathered"
#         }
#     }
# }

# using rendered:

  - name: Render provided configuration
    arista.eos.eos_ntp_global:
      config:
        authenticate:
          enable: true
        authentication_keys:
          - id: 2
            algorithm: "sha1"
            encryption: 7
            key: "123456"
          - id: 23
            algorithm: "md5"
            encryption: 7
            key: "123456"
        local_interface: "Ethernet1"
        qos_dscp: 10
        trusted_key: 23
        servers:
          - server: "10.1.1.1"
            vrf: "vrf01"
            burst: True
            prefer: True
          - server: "25.1.1.1"
            vrf: "vrf01"
            maxpoll: 15
            key_id: 2
        serve:
          access_lists:
            - afi: "ip"
              acls:
                - acl_name: "acl01"
                  direction: "in"
            - afi: "ipv6"
              acls:
                 - acl_name: "acl02"
                   direction: "in"
      state: rendered
    become: yes

# Module Execution:
# "rendered": [
#         "ntp serve ip access-group acl01 in",
#         "ntp serve ipv6 access-group acl02 in",
#         "ntp authentication-key 2 sha1 7 ********",
#         "ntp authentication-key 23 md5 7 ********",
#         "ntp server vrf vrf01 10.1.1.1 burst prefer",
#         "ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
#         "ntp authenticate",
#         "ntp local-interface Ethernet1",
#         "ntp qos dscp 10",
#         "ntp trusted-key 23"
#     ]
#
```

## [Return Values](eos_ntp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  Returned: when changed  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `["ntp master stratum 2", "ntp peer 198.51.100.1 use-vrf test maxpoll 7", "ntp authentication-key 10 md5 wawyhanx2 7", "ntp access-group peer PeerAcl1", "ntp access-group peer PeerAcl2", "ntp access-group query-only QueryAcl1"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  Returned: when *state* is `gathered`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  Returned: when *state* is `parsed`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  Returned: when *state* is `rendered`  Sample: `["ntp authentication-key 2 sha1 7 123456", "ntp authentication-key 23 md5 7 123456", "ntp trusted-key 23", "ntp authenticate", "ntp local-interface Ethernet1", "ntp qos dscp 10", "ntp server vrf vrf01 10.1.1.1 prefer burst", "ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2", "ntp serve ip access-group acl01 in", "ntp serve ipv6 access-group acl02 in"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
