---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_logging_global module – Logging resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_logging_global_module.html
fetched_at: 2026-07-28T02:59:19+00:00
---
# vyos.vyos.vyos_logging_global module – Logging resource module

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
> To use it in a playbook, specify: `vyos.vyos.vyos_logging_global`.

New in vyos.vyos 2.4.0

- [Synopsis](vyos_logging_global_module.md#synopsis)
- [Parameters](vyos_logging_global_module.md#parameters)
- [Notes](vyos_logging_global_module.md#notes)
- [Examples](vyos_logging_global_module.md#examples)
- [Return Values](vyos_logging_global_module.md#return-values)

## [Synopsis](vyos_logging_global_module.md#id1)

- This module manages the logging attributes of Vyos network devices

Aliases: logging_global

## [Parameters](vyos_logging_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list containing dictionary of logging options |
| **console**  dictionary | logging to serial console |
| **facilities**  list / elements=dictionary | facility configurations for console |
| **facility**  string | Facility for logging  **Choices:**   - `"all"` - `"auth"` - `"authpriv"` - `"cron"` - `"daemon"` - `"kern"` - `"lpr"` - `"mail"` - `"mark"` - `"news"` - `"protocols"` - `"security"` - `"syslog"` - `"user"` - `"uucp"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **severity**  string | logging level  **Choices:**   - `"emerg"` - `"alert"` - `"crit"` - `"err"` - `"warning"` - `"notice"` - `"info"` - `"debug"` - `"all"` |
| **state**  string | enable or disable the command  **Choices:**   - `"enabled"` - `"disabled"` |
| **files**  list / elements=dictionary | logging to file |
| **archive**  dictionary | Log file size and rotation characteristics |
| **file_num**  integer | Number of saved files (default is 5) |
| **size**  integer | Size of log files (in kilobytes, default is 256) |
| **state**  string | enable or disable the command  **Choices:**   - `"enabled"` - `"disabled"` |
| **facilities**  list / elements=dictionary | facility configurations |
| **facility**  string | Facility for logging  **Choices:**   - `"all"` - `"auth"` - `"authpriv"` - `"cron"` - `"daemon"` - `"kern"` - `"lpr"` - `"mail"` - `"mark"` - `"news"` - `"protocols"` - `"security"` - `"syslog"` - `"user"` - `"uucp"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **severity**  string | logging level  **Choices:**   - `"emerg"` - `"alert"` - `"crit"` - `"err"` - `"warning"` - `"notice"` - `"info"` - `"debug"` - `"all"` |
| **path**  string | file name or path |
| **global_params**  dictionary | logging to serial console |
| **archive**  dictionary | Log file size and rotation characteristics |
| **file_num**  integer | Number of saved files (default is 5) |
| **size**  integer | Size of log files (in kilobytes, default is 256) |
| **state**  string | enable or disable the command  **Choices:**   - `"enabled"` - `"disabled"` |
| **facilities**  list / elements=dictionary | facility configurations |
| **facility**  string | Facility for logging  **Choices:**   - `"all"` - `"auth"` - `"authpriv"` - `"cron"` - `"daemon"` - `"kern"` - `"lpr"` - `"mail"` - `"mark"` - `"news"` - `"protocols"` - `"security"` - `"syslog"` - `"user"` - `"uucp"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **severity**  string | logging level  **Choices:**   - `"emerg"` - `"alert"` - `"crit"` - `"err"` - `"warning"` - `"notice"` - `"info"` - `"debug"` - `"all"` |
| **marker_interval**  integer | time interval how often a mark message is being sent in seconds (default is 1200) |
| **preserve_fqdn**  boolean | uses FQDN for logging  **Choices:**   - `false` - `true` |
| **state**  string | enable or disable the command  **Choices:**   - `"enabled"` - `"disabled"` |
| **hosts**  list / elements=dictionary | logging to serial console |
| **facilities**  list / elements=dictionary | facility configurations for host |
| **facility**  string | Facility for logging  **Choices:**   - `"all"` - `"auth"` - `"authpriv"` - `"cron"` - `"daemon"` - `"kern"` - `"lpr"` - `"mail"` - `"mark"` - `"news"` - `"protocols"` - `"security"` - `"syslog"` - `"user"` - `"uucp"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **protocol**  string | syslog communication protocol  **Choices:**   - `"udp"` - `"tcp"` |
| **severity**  string | logging level  **Choices:**   - `"emerg"` - `"alert"` - `"crit"` - `"err"` - `"warning"` - `"notice"` - `"info"` - `"debug"` - `"all"` |
| **hostname**  string | Remote host name or IP address |
| **port**  integer | Destination port (1-65535) |
| **syslog**  dictionary | logging syslog |
| **state**  string | enable or disable the command  **Choices:**   - `"enabled"` - `"disabled"` |
| **users**  list / elements=dictionary | logging to file |
| **facilities**  list / elements=dictionary | facility configurations |
| **facility**  string | Facility for logging  **Choices:**   - `"all"` - `"auth"` - `"authpriv"` - `"cron"` - `"daemon"` - `"kern"` - `"lpr"` - `"mail"` - `"mark"` - `"news"` - `"protocols"` - `"security"` - `"syslog"` - `"user"` - `"uucp"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **severity**  string | logging level  **Choices:**   - `"emerg"` - `"alert"` - `"crit"` - `"err"` - `"warning"` - `"notice"` - `"info"` - `"debug"` - `"all"` |
| **username**  string | user login name |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VYOS device by executing the command **show configuration commands | grep syslog**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *replaced* and *overridden* have identical behaviour for this module.  Refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](vyos_logging_global_module.md#id3)

> **Note:**
>
> - Tested against vyos 1.2
> - This module works with connection `network_cli`.
> - The Configuration defaults of the Vyos network devices are supposed to hinder idempotent behavior of plays

## [Examples](vyos_logging_global_module.md#id4)

```yaml+jinja
# Using state: merged

# Before state:
# -------------

# vyos:~$show configuration commands | grep syslog

- name: Apply the provided configuration
  vyos.vyos.vyos_logging_global:
    config:
      console:
        facilities:
          - facility: local7
            severity: err
      files:
        - path: logFile
          archive:
            file_num: 2
          facilities:
            - facility: local6
              severity: emerg
      hosts:
        - hostname: 172.16.0.1
          facilities:
            - facility: local7
              severity: all
            - facility: all
              protocol: udp
          port: 223
      users:
        - username: vyos
          facilities:
          - facility: local7
            severity: debug
      global_params:
        archive:
          file_num: 2
          size: 111
        facilities:
        - facility: cron
          severity: debug
        marker_interval: 111
        preserve_fqdn: true
    state: merged

# Commands Fired:
# ---------------

# "commands": [
#     "set system syslog console facility local7 level err",
#     "set system syslog file logFile archive file 2",
#     "set system syslog host 172.16.0.1 facility local7 level all",
#     "set system syslog file logFile facility local6 level emerg",
#     "set system syslog host 172.16.0.1 facility all protocol udp",
#     "set system syslog user vyos facility local7 level debug",
#     "set system syslog host 172.16.0.1 port 223",
#     "set system syslog global facility cron level debug",
#     "set system syslog global archive file 2",
#     "set system syslog global archive size 111",
#     "set system syslog global marker interval 111",
#     "set system syslog global preserve-fqdn"
# ],

# After state:
# ------------

# vyos:~$ show configuration commands | grep syslog
# set system syslog console facility local7 level 'err'
# set system syslog file logFile archive file '2'
# set system syslog file logFile facility local6 level 'emerg'
# set system syslog global archive file '2'
# set system syslog global archive size '111'
# set system syslog global facility cron level 'debug'
# set system syslog global marker interval '111'
# set system syslog global preserve-fqdn
# set system syslog host 172.16.0.1 facility all protocol 'udp'
# set system syslog host 172.16.0.1 facility local7 level 'all'
# set system syslog host 172.16.0.1 port '223'
# set system syslog user vyos facility local7 level 'debug'

# Using state: deleted

# Before state:
# -------------

# vyos:~$show configuration commands | grep syslog
# set system syslog console facility local7 level 'err'
# set system syslog file logFile archive file '2'
# set system syslog file logFile facility local6 level 'emerg'
# set system syslog global archive file '2'
# set system syslog global archive size '111'
# set system syslog global facility cron level 'debug'
# set system syslog global marker interval '111'
# set system syslog global preserve-fqdn
# set system syslog host 172.16.0.1 facility all protocol 'udp'
# set system syslog host 172.16.0.1 facility local7 level 'all'
# set system syslog host 172.16.0.1 port '223'
# set system syslog user vyos facility local7 level 'debug'

- name: delete the existing configuration
  vyos.vyos.vyos_logging_global:
    state: deleted

# Commands Fired:
# ---------------

# "commands": [
#     "delete system syslog"
# ],

# After state:
# ------------

# vyos:~$show configuration commands | grep syslog

# Using state: overridden

# Before state:
# -------------

# vyos:~$show configuration commands | grep syslog
# set system syslog console facility local7 level 'err'
# set system syslog file logFile archive file '2'
# set system syslog file logFile facility local6 level 'emerg'
# set system syslog global archive file '2'
# set system syslog global archive size '111'
# set system syslog global facility cron level 'debug'
# set system syslog global marker interval '111'
# set system syslog global preserve-fqdn
# set system syslog host 172.16.0.1 facility all protocol 'udp'
# set system syslog host 172.16.0.1 facility local7 level 'all'
# set system syslog host 172.16.0.1 port '223'
# set system syslog user vyos facility local7 level 'debug'

- name: Override the current configuration
  vyos.vyos.vyos_logging_global:
    config:
      console:
        facilities:
          - facility: all
          - facility: local7
            severity: err
          - facility: news
            severity: debug
      files:
        - path: logFileNew
      hosts:
        - hostname: 172.16.0.2
          facilities:
            - facility: local5
              severity: all
      global_params:
        archive:
          file_num: 10
    state: overridden

# Commands Fired:
# ---------------

# "commands": [
#     "delete system syslog file logFile",
#     "delete system syslog global facility cron",
#     "delete system syslog host 172.16.0.1",
#     "delete system syslog user vyos",
#     "set system syslog console facility all",
#     "set system syslog console facility news level debug",
#     "set system syslog file logFileNew",
#     "set system syslog host 172.16.0.2 facility local5 level all",
#     "set system syslog global archive file 10",
#     "delete system syslog global archive size 111",
#     "delete system syslog global marker",
#     "delete system syslog global preserve-fqdn"
# ],

# After state:
# ------------

# vyos:~$show configuration commands | grep syslog
# set system syslog console facility all
# set system syslog console facility local7 level 'err'
# set system syslog console facility news level 'debug'
# set system syslog file logFileNew
# set system syslog global archive file '10'
# set system syslog host 172.16.0.2 facility local5 level 'all'

# Using state: replaced

# Before state:
# -------------

# vyos:~$show configuration commands | grep syslog
# set system syslog console facility all
# set system syslog console facility local7 level 'err'
# set system syslog console facility news level 'debug'
# set system syslog file logFileNew
# set system syslog global archive file '10'
# set system syslog host 172.16.0.2 facility local5 level 'all'

- name: Replace with the provided configuration
  register: result
  vyos.vyos.vyos_logging_global:
    config:
      console:
        facilities:
          - facility: local6
      users:
        - username: paul
          facilities:
          - facility: local7
            severity: err
    state: replaced

# Commands Fired:
# ---------------

# "commands": [
#     "delete system syslog console facility all",
#     "delete system syslog console facility local7",
#     "delete system syslog console facility news",
#     "delete system syslog file logFileNew",
#     "delete system syslog global archive file 10",
#     "delete system syslog host 172.16.0.2",
#     "set system syslog console facility local6",
#     "set system syslog user paul facility local7 level err"
# ],

# After state:
# ------------

# vyos:~$show configuration commands | grep syslog
# set system syslog console facility local6
# set system syslog user paul facility local7 level 'err'

# Using state: gathered

- name: Gather logging config
  vyos.vyos.vyos_logging_global:
    state: gathered

# Module Execution Result:
# ------------------------

# "gathered": {
#     "console": {
#         "facilities": [
#             {
#                 "facility": "local6"
#             },
#             {
#                 "facility": "local7",
#                 "severity": "err"
#             }
#         ]
#     },
#     "files": [
#         {
#             "archive": {
#                 "file_num": 2
#             },
#             "facilities": [
#                 {
#                     "facility": "local6",
#                     "severity": "emerg"
#                 }
#             ],
#             "path": "logFile"
#         }
#     ],
#     "global_params": {
#         "archive": {
#             "file_num": 2,
#             "size": 111
#         },
#         "facilities": [
#             {
#                 "facility": "cron",
#                 "severity": "debug"
#             }
#         ],
#         "marker_interval": 111,
#         "preserve_fqdn": true
#     },
#     "hosts": [
#         {
#             "facilities": [
#                 {
#                     "facility": "all",
#                     "protocol": "udp"
#                 },
#                 {
#                     "facility": "local7",
#                     "severity": "all"
#                 }
#             ],
#             "hostname": "172.16.0.1",
#             "port": 223
#         }
#     ],
#     "users": [
#         {
#             "facilities": [
#                 {
#                     "facility": "local7",
#                     "severity": "err"
#                 }
#             ],
#             "username": "paul"
#         },
#         {
#             "facilities": [
#                 {
#                     "facility": "local7",
#                     "severity": "debug"
#                 }
#             ],
#             "username": "vyos"
#         }
#     ]
# },

# After state:
# ------------

# vyos:~$show configuration commands | grep syslog
# set system syslog console facility local6
# set system syslog console facility local7 level 'err'
# set system syslog file logFile archive file '2'
# set system syslog file logFile facility local6 level 'emerg'
# set system syslog global archive file '2'
# set system syslog global archive size '111'
# set system syslog global facility cron level 'debug'
# set system syslog global marker interval '111'
# set system syslog global preserve-fqdn
# set system syslog host 172.16.0.1 facility all protocol 'udp'
# set system syslog host 172.16.0.1 facility local7 level 'all'
# set system syslog host 172.16.0.1 port '223'
# set system syslog user paul facility local7 level 'err'
# set system syslog user vyos facility local7 level 'debug'

# Using state: rendered

- name: Render the provided configuration
  vyos.vyos.vyos_logging_global:
    config:
      console:
        facilities:
          - facility: local7
            severity: err
      files:
        - path: logFile
          archive:
            file_num: 2
          facilities:
            - facility: local6
              severity: emerg
      hosts:
        - hostname: 172.16.0.1
          facilities:
            - facility: local7
              severity: all
            - facility: all
              protocol: udp
          port: 223
      users:
        - username: vyos
          facilities:
            - facility: local7
              severity: debug
      global_params:
        archive:
          file_num: 2
          size: 111
        facilities:
          - facility: cron
            severity: debug
        marker_interval: 111
        preserve_fqdn: true
    state: rendered

# Module Execution Result:
# ------------------------

# "rendered": [
#     "set system syslog console facility local7 level err",
#     "set system syslog file logFile facility local6 level emerg",
#     "set system syslog file logFile archive file 2",
#     "set system syslog host 172.16.0.1 facility local7 level all",
#     "set system syslog host 172.16.0.1 facility all protocol udp",
#     "set system syslog host 172.16.0.1 port 223",
#     "set system syslog user vyos facility local7 level debug",
#     "set system syslog global facility cron level debug",
#     "set system syslog global archive file 2",
#     "set system syslog global archive size 111",
#     "set system syslog global marker interval 111",
#     "set system syslog global preserve-fqdn"
# ]

# Using state: parsed

# File: parsed.cfg
# ----------------

# set system syslog console facility local6
# set system syslog console facility local7 level 'err'
# set system syslog file logFile archive file '2'
# set system syslog file logFile facility local6 level 'emerg'
# set system syslog global archive file '2'
# set system syslog global archive size '111'
# set system syslog global facility cron level 'debug'
# set system syslog global marker interval '111'
# set system syslog global preserve-fqdn
# set system syslog host 172.16.0.1 facility all protocol 'udp'
# set system syslog host 172.16.0.1 facility local7 level 'all'
# set system syslog host 172.16.0.1 port '223'
# set system syslog user paul facility local7 level 'err'
# set system syslog user vyos facility local7 level 'debug'

- name: Parse the provided configuration
  vyos.vyos.vyos_logging_global:
    running_config: "{{ lookup('file', 'parsed_vyos.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------

# "parsed": {
#     "console": {
#         "facilities": [
#             {
#                 "facility": "local6"
#             },
#             {
#                 "facility": "local7",
#                 "severity": "err"
#             }
#         ]
#     },
#     "files": [
#         {
#             "archive": {
#                 "file_num": 2
#             },
#             "facilities": [
#                 {
#                     "facility": "local6",
#                     "severity": "emerg"
#                 }
#             ],
#             "path": "logFile"
#         }
#     ],
#     "global_params": {
#         "archive": {
#             "file_num": 2,
#             "size": 111
#         },
#         "facilities": [
#             {
#                 "facility": "cron",
#                 "severity": "debug"
#             }
#         ],
#         "marker_interval": 111,
#         "preserve_fqdn": true
#     },
#     "hosts": [
#         {
#             "facilities": [
#                 {
#                     "facility": "all",
#                     "protocol": "udp"
#                 },
#                 {
#                     "facility": "local7",
#                     "severity": "all"
#                 }
#             ],
#             "hostname": "172.16.0.1",
#             "port": 223
#         }
#     ],
#     "users": [
#         {
#             "facilities": [
#                 {
#                     "facility": "local7",
#                     "severity": "err"
#                 }
#             ],
#             "username": "paul"
#         },
#         {
#             "facilities": [
#                 {
#                     "facility": "local7",
#                     "severity": "debug"
#                 }
#             ],
#             "username": "vyos"
#         }
#     ]
#   }
# }
```

## [Return Values](vyos_logging_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `["set system syslog console facility local7 level err", "set system syslog host 172.16.0.1 port 223", "set system syslog global archive size 111"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when state is *parsed*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when state is *rendered*  **Sample:** `["set system syslog host 172.16.0.1 port 223", "set system syslog user vyos facility local7 level debug", "set system syslog global facility cron level debug"]` |

### Authors

- Sagar Paul (@KB-perByte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
