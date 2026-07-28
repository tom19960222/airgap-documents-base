---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_firewall_rules module – FIREWALL rules resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_firewall_rules_module.html
fetched_at: 2026-07-28T00:23:16+00:00
---
# vyos.vyos.vyos_firewall_rules module – FIREWALL rules resource module

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/vyos/vyos) (version 3.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_firewall_rules`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_firewall_rules_module.md#synopsis)
- [Parameters](vyos_firewall_rules_module.md#parameters)
- [Notes](vyos_firewall_rules_module.md#notes)
- [Examples](vyos_firewall_rules_module.md#examples)
- [Return Values](vyos_firewall_rules_module.md#return-values)

## [Synopsis](vyos_firewall_rules_module.md#id1)

- This module manages firewall rule-set attributes on VyOS devices

## [Parameters](vyos_firewall_rules_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Firewall rule-set options. |
| **afi**  string / required | Specifies the type of rule-set.  Choices:   - `"ipv4"` - `"ipv6"` |
| **rule_sets**  list / elements=dictionary | The Firewall rule-set list. |
| **default_action**  string | Default action for rule-set.  drop (Drop if no prior rules are hit (default))  reject (Drop and notify source if no prior rules are hit)  accept (Accept if no prior rules are hit)  Choices:   - `"drop"` - `"reject"` - `"accept"` |
| **description**  string | Rule set description. |
| **enable_default_log**  boolean | Option to log packets hitting default-action.  Choices:   - `false` - `true` |
| **name**  string | Firewall rule set name. |
| **rules**  list / elements=dictionary | A dictionary that specifies the rule-set configurations. |
| **action**  string | Specifying the action.  Choices:   - `"drop"` - `"reject"` - `"accept"` - `"inspect"` |
| **description**  string | Description of this rule. |
| **destination**  dictionary | Specifying the destination parameters. |
| **address**  string | Destination ip address subnet or range.  IPv4/6 address, subnet or range to match.  Match everything except the specified address, subnet or range.  Destination ip address subnet or range. |
| **group**  dictionary | Destination group. |
| **address_group**  string | Group of addresses. |
| **network_group**  string | Group of networks. |
| **port_group**  string | Group of ports. |
| **port**  string | Multiple destination ports can be specified as a comma-separated list.  The whole list can also be “negated” using ‘!’.  For example:’!22,telnet,http,123,1001-1005’. |
| **disable**  aliases: disabled  boolean | Option to disable firewall rule.  Choices:   - `false` - `true` |
| **fragment**  string | IP fragment match.  Choices:   - `"match-frag"` - `"match-non-frag"` |
| **icmp**  dictionary | ICMP type and code information. |
| **code**  integer | ICMP code. |
| **type**  integer | ICMP type. |
| **type_name**  string | ICMP type-name.  Choices:   - `"any"` - `"echo-reply"` - `"destination-unreachable"` - `"network-unreachable"` - `"host-unreachable"` - `"protocol-unreachable"` - `"port-unreachable"` - `"fragmentation-needed"` - `"source-route-failed"` - `"network-unknown"` - `"host-unknown"` - `"network-prohibited"` - `"host-prohibited"` - `"TOS-network-unreachable"` - `"TOS-host-unreachable"` - `"communication-prohibited"` - `"host-precedence-violation"` - `"precedence-cutoff"` - `"source-quench"` - `"redirect"` - `"network-redirect"` - `"host-redirect"` - `"TOS-network-redirect"` - `"TOS-host-redirect"` - `"echo-request"` - `"router-advertisement"` - `"router-solicitation"` - `"time-exceeded"` - `"ttl-zero-during-transit"` - `"ttl-zero-during-reassembly"` - `"parameter-problem"` - `"ip-header-bad"` - `"required-option-missing"` - `"timestamp-request"` - `"timestamp-reply"` - `"address-mask-request"` - `"address-mask-reply"` - `"ping"` - `"pong"` - `"ttl-exceeded"` |
| **ipsec**  string | Inbound ip sec packets.  Choices:   - `"match-ipsec"` - `"match-none"` |
| **limit**  dictionary | Rate limit using a token bucket filter. |
| **burst**  integer | Maximum number of packets to allow in excess of rate. |
| **rate**  dictionary | format for rate (integer/time unit).  any one of second, minute, hour or day may be used to specify time unit.  eg. 1/second implies rule to be matched at an average of once per second. |
| **number**  integer | This is the integer value. |
| **unit**  string | This is the time unit. |
| **log**  string | Option to log packets matching rule  Choices:   - `"disable"` - `"enable"` |
| **number**  integer / required | Rule number. |
| **p2p**  list / elements=dictionary | P2P application packets. |
| **application**  string | Name of the application.  Choices:   - `"all"` - `"applejuice"` - `"bittorrent"` - `"directconnect"` - `"edonkey"` - `"gnutella"` - `"kazaa"` |
| **protocol**  string | Protocol to match (protocol name in /etc/protocols or protocol number or all).  <text> IP protocol name from /etc/protocols (e.g. “tcp” or “udp”).  <0-255> IP protocol number.  tcp_udp Both TCP and UDP.  all All IP protocols.  (!)All IP protocols except for the specified name or number. |
| **recent**  dictionary | Parameters for matching recently seen sources. |
| **count**  integer | Source addresses seen more than N times. |
| **time**  integer | Source addresses seen in the last N seconds. |
| **source**  dictionary | Source parameters. |
| **address**  string | Source ip address subnet or range.  IPv4/6 address, subnet or range to match.  Match everything except the specified address, subnet or range.  Source ip address subnet or range. |
| **group**  dictionary | Source group. |
| **address_group**  string | Group of addresses. |
| **network_group**  string | Group of networks. |
| **port_group**  string | Group of ports. |
| **mac_address**  string | <MAC address> MAC address to match.  <!MAC address> Match everything except the specified MAC address. |
| **port**  string | Multiple source ports can be specified as a comma-separated list.  The whole list can also be “negated” using ‘!’.  For example:’!22,telnet,http,123,1001-1005’. |
| **state**  dictionary | Session state. |
| **established**  boolean | Established state.  Choices:   - `false` - `true` |
| **invalid**  boolean | Invalid state.  Choices:   - `false` - `true` |
| **new**  boolean | New state.  Choices:   - `false` - `true` |
| **related**  boolean | Related state.  Choices:   - `false` - `true` |
| **tcp**  dictionary | TCP flags to match. |
| **flags**  string | TCP flags to be matched. |
| **time**  dictionary | Time to match rule. |
| **monthdays**  string | Monthdays to match rule on. |
| **startdate**  string | Date to start matching rule. |
| **starttime**  string | Time of day to start matching rule. |
| **stopdate**  string | Date to stop matching rule. |
| **stoptime**  string | Time of day to stop matching rule. |
| **utc**  boolean | Interpret times for startdate, stopdate, starttime and stoptime to be UTC.  Choices:   - `false` - `true` |
| **weekdays**  string | Weekdays to match rule on. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VyOS device by executing the command **show configuration commands | grep firewall**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](vyos_firewall_rules_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).

## [Examples](vyos_firewall_rules_module.md#id4)

```yaml+jinja
# Using deleted to delete firewall rules based on rule-set name
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall group address-group 'inbound'
# set firewall name Downlink default-action 'accept'
# set firewall name Downlink description 'IPv4 INBOUND rule set'
# set firewall name Downlink rule 501 action 'accept'
# set firewall name Downlink rule 501 description 'Rule 501 is configured by Ansible'
# set firewall name Downlink rule 501 ipsec 'match-ipsec'
# set firewall name Downlink rule 502 action 'reject'
# set firewall name Downlink rule 502 description 'Rule 502 is configured by Ansible'
# set firewall name Downlink rule 502 ipsec 'match-ipsec'
#
- name: Delete attributes of given firewall rules.
  vyos.vyos.vyos_firewall_rules:
    config:
    - afi: ipv4
      rule_sets:
      - name: Downlink
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": [
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "Downlink",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 501 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 501
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 502 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 502
#                        }
#                    ]
#               }
#            ]
#        }
#    ]
#    "commands": [
#        "delete firewall name Downlink"
#    ]
#
# "after": []
# After state
# ------------
# vyos@vyos# run show configuration commands | grep firewall
# set firewall group address-group 'inbound'

# Using deleted to delete firewall rules based on afi
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name UPLINK default-action 'accept'
# set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'
# set firewall ipv6-name UPLINK rule 1 action 'accept'
# set firewall ipv6-name UPLINK rule 1
# set firewall ipv6-name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 1 ipsec 'match-ipsec'
# set firewall ipv6-name UPLINK rule 2 action 'accept'
# set firewall ipv6-name UPLINK rule 2
# set firewall ipv6-name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 2 ipsec 'match-ipsec'
# set firewall group address-group 'inbound'
# set firewall name Downlink default-action 'accept'
# set firewall name Downlink description 'IPv4 INBOUND rule set'
# set firewall name Downlink rule 501 action 'accept'
# set firewall name Downlink rule 501 description 'Rule 501 is configured by Ansible'
# set firewall name Downlink rule 501 ipsec 'match-ipsec'
# set firewall name Downlink rule 502 action 'reject'
# set firewall name Downlink rule 502 description 'Rule 502 is configured by Ansible'
# set firewall name Downlink rule 502 ipsec 'match-ipsec'

#
- name: Delete attributes of given firewall rules.
  vyos.vyos.vyos_firewall_rules:
    config:
    - afi: ipv4
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": [
#        {
#            "afi": "ipv6",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "This is ipv6 specific rule-set",
#                    "name": "UPLINK",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 1 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 1
#                        },
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 2 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 2
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "Downlink",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 501 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 501
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 502 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 502
#                        }
#                    ]
#               }
#            ]
#        }
#    ]
#    "commands": [
#        "delete firewall name"
#    ]
#
# "after": []
# After state
# ------------
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name UPLINK default-action 'accept'
# set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'
# set firewall ipv6-name UPLINK rule 1 action 'accept'
# set firewall ipv6-name UPLINK rule 1
# set firewall ipv6-name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 1 ipsec 'match-ipsec'
# set firewall ipv6-name UPLINK rule 2 action 'accept'
# set firewall ipv6-name UPLINK rule 2
# set firewall ipv6-name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 2 ipsec 'match-ipsec'

# Using deleted to delete all the the firewall rules when provided config is empty
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall group address-group 'inbound'
# set firewall name Downlink default-action 'accept'
# set firewall name Downlink description 'IPv4 INBOUND rule set'
# set firewall name Downlink rule 501 action 'accept'
# set firewall name Downlink rule 501 description 'Rule 501 is configured by Ansible'
# set firewall name Downlink rule 501 ipsec 'match-ipsec'
# set firewall name Downlink rule 502 action 'reject'
# set firewall name Downlink rule 502 description 'Rule 502 is configured by Ansible'
# set firewall name Downlink rule 502 ipsec 'match-ipsec'
#
- name: Delete attributes of given firewall rules.
  vyos.vyos.vyos_firewall_rules:
    config:
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": [
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "Downlink",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 501 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 501
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 502 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 502
#                        }
#                    ]
#               }
#            ]
#        }
#    ]
#    "commands": [
#        "delete firewall name"
#    ]
#
# "after": []
# After state
# ------------
# vyos@vyos# run show configuration commands | grep firewall
# set firewall group address-group 'inbound'

# Using merged
#
# Before state:
# -------------
#
# vyos@vyos# run show  configuration commands | grep firewall
# set firewall group address-group 'inbound'
#
- name: Merge the provided configuration with the existing running configuration
  vyos.vyos.vyos_firewall_rules:
    config:
    - afi: ipv6
      rule_sets:
      - name: UPLINK
        description: This is ipv6 specific rule-set
        default_action: accept
        rules:
        - number: 1
          action: accept
          description: Fwipv6-Rule 1 is configured by Ansible
          ipsec: match-ipsec
        - number: 2
          action: accept
          description: Fwipv6-Rule 2 is configured by Ansible
          ipsec: match-ipsec

    - afi: ipv4
      rule_sets:
      - name: INBOUND
        description: IPv4 INBOUND rule set
        default_action: accept
        rules:
        - number: 101
          action: accept
          description: Rule 101 is configured by Ansible
          ipsec: match-ipsec
        - number: 102
          action: reject
          description: Rule 102 is configured by Ansible
          ipsec: match-ipsec
        - number: 103
          action: accept
          description: Rule 103 is configured by Ansible
          destination:
            group:
              address_group: inbound
          source:
            address: 192.0.2.0
          state:
            established: true
            new: false
            invalid: false
            related: true
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
#       "set firewall ipv6-name UPLINK default-action 'accept'",
#       "set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'",
#       "set firewall ipv6-name UPLINK rule 1 action 'accept'",
#       "set firewall ipv6-name UPLINK rule 1",
#       "set firewall ipv6-name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'",
#       "set firewall ipv6-name UPLINK rule 1 ipsec 'match-ipsec'",
#       "set firewall ipv6-name UPLINK rule 2 action 'accept'",
#       "set firewall ipv6-name UPLINK rule 2",
#       "set firewall ipv6-name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'",
#       "set firewall ipv6-name UPLINK rule 2 ipsec 'match-ipsec'",
#       "set firewall name INBOUND default-action 'accept'",
#       "set firewall name INBOUND description 'IPv4 INBOUND rule set'",
#       "set firewall name INBOUND rule 101 action 'accept'",
#       "set firewall name INBOUND rule 101",
#       "set firewall name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
#       "set firewall name INBOUND rule 101 ipsec 'match-ipsec'",
#       "set firewall name INBOUND rule 102 action 'reject'",
#       "set firewall name INBOUND rule 102",
#       "set firewall name INBOUND rule 102 description 'Rule 102 is configured by Ansible'",
#       "set firewall name INBOUND rule 102 ipsec 'match-ipsec'",
#       "set firewall name INBOUND rule 103 description 'Rule 103 is configured by Ansible'",
#       "set firewall name INBOUND rule 103 destination group address-group inbound",
#       "set firewall name INBOUND rule 103",
#       "set firewall name INBOUND rule 103 source address 192.0.2.0",
#       "set firewall name INBOUND rule 103 state established enable",
#       "set firewall name INBOUND rule 103 state related enable",
#       "set firewall name INBOUND rule 103 state invalid disable",
#       "set firewall name INBOUND rule 103 state new disable",
#       "set firewall name INBOUND rule 103 action 'accept'"
#    ]
#
# "after": [
#        {
#            "afi": "ipv6",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "This is ipv6 specific rule-set",
#                    "name": "UPLINK",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 1 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 1
#                        },
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 2 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 2
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "INBOUND",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 101 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 101
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 102 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 102
#                        },
#                        {
#                            "action": "accept",
#                            "description": "Rule 103 is configured by Ansible",
#                            "destination": {
#                                "group": {
#                                    "address_group": "inbound"
#                                }
#                            },
#                            "number": 103,
#                            "source": {
#                                "address": "192.0.2.0"
#                            },
#                            "state": {
#                                "established": true,
#                                "invalid": false,
#                                "new": false,
#                                "related": true
#                            }
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall group address-group 'inbound'
# set firewall ipv6-name UPLINK default-action 'accept'
# set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'
# set firewall ipv6-name UPLINK rule 1 action 'accept'
# set firewall ipv6-name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 1 ipsec 'match-ipsec'
# set firewall ipv6-name UPLINK rule 2 action 'accept'
# set firewall ipv6-name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 2 ipsec 'match-ipsec'
# set firewall name INBOUND default-action 'accept'
# set firewall name INBOUND description 'IPv4 INBOUND rule set'
# set firewall name INBOUND rule 101 action 'accept'
# set firewall name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
# set firewall name INBOUND rule 101 ipsec 'match-ipsec'
# set firewall name INBOUND rule 102 action 'reject'
# set firewall name INBOUND rule 102 description 'Rule 102 is configured by Ansible'
# set firewall name INBOUND rule 102 ipsec 'match-ipsec'
# set firewall name INBOUND rule 103 action 'accept'
# set firewall name INBOUND rule 103 description 'Rule 103 is configured by Ansible'
# set firewall name INBOUND rule 103 destination group address-group 'inbound'
# set firewall name INBOUND rule 103 source address '192.0.2.0'
# set firewall name INBOUND rule 103 state established 'enable'
# set firewall name INBOUND rule 103 state invalid 'disable'
# set firewall name INBOUND rule 103 state new 'disable'
# set firewall name INBOUND rule 103 state related 'enable'

# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall group address-group 'inbound'
# set firewall ipv6-name UPLINK default-action 'accept'
# set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'
# set firewall ipv6-name UPLINK rule 1 action 'accept'
# set firewall ipv6-name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 1 ipsec 'match-ipsec'
# set firewall ipv6-name UPLINK rule 2 action 'accept'
# set firewall ipv6-name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 2 ipsec 'match-ipsec'
# set firewall name INBOUND default-action 'accept'
# set firewall name INBOUND description 'IPv4 INBOUND rule set'
# set firewall name INBOUND rule 101 action 'accept'
# set firewall name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
# set firewall name INBOUND rule 101 ipsec 'match-ipsec'
# set firewall name INBOUND rule 102 action 'reject'
# set firewall name INBOUND rule 102 description 'Rule 102 is configured by Ansible'
# set firewall name INBOUND rule 102 ipsec 'match-ipsec'
# set firewall name INBOUND rule 103 action 'accept'
# set firewall name INBOUND rule 103 description 'Rule 103 is configured by Ansible'
# set firewall name INBOUND rule 103 destination group address-group 'inbound'
# set firewall name INBOUND rule 103 source address '192.0.2.0'
# set firewall name INBOUND rule 103 state established 'enable'
# set firewall name INBOUND rule 103 state invalid 'disable'
# set firewall name INBOUND rule 103 state new 'disable'
# set firewall name INBOUND rule 103 state related 'enable'
#
- name: Replace device configurations of listed firewall rules with provided configurations
  vyos.vyos.vyos_firewall_rules:
    config:
    - afi: ipv6
      rule_sets:
      - name: UPLINK
        description: This is ipv6 specific rule-set
        default_action: accept
    - afi: ipv4
      rule_sets:
      - name: INBOUND
        description: IPv4 INBOUND rule set
        default_action: accept
        rules:
        - number: 101
          action: accept
          description: Rule 101 is configured by Ansible
          ipsec: match-ipsec
        - number: 104
          action: reject
          description: Rule 104 is configured by Ansible
          ipsec: match-none
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "afi": "ipv6",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "This is ipv6 specific rule-set",
#                    "name": "UPLINK",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 1 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 1
#                        },
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 2 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 2
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "INBOUND",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 101 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 101
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 102 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 102
#                        },
#                        {
#                            "action": "accept",
#                            "description": "Rule 103 is configured by Ansible",
#                            "destination": {
#                                "group": {
#                                    "address_group": "inbound"
#                                }
#                            },
#                            "number": 103,
#                            "source": {
#                                "address": "192.0.2.0"
#                            },
#                            "state": {
#                                "established": true,
#                                "invalid": false,
#                                "new": false,
#                                "related": true
#                            }
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
# "commands": [
#        "delete firewall ipv6-name UPLINK rule 1",
#        "delete firewall ipv6-name UPLINK rule 2",
#        "delete firewall name INBOUND rule 102",
#        "delete firewall name INBOUND rule 103",
#        "set firewall name INBOUND rule 104 action 'reject'",
#        "set firewall name INBOUND rule 104 description 'Rule 104 is configured by Ansible'",
#        "set firewall name INBOUND rule 104",
#        "set firewall name INBOUND rule 104 ipsec 'match-none'"
#    ]
#
#    "after": [
#        {
#            "afi": "ipv6",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "This is ipv6 specific rule-set",
#                    "name": "UPLINK"
#                }
#            ]
#        },
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "INBOUND",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 101 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 101
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 104 is configured by Ansible",
#                            "ipsec": "match-none",
#                            "number": 104
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall group address-group 'inbound'
# set firewall ipv6-name UPLINK default-action 'accept'
# set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'
# set firewall name INBOUND default-action 'accept'
# set firewall name INBOUND description 'IPv4 INBOUND rule set'
# set firewall name INBOUND rule 101 action 'accept'
# set firewall name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
# set firewall name INBOUND rule 101 ipsec 'match-ipsec'
# set firewall name INBOUND rule 104 action 'reject'
# set firewall name INBOUND rule 104 description 'Rule 104 is configured by Ansible'
# set firewall name INBOUND rule 104 ipsec 'match-none'

# Using overridden
#
# Before state
# --------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall group address-group 'inbound'
# set firewall ipv6-name UPLINK default-action 'accept'
# set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'
# set firewall name INBOUND default-action 'accept'
# set firewall name INBOUND description 'IPv4 INBOUND rule set'
# set firewall name INBOUND rule 101 action 'accept'
# set firewall name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
# set firewall name INBOUND rule 101 ipsec 'match-ipsec'
# set firewall name INBOUND rule 104 action 'reject'
# set firewall name INBOUND rule 104 description 'Rule 104 is configured by Ansible'
# set firewall name INBOUND rule 104 ipsec 'match-none'
#
- name: Overrides all device configuration with provided configuration
  vyos.vyos.vyos_firewall_rules:
    config:
    - afi: ipv4
      rule_sets:
      - name: Downlink
        description: IPv4 INBOUND rule set
        default_action: accept
        rules:
        - number: 501
          action: accept
          description: Rule 501 is configured by Ansible
          ipsec: match-ipsec
        - number: 502
          action: reject
          description: Rule 502 is configured by Ansible
          ipsec: match-ipsec
    state: overridden
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# "before": [
#        {
#            "afi": "ipv6",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "This is ipv6 specific rule-set",
#                    "name": "UPLINK"
#                }
#            ]
#        },
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "INBOUND",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 101 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 101
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 104 is configured by Ansible",
#                            "ipsec": "match-none",
#                            "number": 104
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
#    "commands": [
#        "delete firewall ipv6-name UPLINK",
#        "delete firewall name INBOUND",
#        "set firewall name Downlink default-action 'accept'",
#        "set firewall name Downlink description 'IPv4 INBOUND rule set'",
#        "set firewall name Downlink rule 501 action 'accept'",
#        "set firewall name Downlink rule 501",
#        "set firewall name Downlink rule 501 description 'Rule 501 is configured by Ansible'",
#        "set firewall name Downlink rule 501 ipsec 'match-ipsec'",
#        "set firewall name Downlink rule 502 action 'reject'",
#        "set firewall name Downlink rule 502",
#        "set firewall name Downlink rule 502 description 'Rule 502 is configured by Ansible'",
#        "set firewall name Downlink rule 502 ipsec 'match-ipsec'"
#
#
#    "after": [
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "Downlink",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 501 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 501
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 502 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 502
#                        }
#                    ]
#               }
#            ]
#        }
#    ]
#
#
# After state
# ------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall group address-group 'inbound'
# set firewall name Downlink default-action 'accept'
# set firewall name Downlink description 'IPv4 INBOUND rule set'
# set firewall name Downlink rule 501 action 'accept'
# set firewall name Downlink rule 501 description 'Rule 501 is configured by Ansible'
# set firewall name Downlink rule 501 ipsec 'match-ipsec'
# set firewall name Downlink rule 502 action 'reject'
# set firewall name Downlink rule 502 description 'Rule 502 is configured by Ansible'
# set firewall name Downlink rule 502 ipsec 'match-ipsec'

# Using gathered
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall group address-group 'inbound'
# set firewall ipv6-name UPLINK default-action 'accept'
# set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'
# set firewall ipv6-name UPLINK rule 1 action 'accept'
# set firewall ipv6-name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 1 ipsec 'match-ipsec'
# set firewall ipv6-name UPLINK rule 2 action 'accept'
# set firewall ipv6-name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 2 ipsec 'match-ipsec'
# set firewall name INBOUND default-action 'accept'
# set firewall name INBOUND description 'IPv4 INBOUND rule set'
# set firewall name INBOUND rule 101 action 'accept'
# set firewall name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
# set firewall name INBOUND rule 101 ipsec 'match-ipsec'
# set firewall name INBOUND rule 102 action 'reject'
# set firewall name INBOUND rule 102 description 'Rule 102 is configured by Ansible'
# set firewall name INBOUND rule 102 ipsec 'match-ipsec'
# set firewall name INBOUND rule 103 action 'accept'
# set firewall name INBOUND rule 103 description 'Rule 103 is configured by Ansible'
# set firewall name INBOUND rule 103 destination group address-group 'inbound'
# set firewall name INBOUND rule 103 source address '192.0.2.0'
# set firewall name INBOUND rule 103 state established 'enable'
# set firewall name INBOUND rule 103 state invalid 'disable'
# set firewall name INBOUND rule 103 state new 'disable'
# set firewall name INBOUND rule 103 state related 'enable'
#
- name: Gather listed firewall rules with provided configurations
  vyos.vyos.vyos_firewall_rules:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#        {
#            "afi": "ipv6",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "This is ipv6 specific rule-set",
#                    "name": "UPLINK",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 1 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 1
#                        },
#                        {
#                            "action": "accept",
#                            "description": "Fwipv6-Rule 2 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 2
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "INBOUND",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 101 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 101
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 102 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 102
#                        },
#                        {
#                            "action": "accept",
#                            "description": "Rule 103 is configured by Ansible",
#                            "destination": {
#                                "group": {
#                                    "address_group": "inbound"
#                                }
#                            },
#                            "number": 103,
#                            "source": {
#                                "address": "192.0.2.0"
#                            },
#                            "state": {
#                                "established": true,
#                                "invalid": false,
#                                "new": false,
#                                "related": true
#                            }
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
#
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall group address-group 'inbound'
# set firewall ipv6-name UPLINK default-action 'accept'
# set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'
# set firewall ipv6-name UPLINK rule 1 action 'accept'
# set firewall ipv6-name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 1 ipsec 'match-ipsec'
# set firewall ipv6-name UPLINK rule 2 action 'accept'
# set firewall ipv6-name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
# set firewall ipv6-name UPLINK rule 2 ipsec 'match-ipsec'
# set firewall name INBOUND default-action 'accept'
# set firewall name INBOUND description 'IPv4 INBOUND rule set'
# set firewall name INBOUND rule 101 action 'accept'
# set firewall name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
# set firewall name INBOUND rule 101 ipsec 'match-ipsec'
# set firewall name INBOUND rule 102 action 'reject'
# set firewall name INBOUND rule 102 description 'Rule 102 is configured by Ansible'
# set firewall name INBOUND rule 102 ipsec 'match-ipsec'
# set firewall name INBOUND rule 103 action 'accept'
# set firewall name INBOUND rule 103 description 'Rule 103 is configured by Ansible'
# set firewall name INBOUND rule 103 destination group address-group 'inbound'
# set firewall name INBOUND rule 103 source address '192.0.2.0'
# set firewall name INBOUND rule 103 state established 'enable'
# set firewall name INBOUND rule 103 state invalid 'disable'
# set firewall name INBOUND rule 103 state new 'disable'
# set firewall name INBOUND rule 103 state related 'enable'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_firewall_rules:
    config:
    - afi: ipv6
      rule_sets:
      - name: UPLINK
        description: This is ipv6 specific rule-set
        default_action: accept
    - afi: ipv4
      rule_sets:
      - name: INBOUND
        description: IPv4 INBOUND rule set
        default_action: accept
        rules:
        - number: 101
          action: accept
          description: Rule 101 is configured by Ansible
          ipsec: match-ipsec
        - number: 102
          action: reject
          description: Rule 102 is configured by Ansible
          ipsec: match-ipsec
        - number: 103
          action: accept
          description: Rule 103 is configured by Ansible
          destination:
            group:
              address_group: inbound
          source:
            address: 192.0.2.0
          state:
            established: true
            new: false
            invalid: false
            related: true
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        "set firewall ipv6-name UPLINK default-action 'accept'",
#        "set firewall ipv6-name UPLINK description 'This is ipv6 specific rule-set'",
#        "set firewall name INBOUND default-action 'accept'",
#        "set firewall name INBOUND description 'IPv4 INBOUND rule set'",
#        "set firewall name INBOUND rule 101 action 'accept'",
#        "set firewall name INBOUND rule 101",
#        "set firewall name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
#        "set firewall name INBOUND rule 101 ipsec 'match-ipsec'",
#        "set firewall name INBOUND rule 102 action 'reject'",
#        "set firewall name INBOUND rule 102",
#        "set firewall name INBOUND rule 102 description 'Rule 102 is configured by Ansible'",
#        "set firewall name INBOUND rule 102 ipsec 'match-ipsec'",
#        "set firewall name INBOUND rule 103 description 'Rule 103 is configured by Ansible'",
#        "set firewall name INBOUND rule 103 destination group address-group inbound",
#        "set firewall name INBOUND rule 103",
#        "set firewall name INBOUND rule 103 source address 192.0.2.0",
#        "set firewall name INBOUND rule 103 state established enable",
#        "set firewall name INBOUND rule 103 state related enable",
#        "set firewall name INBOUND rule 103 state invalid disable",
#        "set firewall name INBOUND rule 103 state new disable",
#        "set firewall name INBOUND rule 103 action 'accept'"
#    ]

# Using parsed
#
#
- name: Parsed the provided input commands.
  vyos.vyos.vyos_firewall_rules:
    running_config:
      "set firewall group address-group 'inbound'
       set firewall name Downlink default-action 'accept'
       set firewall name Downlink description 'IPv4 INBOUND rule set'
       set firewall name Downlink rule 501 action 'accept'
       set firewall name Downlink rule 501 description 'Rule 501 is configured by Ansible'
       set firewall name Downlink rule 501 ipsec 'match-ipsec'
       set firewall name Downlink rule 502 action 'reject'
       set firewall name Downlink rule 502 description 'Rule 502 is configured by Ansible'
       set firewall name Downlink rule 502 ipsec 'match-ipsec'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#        {
#            "afi": "ipv4",
#            "rule_sets": [
#                {
#                    "default_action": "accept",
#                    "description": "IPv4 INBOUND rule set",
#                    "name": "Downlink",
#                    "rules": [
#                        {
#                            "action": "accept",
#                            "description": "Rule 501 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 501
#                        },
#                        {
#                            "action": "reject",
#                            "description": "Rule 502 is configured by Ansible",
#                            "ipsec": "match-ipsec",
#                            "number": 502
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
```

## [Return Values](vyos_firewall_rules_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["set firewall name Downlink default-action 'accept'", "set firewall name Downlink description 'IPv4 INBOUND rule set'", "set firewall name Downlink rule 501 action 'accept'", "set firewall name Downlink rule 502 description 'Rule 502 is configured by Ansible'", "set firewall name Downlink rule 502 ipsec 'match-ipsec'"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
