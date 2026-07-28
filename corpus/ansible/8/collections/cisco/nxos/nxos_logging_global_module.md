---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_logging_global module – Logging resource module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_logging_global_module.html
fetched_at: 2026-07-28T01:38:53+00:00
---
# cisco.nxos.nxos_logging_global module – Logging resource module.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_logging_global`.

New in cisco.nxos 2.5.0

- [Synopsis](nxos_logging_global_module.md#synopsis)
- [Parameters](nxos_logging_global_module.md#parameters)
- [Notes](nxos_logging_global_module.md#notes)
- [Examples](nxos_logging_global_module.md#examples)
- [Return Values](nxos_logging_global_module.md#return-values)

## [Synopsis](nxos_logging_global_module.md#id1)

- This module manages logging configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: logging_global

## [Parameters](nxos_logging_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of logging configuration. |
| **console**  dictionary | Set console logging parameters. |
| **severity**  string | Set severity severity for console.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **state**  string | Enable or disable monitor logging.  **Choices:**   - `"enabled"` - `"disabled"` |
| **event**  dictionary | Interface events. |
| **link_status**  dictionary | UPDOWN and CHANGE messages. |
| **default**  boolean | Default logging configuration used by interfaces not explicitly configured.  **Choices:**   - `false` - `true` |
| **enable**  boolean | To enable logging overriding port severity configuration.  **Choices:**   - `false` - `true` |
| **trunk_status**  dictionary | TRUNK status messages. |
| **default**  boolean | Default logging configuration used by interfaces not explicitly configured.  **Choices:**   - `false` - `true` |
| **enable**  boolean | To enable logging overriding port severity configuration.  **Choices:**   - `false` - `true` |
| **facilities**  list / elements=dictionary | Facility parameter for syslog messages. |
| **facility**  string | Facility name. |
| **severity**  string | Set severity severity for console.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **history**  dictionary | Modifies severity severity or size for history table. |
| **severity**  string | Set severity severity for console.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **size**  integer | Set history table size. |
| **hosts**  list / elements=dictionary | Enable forwarding to Remote Syslog Servers. |
| **facility**  string | Facility to use when forwarding to server. |
| **host**  string | Hostname/IPv4/IPv6 address of the Remote Syslog Server. |
| **port**  integer | Destination Port when forwarding to remote server. |
| **secure**  dictionary | Enable secure connection to remote server. |
| **trustpoint**  dictionary | Trustpoint configuration. |
| **client_identity**  string | Client Identity certificate for mutual authentication.  Trustpoint to use for client certificate authentication. |
| **severity**  string | Set severity severity for console.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **use_vrf**  string | Display per-VRF information.  This option is unsupported on MDS switches. |
| **ip**  dictionary | IP configuration.  This option is unsupported on MDS switches. |
| **access_list**  dictionary | Access-List. |
| **cache**  dictionary | Set caching settings. |
| **entries**  integer | Maximum number of log entries cached in software. |
| **interval**  integer | Log-update interval (in sec). |
| **threshold**  integer | Log-update threshold (number of hits) |
| **detailed**  boolean | Detailed ACL information.  **Choices:**   - `false` - `true` |
| **include**  dictionary | Include additional fields in syslogs. |
| **sgt**  boolean | Include source group tag info in syslogs.  **Choices:**   - `false` - `true` |
| **logfile**  dictionary | Set file logging. |
| **name**  string | Logfile name. |
| **persistent_threshold**  integer | Set persistent logging utilization alert threshold in percentage.  This option is unsupported on MDS switches. |
| **severity**  string | Set severity severity for console.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **size**  integer | Enter the logfile size in bytes. |
| **state**  string | Enable or disable logfile.  **Choices:**   - `"enabled"` - `"disabled"` |
| **module**  dictionary | Set module(linecard) logging. |
| **severity**  string | Set severity severity for console.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **state**  string | Enable or disable module logging.  **Choices:**   - `"enabled"` - `"disabled"` |
| **monitor**  dictionary | Set terminal line(monitor) logging severity. |
| **severity**  string | Set severity severity for console.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **state**  string | Enable or disable monitor logging.  **Choices:**   - `"enabled"` - `"disabled"` |
| **origin_id**  dictionary | Enable origin information for Remote Syslog Server. |
| **hostname**  boolean | Use hostname as origin-id of logging messages.  This option is mutually exclusive with *ip* and *string*.  **Choices:**   - `false` - `true` |
| **ip**  string | Use ip address as origin-id of logging messages.  This option is mutually exclusive with *hostname* and *string*. |
| **string**  string | Use text string as origin-id of logging messages.  This option is mutually exclusive with *hostname* and *ip*. |
| **rate_limit**  string | Enable or disable rate limit for log messages.  **Choices:**   - `"enabled"` - `"disabled"` |
| **rfc_strict**  boolean | Set RFC to which messages should compliant.  Syslogs will be compliant to RFC 5424.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **source_interface**  string | Enable Source-Interface for Remote Syslog Server.  This option is unsupported on MDS switches. |
| **timestamp**  string | Set logging timestamp granularity.  **Choices:**   - `"microseconds"` - `"milliseconds"` - `"seconds"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | include logging**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states *replaced* and *overridden* have identical behaviour for this module.  Refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](nxos_logging_global_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 9.3.6 on Cisco Nexus Switches.
> - Limited Support for Cisco MDS
> - This module works with connection `network_cli` and `httpapi`.
> - Tested against Cisco MDS NX-OS 9.2(2) with connection `network_cli`.

## [Examples](nxos_logging_global_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# nxos-9k-rdo# show running-config | include logging
# nxos-9k-rdo#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_logging_global:
    config:
      console:
        severity: error
      monitor:
        severity: warning
      ip:
        access_list:
          cache:
            entries: 16384
            interval: 200
            threshold: 5000
      facilities:
        - facility: auth
          severity: critical
        - facility: ospfv3
          severity: alert
        - facility: ftp
          severity: informational
      hosts:
        - host: 203.0.113.100
          severity: alert
          use_vrf: management
        - host: 203.0.113.101
          severity: error
          facility: local6
          use_vrf: default
      origin_id:
        hostname: True

# Task output
# -------------
#  before: {}
#
#  commands:
#    - "logging console 3"
#    - "logging monitor 4"
#    - "logging ip access-list cache entries 16384"
#    - "logging ip access-list cache interval 200"
#    - "logging ip access-list cache threshold 5000"
#    - "logging severity auth 2"
#    - "logging severity ospfv3 1"
#    - "logging severity ftp 6"
#    - "logging server 203.0.113.100 1 use-vrf management"
#    - "logging server 203.0.113.101 3 facility local6 use-vrf default"
#    - "logging origin-id hostname"
#
# after:
#   console:
#      severity: error
#    facilities:
#      - facility: auth
#        severity: critical
#      - facility: ftp
#        severity: informational
#      - facility: ospfv3
#        severity: alert
#    ip:
#      access_list:
#        cache:
#          entries: 16384
#          interval: 200
#          threshold: 5000
#    monitor:
#      severity: warning
#    origin_id:
#      hostname: true
#    hosts:
#      - severity: alert
#        host: 203.0.113.100
#        use_vrf: management
#      - facility: local6
#        severity: error
#        host: 203.0.113.101
#        use_vrf: default

# After state:
# ------------
# nxos-9k-rdo# show running-config | include logging
# logging console 3
# logging monitor 4
# logging ip access-list cache entries 16384
# logging ip access-list cache interval 200
# logging ip access-list cache threshold 5000
# logging severity auth 2
# logging severity ospfv3 1
# logging severity ftp 6
# logging origin-id hostname
# logging server 203.0.113.100 1 use-vrf management
# logging server 203.0.113.101 3 use-vrf default facility local6

# Using replaced

# Before state:
# ------------
# nxos-9k-rdo# show running-config | include logging
# logging console 3
# logging monitor 4
# logging ip access-list cache entries 16384
# logging ip access-list cache interval 200
# logging ip access-list cache threshold 5000
# logging severity auth 2
# logging severity ospfv3 1
# logging severity ftp 6
# logging origin-id hostname
# logging server 203.0.113.100 1 use-vrf management
# logging server 203.0.113.101 3 use-vrf default facility local6

- name: Replace logging configurations with provided config
  cisco.nxos.nxos_logging_global:
    config:
      monitor:
        severity: warning
      ip:
        access_list:
          cache:
            entries: 4096
      facilities:
        - facility: auth
          severity: critical
        - facility: ospfv3
          severity: alert
        - facility: ftp
          severity: informational
      hosts:
        - host: 203.0.113.101
          severity: error
          facility: local6
          use_vrf: default
        - host: 198.51.100.101
          severity: alert
          port: 6538
          use_vrf: management
      origin_id:
        ip: 192.0.2.100
    state: replaced

# Task output
# -------------
# before:
#   console:
#      severity: error
#    facilities:
#      - facility: auth
#        severity: critical
#      - facility: ftp
#        severity: informational
#      - facility: ospfv3
#        severity: alert
#    ip:
#      access_list:
#        cache:
#          entries: 16384
#          interval: 200
#          threshold: 5000
#    monitor:
#      severity: warning
#    origin_id:
#      hostname: true
#    hosts:
#      - severity: alert
#        host: 203.0.113.100
#        use_vrf: management
#      - facility: local6
#        severity: error
#        host: 203.0.113.101
#        use_vrf: default
#
# commands:
#   - "logging console"
#   - "logging ip access-list cache entries 4096"
#   - "no logging ip access-list cache interval 200"
#   - "no logging ip access-list cache threshold 5000"
#   - "no logging origin-id hostname"
#   - "logging origin-id ip 192.0.2.100"
#   - "logging server 198.51.100.101 1 port 6538 use-vrf management"
#   - "no logging server 203.0.113.100 1 use-vrf management"
#
#  after:
#    facilities:
#      - facility: auth
#        severity: critical
#      - facility: ftp
#        severity: informational
#      - facility: ospfv3
#        severity: alert
#    ip:
#      access_list:
#        cache:
#          entries: 4096
#    monitor:
#      severity: warning
#    origin_id:
#      ip: 192.0.2.100
#    hosts:
#      - severity: alert
#        port: 6538
#        host: 198.51.100.101
#        use_vrf: management
#      - facility: local6
#        severity: error
#        host: 203.0.113.101
#        use_vrf: default
#
# After state:
# ------------
# nxos-9k-rdo# show running-config | include logging
# logging monitor 4
# logging ip access-list cache entries 4096
# logging severity auth 2
# logging severity ospfv3 1
# logging severity ftp 6
# logging origin-id ip 192.0.2.100
# logging server 203.0.113.101 3 use-vrf default facility local6
# logging server 198.51.100.101 1 port 6538 use-vrf management

# Using deleted to delete all logging configurations

# Before state:
# ------------
# nxos-9k-rdo# show running-config | include logging
# logging console 3
# logging monitor 4
# logging ip access-list cache entries 16384
# logging ip access-list cache interval 200
# logging ip access-list cache threshold 5000
# logging severity auth 2
# logging severity ospfv3 1
# logging severity ftp 6
# logging origin-id hostname
# logging server 203.0.113.100 1 use-vrf management
# logging server 203.0.113.101 3 use-vrf default facility local6

- name: Delete all logging configuration
  cisco.nxos.nxos_logging_global:
    state: deleted

# Task output
# -------------
# before:
#   console:
#      severity: error
#    facilities:
#      - facility: auth
#        severity: critical
#      - facility: ftp
#        severity: informational
#      - facility: ospfv3
#        severity: alert
#    ip:
#      access_list:
#        cache:
#          entries: 16384
#          interval: 200
#          threshold: 5000
#    monitor:
#      severity: warning
#    origin_id:
#      hostname: true
#    hosts:
#      - severity: alert
#        host: 203.0.113.100
#        use_vrf: management
#      - facility: local6
#        severity: error
#        host: 203.0.113.101
#        use_vrf: default
#
# commands:
#   - "logging console"
#   - "logging monitor"
#   - "no logging ip access-list cache entries 16384"
#   - "no logging ip access-list cache interval 200"
#   - "no logging ip access-list cache threshold 5000"
#   - "no logging origin-id hostname"
#   - "no logging severity auth 2"
#   - "no logging severity ospfv3 1"
#   - "no logging severity ftp 6"
#   - "no logging server 203.0.113.100 1 use-vrf management"
#   - "no logging server 203.0.113.101 3 facility local6 use-vrf default"
#
# after: {}

# Using rendered

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.nxos.nxos_logging_global:
    config:
      console:
        severity: error
      monitor:
        severity: warning
      ip:
        access_list:
          cache:
            entries: 16384
            interval: 200
            threshold: 5000
      facilities:
        - facility: auth
          severity: critical
        - facility: ospfv3
          severity: alert
        - facility: ftp
          severity: informational
      hosts:
        - host: 203.0.113.100
          severity: alert
          use_vrf: management
        - host: 203.0.113.101
          severity: error
          facility: local6
          use_vrf: default
      origin_id:
        hostname: True

# Task Output (redacted)
# -----------------------
#  rendered:
#    - "logging console 3"
#    - "logging monitor 4"
#    - "logging ip access-list cache entries 16384"
#    - "logging ip access-list cache interval 200"
#    - "logging ip access-list cache threshold 5000"
#    - "logging severity auth 2"
#    - "logging severity ospfv3 1"
#    - "logging severity ftp 6"
#    - "logging server 203.0.113.100 1 use-vrf management"
#    - "logging server 203.0.113.101 3 facility local6 use-vrf default"
#    - "logging origin-id hostname"

# Using parsed

# parsed.cfg
# ------------
# logging console 3
# logging monitor 4
# logging ip access-list cache entries 16384
# logging ip access-list cache interval 200
# logging ip access-list cache threshold 5000
# logging severity auth 2
# logging severity ospfv3 1
# logging severity ftp 6
# logging origin-id hostname
# logging server 203.0.113.100 1 use-vrf management
# logging server 203.0.113.101 3 use-vrf default facility local6

- name: Parse externally provided logging configuration
  cisco.nxos.nxos_logging_global:
    running_config: "{{ lookup('file', './fixtures/parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# parsed:
#   console:
#      severity: error
#    facilities:
#      - facility: auth
#        severity: critical
#      - facility: ftp
#        severity: informational
#      - facility: ospfv3
#        severity: alert
#    ip:
#      access_list:
#        cache:
#          entries: 16384
#          interval: 200
#          threshold: 5000
#    monitor:
#      severity: warning
#    origin_id:
#      hostname: true
#    hosts:
#      - severity: alert
#        host: 203.0.113.100
#        use_vrf: management
#      - facility: local6
#        severity: error
#        host: 203.0.113.101
#        use_vrf: default
```

## [Return Values](nxos_logging_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `["logging console 3", "logging monitor 4", "logging ip access-list cache entries 16384", "logging ip access-list cache interval 200", "logging ip access-list cache threshold 5000"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when state is *parsed*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when state is *rendered*  **Sample:** `["logging ip access-list cache entries 4096", "no logging ip access-list cache interval 200", "no logging ip access-list cache threshold 5000", "no logging origin-id hostname", "logging origin-id ip 192.0.2.100", "logging server 198.51.100.101 1 port 6538 use-vrf management"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
