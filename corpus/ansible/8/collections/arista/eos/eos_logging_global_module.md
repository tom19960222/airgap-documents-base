---
collection: ansible
version: "8"
title: "arista.eos.eos_logging_global module – Manages logging resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_logging_global_module.html
fetched_at: 2026-07-28T01:11:09+00:00
---
# arista.eos.eos_logging_global module – Manages logging resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_logging_global`.

New in arista.eos 3.0.0

- [Synopsis](eos_logging_global_module.md#synopsis)
- [Parameters](eos_logging_global_module.md#parameters)
- [Notes](eos_logging_global_module.md#notes)
- [Examples](eos_logging_global_module.md#examples)

## [Synopsis](eos_logging_global_module.md#id1)

- This module configures and manages the attributes of logging on Arista EOS platforms.

Aliases: logging_global

## [Parameters](eos_logging_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of logging options |
| **buffered**  dictionary | Set buffered logging parameters. |
| **buffer_size**  integer | Logging buffer size |
| **severity**  string | Severity level .  **Choices:**   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warnings"` - `"notifications"` - `"informational"` - `"debugging"` |
| **console**  dictionary | Set console logging parameters. |
| **severity**  string | Severity level .  **Choices:**   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warnings"` - `"notifications"` - `"informational"` - `"debugging"` |
| **event**  string | Global events  **Choices:**   - `"link-status"` - `"port-channel"` - `"spanning-tree"` |
| **facility**  string | Set logging facility.  **Choices:**   - `"auth"` - `"cron"` - `"daemon"` - `"kern"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` - `"lpr"` - `"mail"` - `"news"` - `"sys10"` - `"sys11"` - `"sys12"` - `"sys13"` - `"sys14"` - `"sys9"` - `"syslog"` - `"user"` - `"uucp"` |
| **format**  dictionary | Set logging format parameters |
| **hostname**  string | Specify hostname logging format. |
| **sequence_numbers**  boolean | No. of log messages.  **Choices:**   - `false` - `true` |
| **timestamp**  dictionary | Set timestamp logging parameters. |
| **high_resolution**  boolean | RFC3339 timestamps.  **Choices:**   - `false` - `true` |
| **traditional**  dictionary | Traditional syslog timestamp format as specified in RFC3164. |
| **state**  string | When enabled traditional timestamp format is set.  **Choices:**   - `"enabled"` - `"disabled"` |
| **timezone**  boolean | Show timezone in traditional format timestamp  **Choices:**   - `false` - `true` |
| **year**  boolean | Show year in traditional format timestamp  **Choices:**   - `false` - `true` |
| **hosts**  list / elements=dictionary | Set syslog server IP address and parameters. |
| **add**  boolean | Configure ports on the given host.  **Choices:**   - `false` - `true` |
| **name**  string | Hostname or IP address of the syslog server. |
| **port**  integer | Port of the syslog server. |
| **protocol**  string | Set syslog server transport protocol  **Choices:**   - `"tcp"` - `"udp"` |
| **remove**  boolean | Remove configured ports from the given host  **Choices:**   - `false` - `true` |
| **level**  dictionary | Configure logging severity |
| **facility**  string | Facility level |
| **severity**  string | Severity level .  **Choices:**   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warnings"` - `"notifications"` - `"informational"` - `"debugging"` |
| **monitor**  string | Set terminal monitor severity |
| **persistent**  dictionary | Save logging messages to the flash disk. |
| **set**  boolean | Save logging messages to the flash dis.  **Choices:**   - `false` - `true` |
| **size**  integer | The maximum size (in bytes) of logging file stored on flash disk. |
| **policy**  dictionary | Configure logging policies. |
| **invert_result**  boolean | Invert the match of match-list.  **Choices:**   - `false` - `true` |
| **match_list**  string | Configure logging message filtering. |
| **qos**  integer | Set DSCP value in IP header. |
| **relogging_interval**  integer | Configure relogging-interval for critical log messages |
| **repeat_messages**  boolean | Repeat messages instead of summarizing number of repeats  **Choices:**   - `false` - `true` |
| **source_interface**  string | Use IP Address of interface as source IP of log messages. |
| **synchronous**  dictionary | Set synchronizing unsolicited with solicited messages |
| **level**  string | Configure logging severity |
| **set**  boolean | Set synchronizing unsolicited with solicited messages.  **Choices:**   - `false` - `true` |
| **trap**  dictionary | Severity of messages sent to the syslog server. |
| **set**  boolean | Severity of messages sent to the syslog server.  **Choices:**   - `false` - `true` |
| **severity**  string | Severity level .  **Choices:**   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warnings"` - `"notifications"` - `"informational"` - `"debugging"` |
| **turn_on**  boolean | Turn on logging.  **Choices:**   - `false` - `true` |
| **vrfs**  list / elements=dictionary | Specify vrf |
| **hosts**  list / elements=dictionary | Set syslog server IP address and parameters. |
| **add**  boolean | Configure ports on the given host.  **Choices:**   - `false` - `true` |
| **name**  string | Hostname or IP address of the syslog server. |
| **port**  integer | Port of the syslog server. |
| **protocol**  string | Set syslog server transport protocol  **Choices:**   - `"tcp"` - `"udp"` |
| **remove**  boolean | Remove configured ports from the given host  **Choices:**   - `false` - `true` |
| **name**  string | vrf name. |
| **source_interface**  string | Use IP Address of interface as source IP of log messages. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section access-list**.  The states *replaced* and *overridden* have identical behaviour for this module.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_logging_global_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6M
> - This module works with connection `network_cli`. See the [EOS Platform Options](eos_platform_options.md).

## [Examples](eos_logging_global_module.md#id4)

```yaml+jinja
# Using merged
# Before state

# test(config)#show running-config | section logging
# test(config)#

- name: Merge provided configuration with device configuration
  arista.eos.eos_logging_global:
    config:
      hosts:
        - name: "host01"
          protocol: "tcp"
        - name: "11.11.11.1"
          port: 25
      vrfs:
        - name: "vrf01"
          source_interface: "Ethernet1"
        - name: "vrf02"
          hosts:
            - name: "hostvrf1"
              protocol: "tcp"
            - name: "24.1.1.1"
              port: "33"

# After State:

# test(config)#show running-config | section logging
# logging host 11.11.11.1 25
# logging host host01 514 protocol tcp
# logging vrf vrf02 host 24.1.1.1 33
# logging vrf vrf02 host hostvrf1 514 protocol tcp
# logging vrf vrf01 source-interface Ethernet1
# test(config)#
#
#
# Module Execution:
# "after": {
#         "hosts": [
#             {
#                 "name": "11.11.11.1",
#                 "port": 25
#             },
#             {
#                 "name": "host01",
#                 "port": 514,
#                 "protocol": "tcp"
#             }
#         ],
#         "vrfs": [
#             {
#                 "name": "vrf01",
#                 "source_interface": "Ethernet1"
#             },
#             {
#                 "hosts": [
#                     {
#                         "name": "24.1.1.1",
#                         "port": 33
#                     },
#                     {
#                         "name": "hostvrf1",
#                         "port": 514,
#                         "protocol": "tcp"
#                     }
#                 ],
#                 "name": "vrf02"
#             }
#         ]
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "logging host host01 protocol tcp",
#         "logging host 11.11.11.1 25",
#         "logging vrf vrf01 source-interface Ethernet1",
#         "logging vrf vrf02 host hostvrf1 protocol tcp",
#         "logging vrf vrf02 host 24.1.1.1 33"
#     ],
#

# Using replaced:
# Before State:

# test(config)#show running-config | section logging
# logging host 11.11.11.1 25
# logging host host01 514 protocol tcp
# logging vrf vrf02 host 24.1.1.1 33
# logging vrf vrf02 host hostvrf1 514 protocol tcp
# logging format timestamp traditional timezone
# logging vrf vrf01 source-interface Ethernet1
# logging policy match inverse-result match-list                           list01 discard
# logging persistent 4096
# !
# logging level AAA alerts
# test(config)#

- name: Repalce
  arista.eos.eos_logging_global:
    config:
      synchronous:
        set: true
      trap:
        severity: "critical"
      hosts:
        - name: "host02"
          protocol: "tcp"
      vrfs:
        - name: "vrf03"
          source_interface: "Vlan100"
        - name: "vrf04"
          hosts:
            - name: "hostvrf1"
              protocol: "tcp"

    state: replaced

# After State:
# test(config)#show running-config | section logging
# logging synchronous
# logging trap critical
# logging host host02 514 protocol tcp
# logging vrf vrf04 host hostvrf1 514 protocol tcp
# logging vrf vrf03 source-interface Vlan100
# test(config)#
#
# Module Execution:
# "after": {
#         "hosts": [
#             {
#                 "name": "host02",
#                 "port": 514,
#                 "protocol": "tcp"
#             }
#         ],
#         "synchronous": {
#             "set": true
#         },
#         "trap": {
#            "severity": "critical"
#         },
#         "vrfs": [
#             {
#                 "name": "vrf03",
#                 "source_interface": "Vlan100"
#             },
#             {
#                 "hosts": [
#                     {
#                         "name": "hostvrf1",
#                         "port": 514,
#                         "protocol": "tcp"
#                     }
#                 ],
#                 "name": "vrf04"
#             }
#         ]
#     },
#     "before": {
#         "format": {
#             "timestamp": {
#                 "traditional": {
#                     "timezone": true
#                 }
#             }
#         },
#         "hosts": [
#             {
#                 "name": "11.11.11.1",
#                 "port": 25
#             },
#             {
#                 "name": "host01",
#                 "port": 514,
#                 "protocol": "tcp"
#             }
#         ],
#         "level": {
#             "facility": "AAA",
#             "severity": "alerts"
#         },
#         "persistent": {
#             "size": 4096
#         },
#         "policy": {
#             "invert_result": true,
#             "match_list": "list01"
#         },
#         "vrfs": [
#             {
#                 "name": "vrf01",
#                 "source_interface": "Ethernet1"
#             },
#             {
#                 "hosts": [
#                     {
#                         "name": "24.1.1.1",
#                         "port": 33
#                     },
#                     {
#                         "name": "hostvrf1",
#                         "port": 514,
#                         "protocol": "tcp"
#                     }
#                 ],
#                 "name": "vrf02"
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#         "logging host host02 protocol tcp",
#         "no logging host 11.11.11.1 25",
#         "no logging host host01 514 protocol tcp",
#         "logging vrf vrf03 source-interface Vlan100",
#         "logging vrf vrf04 host hostvrf1 protocol tcp",
#         "no logging vrf vrf01 source-interface Ethernet1",
#         "no logging vrf vrf02 host 24.1.1.1 33",
#         "no logging vrf vrf02 host hostvrf1 514 protocol tcp",
#         "no logging format timestamp traditional timezone",
#         "no logging level AAA alerts",
#         "no logging persistent 4096",
#         "no logging policy match invert-result match-list list01 discard",
#         "logging synchronous",
#         "logging trap critical"
#     ],
#
#

# Using overridden:
# Before State:

# test(config)#show running-config | section logging
# logging host 11.11.11.1 25
# logging host host01 514 protocol tcp
# logging vrf vrf02 host 24.1.1.1 33
# logging vrf vrf02 host hostvrf1 514 protocol tcp
# logging format timestamp traditional timezone
# logging vrf vrf01 source-interface Ethernet1
# logging policy match inverse-result match-list                           list01 discard
# logging persistent 4096
# !
# logging level AAA alerts
# test(config)#

- name: Repalce
  arista.eos.eos_logging_global:
    config:
      synchronous:
        set: true
      trap:
        severity: "critical"
      hosts:
        - name: "host02"
          protocol: "tcp"
      vrfs:
        - name: "vrf03"
          source_interface: "Vlan100"
        - name: "vrf04"
          hosts:
            - name: "hostvrf1"
              protocol: "tcp"

    state: overridden

# After State:
# test(config)#show running-config | section logging
# logging synchronous
# logging trap critical
# logging host host02 514 protocol tcp
# logging vrf vrf04 host hostvrf1 514 protocol tcp
# logging vrf vrf03 source-interface Vlan100
# test(config)#
#
# Module Execution:
# "after": {
#         "hosts": [
#             {
#                 "name": "host02",
#                 "port": 514,
#                 "protocol": "tcp"
#             }
#         ],
#         "synchronous": {
#             "set": true
#         },
#         "trap": {
#            "severity": "critical"
#         },
#         "vrfs": [
#             {
#                 "name": "vrf03",
#                 "source_interface": "Vlan100"
#             },
#             {
#                 "hosts": [
#                     {
#                         "name": "hostvrf1",
#                         "port": 514,
#                         "protocol": "tcp"
#                     }
#                 ],
#                 "name": "vrf04"
#             }
#         ]
#     },
#     "before": {
#         "format": {
#             "timestamp": {
#                 "traditional": {
#                     "timezone": true
#                 }
#             }
#         },
#         "hosts": [
#             {
#                 "name": "11.11.11.1",
#                 "port": 25
#             },
#             {
#                 "name": "host01",
#                 "port": 514,
#                 "protocol": "tcp"
#             }
#         ],
#         "level": {
#             "facility": "AAA",
#             "severity": "alerts"
#         },
#         "persistent": {
#             "size": 4096
#         },
#         "policy": {
#             "invert_result": true,
#             "match_list": "list01"
#         },
#         "vrfs": [
#             {
#                 "name": "vrf01",
#                 "source_interface": "Ethernet1"
#             },
#             {
#                 "hosts": [
#                     {
#                         "name": "24.1.1.1",
#                         "port": 33
#                     },
#                     {
#                         "name": "hostvrf1",
#                         "port": 514,
#                         "protocol": "tcp"
#                     }
#                 ],
#                 "name": "vrf02"
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#         "logging host host02 protocol tcp",
#         "no logging host 11.11.11.1 25",
#         "no logging host host01 514 protocol tcp",
#         "logging vrf vrf03 source-interface Vlan100",
#         "logging vrf vrf04 host hostvrf1 protocol tcp",
#         "no logging vrf vrf01 source-interface Ethernet1",
#         "no logging vrf vrf02 host 24.1.1.1 33",
#         "no logging vrf vrf02 host hostvrf1 514 protocol tcp",
#         "no logging format timestamp traditional timezone",
#         "no logging level AAA alerts",
#         "no logging persistent 4096",
#         "no logging policy match invert-result match-list list01 discard",
#         "logging synchronous",
#         "logging trap critical"
#     ],
#
#

# Using deleted:

# Before State:
# test(config)#show running-config | section logging
# logging synchronous level critical
# logging host 11.11.11.1 25
# logging host host01 514 protocol tcp
# logging host host02 514 protocol tcp
# logging vrf vrf02 host 24.1.1.1 33
# logging vrf vrf02 host hostvrf1 514 protocol tcp
# logging vrf vrf04 host hostvrf1 514 protocol tcp
# logging vrf vrf01 source-interface Ethernet1
# logging vrf vrf03 source-interface Vlan100
# test(config)#

- name: Delete all logging configs
  arista.eos.eos_logging_global:
    state: deleted
  become: true

# After state:
# test(config)#show running-config | section logging
# test(config)#
#
# "after": {},
#     "before": {
#         "hosts": [
#             {
#                 "name": "11.11.11.1",
#                 "port": 25
#             },
#             {
#                 "name": "host01",
#                 "port": 514,
#                 "protocol": "tcp"
#             },
#             {
#                 "name": "host02",
#                 "port": 514,
#                 "protocol": "tcp"
#             }
#         ],
#         "synchronous": {
#             "level": "critical"
#         },
#         "vrfs": [
#             {
#                 "name": "vrf01",
#                 "source_interface": "Ethernet1"
#             },
#             {
#                 "hosts": [
#                     {
#                         "name": "24.1.1.1",
#                         "port": 33
#                     },
#                     {
#                         "name": "hostvrf1",
#                         "port": 514,
#                         "protocol": "tcp"
#                     }
#                 ],
#                 "name": "vrf02"
#             },
#             {
#                 "name": "vrf03",
#                 "source_interface": "Vlan100"
#             },
#             {
#                 "hosts": [
#                     {
#                         "name": "hostvrf1",
#                         "port": 514,
#                         "protocol": "tcp"
#                     }
#                 ],
#                 "name": "vrf04"
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#         "no logging host 11.11.11.1 25",
#         "no logging host host01 514 protocol tcp",
#         "no logging host host02 514 protocol tcp",
#         "no logging vrf vrf01 source-interface Ethernet1",
#         "no logging vrf vrf02 host 24.1.1.1 33",
#         "no logging vrf vrf02 host hostvrf1 514 protocol tcp",
#         "no logging vrf vrf03 source-interface Vlan100",
#         "no logging vrf vrf04 host hostvrf1 514 protocol tcp",
#         "no logging synchronous level critical"
#     ],

# Using parsed:
# parsed.cfg

# logging host 11.11.11.1 25
# logging host host01 514 protocol tcp
# logging vrf vrf02 host 24.1.1.1 33
# logging vrf vrf02 host hostvrf1 514 protocol tcp
# logging format timestamp traditional timezone
# logging vrf vrf01 source-interface Ethernet1
# logging policy match inverse-result match-list                           list01 discard
# logging persistent 4096
# !
# logging level AAA alerts

- name: parse configs
  arista.eos.eos_logging_global:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Module Execution
# "parsed": {
#         "format": {
#             "timestamp": {
#                 "traditional": {
#                     "timezone": true
#                 }
#             }
#         },
#         "hosts": [
#             {
#                 "name": "11.11.11.1",
#                 "port": 25
#             },
#             {
#                 "name": "host01",
#                 "port": 514,
#                 "protocol": "tcp"
#             }
#         ],
#         "level": {
#             "facility": "AAA",
#             "severity": "alerts"
#         },
#         "persistent": {
#             "size": 4096
#         },
#         "policy": {
#             "invert_result": true,
#             "match_list": "list01"
#         },
#         "vrfs": [
#             {
#                 "name": "vrf01",
#                 "source_interface": "Ethernet1"
#             },
#             {
#                 "hosts": [
#                     {
#                         "name": "24.1.1.1",
#                         "port": 33
#                     },
#                     {
#                         "name": "hostvrf1",
#                         "port": 514,
#                         "protocol": "tcp"
#                     }
#                 ],
#                 "name": "vrf02"
#             }
#         ]
#     }
#

# Using gathered:
# Before State:
# test(config)#show running-config | section logging
# logging host 11.11.11.1 25
# logging host host01 514 protocol tcp
# logging vrf vrf02 host 24.1.1.1 33
# logging vrf vrf02 host hostvrf1 514 protocol tcp
# logging format timestamp traditional timezone
# logging vrf vrf01 source-interface Ethernet1
# logging policy match inverse-result match-list                           list01 discard
# logging persistent 4096
# !
# logging level AAA alerts
# test(config)#

- name: gather configs
  arista.eos.eos_logging_global:
    state: gathered

# Module Execution:
# "gathered": {
#         "format": {
#             "timestamp": {
#                 "traditional": {
#                     "timezone": true
#                 }
#             }
#         },
#         "hosts": [
#             {
#                 "name": "11.11.11.1",
#                 "port": 25
#             },
#             {
#                 "name": "host01",
#                 "port": 514,
#                 "protocol": "tcp"
#             }
#         ],
#         "level": {
#             "facility": "AAA",
#             "severity": "alerts"
#         },
#         "persistent": {
#             "size": 4096
#         },
#         "policy": {
#             "invert_result": true,
#             "match_list": "list01"
#         },
#         "vrfs": [
#             {
#                 "name": "vrf01",
#                 "source_interface": "Ethernet1"
#             },
#             {
#                 "hosts": [
#                     {
#                         "name": "24.1.1.1",
#                         "port": 33
#                     },
#                     {
#                         "name": "hostvrf1",
#                         "port": 514,
#                         "protocol": "tcp"
#                     }
#                 ],
#                 "name": "vrf02"
#             }
#         ]
#     },
#

# Using rendered:
- name: Render provided configuration
  arista.eos.eos_logging_global:
    config:
      format:
        timestamp:
          traditional:
            timezone: true
      level:
        facility: "AAA"
        severity: "alerts"
      persistent:
        size: 4096
      policy:
        invert_result: true
        match_list: "list01"
      hosts:
        - name: "host01"
          protocol: "tcp"
        - name: "11.11.11.1"
          port: 25
      vrfs:
        - name: "vrf01"
          source_interface: "Ethernet1"
        - name: "vrf02"
          hosts:
            - name: "hostvrf1"
              protocol: "tcp"
            - name: "24.1.1.1"
              port: "33"
# Module Execution:

# "rendered": [
#         "logging host host01 protocol tcp",
#         "logging host 11.11.11.1 25",
#         "logging vrf vrf01 source-interface Ethernet1",
#         "logging vrf vrf02 host hostvrf1 protocol tcp",
#         "logging vrf vrf02 host 24.1.1.1 33",
#         "logging format timestamp traditional timezone",
#         "logging level AAA alerts",
#         "logging persistent 4096",
#         "logging policy match invert-result match-list list01 discard"
#     ]
#
```

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
