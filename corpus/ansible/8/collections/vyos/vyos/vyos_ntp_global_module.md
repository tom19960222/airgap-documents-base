---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_ntp_global module – Manages ntp modules of Vyos network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_ntp_global_module.html
fetched_at: 2026-07-28T02:59:19+00:00
---
# vyos.vyos.vyos_ntp_global module – Manages ntp modules of Vyos network devices

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
> To use it in a playbook, specify: `vyos.vyos.vyos_ntp_global`.

New in vyos.vyos 2.4.0

- [Synopsis](vyos_ntp_global_module.md#synopsis)
- [Parameters](vyos_ntp_global_module.md#parameters)
- [Notes](vyos_ntp_global_module.md#notes)
- [Examples](vyos_ntp_global_module.md#examples)
- [Return Values](vyos_ntp_global_module.md#return-values)

## [Synopsis](vyos_ntp_global_module.md#id1)

- This module manages ntp configuration on devices running Vyos

Aliases: ntp_global

## [Parameters](vyos_ntp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | List of configurations for ntp module |
| **allow_clients**  list / elements=string | Network Time Protocol (NTP) server options |
| **listen_addresses**  list / elements=string | local IP addresses for service to listen on |
| **servers**  list / elements=dictionary | Network Time Protocol (NTP) server |
| **options**  list / elements=string | server options for NTP  **Choices:**   - `"noselect"` - `"dynamic"` - `"pool"` - `"preempt"` - `"prefer"` |
| **server**  string | server name for NTP |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VYOS device by executing the command **show configuration commands | grep ntp**.  The states *replaced* and *overridden* have identical behaviour for this module.  The state *parsed* reads the configuration from `show configuration commands | grep ntp` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](vyos_ntp_global_module.md#id3)

> **Note:**
>
> - Tested against vyos 1.3
> - This module works with connection `network_cli`.

## [Examples](vyos_ntp_global_module.md#id4)

```yaml+jinja
# # -------------------
# # 1. Using merged
# # -------------------

# # Before state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep ntp
#     set system ntp server time1.vyos.net
#     set system ntp server time2.vyos.net
#     set system ntp server time3.vyos.net
#   vyos@vyos:~$

# # Task
# # -------------
- name: Replace the existing ntp config with the new config
  vyos.vyos.vyos_ntp_global:
    config:
        allow_clients:
          - 10.6.6.0/24
        listen_addresses:
          - 10.1.3.1
        servers:
          - server: 203.0.113.0
            options:
                - prefer

# # Task output:
# # -------------
#        "after": {
#         "allow_clients": [
#            "10.6.6.0/24"
#        ],
#        "listen_addresses": [
#            "10.1.3.1"
#        ],
#        "servers": [
#            {
#                "server": "ser",
#                "options": [
#                    "prefer"
#                ]
#            },
#            {
#                "server": "time1.vyos.net"
#            },
#            {
#                "server": "time2.vyos.net"
#            },
#            {
#                "server": "time3.vyos.net"
#            }
#        ]
#    },
#    "before": {
#    },
#    "changed": true,
#    "commands": [
#        "set system ntp allow-clients address 10.6.6.0/24",
#        "set system ntp listen-address 10.1.3.1",
#        "set system ntp server 203.0.113.0 prefer"
#    ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.6.6.0/24'
#        set system ntp listen-address '10.1.3.1'
#        set system ntp server 203.0.113.0 prefer,
#        set system ntp server time1.vyos.net
#        set system ntp server time2.vyos.net
#        set system ntp server time3.vyos.net
#        vyos@vyos:~$

# # -------------------
# # 2. Using replaced
# # -------------------

# # Before state:
# # -------------
#    vyos@vyos:~$ show configuration commands | grep ntp
#    set system ntp allow-clients address '10.4.9.0/24'
#    set system ntp allow-clients address '10.4.7.0/24'
#    set system ntp allow-clients address '10.1.2.0/24'
#    set system ntp allow-clients address '10.2.3.0/24'
#    set system ntp listen-address '10.1.9.16'
#    set system ntp listen-address '10.5.3.2'
#    set system ntp listen-address '10.7.9.21'
#    set system ntp listen-address '10.8.9.4'
#    set system ntp listen-address '10.4.5.1'
#    set system ntp server 10.3.6.5 noselect
#    set system ntp server 10.3.6.5 dynamic
#    set system ntp server 10.3.6.5 preempt
#    set system ntp server 10.3.6.5 prefer
#    set system ntp server server4 noselect
#    set system ntp server server4 dynamic
#    set system ntp server server5
#    set system ntp server time1.vyos.net
#    set system ntp server time2.vyos.net
#    set system ntp server time3.vyos.net
#    vyos@vyos:~$

# # Task
# # -------------
- name: Replace the existing ntp config with the new config
  vyos.vyos.vyos_ntp_global:
    config:
        allow_clients:
          - 10.6.6.0/24
        listen_addresses:
          - 10.1.3.1
        servers:
          - server: 203.0.113.0
            options:
                - prefer
    state: replaced

# # Task output:
# # -------------
#        "after": {
#         "allow_clients": [
#            "10.6.6.0/24"
#        ],
#        "listen_addresses": [
#            "10.1.3.1"
#        ],
#        "servers": [
#            {
#                "server": "ser",
#                "options": [
#                    "prefer"
#                ]
#            },
#            {
#                "server": "time1.vyos.net"
#            },
#            {
#                "server": "time2.vyos.net"
#            },
#            {
#                "server": "time3.vyos.net"
#            }
#        ]
#    },
#    "before": {
#        "allow_clients": [
#            "10.4.7.0/24",
#            "10.2.3.0/24",
#            "10.1.2.0/24",
#            "10.4.9.0/24"
#        ],
#        "listen_addresses": [
#            "10.7.9.21",
#            "10.4.5.1",
#            "10.5.3.2",
#            "10.8.9.4",
#            "10.1.9.16"
#        ],
#        "servers": [
#            {
#                "server": "10.3.6.5",
#                "options": [
#                    "noselect",
#                    "dynamic",
#                    "preempt",
#                    "prefer"
#                ]
#            },
#            {
#                "server": "server4",
#                "options": [
#                    "noselect",
#                    "dynamic"
#                ]
#            },
#            {
#                "server": "server5"
#            },
#            {
#                "server": "time1.vyos.net"
#            },
#            {
#                "server": "time2.vyos.net"
#            },
#            {
#                "server": "time3.vyos.net"
#            }
#        ]
#    },
#    "changed": true,
#    "commands": [
#        "delete system ntp allow-clients address 10.4.7.0/24",
#        "delete system ntp allow-clients address 10.2.3.0/24",
#        "delete system ntp allow-clients address 10.1.2.0/24",
#        "delete system ntp allow-clients address 10.4.9.0/24",
#        "delete system ntp listen-address 10.7.9.21",
#        "delete system ntp listen-address 10.4.5.1",
#        "delete system ntp listen-address 10.5.3.2",
#        "delete system ntp listen-address 10.8.9.4",
#        "delete system ntp listen-address 10.1.9.16",
#        "delete system ntp server 10.3.6.5",
#        "delete system ntp server server4",
#        "delete system ntp server server5",
#        "set system ntp allow-clients address 10.6.6.0/24",
#        "set system ntp listen-address 10.1.3.1",
#        "set system ntp server 203.0.113.0 prefer"
#    ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.6.6.0/24'
#        set system ntp listen-address '10.1.3.1'
#        set system ntp server 203.0.113.0 prefer,
#        set system ntp server time1.vyos.net
#        set system ntp server time2.vyos.net
#        set system ntp server time3.vyos.net
#        vyos@vyos:~$

# # -------------------
# # 3. Using overridden
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.6.6.0/24'
#        set system ntp listen-address '10.1.3.1'
#        set system ntp server 203.0.113.0 prefer,
#        set system ntp server time1.vyos.net
#        set system ntp server time2.vyos.net
#        set system ntp server time3.vyos.net
#        vyos@vyos:~$

# # Task
# # -------------
- name: Override ntp config
  vyos.vyos.vyos_ntp_global:
        config:
          allow_clients:
            - 10.3.3.0/24
          listen_addresses:
            - 10.7.8.1
          servers:
            - server: server1
              options:
                - dynamic
                - prefer

            - server: server2
              options:
                - noselect
                - preempt

            - server: serv
        state: overridden

# # Task output:
# # -------------
#            "after": {
#                "allow_clients": [
#                    "10.3.3.0/24"
#                ],
#                "listen_addresses": [
#                    "10.7.8.1"
#                ],
#                "servers": [
#                    {
#                "server": "serv"
#            },
#            {
#                "server": "server1",
#                "options": [
#                    "dynamic",
#                    "prefer"
#                ]
#            },
#            {
#                "server": "server2",
#                "options": [
#                    "noselect",
#                    "preempt"
#                ]
#            },
#            {
#                "server": "time1.vyos.net"
#            },
#            {
#                "server": "time2.vyos.net"
#            },
#            {
#                "server": "time3.vyos.net"
#            }
#                ]
#            },
#            "before": {
#                "allow_clients": [
#                    "10.6.6.0/24"
#                ],
#                "listen_addresses": [
#                    "10.1.3.1"
#                ],
#                "servers": [
#                    {
#                        "server": "ser",
#                        "options": [
#                            "prefer"
#                        ]
#                    },
#                    {
#                        "server": "time1.vyos.net"
#                    },
#                    {
#                        "server": "time2.vyos.net"
#                    },
#                    {
#                        "server": "time3.vyos.net"
#                    }
#                ]
#            },
#            "changed": true,
#            "commands": [
#                "delete system ntp allow-clients address 10.6.6.0/24",
#                "delete system ntp listen-address 10.1.3.1",
#                "delete system ntp server ser",
#                "set system ntp allow-clients address 10.3.3.0/24",
#                "set system ntp listen-address 10.7.8.1",
#                "set system ntp server server1 dynamic",
#                "set system ntp server server1 prefer",
#                "set system ntp server server2 noselect",
#                "set system ntp server server2 preempt",
#                "set system ntp server serv"
#            ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.3.3.0/24'
#        set system ntp listen-address '10.7.8.1'
#        set system ntp server serv
#        set system ntp server server1 dynamic
#        set system ntp server server1 prefer
#        set system ntp server server2 noselect
#        set system ntp server server2 preempt
#        set system ntp server time1.vyos.net
#        set system ntp server time2.vyos.net
#        set system ntp server time3.vyos.net
#        vyos@vyos:~$

# # -------------------
# # 4. Using gathered
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.3.3.0/24'
#        set system ntp listen-address '10.7.8.1'
#        set system ntp server serv
#        set system ntp server server1 dynamic
#        set system ntp server server1 prefer
#        set system ntp server server2 noselect
#        set system ntp server server2 preempt
#        set system ntp server time1.vyos.net
#        set system ntp server time2.vyos.net
#        set system ntp server time3.vyos.net
#        vyos@vyos:~$

# # Task
# # -------------
- name: Gather ntp config
  vyos.vyos.vyos_ntp_global:
        state: gathered

# # Task output:
# # -------------
#        "gathered": {
#                "allow_clients": [
#                    "10.3.3.0/24"
#                ],
#                "listen_addresses": [
#                    "10.7.8.1"
#                ],
#                "servers": [
#                    {
#                        "server": "serv"
#                    },
#                    {
#                        "server": "server1",
#                        "options": [
#                            "dynamic",
#                            "prefer"
#                        ]
#                    },
#                    {
#                         "server": "server2",
#                         "options": [
#                             "noselect",
#                             "preempt"
#                         ]
#                     },
#                     {
#                          "server": "time1.vyos.net"
#                     },
#                     {
#                         "server": "time2.vyos.net"
#                     },
#                     {
#                         "server": "time3.vyos.net"
#                     }
#                ]
#            }

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.3.3.0/24'
#        set system ntp listen-address '10.7.8.1'
#        set system ntp server serv
#        set system ntp server server1 dynamic
#        set system ntp server server1 prefer
#        set system ntp server server2 noselect
#        set system ntp server server2 preempt
#        set system ntp server time1.vyos.net
#        set system ntp server time2.vyos.net
#        set system ntp server time3.vyos.net
#        vyos@vyos:~$

# # -------------------
# # 5. Using deleted
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.3.3.0/24'
#        set system ntp listen-address '10.7.8.1'
#        set system ntp server serv
#        set system ntp server server1 dynamic
#        set system ntp server server1 prefer
#        set system ntp server server2 noselect
#        set system ntp server server2 preempt
#        set system ntp server time1.vyos.net
#        set system ntp server time2.vyos.net
#        set system ntp server time3.vyos.net
#        vyos@vyos:~$

# # Task
# # -------------
- name: Delete ntp config
  vyos.vyos.vyos_ntp_global:
    state: deleted

# # Task output:
# # -------------
#            "after": {
#                "servers": [
#                    {
#                        "server": "time1.vyos.net"
#                    },
#                    {
#                       "server": "time2.vyos.net"
#                    },
#                    {
#                        "server": "time3.vyos.net"
#                    }
#                ]
#            },
#            "before": {
#                "allow_clients": [
#                    "10.3.3.0/24"
#                ],
#                "listen_addresses": [
#                    "10.7.8.1"
#                ],
#                "servers": [
#                    {
#                        "server": "serv"
#                    },
#                    {
#                        "server": "server1",
#                        "options": [
#                            "dynamic",
#                            "prefer"
#                        ]
#                    },
#                    {
#                          "server": "server2",
#                          "options": [
#                              "noselect",
#                              "preempt"
#                          ]
#                      },
#                      {
#                          "server": "time1.vyos.net"
#                      },
#                      {
#                          "server": "time2.vyos.net"
#                      },
#                      {
#                          "server": "time3.vyos.net"
#                      }
#                ]
#            },
#            "changed": true,
#            "commands": [
#                "delete system ntp allow-clients",
#                "delete system ntp listen-address",
#                "delete system ntp server serv",
#                "delete system ntp server server1",
#                "delete system ntp server server2"
#
#            ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp server time1.vyos.net
#        set system ntp server time2.vyos.net
#        set system ntp server time3.vyos.net
#        vyos@vyos:~$

# # -------------------
# # 6. Using rendered
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp server time1.vyos.net
#        set system ntp server time2.vyos.net
#        set system ntp server time3.vyos.net
#        vyos@vyos:~$

# # Task
# # -------------
- name: Render ntp config
  vyos.vyos.vyos_ntp_global:
       config:
        allow_clients:
            - 10.7.7.0/24
            - 10.8.8.0/24
        listen_addresses:
            - 10.7.9.1
        servers:
            - server: server7

            - server: server45
              options:
                - noselect
                - prefer
                - pool
            - server: time1.vyos.net

            - server: time2.vyos.net

            - server: time3.vyos.net

        state: rendered

# # Task output:
# # -------------
#           "rendered": [
#                "set system ntp allow-clients address 10.7.7.0/24",
#                "set system ntp allow-clients address 10.8.8.0/24",
#                "set system ntp listen-address 10.7.9.1",
#                "set system ntp server server7",
#                "set system ntp server server45 noselect",
#                "set system ntp server server45 prefer",
#                "set system ntp server server45 pool",
#                "set system ntp server time1.vyos.net",
#                "set system ntp server time2.vyos.net",
#                "set system ntp server time3.vyos.net"
#            ]

# # -------------------
# # 7. Using parsed
# # -------------------

# # sample_config.cfg:
# # -------------
#           "set system ntp allow-clients address 10.7.7.0/24",
#           "set system ntp listen-address 10.7.9.1",
#           "set system ntp server server45 noselect",
#           "set system ntp allow-clients addres 10.8.6.0/24",
#           "set system ntp listen-address 10.5.4.1",
#           "set system ntp server server45 dynamic",
#           "set system ntp server time1.vyos.net",
#           "set system ntp server time2.vyos.net",
#           "set system ntp server time3.vyos.net"

# # Task:
# # -------------
- name: Parse externally provided ntp configuration
  vyos.vyos.vyos_ntp_global:
     running_config: "{{ lookup('file', './sample_config.cfg') }}"
     state: parsed

# # Task output:
# # -------------
#           parsed = {
#                "allow_clients": [
#                    "10.7.7.0/24",
#                    "10.8.6.0/24
#                ],
#                "listen_addresses": [
#                    "10.5.4.1",
#                    "10.7.9.1"
#                ],
#                "servers": [
#                    {
#                        "server": "server45",
#                        "options": [
#                            "noselect",
#                            "dynamic"
#
#                        ]
#                    },
#                    {
#                        "server": "time1.vyos.net"
#                    },
#                    {
#                        "server": "time2.vyos.net"
#                    },
#                    {
#                        "server": "time3.vyos.net"
#                    }
#
#                ]
#            }
```

## [Return Values](vyos_ntp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["set system ntp server server1 dynamic", "set system ntp server server1 prefer", "set system ntp server server2 noselect", "set system ntp server server2 preempt", "set system ntp server server_add preempt"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["set system ntp server server1 dynamic", "set system ntp server server1 prefer", "set system ntp server server2 noselect", "set system ntp server server2 preempt", "set system ntp server server_add preempt"]` |

### Authors

- Varshitha Yataluru (@YVarshitha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
