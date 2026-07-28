---
collection: ansible
version: "8"
title: "cisco.ios.ios_service module – Resource module to configure service."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_service_module.html
fetched_at: 2026-07-28T01:26:26+00:00
---
# cisco.ios.ios_service module – Resource module to configure service.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_service`.

New in cisco.ios 4.6.0

- [Synopsis](ios_service_module.md#synopsis)
- [Parameters](ios_service_module.md#parameters)
- [Notes](ios_service_module.md#notes)
- [Examples](ios_service_module.md#examples)
- [Return Values](ios_service_module.md#return-values)

## [Synopsis](ios_service_module.md#id1)

- This module configures and manages service attributes on IOS platforms

Aliases: service

## [Parameters](ios_service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionnary of service configuration |
| **call_home**  boolean | Cisco call-home service  **Choices:**   - `false` - `true` |
| **compress_config**  boolean | Compress the nvram configuration file  **Choices:**   - `false` - `true` |
| **config**  boolean | TFTP load config files  **Choices:**   - `false` - `true` |
| **counters**  integer | Control aging of interface counters by setting the maximum counter aging threshold  **Default:** `0` |
| **dhcp**  boolean | Enable DHCP server and relay agent  **Choices:**   - `false` - `true` ← (default) |
| **disable_ip_fast_frag**  boolean | Disable IP particle-based fast fragmentation  **Choices:**   - `false` - `true` |
| **exec_callback**  boolean | Enable exec callback  **Choices:**   - `false` - `true` |
| **exec_wait**  boolean | Delay EXEC startup on noisy lines  **Choices:**   - `false` - `true` |
| **hide_telnet_addresses**  boolean | Hide destination addresses in telnet command  **Choices:**   - `false` - `true` |
| **internal**  boolean | Enable/Disable Internal commands  **Choices:**   - `false` - `true` |
| **linenumber**  boolean | enable line number banner for each exec  **Choices:**   - `false` - `true` |
| **log**  boolean | log backtrace  **Choices:**   - `false` - `true` |
| **log_hidden**  boolean | Enable syslog msgs for hidden/internal commands  **Choices:**   - `false` - `true` |
| **nagle**  boolean | Enable Nagle’s congestion control algorithm  **Choices:**   - `false` - `true` |
| **old_slip_prompts**  boolean | Allow old scripts to operate with slip/ppp  **Choices:**   - `false` - `true` |
| **pad**  boolean | Enable PAD commands  **Choices:**   - `false` - `true` |
| **pad_cmns**  boolean | Enable PAD over CMNS connections  **Choices:**   - `false` - `true` |
| **pad_from_xot**  boolean | Accept XOT to PAD connections  **Choices:**   - `false` - `true` |
| **pad_to_xot**  boolean | Allow outgoing PAD over XOT connections  **Choices:**   - `false` - `true` |
| **password_encryption**  boolean | Encrypt system passwords  **Choices:**   - `false` - `true` |
| **password_recovery**  boolean | Password recovery  **Choices:**   - `false` - `true` ← (default) |
| **private_config_encryption**  boolean | Enable private config file encryption  **Choices:**   - `false` - `true` |
| **prompt**  boolean | Enable mode specific prompt  **Choices:**   - `false` - `true` ← (default) |
| **pt_vty_logging**  boolean | Log significant VTY-Async events  **Choices:**   - `false` - `true` |
| **scripting**  boolean | scripting  **Choices:**   - `false` - `true` |
| **sequence_numbers**  boolean | Stamp logger messages with a sequence number  **Choices:**   - `false` - `true` |
| **slave_coredump**  boolean | slave-coredump  **Choices:**   - `false` - `true` |
| **slave_log**  boolean | Enable log capability of slave IPs  **Choices:**   - `false` - `true` ← (default) |
| **tcp_keepalives_in**  boolean | Generate keepalives on idle incoming network connections  **Choices:**   - `false` - `true` |
| **tcp_keepalives_out**  boolean | Generate keepalives on idle outgoing network connections  **Choices:**   - `false` - `true` |
| **tcp_small_servers**  dictionary | TCP and UDP small servers are servers (daemons, in Unix parlance) that run in the router which are useful for diagnostics. |
| **enable**  boolean | Enable small TCP servers (e.g., ECHO)  **Choices:**   - `false` - `true` |
| **max_servers**  string | Set number of allowable TCP small servers  1 to 2147483647 or no-limit |
| **telnet_zeroidle**  boolean | Set TCP window 0 when connection is idle  **Choices:**   - `false` - `true` |
| **timestamps**  list / elements=dictionary | Timestamp debug/log messages |
| **datetime_options**  dictionary | Options for date and time timestamp |
| **localtime**  boolean | Use local time zone for timestamps  **Choices:**   - `false` - `true` |
| **msec**  boolean | Include milliseconds in timestamp  **Choices:**   - `false` - `true` |
| **show_timezone**  boolean | Add time zone information to timestamp  **Choices:**   - `false` - `true` |
| **year**  boolean | Include year in timestam  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable timestamp for the choosen message  **Choices:**   - `false` - `true` |
| **msg**  string | Timestamp log or debug messages  **Choices:**   - `"debug"` - `"log"` |
| **timestamp**  string | Timestamp with date and time or with system uptime  **Choices:**   - `"datetime"` - `"uptime"` |
| **udp_small_servers**  dictionary | TCP and UDP small servers are servers (daemons, in Unix parlance) that run in the router which are useful for diagnostics. |
| **enable**  boolean | Enable small UDP servers (e.g., ECHO)  **Choices:**   - `false` - `true` |
| **max_servers**  string | Set number of allowable TCP small servers  1 to 2147483647 or no-limit |
| **unsupported_transceiver**  boolean | enable support for third-party transceivers  **Choices:**   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^service|^no service**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](ios_service_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 16.9
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_service_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------

# router-ios#show running-config all | section ^service
# service slave-log
# service timestamps debug datetime msec
# service timestamps log datetime msec
# service private-config-encryption
# service prompt config
# service counters max age 0
# service dhcp
# service call-home
# service password-recovery

- name: Merge provided configuration with device configuration
  cisco.ios.ios_service:
    config:
      tcp_keepalives_in: true
      tcp_keepalives_out: true
      timestamps:
        - msg: debug
          enable: true
          timestamp: datetime
        - msg: log
          enable: true
          timestamp: datetime
      pad: false
      password_encryption: true
    state: merged

# Task Output
# -----------
#
# before:
#   call_home: true
#   counters: 0
#   dhcp: true
#   password_recovery: true
#   private_config_encryption: true
#   prompt: true
#   slave_log: true
#   timestamps:
#   - datetime_options:
#       msec: true
#     msg: debug
#     timestamp: datetime
#   - datetime_options:
#       msec: true
#     msg: log
#     timestamp: datetime
# commands:
# - service password-encryption
# - service tcp-keepalives-in
# - service tcp-keepalives-out
# after:
#   call_home: true
#   counters: 0
#   dhcp: true
#   password_encryption: true
#   password_recovery: true
#   private_config_encryption: true
#   prompt: true
#   slave_log: true
#   tcp_keepalives_in: true
#   tcp_keepalives_out: true
#   timestamps:
#   - datetime_options:
#       msec: true
#     msg: debug
#     timestamp: datetime
#   - datetime_options:
#       msec: true
#     msg: log
#     timestamp: datetime

# After state:
# ------------

# router-ios#show running-config all | section ^service
# service slave-log
# service tcp-keepalives-in
# service tcp-keepalives-out
# service timestamps debug datetime msec
# service timestamps log datetime msec
# service password-encryption
# service private-config-encryption
# service prompt config
# service counters max age 0
# service dhcp
# service call-home
# service password-recovery

# Using replaced

# Before state:
# -------------

# router-ios#show running-config all | section ^service
# service slave-log
# service tcp-keepalives-in
# service tcp-keepalives-out
# service timestamps debug datetime msec
# service timestamps log datetime msec
# service password-encryption
# service private-config-encryption
# service prompt config
# service counters max age 0
# service dhcp
# service call-home
# service password-recovery

- name: Replaces device configuration of services with provided configuration
  cisco.ios.ios_service:
    config:
      timestamps:
        - msg: log
          enable: true
          timestamp: datetime
          datetime_options:
            localtime: true
            msec: true
            show_timezone: true
            year: true
        - msg: debug
          enable: true
          timestamp: datetime
      pad: false
      password_encryption: true
    state: "replaced"

# Task Output
# -----------
#
# before:
#   call_home: true
#   counters: 0
#   dhcp: true
#   password_encryption: true
#   password_recovery: true
#   private_config_encryption: true
#   prompt: true
#   slave_log: true
#   tcp_keepalives_in: true
#   tcp_keepalives_out: true
#   timestamps:
#   - datetime_options:
#       msec: true
#     msg: debug
#     timestamp: datetime
#   - datetime_options:
#       msec: true
#     msg: log
#     timestamp: datetime
# commands:
# - no service call-home
# - no service tcp-keepalives-in
# - no service tcp-keepalives-out
# - no service timestamps log
# - service timestamps log datetime msec localtime show-timezone year
# - no service timestamps debug
# - service timestamps debug datetime
# after:
#   counters: 0
#   dhcp: true
#   password_encryption: true
#   password_recovery: true
#   private_config_encryption: true
#   prompt: true
#   slave_log: true
#   timestamps:
#   - msg: debug
#     timestamp: datetime
#   - datetime_options:
#       localtime: true
#       msec: true
#       show_timezone: true
#       year: true
#     msg: log
#     timestamp: datetime

# After state:
# ------------

# router-ios#show running-config all | section ^service
# service slave-log
# service timestamps debug datetime
# service timestamps log datetime msec localtime show-timezone year
# service password-encryption
# service private-config-encryption
# service prompt config
# service counters max age 0
# service dhcp
# service password-recovery

# Using Deleted

# Before state:
# -------------

# router-ios#show running-config all | section ^service
# service slave-log
# service timestamps debug datetime
# service timestamps log datetime msec localtime show-timezone year
# service password-encryption
# service private-config-encryption
# service prompt config
# service counters max age 0
# service dhcp
# service password-recovery

- name: "Delete service configuration and restore default configuration for some importants service (those with a default value in module)"
  cisco.ios.ios_service:
    state: deleted

# Task Output
# -----------
#
# before:
#   counters: 0
#   dhcp: true
#   password_encryption: true
#   password_recovery: true
#   private_config_encryption: true
#   prompt: true
#   slave_log: true
#   timestamps:
#   - msg: debug
#     timestamp: datetime
#   - datetime_options:
#       localtime: true
#       msec: true
#       show_timezone: true
#       year: true
#     msg: log
#     timestamp: datetime
# commands:
# - no service password-encryption
# - no service timestamps debug
# - no service timestamps log
# after:
#   counters: 0
#   dhcp: true
#   password_recovery: true
#   private_config_encryption: true
#   prompt: true
#   slave_log: true

#·After·state:
#·------------
#
# router-ios#show running-config all | section ^service
# service slave-log
# service private-config-encryption
# service prompt config
# service counters max age 0
# service dhcp
# service password-recovery

# Using gathered

# Before state:
# -------------
#
# router-ios#show running-config all | section ^service
# service slave-log
# service timestamps debug datetime
# service timestamps log datetime msec localtime show-timezone year
# service password-encryption
# service private-config-encryption
# service prompt config
# service counters max age 0
# service dhcp
# service password-recovery

- name: Gather facts of interfaces
  cisco.ios.ios_service:
    config:
    state: gathered

# Task Output
# -----------
#
# gathered:
#   counters: 0
#   dhcp: true
#   password_encryption: true
#   password_recovery: true
#   private_config_encryption: true
#   prompt: true
#   slave_log: true
#   timestamps:
#   - msg: debug
#     timestamp: datetime
#   - datetime_options:
#       localtime: true
#       msec: true
#       show_timezone: true
#       year: true
#     msg: log
#     timestamp: datetime

# Using rendered

- name: Render the commands for provided configuration
  cisco.ios.ios_service:
    config:
      timestamps:
        - msg: log
          enable: true
          timestamp: datetime
          datetime_options:
            localtime: true
            msec: true
            show_timezone: true
            year: true
        - msg: debug
          enable: true
          timestamp: datetime
      pad: false
      password_encryption: true
    state: rendered

# ·Task·Output
# -----------
#
# rendered:
# - service dhcp
# - service password-encryption
# - service password-recovery
# - service prompt config
# - service slave-log
# - service timestamps log datetime msec localtime show-timezone year
# - service timestamps debug datetime

# Using parsed

# File: parsed.cfg
# ----------------
#
# no service pad
# service password-encryption
# service tcp-keepalives-in
# service tcp-keepalives-out
# service timestamps debug datetime msec localtime show-timezone year
# service timestamps log datetime msec localtime show-timezone year
# service counters max age 5

- name: Parse the provided configuration
  cisco.ios.ios_service:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task Output
# -----------
#
# parsed:
#   counters: 5
#   dhcp: true
#   password_encryption: true
#   password_recovery: true
#   prompt: true
#   slave_log: true
#   tcp_keepalives_in: true
#   tcp_keepalives_out: true
#   timestamps:
#   - datetime_options:
#       localtime: true
#       msec: true
#       show_timezone: true
#       year: true
#     msg: debug
#     timestamp: datetime
#   - datetime_options:
#       localtime: true
#       msec: true
#       show_timezone: true
#       year: true
#     msg: log
#     timestamp: datetime
```

## [Return Values](ios_service_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["no service config", "service tcp-keepalives-in", "service tcp-keepalives-out"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["service dhcp", "service password-encryption", "service password-recovery", "service prompt config", "service slave-log"]` |

### Authors

- Ambroise Rosset (@earendilfr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
