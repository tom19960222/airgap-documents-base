---
collection: ansible
version: "6"
title: "cisco.ios.ios_logging_global module – Resource module to configure logging."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_logging_global_module.html
fetched_at: 2026-07-27T16:55:21+00:00
---
# cisco.ios.ios_logging_global module – Resource module to configure logging.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_logging_global`.

New in cisco.ios 2.2.0

- [Synopsis](ios_logging_global_module.md#synopsis)
- [Parameters](ios_logging_global_module.md#parameters)
- [Notes](ios_logging_global_module.md#notes)
- [Examples](ios_logging_global_module.md#examples)
- [Return Values](ios_logging_global_module.md#return-values)

## [Synopsis](ios_logging_global_module.md#id1)

- This module manages the logging attributes of Cisco IOS network devices

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_logging_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of logging options |
| **buffered**  dictionary | Set buffered logging parameters |
| **discriminator**  string | Establish MD-Buffer association |
| **filtered**  boolean | Enable filtered logging  Choices:   - `false` - `true` |
| **severity**  string | Logging severity level  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **size**  integer | Logging buffer size |
| **xml**  boolean | Enable logging in XML to XML logging buffer  Choices:   - `false` - `true` |
| **buginf**  boolean | Enable buginf logging for debugging  Choices:   - `false` - `true` |
| **cns_events**  string | Set CNS Event logging level  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **console**  dictionary | Set console logging parameters |
| **discriminator**  string | Establish MD-Buffer association |
| **filtered**  boolean | Enable filtered logging  Choices:   - `false` - `true` |
| **severity**  string | Logging severity level  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` - `"guaranteed"` |
| **xml**  boolean | Enable logging in XML to XML logging buffer  Choices:   - `false` - `true` |
| **count**  boolean | Count every log message and timestamp last occurrence  Choices:   - `false` - `true` |
| **delimiter**  dictionary | Append delimiter to syslog messages |
| **tcp**  boolean | Append delimiter to syslog messages over TCP  Choices:   - `false` - `true` |
| **discriminator**  list / elements=string | Create or modify a message discriminator |
| **dmvpn**  dictionary | DMVPN Configuration |
| **rate_limit**  integer | rate in messages/minute, default is 600 messages/minute (1-10000) |
| **esm**  dictionary | Set ESM filter restrictions |
| **config**  boolean | Permit/Deny configuration changes from ESM filters  Choices:   - `false` - `true` |
| **exception**  integer | Limit size of exception flush output (4096-2147483647) |
| **facility**  string | Facility parameter for syslog messages  Choices:   - `"auth"` - `"cron"` - `"daemon"` - `"kern"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` - `"lpr"` - `"mail"` - `"news"` - `"sys10"` - `"sys11"` - `"sys12"` - `"sys13"` - `"sys14"` - `"sys9"` - `"syslog"` - `"user"` - `"uucp"` |
| **filter**  list / elements=dictionary | Specify logging filter |
| **args**  string | Arguments passed to filter module. |
| **order**  integer | Order of filter execution |
| **url**  string | Filter Uniform Resource Locator |
| **history**  dictionary | Configure syslog history table |
| **severity**  string | Logging severity level  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **size**  integer | Logging buffer size |
| **hosts**  list / elements=dictionary | Set syslog server IP address and parameters |
| **discriminator**  string | Establish MD-Buffer association |
| **filtered**  boolean | Enable filtered logging  Choices:   - `false` - `true` |
| **host**  aliases: hostname  string | IP address of the syslog server |
| **ipv6**  string | Configure IPv6 syslog server |
| **sequence_num_session**  boolean | Include session sequence number tag in syslog message  Choices:   - `false` - `true` |
| **session_id**  dictionary | Specify syslog message session ID tagging |
| **tag**  string | Include hostname in session ID tag  Choices:   - `"hostname"` - `"ipv4"` - `"ipv6"` |
| **text**  string | Include custom string in session ID tag |
| **stream**  integer | This server should only receive messages from a numbered stream |
| **transport**  dictionary | Specify the transport protocol (default=UDP) |
| **tcp**  dictionary | Transport Control Protocol |
| **audit**  boolean | Set this host for IOS firewall audit logging  Choices:   - `false` - `true` |
| **discriminator**  string | Establish MD-Buffer association |
| **filtered**  boolean | Enable filtered logging  Choices:   - `false` - `true` |
| **port**  integer | Specify the TCP port number (default=601) (1 - 65535) |
| **sequence_num_session**  boolean | Include session sequence number tag in syslog message  Choices:   - `false` - `true` |
| **session_id**  dictionary | Specify syslog message session ID tagging |
| **tag**  string | Include hostname in session ID tag  Choices:   - `"hostname"` - `"ipv4"` - `"ipv6"` |
| **text**  string | Include custom string in session ID tag |
| **stream**  integer | This server should only receive messages from a numbered stream |
| **xml**  boolean | Enable logging in XML to XML logging buffer  Choices:   - `false` - `true` |
| **udp**  dictionary | User Datagram Protocol |
| **discriminator**  string | Establish MD-Buffer association |
| **filtered**  boolean | Enable filtered logging  Choices:   - `false` - `true` |
| **port**  integer | Specify the UDP port number (default=514) (1 - 65535) |
| **sequence_num_session**  boolean | Include session sequence number tag in syslog message  Choices:   - `false` - `true` |
| **session_id**  dictionary | Specify syslog message session ID tagging |
| **tag**  string | Include hostname in session ID tag  Choices:   - `"hostname"` - `"ipv4"` - `"ipv6"` |
| **text**  string | Include custom string in session ID tag |
| **stream**  integer | This server should only receive messages from a numbered stream |
| **xml**  boolean | Enable logging in XML to XML logging buffer  Choices:   - `false` - `true` |
| **vrf**  string | Set VRF option |
| **xml**  boolean | Enable logging in XML to XML logging buffer  Choices:   - `false` - `true` |
| **logging_on**  string | Enable logging to all enabled destinations  Choices:   - `"enable"` - `"disable"` |
| **message_counter**  list / elements=string | Configure log message to include certain counter value  Choices:   - `"log"` - `"debug"` - `"syslog"` |
| **monitor**  dictionary | Set terminal line (monitor) logging parameters |
| **discriminator**  string | Establish MD-Buffer association |
| **filtered**  boolean | Enable filtered logging  Choices:   - `false` - `true` |
| **severity**  string | Logging severity level  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **xml**  boolean | Enable logging in XML to XML logging buffer  Choices:   - `false` - `true` |
| **origin_id**  dictionary | Add origin ID to syslog messages |
| **tag**  string | Include hostname in session ID tag  Choices:   - `"hostname"` - `"ip"` - `"ipv6"` |
| **text**  string | Include custom string in session ID tag |
| **persistent**  dictionary | Set persistent logging parameters |
| **batch**  integer | Set batch size for writing to persistent storage (4096-2142715904) |
| **filesize**  integer | Set size of individual log files (4096-2142715904) |
| **immediate**  boolean | Write log entry to storage immediately (no buffering).  Choices:   - `false` - `true` |
| **notify**  boolean | Notify when show logging [persistent] is activated.  Choices:   - `false` - `true` |
| **protected**  boolean | Eliminates manipulation on logging-persistent files.  Choices:   - `false` - `true` |
| **size**  integer | Set disk space for writing log messages (4096-2142715904) |
| **threshold**  integer | Set threshold for logging persistent |
| **url**  string | URL to store logging messages |
| **policy_firewall**  dictionary | Firewall configuration |
| **rate_limit**  integer | (0-3600) value in seconds, default is 30 Sec. |
| **queue_limit**  dictionary | Set logger message queue size |
| **esm**  integer | (100-2147483647) set new queue size |
| **size**  integer | (100-2147483647) set new queue size |
| **trap**  integer | (100-2147483647) set new queue size |
| **rate_limit**  dictionary | Set messages per second limit |
| **all**  boolean | (1-10000) message per second  Choices:   - `false` - `true` |
| **console**  boolean | (1-10000) message per second  Choices:   - `false` - `true` |
| **except_severity**  string | Messages of this severity or higher  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **size**  integer / required | (1-10000) message per second |
| **reload**  dictionary | Set reload logging level |
| **message_limit**  integer | Number of messages (1-4294967295) |
| **severity**  string | Logging severity level  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **server_arp**  boolean | Enable sending ARP requests for syslog servers when first configured  Choices:   - `false` - `true` |
| **snmp_trap**  list / elements=string | Set syslog level for sending snmp trap  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **source_interface**  list / elements=dictionary | Specify interface for source address in logging transactions |
| **interface**  string | Interface name with number |
| **vrf**  string | VPN Routing/Forwarding instance name |
| **trap**  string | Set syslog server logging level  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **userinfo**  boolean | Enable logging of user info on privileged mode enabling  Choices:   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | include logging**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  With state *replaced*, for the listed logging configurations, that are in running-config and can have multiple set of commands but not in the task are negated.  With state *overridden*, all configurations that are in running-config but not in the task are negated.  Please refer to examples for more details.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](ios_logging_global_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.6
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - The Configuration defaults of the Cisco IOS network devices are supposed to hinder idempotent behavior of plays

## [Examples](ios_logging_global_module.md#id4)

```yaml+jinja
# Using state: merged

# Before state:
# -------------

# router-ios#show running-config | section logging
# no logging exception
# no logging buffered
# no logging reload
# no logging rate-limit
# no logging console
# no logging monitor
# no logging cns-events
# no logging trap

- name: Apply the provided configuration
  cisco.ios.ios_logging_global:
    config:
      buffered:
        severity: notifications
        size: 5099
        xml: True
      console:
        severity: critical
        xml: True
      facility: local5
      hosts:
        - hostname: 172.16.1.12
        - hostname: 172.16.1.11
          xml: True
        - hostname: 172.16.1.10
          filtered: True
          stream: 10
        - hostname: 172.16.1.13
          transport:
            tcp:
              port: 514
      monitor:
        severity: warnings
      message_counter: log
      snmp_trap:
        - errors
      trap: errors
      userinfo: True
      policy_firewall:
        rate_limit: 10
      logging_on: True
      exception: 4099
      dmvpn:
        rate_limit: 10
      cns_events: warnings
    state: merged

# Commands Fired:
# ---------------

# "commands": [
#       "logging buffered xml 5099 notifications",
#       "logging cns-events warnings",
#       "logging console xml critical",
#       "logging dmvpn rate-limit 10",
#       "logging exception 4099",
#       "logging facility local5",
#       "logging monitor warnings",
#       "logging on",
#       "logging policy-firewall rate-limit 10",
#       "logging trap errors",
#       "logging userinfo",
#       "logging host 172.16.1.12",
#       "logging host 172.16.1.10 filtered stream 10",
#       "logging host 172.16.1.13 transport tcp port 514",
#       "logging message-counter log",
#       "logging snmp-trap errors",
#       "logging host 172.16.1.11 xml"
#     ],

# After state:
# ------------

# router-ios#show running-config | section logging
# logging exception 4099
# logging message-counter log
# logging userinfo
# logging buffered xml 5099 notifications
# no logging reload
# no logging rate-limit
# logging console xml critical
# logging monitor warnings
# logging cns-events warnings
# logging policy-firewall rate-limit 10
# logging dmvpn rate-limit 10
# logging trap errors
# logging facility local5
# logging snmp-trap errors
# logging snmp-trap warnings
# logging host 172.16.1.13 transport tcp port 514
# logging host 172.16.1.11 xml
# logging host 172.16.1.12
# logging host 172.16.1.10 filtered stream 10

# Using state: deleted

# Before state:
# -------------

# router-ios#show running-config | section logging
# logging exception 4099
# logging message-counter log
# logging userinfo
# logging buffered xml 5099 notifications
# no logging reload
# no logging rate-limit
# logging console xml critical
# logging monitor warnings
# logging cns-events warnings
# logging policy-firewall rate-limit 10
# logging dmvpn rate-limit 10
# logging trap errors
# logging facility local5
# logging snmp-trap errors
# logging host 172.16.1.13 transport tcp port 514
# logging host 172.16.1.11 xml
# logging host 172.16.1.12
# logging host 172.16.1.10 filtered stream 10

- name: Remove all existing configuration
  cisco.ios.ios_logging_global:
    state: deleted

# Commands Fired:
# ---------------

# "commands": [
#       "no logging message-counter log",
#       "no logging snmp-trap errors",
#       "no logging host 172.16.1.13",
#       "no logging host 172.16.1.11",
#       "no logging host 172.16.1.12",
#       "no logging host 172.16.1.10",
#       "no logging exception 4099",
#       "no logging userinfo",
#       "no logging buffered xml 5099 notifications",
#       "no logging console xml critical",
#       "no logging monitor warnings",
#       "no logging cns-events warnings",
#       "no logging policy-firewall rate-limit 10",
#       "no logging dmvpn rate-limit 10",
#       "no logging trap errors",
#       "no logging facility local5"
#     ],

# After state:
# ------------

# router-ios#show running-config | section logging
# no logging exception
# no logging buffered
# no logging reload
# no logging rate-limit
# no logging console
# no logging monitor
# no logging cns-events
# no logging trap

# Using state: overridden

# Before state:
# -------------

# router-ios#show running-config | section logging
# logging exception 4099
# logging message-counter log
# logging userinfo
# logging buffered 6000 critical
# no logging reload
# no logging rate-limit
# logging console xml critical
# logging monitor warnings
# logging cns-events warnings
# logging policy-firewall rate-limit 10
# logging dmvpn rate-limit 10
# logging trap errors
# logging facility local6
# logging host 172.16.1.13 transport tcp port 514
# logging host 172.16.1.12
# logging host 172.16.1.10 filtered stream 10
# logging host 172.16.1.25 filtered

- name: Override commands with provided configuration
  cisco.ios.ios_logging_global:
    config:
      hosts:
        - hostname: 172.16.1.27
          filtered: True
    state: overridden

# Commands Fired:
# ---------------
# "commands": [
#         "no logging message-counter log",
#         "no logging host 172.16.1.12",
#         "no logging host 172.16.1.10",
#         "no logging host 172.16.1.13",
#         "no logging exception 4099",
#         "no logging userinfo",
#         "no logging console xml critical",
#         "no logging monitor warnings",
#         "no logging cns-events warnings",
#         "no logging policy-firewall rate-limit 10",
#         "no logging dmvpn rate-limit 10",
#         "no logging trap errors",
#         "no logging buffered 6000 critical",
#         "no logging facility local6",
#         "logging host 172.16.1.27 filtered",
#     ],

# After state:
# ------------

# router-ios#show running-config | section logging
# no logging exception
# no logging buffered
# no logging reload
# no logging rate-limit
# no logging console
# no logging monitor
# no logging cns-events
# no logging trap
# logging host 172.16.1.27 filtered

# Using state: replaced

# Before state:
# -------------

# router-ios#show running-config | section logging
# logging exception 4099
# logging message-counter log
# logging userinfo
# logging buffered xml 5099 notifications
# no logging reload
# no logging rate-limit
# logging console xml critical
# logging monitor warnings
# logging cns-events warnings
# logging policy-firewall rate-limit 10
# logging dmvpn rate-limit 10
# logging trap errors
# logging facility local5
# logging snmp-trap errors
# logging host 172.16.1.13 transport tcp port 514
# logging host 172.16.1.11 xml
# logging host 172.16.1.12
# logging host 172.16.1.10 filtered stream 10

- name: Replace commands with provided configuration
  cisco.ios.ios_logging_global:
    config:
      buffered:
        severity: alerts
        size: 6025
      facility: local6
      hosts:
        - hostname: 172.16.1.19
        - hostname: 172.16.1.10
          filtered: true
          stream: 15
    state: replaced

# Commands Fired:
# ---------------

# "commands": [
#         "no logging host 172.16.1.13",
#         "no logging host 172.16.1.11",
#         "no logging host 172.16.1.12",
#         "no logging host 172.16.1.10",
#         "logging host 172.16.1.19",
#         "logging host 172.16.1.10 filtered stream 15",
#         "logging buffered 6025 alerts",
#         "logging facility local6"
#     ],

# After state:
# ------------

# router-ios#show running-config | section logging
# logging exception 4099
# logging message-counter log
# logging userinfo
# logging buffered 6025 alerts
# no logging reload
# no logging rate-limit
# logging console xml critical
# logging monitor warnings
# logging cns-events warnings
# logging policy-firewall rate-limit 10
# logging dmvpn rate-limit 10
# logging trap errors
# logging facility local6
# logging snmp-trap errors
# logging host 172.16.1.19

# Using state: gathered

# Before state:
# -------------

#router-ios#show running-config | section logging
# logging exception 4099
# logging message-counter log
# logging userinfo
# logging buffered xml 5099 notifications
# no logging reload
# no logging rate-limit
# logging console xml critical
# logging monitor warnings
# logging cns-events warnings
# logging policy-firewall rate-limit 10
# logging dmvpn rate-limit 10
# logging trap errors
# logging facility local5
# logging snmp-trap errors
# logging host 172.16.1.13 transport tcp port 514
# logging host 172.16.1.11 xml
# logging host 172.16.1.12
# logging host 172.16.1.10 filtered stream 10
# logging host 172.16.1.25 filtered

- name: Gather listed logging config
  cisco.ios.ios_logging_global:
    state: gathered

# Module Execution Result:
# ------------------------

# "gathered": {
#     "buffered": {
#         "severity": "notifications",
#         "size": 5099,
#         "xml": true
#     },
#     "cns_events": "warnings",
#     "console": {
#         "severity": "critical",
#         "xml": true
#     },
#     "dmvpn": {
#         "rate_limit": 10
#     },
#     "exception": 4099,
#     "facility": "local5",
#     "hosts": [
#         {
#             "hostname": "172.16.1.11",
#             "xml": true
#         },
#         {
#             "hostname": "172.16.1.12"
#         },
#         {
#             "filtered": true,
#             "hostname": "172.16.1.10",
#             "stream": 10
#         },
#         {
#             "hostname": "172.16.1.13",
#             "transport": {
#                 "tcp": {
#                     "port": 514
#                 }
#             }
#         },
#         {
#             "filtered": true,
#             "hostname": "172.16.1.25"
#         }
#     ],
#     "message_counter": [
#         "log"
#     ],
#     "monitor": {
#         "severity": "warnings"
#     },
#     "policy_firewall": {
#         "rate_limit": 10
#     },
#     "snmp_trap": [
#         "errors"
#     ],
#     "trap": "errors",
#     "userinfo": true
# },

# After state:
# -------------

# router-ios#show running-config | section logging
# logging exception 4099
# logging message-counter log
# logging userinfo
# logging buffered xml 5099 notifications
# no logging reload
# no logging rate-limit
# logging console xml critical
# logging monitor warnings
# logging cns-events warnings
# logging policy-firewall rate-limit 10
# logging dmvpn rate-limit 10
# logging trap errors
# logging facility local5
# logging snmp-trap errors
# logging host 172.16.1.13 transport tcp port 514
# logging host 172.16.1.11 xml
# logging host 172.16.1.12
# logging host 172.16.1.10 filtered stream 10
# logging host 172.16.1.25 filtered

# Using state: rendered

- name: Render the commands for provided configuration
  cisco.ios.ios_logging_global:
    config:
      buffered:
        severity: notifications
        size: 5099
        xml: True
      console:
        severity: critical
        xml: True
      facility: local5
      hosts:
        - hostname: 172.16.1.12
        - hostname: 172.16.1.11
          xml: True
        - hostname: 172.16.1.10
          filtered: True
          stream: 10
        - hostname: 172.16.1.13
          transport:
            tcp:
              port: 514
      monitor:
        severity: warnings
      message_counter: log
      snmp_trap: errors
      trap: errors
      userinfo: True
      policy_firewall:
          rate_limit: 10
      logging_on: True
      exception: 10
      dmvpn:
        rate_limit: 10
      cns_events: warnings
    state: rendered

# Module Execution Result:
# ------------------------

# "rendered": [
#     "logging host 172.16.1.12",
#     "logging host 172.16.1.11 xml",
#     "logging host 172.16.1.10 filtered stream 10",
#     "logging host 172.16.1.13 transport tcp port 514",
#     "logging message-counter log",
#     "logging snmp-trap errors",
#     "logging buffered xml 5099 notifications",
#     "logging console xml critical",
#     "logging facility local5",
#     "logging monitor warnings",
#     "logging trap errors",
#     "logging userinfo",
#     "logging policy-firewall rate-limit 10",
#     "logging on",
#     "logging exception 10",
#     "logging dmvpn rate-limit 10",
#     "logging cns-events warnings"
#     ]

# Using state: parsed

# File: parsed.cfg
# ----------------

# logging on
# logging count
# logging userinfo
# logging trap errors
# logging reload alerts
# logging host 172.16.1.1
# logging exception 4099
# logging history alerts
# logging facility local5
# logging snmp-trap errors
# logging monitor warnings
# logging origin-id hostname
# logging host 172.16.1.11 xml
# logging cns-events warnings
# logging dmvpn rate-limit 10
# logging message-counter log
# logging console xml critical
# logging message-counter debug
# logging persistent batch 4444
# logging host 172.16.1.25 filtered
# logging source-interface GBit1/0
# logging source-interface CTunnel2
# logging policy-firewall rate-limit 10
# logging buffered xml 5099 notifications
# logging rate-limit all 2 except warnings
# logging host 172.16.1.10 filtered stream 10
# logging host 172.16.1.13 transport tcp port 514
# logging discriminator msglog01 severity includes 5
# logging filter tftp://172.16.2.18/ESM/elate.tcl args TESTInst2
# logging filter tftp://172.16.2.14/ESM/escalate.tcl args TESTInst

- name: Parse the provided configuration with the existing running configuration
  cisco.ios.ios_logging_global:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------

# "parsed": {
#     "buffered": {
#         "severity": "notifications",
#         "size": 5099,
#         "xml": true
#     },
#     "cns_events": "warnings",
#     "console": {
#         "severity": "critical",
#         "xml": true
#     },
#     "count": true,
#     "discriminator": [
#         "msglog01 severity includes 5"
#     ],
#     "dmvpn": {
#         "rate_limit": 10
#     },
#     "exception": 4099,
#     "facility": "local5",
#     "filter": [
#         {
#             "args": "TESTInst2",
#             "url": "tftp://172.16.2.18/ESM/elate.tcl"
#         },
#         {
#             "args": "TESTInst",
#             "url": "tftp://172.16.2.14/ESM/escalate.tcl"
#         }
#     ],
#     "history": {
#         "severity": "alerts"
#     },
#     "hosts": [
#         {
#             "hostname": "172.16.1.1"
#         },
#         {
#             "hostname": "172.16.1.11",
#             "xml": true
#         },
#         {
#             "filtered": true,
#             "hostname": "172.16.1.25"
#         },
#         {
#             "filtered": true,
#             "hostname": "172.16.1.10",
#             "stream": 10
#         },
#         {
#             "hostname": "172.16.1.13",
#             "transport": {
#                 "tcp": {
#                     "port": 514
#                 }
#             }
#         }
#     ],
#     "logging_on": "enable",
#     "message_counter": [
#         "log",
#         "debug"
#     ],
#     "monitor": {
#         "severity": "warnings"
#     },
#     "origin_id": {
#         "tag": "hostname"
#     },
#     "persistent": {
#         "batch": 4444
#     },
#     "policy_firewall": {
#         "rate_limit": 10
#     },
#     "rate_limit": {
#         "all": true,
#         "except_severity": "warnings",
#         "size": 2
#     },
#     "reload": {
#         "severity": "alerts"
#     },
#     "snmp_trap": [
#         "errors"
#     ],
#     "source_interface": [
#         {
#             "interface": "GBit1/0"
#         },
#         {
#             "interface": "CTunnel2"
#         }
#     ],
#     "trap": "errors",
#     "userinfo": true
# }
```

## [Return Values](ios_logging_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["logging on", "logging userinfo", "logging trap errors", "logging host 172.16.1.12", "logging console xml critical", "logging message-counter log", "logging policy-firewall rate-limit 10"]` |

### Authors

- Sagar Paul (@KB-perByte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
