---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_logging_global module – Resource module to configure logging."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_logging_global_module.html
fetched_at: 2026-07-28T01:26:51+00:00
---
# cisco.iosxr.iosxr_logging_global module – Resource module to configure logging.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_logging_global`.

New in cisco.iosxr 2.4.0

- [Synopsis](iosxr_logging_global_module.md#synopsis)
- [Parameters](iosxr_logging_global_module.md#parameters)
- [Notes](iosxr_logging_global_module.md#notes)
- [Examples](iosxr_logging_global_module.md#examples)
- [Return Values](iosxr_logging_global_module.md#return-values)

## [Synopsis](iosxr_logging_global_module.md#id1)

- This module manages the logging attributes of Cisco IOSXR network devices

Aliases: logging_global

## [Parameters](iosxr_logging_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of logging options. |
| **archive**  dictionary | logging to a persistent device(disk/harddisk) |
| **archive_length**  integer | The maximum no of weeks of log to maintain. |
| **archive_size**  integer | The total size of the archive. |
| **device**  string | Configure the archive device |
| **file_size**  integer | The maximum file size for a single log file.. |
| **frequency**  string | The collection interval for logs.  **Choices:**   - `"daily"` - `"weekly"` |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **threshold**  integer | Threshold percent <1-99>. |
| **buffered**  dictionary | Set buffered logging parameters |
| **discriminator**  list / elements=dictionary | Establish MD-Buffer association |
| **match_params**  string | Set match/no-match discriminator.  **Choices:**   - `"match1"` - `"match2"` - `"match3"` - `"nomatch1"` - `"nomatch2"` - `"nomatch3"` |
| **name**  string | discriminator name. |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **size**  integer | Logging buffer size |
| **console**  dictionary | Set console logging parameters |
| **discriminator**  list / elements=dictionary | Establish MD-Buffer association |
| **match_params**  string | Set match/no-match discriminator.  **Choices:**   - `"match1"` - `"match2"` - `"match3"` - `"nomatch1"` - `"nomatch2"` - `"nomatch3"` |
| **name**  string | discriminator name. |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warning"` |
| **state**  string | Enable or disable logging.  **Choices:**   - `"enabled"` - `"disabled"` |
| **correlator**  dictionary | Configure properties of the event correlator |
| **buffer_size**  integer | Configure size of the correlator buffer. |
| **rule_sets**  list / elements=dictionary | Configure a specified correlation ruleset. |
| **name**  string | Name of the ruleset |
| **rulename**  list / elements=string | Name of the rule |
| **rules**  list / elements=dictionary | Configure a specified correlation rule. |
| **context_correlation**  boolean | Specify enable correlation on context.  **Choices:**   - `false` - `true` |
| **reissue_nonbistate**  boolean | Specify reissue of non-bistate alarms on parent clear.This option is allowed for the rules whose type is stateful.  **Choices:**   - `false` - `true` |
| **reparent**  boolean | Specify reparent of alarm on parent clear.This option is allowed for the rules whose type is stateful.  **Choices:**   - `false` - `true` |
| **rule_name**  string | name of rule. |
| **rule_type**  string | type of rule - stateful or nonstateful.  **Choices:**   - `"stateful"` - `"nonstateful"` |
| **timeout**  integer | Specify timeout. |
| **timeout_rootcause**  integer | Specify timeout for root-cause. |
| **events**  dictionary | Configure event monitoring parameters. |
| **buffer_size**  integer | Set size of the local event buffer. |
| **display_location**  boolean | Include alarm source location in message text.  **Choices:**   - `false` - `true` |
| **filter_match**  list / elements=string | Configure filter. |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **threshold**  integer | Capacity alarm threshold. |
| **facility**  string | Facility parameter for syslog messages  **Choices:**   - `"auth"` - `"cron"` - `"daemon"` - `"kern"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` - `"lpr"` - `"mail"` - `"news"` - `"sys10"` - `"sys11"` - `"sys12"` - `"sys13"` - `"sys14"` - `"sys9"` - `"syslog"` - `"user"` - `"uucp"` |
| **files**  list / elements=dictionary | Set file logging. |
| **maxfilesize**  integer | Set max file size. |
| **name**  string | name of file. |
| **path**  string | Set file path. |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"info"` - `"notifications"` - `"warning"` |
| **format**  boolean | Enable to send the syslog message rfc5424 format .  **Choices:**   - `false` - `true` |
| **history**  dictionary | Configure syslog history table |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **size**  integer | Logging buffer size |
| **state**  string | Enable or disable logging.  **Choices:**   - `"enabled"` - `"disabled"` |
| **hostnameprefix**  string | Hostname prefix to add on msgs to servers. |
| **hosts**  list / elements=dictionary | Set syslog server IP address and parameters |
| **host**  string | IPv4/Ipv6 address or hostname of the syslog server |
| **port**  string | Set <0-65535> non-default Port.  **Default:** `"default"` |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"error"` - `"info"` - `"notifications"` - `"warning"` |
| **vrf**  string | Set VRF option  **Default:** `"default"` |
| **ipv4**  dictionary | Mark the dscp/precedence bit for ipv4 packets. |
| **dscp**  string | Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries. |
| **precedence**  string | Set precedence Please refer vendor document for valid entries. |
| **ipv6**  dictionary | Mark the dscp/precedence bit for ipv4 packets. |
| **dscp**  string | Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries. |
| **precedence**  string | Set precedence Please refer vendor document for valid entries. |
| **localfilesize**  integer | Set size of the local log file |
| **monitor**  dictionary | Set terminal line (monitor) logging parameters |
| **discriminator**  list / elements=dictionary | Establish MD-Buffer association |
| **match_params**  string | Set match/no-match discriminator.  **Choices:**   - `"match1"` - `"match2"` - `"match3"` - `"nomatch1"` - `"nomatch2"` - `"nomatch3"` |
| **name**  string | discriminator name. |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warning"` |
| **state**  string | Enable or disable logging.  **Choices:**   - `"enabled"` - `"disabled"` |
| **source_interfaces**  list / elements=dictionary | Specify interface for source address in logging transactions |
| **interface**  string | Interface name with number |
| **vrf**  string | VPN Routing/Forwarding instance name |
| **suppress**  dictionary | Suppress logging behaviour. |
| **apply_rule**  string | Apply suppression rule. |
| **duplicates**  boolean | Suppress consecutive duplicate messages.  **Choices:**   - `false` - `true` |
| **tls_servers**  list / elements=dictionary | Secure server over tls. |
| **name**  string | Name for the tls peer configuration. |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **tls_hostname**  string | Name of the logging host. |
| **trustpoint**  string | Name of the trustpoint configured. |
| **vrf**  string | name of vrf. |
| **trap**  dictionary | Set syslog server logging level |
| **severity**  string | Logging severity level  **Choices:**   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warning"` |
| **state**  string | Enable or disable logging.  **Choices:**   - `"enabled"` - `"disabled"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | include logging**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](iosxr_logging_global_module.md#id3)

> **Note:**
>
> - Tested against IOSXR 7.0.2.
> - This module works with connection `network_cli`.

## [Examples](iosxr_logging_global_module.md#id4)

```yaml+jinja
# Using merged
#-----------------
# Before state
#RP/0/0/CPU0:10#show running-config logging
#Thu Feb  4 09:38:36.245 UTC
#% No such configuration item(s)
#RP/0/0/CPU0:10#
#
#
- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_logging_global:
         config:
           buffered:
             size: 2097152
             severity: warnings
           correlator:
             buffer_size: 1024
           events:
             display_location: True
           files:
             - maxfilesize: '1024'
               name: test
               path: test
               severity: info
           hostnameprefix: test
           hosts:
             - host: 1.1.1.1
               port: default
               severity: critical
               vrf: default
           ipv4:
             dscp: af11
           localfilesize: 1024
           monitor:
             severity: errors
           source_interfaces:
             - interface: GigabitEthernet0/0/0/0
               vrf: test
           tls_servers:
             - name: test
               tls_hostname: test2
               trustpoint: test2
               vrf: test
           trap:
             severity: informational
         state: merged
#
#
# After state:
#-------------------------------------------
#RP/0/0/CPU0:10#show running-config logging
# Tue Jul 20 18:09:18.491 UTC
# logging tls-server test
#  vrf test
#  trustpoint test2
#  tls-hostname test2
# !
# logging file test path test maxfilesize 1024 severity info
# logging ipv4 dscp af11
# logging trap informational
# logging events display-location
# logging monitor errors
# logging buffered 2097152
# logging buffered warnings
# logging 1.1.1.1 vrf default severity critical port default
# logging correlator buffer-size 1024
# logging localfilesize 1024
# logging source-interface GigabitEthernet0/0/0/0 vrf test
# logging hostnameprefix test
#------------------------------------------------
#Module execution
#
#     "after": {
#         "buffered": {
#             "severity": "errors"
#         },
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "files": [
#             {
#                 "maxfilesize": "1024",
#                 "name": "test",
#                 "path": "test1",
#                 "severity": "info"
#             }
#         ],
#         "hostnameprefix": "test1",
#         "hosts": [
#             {
#                 "host": "1.1.1.3",
#                 "port": "default",
#                 "severity": "critical",
#                 "vrf": "default"
#             }
#         ],
#         "ipv6": {
#             "dscp": "af11"
#         },
#         "localfilesize": 1024,
#         "source_interfaces": [
#             {
#                 "interface": "GigabitEthernet0/0/0/0",
#                 "vrf": "test1"
#             }
#         ],
#         "tls_servers": [
#             {
#                 "name": "test",
#                 "tls_hostname": "test2",
#                 "trustpoint": "test",
#                 "vrf": "test"
#             }
#         ]
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "logging buffered errors",
#         "logging correlator buffer-size 1024",
#         "logging hostnameprefix test1",
#         "logging ipv6 dscp af11",
#         "logging localfilesize 1024",
#         "logging trap disable",
#         "logging monitor disable",
#         "logging history disable",
#         "logging console disable",
#         "logging 1.1.1.3 vrf default severity critical port default",
#         "logging file test path test1 maxfilesize 1024 severity info",
#         "logging source-interface GigabitEthernet0/0/0/0 vrf test1",
#         "logging tls-server test tls-hostname test2",
#         "logging tls-server test trustpoint test",
#         "logging tls-server test vrf test"
#     ],
#     "invocation": {
#         "module_args": {
#             "config": {
#                 "archive": null,
#                 "buffered": {
#                     "discriminator": null,
#                     "severity": "errors",
#                     "size": null
#                 },
#                 "console": {
#                     "discriminator": null,
#                     "severity": null,
#                     "state": "disabled"
#                 },
#                 "correlator": {
#                     "buffer_size": 1024,
#                     "rule_set": null,
#                     "rules": null
#                 },
#                 "events": null,
#                 "facility": null,
#                 "files": [
#                     {
#                         "maxfilesize": "1024",
#                         "name": "test",
#                         "path": "test1",
#                         "severity": "info"
#                     }
#                 ],
#                 "format": null,
#                 "history": {
#                     "severity": null,
#                     "size": null,
#                     "state": "disabled"
#                 },
#                 "hostnameprefix": "test1",
#                 "hosts": [
#                     {
#                         "host": "1.1.1.3",
#                         "port": "default",
#                         "severity": "critical",
#                         "vrf": "default"
#                     }
#                 ],
#                 "ipv4": null,
#                 "ipv6": {
#                     "dscp": "af11",
#                     "precedence": null
#                 },
#                 "localfilesize": 1024,
#                 "monitor": {
#                     "discriminator": null,
#                     "severity": null,
#                     "state": "disabled"
#                 },
#                 "source_interfaces": [
#                     {
#                         "interface": "GigabitEthernet0/0/0/0",
#                         "vrf": "test1"
#                     }
#                 ],
#                 "suppress": null,
#                 "tls_servers": [
#                     {
#                         "name": "test",
#                         "severity": null,
#                         "tls_hostname": "test2",
#                         "trustpoint": "test",
#                         "vrf": "test"
#                     }
#                 ],
#                 "trap": {
#                     "severity": null,
#                     "state": "disabled"
#                 }
#             },
#             "running_config": null,
#             "state": "merged"
#         }
#     }
# }
#
# Using replaced:
# -----------------------------------------------------------
#
#Before state
#RP/0/0/CPU0:10#show running-config logging
# Tue Jul 20 18:09:18.491 UTC
# logging tls-server test
#  vrf test
#  trustpoint test2
#  tls-hostname test2
# !
# logging file test path test maxfilesize 1024 severity info
# logging ipv4 dscp af11
# logging trap informational
# logging events display-location
# logging monitor errors
# logging buffered 2097152
# logging buffered warnings
# logging 1.1.1.1 vrf default severity critical port default
# logging correlator buffer-size 1024
# logging localfilesize 1024
# logging source-interface GigabitEthernet0/0/0/0 vrf test
# logging hostnameprefix test
#-----------------------------------------------------------
#
- name: Replace BGP configuration with provided configuration
  cisco.iosxr.iosxr_logging_global:
     state: replaced
     config:
           buffered:
             severity: errors
           correlator:
             buffer_size: 1024
           files:
             - maxfilesize: '1024'
               name: test
               path: test1
               severity: info
           hostnameprefix: test1
           hosts:
             - host: 1.1.1.3
               port: default
               severity: critical
               vrf: default
           ipv6:
             dscp: af11
           localfilesize: 1024
           monitor:
             severity: errors
           tls_servers:
             - name: test
               tls_hostname: test2
               trustpoint: test
               vrf: test
           trap:
             severity: critical
#
# After state:
#RP/0/0/CPU0:10#show running-config logging
# Tue Jul 20 18:31:51.709 UTC
# logging tls-server test
#  vrf test
#  trustpoint test
#  tls-hostname test2
# !
# logging file test path test1 maxfilesize 1024 severity info
# logging ipv6 dscp af11
# logging trap critical
# logging monitor errors
# logging buffered errors
# logging 1.1.1.3 vrf default severity critical port default
# logging correlator buffer-size 1024
# logging localfilesize 1024
# logging hostnameprefix test1
#-----------------------------------------------------------------
#
# Module Execution:
# "after": {
#         "buffered": {
#             "severity": "errors"
#         },
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "files": [
#             {
#                 "maxfilesize": "1024",
#                 "name": "test",
#                 "path": "test1",
#                 "severity": "info"
#             }
#         ],
#         "hostnameprefix": "test1",
#         "hosts": [
#             {
#                 "host": "1.1.1.3",
#                 "port": "default",
#                 "severity": "critical",
#                 "vrf": "default"
#             }
#         ],
#         "ipv6": {
#             "dscp": "af11"
#         },
#         "localfilesize": 1024,
#         "monitor": {
#             "severity": "errors"
#         },
#         "tls_servers": [
#             {
#                 "name": "test",
#                 "tls_hostname": "test2",
#                 "trustpoint": "test",
#                 "vrf": "test"
#             }
#         ],
#         "trap": {
#             "severity": "critical"
#         }
#     },
#     "before": {
#         "buffered": {
#             "severity": "warnings",
#             "size": 2097152
#         },
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "events": {
#             "display_location": true
#         },
#         "files": [
#             {
#                 "maxfilesize": "1024",
#                 "name": "test",
#                 "path": "test",
#                 "severity": "info"
#             }
#         ],
#         "hostnameprefix": "test",
#         "hosts": [
#             {
#                 "host": "1.1.1.1",
#                 "port": "default",
#                 "severity": "critical",
#                 "vrf": "default"
#             }
#         ],
#         "ipv4": {
#             "dscp": "af11"
#         },
#         "localfilesize": 1024,
#         "monitor": {
#             "severity": "errors"
#         },
#         "source_interfaces": [
#             {
#                 "interface": "GigabitEthernet0/0/0/0",
#                 "vrf": "test"
#             }
#         ],
#         "tls_servers": [
#             {
#                 "name": "test",
#                 "tls_hostname": "test2",
#                 "trustpoint": "test2",
#                 "vrf": "test"
#             }
#         ],
#         "trap": {
#             "severity": "informational"
#         }
#     },
#     "changed": true,
#     "commands": [
#         "no logging buffered 2097152",
#         "no logging events display-location",
#         "no logging ipv4 dscp af11",
#         "no logging 1.1.1.1 vrf default severity critical port default",
#         "no logging source-interface GigabitEthernet0/0/0/0 vrf test",
#         "logging buffered errors",
#         "logging hostnameprefix test1",
#         "logging ipv6 dscp af11",
#         "logging trap critical",
#         "logging 1.1.1.3 vrf default severity critical port default",
#         "logging file test path test1 maxfilesize 1024 severity info",
#         "logging tls-server test trustpoint test"
#     ],
#
#
#
# Using deleted:
# -----------------------------------------------------------
# Before state:
#RP/0/0/CPU0:10#show running-config logging
# Tue Jul 20 18:09:18.491 UTC
# logging tls-server test
#  vrf test
#  trustpoint test2
#  tls-hostname test2
# !
# logging file test path test maxfilesize 1024 severity info
# logging ipv4 dscp af11
# logging trap informational
# logging events display-location
# logging monitor errors
# logging buffered 2097152
# logging buffered warnings
# logging 1.1.1.1 vrf default severity critical port default
# logging correlator buffer-size 1024
# logging localfilesize 1024
# logging source-interface GigabitEthernet0/0/0/0 vrf test
# logging hostnameprefix test
#
#-----------------------------------------------------------
- name: Delete given logging_global configuration
  cisco.iosxr.iosxr_logging_global:
     state: deleted
#
# After state:
#RP/0/0/CPU0:10#show running-config
#
#-------------------------------------------------------------
# Module Execution:
#
# "after": {},
#     "before": {
#         "buffered": {
#             "severity": "warnings",
#             "size": 2097152
#         },
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "events": {
#             "display_location": true
#         },
#         "files": [
#             {
#                 "maxfilesize": "1024",
#                 "name": "test",
#                 "path": "test",
#                 "severity": "info"
#             }
#         ],
#         "hostnameprefix": "test",
#         "hosts": [
#             {
#                 "host": "1.1.1.1",
#                 "port": "default",
#                 "severity": "critical",
#                 "vrf": "default"
#             }
#         ],
#         "ipv4": {
#             "dscp": "af11"
#         },
#         "localfilesize": 1024,
#         "monitor": {
#             "severity": "errors"
#         },
#         "source_interfaces": [
#             {
#                 "interface": "GigabitEthernet0/0/0/0",
#                 "vrf": "test"
#             }
#         ],
#         "tls_servers": [
#             {
#                 "name": "test",
#                 "tls_hostname": "test2",
#                 "trustpoint": "test2",
#                 "vrf": "test"
#             }
#         ],
#         "trap": {
#             "severity": "informational"
#         }
#     },
#     "changed": true,
#     "commands": [
#         "no logging buffered 2097152",
#         "no logging buffered warnings",
#         "no logging correlator buffer-size 1024",
#         "no logging events display-location",
#         "no logging hostnameprefix test",
#         "no logging ipv4 dscp af11",
#         "no logging localfilesize 1024",
#         "no logging monitor errors",
#         "no logging trap informational",
#         "no logging 1.1.1.1 vrf default severity critical port default",
#         "no logging file test path test maxfilesize 1024 severity info",
#         "no logging source-interface GigabitEthernet0/0/0/0 vrf test",
#         "no logging tls-server test"
#     ],
#     "invocation": {
#         "module_args": {
#             "config": null,
#             "running_config": null,
#             "state": "deleted"
#         }
#     }
#
#
#
# using gathered:
# ------------------------------------------------------------
# Before state:
#RP/0/0/CPU0:10#show running-config logging
# Tue Jul 20 18:09:18.491 UTC
# logging tls-server test
#  vrf test
#  trustpoint test2
#  tls-hostname test2
# !
# logging file test path test maxfilesize 1024 severity info
# logging ipv4 dscp af11
# logging trap informational
# logging events display-location
# logging monitor errors
# logging buffered 2097152
# logging buffered warnings
# logging 1.1.1.1 vrf default severity critical port default
# logging correlator buffer-size 1024
# logging localfilesize 1024
# logging source-interface GigabitEthernet0/0/0/0 vrf test
# logging hostnameprefix test
#
#
- name: Gather iosxr_logging_global facts using gathered state
  cisco.iosxr.iosxr_logging_global:
     state: gathered
#
#-------------------------------------------------------------
# Module Execution:
#
# "changed": false,
# "gathered": {
#         "buffered": {
#             "severity": "warnings",
#             "size": 2097152
#         },
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "events": {
#             "display_location": true
#         },
#         "files": [
#             {
#                 "maxfilesize": "1024",
#                 "name": "test",
#                 "path": "test",
#                 "severity": "info"
#             }
#         ],
#         "hostnameprefix": "test",
#         "hosts": [
#             {
#                 "host": "1.1.1.1",
#                 "port": "default",
#                 "severity": "critical",
#                 "vrf": "default"
#             }
#         ],
#         "ipv4": {
#             "dscp": "af11"
#         },
#         "localfilesize": 1024,
#         "monitor": {
#             "severity": "errors"
#         },
#         "source_interfaces": [
#             {
#                 "interface": "GigabitEthernet0/0/0/0",
#                 "vrf": "test"
#             }
#         ],
#         "tls_servers": [
#             {
#                 "name": "test",
#                 "tls_hostname": "test2",
#                 "trustpoint": "test2",
#                 "vrf": "test"
#             }
#         ],
#         "trap": {
#             "severity": "informational"
#         }
#     },
#     "invocation": {
#         "module_args": {
#             "config": null,
#             "running_config": null,
#             "state": "gathered"
#         }
# }
#
#
# Using parsed:
#---------------------------------------------------------------
#
# parsed.cfg
#
# logging tls-server test
#  vrf test
#  trustpoint test2
#  tls-hostname test2
# !
# logging file test path test maxfilesize 1024 severity info
# logging ipv4 dscp af11
# logging trap informational
# logging events display-location
# logging monitor errors
# logging buffered 2097152
# logging buffered warnings
# logging 1.1.1.1 vrf default severity critical port default
# logging correlator buffer-size 1024
# logging localfilesize 1024
# logging source-interface GigabitEthernet0/0/0/0 vrf test
# logging hostnameprefix test
#
#
- name: Parse externally provided Logging global config to agnostic model
  cisco.iosxr.iosxr_logging_global:
     running_config: "{{ lookup('file', './fixtures/parsed.cfg') }}"
     state: parsed
#----------------------------------------------------------------
# Module execution:
# "changed": false,
# "parsed": {
#         "buffered": {
#             "severity": "warnings",
#             "size": 2097152
#         },
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "events": {
#             "display_location": true
#         },
#         "files": [
#             {
#                 "maxfilesize": "1024",
#                 "name": "test",
#                 "path": "test",
#                 "severity": "info"
#             }
#         ],
#         "hostnameprefix": "test",
#         "hosts": [
#             {
#                 "host": "1.1.1.1",
#                 "port": "default",
#                 "severity": "critical",
#                 "vrf": "default"
#             }
#         ],
#         "ipv4": {
#             "dscp": "af11"
#         },
#         "localfilesize": 1024,
#         "monitor": {
#             "severity": "errors"
#         },
#         "source_interfaces": [
#             {
#                 "interface": "GigabitEthernet0/0/0/0",
#                 "vrf": "test"
#             }
#         ],
#         "tls_servers": [
#             {
#                 "name": "test",
#                 "tls_hostname": "test2",
#                 "trustpoint": "test2",
#                 "vrf": "test"
#             }
#         ],
#         "trap": {
#             "severity": "informational"
#         }
#     }
#
#
# Using rendered:
# ----------------------------------------------------------------------------
- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.iosxr.iosxr_logging_global:
     state: rendered
     config:
       buffered:
         size: 2097152
         severity: warnings
       correlator:
         buffer_size: 1024
       events:
         display_location: True
       files:
         - maxfilesize: '1024'
           name: test
           path: test
           severity: info
       hostnameprefix: test
       hosts:
         - host: 1.1.1.1
           port: default
           severity: critical
           vrf: default
       ipv4:
         dscp: af11
       localfilesize: 1024
       monitor:
         severity: errors
       source_interfaces:
         - interface: GigabitEthernet0/0/0/0
           vrf: test
       tls_servers:
         - name: test
           tls_hostname: test2
           trustpoint: test2
           vrf: test
       trap:
         severity: informational
#----------------------------------------------------------------
# Module Execution:
# "rendered": [
#         "logging buffered errors",
#         "logging correlator buffer-size 1024",
#         "logging hostnameprefix test1",
#         "logging ipv6 dscp af11",
#         "logging localfilesize 1024",
#         "logging trap disable",
#         "logging monitor disable",
#         "logging history disable",
#         "logging console disable",
#         "logging 1.1.1.3 vrf default severity critical port default",
#         "logging file test path test1 maxfilesize 1024 severity info",
#         "logging source-interface GigabitEthernet0/0/0/0 vrf test1",
#         "logging tls-server test tls-hostname test2",
#         "logging tls-server test trustpoint test",
#         "logging tls-server test vrf test"
#     ]
#
# Using overridden:
# ---------------------------------------------------------------------------------
# Before state:
#RP/0/0/CPU0:10#show running-config logging
# Tue Jul 20 18:09:18.491 UTC
# logging tls-server test
#  vrf test
#  trustpoint test2
#  tls-hostname test2
# !
# logging file test path test maxfilesize 1024 severity info
# logging ipv4 dscp af11
# logging trap informational
# logging events display-location
# logging monitor errors
# logging buffered 2097152
# logging buffered warnings
# logging 1.1.1.1 vrf default severity critical port default
# logging correlator buffer-size 1024
# logging localfilesize 1024
# logging source-interface GigabitEthernet0/0/0/0 vrf test
# logging hostnameprefix test
#
#-----------------------------------------------------------
#
- name: Overridde logging global configuration with provided configuration
  cisco.iosxr.iosxr_logging_global:
     state: overridden
     config:
           buffered:
             severity: errors
           correlator:
             buffer_size: 1024
           files:
             - maxfilesize: '1024'
               name: test
               path: test1
               severity: info
           hostnameprefix: test1
           hosts:
             - host: 1.1.1.3
               port: default
               severity: critical
               vrf: default
           ipv6:
             dscp: af11
           localfilesize: 1024
           monitor:
             severity: errors
           tls_servers:
             - name: test
               tls_hostname: test2
               trustpoint: test
               vrf: test
           trap:
             severity: critical
#
# After state:
#RP/0/0/CPU0:10#show running-config logging
# Tue Jul 20 18:31:51.709 UTC
# logging tls-server test
#  vrf test
#  trustpoint test
#  tls-hostname test2
# !
# logging file test path test1 maxfilesize 1024 severity info
# logging ipv6 dscp af11
# logging trap critical
# logging monitor errors
# logging buffered errors
# logging 1.1.1.3 vrf default severity critical port default
# logging correlator buffer-size 1024
# logging localfilesize 1024
# logging hostnameprefix test1
#-----------------------------------------------------------------
#
# Module Execution:
# "after": {
#         "buffered": {
#             "severity": "errors"
#         },
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "files": [
#             {
#                 "maxfilesize": "1024",
#                 "name": "test",
#                 "path": "test1",
#                 "severity": "info"
#             }
#         ],
#         "hostnameprefix": "test1",
#         "hosts": [
#             {
#                 "host": "1.1.1.3",
#                 "port": "default",
#                 "severity": "critical",
#                 "vrf": "default"
#             }
#         ],
#         "ipv6": {
#             "dscp": "af11"
#         },
#         "localfilesize": 1024,
#         "monitor": {
#             "severity": "errors"
#         },
#         "tls_servers": [
#             {
#                 "name": "test",
#                 "tls_hostname": "test2",
#                 "trustpoint": "test",
#                 "vrf": "test"
#             }
#         ],
#         "trap": {
#             "severity": "critical"
#         }
#     },
#     "before": {
#         "buffered": {
#             "severity": "warnings",
#             "size": 2097152
#         },
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "events": {
#             "display_location": true
#         },
#         "files": [
#             {
#                 "maxfilesize": "1024",
#                 "name": "test",
#                 "path": "test",
#                 "severity": "info"
#             }
#         ],
#         "hostnameprefix": "test",
#         "hosts": [
#             {
#                 "host": "1.1.1.1",
#                 "port": "default",
#                 "severity": "critical",
#                 "vrf": "default"
#             }
#         ],
#         "ipv4": {
#             "dscp": "af11"
#         },
#         "localfilesize": 1024,
#         "monitor": {
#             "severity": "errors"
#         },
#         "source_interfaces": [
#             {
#                 "interface": "GigabitEthernet0/0/0/0",
#                 "vrf": "test"
#             }
#         ],
#         "tls_servers": [
#             {
#                 "name": "test",
#                 "tls_hostname": "test2",
#                 "trustpoint": "test2",
#                 "vrf": "test"
#             }
#         ],
#         "trap": {
#             "severity": "informational"
#         }
#     },
#     "changed": true,
#     "commands": [
#         "no logging buffered 2097152",
#         "no logging events display-location",
#         "no logging ipv4 dscp af11",
#         "no logging 1.1.1.1 vrf default severity critical port default",
#         "no logging source-interface GigabitEthernet0/0/0/0 vrf test",
#         "logging buffered errors",
#         "logging hostnameprefix test1",
#         "logging ipv6 dscp af11",
#         "logging trap critical",
#         "logging 1.1.1.3 vrf default severity critical port default",
#         "logging file test path test1 maxfilesize 1024 severity info",
#         "logging tls-server test trustpoint test"
#     ],
#
```

## [Return Values](iosxr_logging_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `["logging file test path test1 maxfilesize 1024 severity info", "logging ipv6 dscp af11", "logging trap critical", "logging monitor errors", "logging buffered errors", "logging 1.1.1.3 vrf default severity critical port default"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when state is *parsed*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when state is *rendered*  **Sample:** `["logging buffered errors", "logging correlator buffer-size 1024", "logging hostnameprefix test1", "logging ipv6 dscp af11", "logging localfilesize 1024", "logging trap disable", "logging monitor disable", "logging history disable", "logging console disable"]` |

### Authors

- Ashwini Mhatre (@amhatre)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
