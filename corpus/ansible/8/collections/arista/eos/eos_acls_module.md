---
collection: ansible
version: "8"
title: "arista.eos.eos_acls module – ACLs resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_acls_module.html
fetched_at: 2026-07-28T01:10:57+00:00
---
# arista.eos.eos_acls module – ACLs resource module

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
> To use it in a playbook, specify: `arista.eos.eos_acls`.

New in arista.eos 1.0.0

- [Synopsis](eos_acls_module.md#synopsis)
- [Parameters](eos_acls_module.md#parameters)
- [Notes](eos_acls_module.md#notes)
- [Examples](eos_acls_module.md#examples)
- [Return Values](eos_acls_module.md#return-values)

## [Synopsis](eos_acls_module.md#id1)

- This module manages the IP access-list attributes of Arista EOS interfaces.

Aliases: acls

## [Parameters](eos_acls_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of IP access-list options |
| **acls**  list / elements=dictionary | A list of Access Control Lists (ACL). |
| **aces**  list / elements=dictionary | Filtering data |
| **destination**  dictionary | The packet’s destination address |
| **address**  string | dotted decimal notation of IP address |
| **any**  boolean | Rule matches all source addresses  **Choices:**   - `false` - `true` |
| **host**  string | Host IP address |
| **port_protocol**  dictionary | Specify dest port/protocol, along with operator . (comes with tcp/udp). |
| **subnet_address**  string | A subnet address |
| **wildcard_bits**  string | Source wildcard bits |
| **fragment_rules**  boolean | Add fragment rules  **Choices:**   - `false` - `true` |
| **fragments**  boolean | Match non-head fragment packets  **Choices:**   - `false` - `true` |
| **grant**  string | Action to be applied on the rule  **Choices:**   - `"permit"` - `"deny"` |
| **hop_limit**  dictionary | Hop limit value. |
| **line**  aliases: ace  string | For fact gathering, any ACE that is not fully parsed, while show up as a value of this attribute. |
| **log**  boolean | Log matches against this rule  **Choices:**   - `false` - `true` |
| **protocol**  string | Specify the protocol to match.  Refer to vendor documentation for valid values. |
| **protocol_options**  dictionary | All the possible sub options for the protocol chosen. |
| **icmp**  dictionary | Internet Control Message Protocol settings. |
| **administratively_prohibited**  boolean | Administratively prohibited  **Choices:**   - `false` - `true` |
| **alternate_address**  boolean | Alternate address  **Choices:**   - `false` - `true` |
| **conversion_error**  boolean | Datagram conversion  **Choices:**   - `false` - `true` |
| **dod_host_prohibited**  boolean | Host prohibited  **Choices:**   - `false` - `true` |
| **dod_net_prohibited**  boolean | Net prohibited  **Choices:**   - `false` - `true` |
| **echo**  boolean | Echo (ping)  **Choices:**   - `false` - `true` |
| **echo_reply**  boolean | Echo reply  **Choices:**   - `false` - `true` |
| **general_parameter_problem**  boolean | Parameter problem  **Choices:**   - `false` - `true` |
| **host_isolated**  boolean | Host isolated  **Choices:**   - `false` - `true` |
| **host_precedence_unreachable**  boolean | Host unreachable for precedence  **Choices:**   - `false` - `true` |
| **host_redirect**  boolean | Host redirect  **Choices:**   - `false` - `true` |
| **host_tos_redirect**  boolean | Host redirect for TOS  **Choices:**   - `false` - `true` |
| **host_tos_unreachable**  boolean | Host unreachable for TOS  **Choices:**   - `false` - `true` |
| **host_unknown**  boolean | Host unknown  **Choices:**   - `false` - `true` |
| **host_unreachable**  boolean | Host unreachable  **Choices:**   - `false` - `true` |
| **information_reply**  boolean | Information replies  **Choices:**   - `false` - `true` |
| **information_request**  boolean | Information requests  **Choices:**   - `false` - `true` |
| **mask_reply**  boolean | Mask replies  **Choices:**   - `false` - `true` |
| **mask_request**  boolean | Mask requests  **Choices:**   - `false` - `true` |
| **message_code**  integer | ICMP message code |
| **message_num**  integer | icmp msg type number. |
| **message_type**  integer | ICMP message type |
| **mobile_redirect**  boolean | Mobile host redirect  **Choices:**   - `false` - `true` |
| **net_redirect**  boolean | Network redirect  **Choices:**   - `false` - `true` |
| **net_tos_redirect**  boolean | Net redirect for TOS  **Choices:**   - `false` - `true` |
| **net_tos_unreachable**  boolean | Network unreachable for TOS  **Choices:**   - `false` - `true` |
| **net_unreachable**  boolean | Net unreachable  **Choices:**   - `false` - `true` |
| **network_unknown**  boolean | Network unknown  **Choices:**   - `false` - `true` |
| **no_room_for_option**  boolean | Parameter required but no room  **Choices:**   - `false` - `true` |
| **option_missing**  boolean | Parameter required but not present  **Choices:**   - `false` - `true` |
| **packet_too_big**  boolean | Fragmentation needed and DF set  **Choices:**   - `false` - `true` |
| **parameter_problem**  boolean | All parameter problems  **Choices:**   - `false` - `true` |
| **port_unreachable**  boolean | Port unreachable  **Choices:**   - `false` - `true` |
| **precedence_unreachable**  boolean | Precedence cutoff  **Choices:**   - `false` - `true` |
| **protocol_unreachable**  boolean | Protocol unreachable  **Choices:**   - `false` - `true` |
| **reassembly_timeout**  boolean | Reassembly timeout  **Choices:**   - `false` - `true` |
| **redirect**  boolean | All redirects  **Choices:**   - `false` - `true` |
| **router_advertisement**  boolean | Router discovery advertisements  **Choices:**   - `false` - `true` |
| **router_solicitation**  boolean | Router discovery solicitations  **Choices:**   - `false` - `true` |
| **source_quench**  boolean | Source quenches  **Choices:**   - `false` - `true` |
| **source_route_failed**  boolean | Source route failed  **Choices:**   - `false` - `true` |
| **time_exceeded**  boolean | All time exceededs  **Choices:**   - `false` - `true` |
| **timestamp_reply**  boolean | Timestamp replies  **Choices:**   - `false` - `true` |
| **timestamp_request**  boolean | Timestamp requests  **Choices:**   - `false` - `true` |
| **traceroute**  boolean | Traceroute  **Choices:**   - `false` - `true` |
| **ttl_exceeded**  boolean | TTL exceeded  **Choices:**   - `false` - `true` |
| **unreachable**  boolean | All unreachables  **Choices:**   - `false` - `true` |
| **icmpv6**  dictionary | Options for icmpv6. |
| **address_unreachable**  boolean | address unreachable  **Choices:**   - `false` - `true` |
| **beyond_scope**  boolean | beyond_scope  **Choices:**   - `false` - `true` |
| **echo_reply**  boolean | echo_reply  **Choices:**   - `false` - `true` |
| **echo_request**  boolean | echo reques  **Choices:**   - `false` - `true` |
| **erroneous_header**  boolean | erroneous header  **Choices:**   - `false` - `true` |
| **fragment_reassembly_exceeded**  boolean | fragment_reassembly_exceeded  **Choices:**   - `false` - `true` |
| **hop_limit_exceeded**  boolean | hop limit exceeded  **Choices:**   - `false` - `true` |
| **neighbor_advertisement**  boolean | neighbor advertisement  **Choices:**   - `false` - `true` |
| **neighbor_solicitation**  boolean | neighbor_solicitation  **Choices:**   - `false` - `true` |
| **no_admin**  boolean | no admin  **Choices:**   - `false` - `true` |
| **no_route**  boolean | no route  **Choices:**   - `false` - `true` |
| **packet_too_big**  boolean | packet too big  **Choices:**   - `false` - `true` |
| **parameter_problem**  boolean | parameter problem  **Choices:**   - `false` - `true` |
| **port_unreachable**  boolean | port unreachable  **Choices:**   - `false` - `true` |
| **redirect_message**  boolean | redirect message  **Choices:**   - `false` - `true` |
| **reject_route**  boolean | reject route  **Choices:**   - `false` - `true` |
| **router_advertisement**  boolean | router_advertisement  **Choices:**   - `false` - `true` |
| **router_solicitation**  boolean | router_solicitation  **Choices:**   - `false` - `true` |
| **source_address_failed**  boolean | source_address_failed  **Choices:**   - `false` - `true` |
| **source_routing_error**  boolean | source_routing_error  **Choices:**   - `false` - `true` |
| **time_exceeded**  boolean | time_exceeded  **Choices:**   - `false` - `true` |
| **unreachable**  boolean | unreachable  **Choices:**   - `false` - `true` |
| **unrecognized_ipv6_option**  boolean | unrecognized_ipv6_option  **Choices:**   - `false` - `true` |
| **unrecognized_next_header**  boolean | unrecognized_next_header  **Choices:**   - `false` - `true` |
| **ip**  dictionary | Internet Protocol. |
| **nexthop_group**  string | Nexthop-group name. |
| **ipv6**  dictionary | Internet V6 Protocol. |
| **nexthop_group**  string | Nexthop-group name. |
| **tcp**  dictionary | Options for tcp protocol. |
| **flags**  dictionary | Match TCP packet flags |
| **ack**  boolean | Match on the ACK bit  **Choices:**   - `false` - `true` |
| **established**  boolean | Match established connections  **Choices:**   - `false` - `true` |
| **fin**  boolean | Match on the FIN bit  **Choices:**   - `false` - `true` |
| **psh**  boolean | Match on the PSH bit  **Choices:**   - `false` - `true` |
| **rst**  boolean | Match on the RST bit  **Choices:**   - `false` - `true` |
| **syn**  boolean | Match on the SYN bit  **Choices:**   - `false` - `true` |
| **urg**  boolean | Match on the URG bit  **Choices:**   - `false` - `true` |
| **remark**  string | Specify a comment |
| **sequence**  integer | sequence number for the ordered list of rules |
| **source**  dictionary | The packet’s source address |
| **address**  string | dotted decimal notation of IP address |
| **any**  boolean | Rule matches all source addresses  **Choices:**   - `false` - `true` |
| **host**  string | Host IP address |
| **port_protocol**  dictionary | Specify source port/protocoli, along with operator. (comes with tcp/udp). |
| **subnet_address**  string | A subnet address |
| **wildcard_bits**  string | Source wildcard bits |
| **tracked**  boolean | Match packets in existing ICMP/UDP/TCP connections  **Choices:**   - `false` - `true` |
| **ttl**  dictionary | Compares the TTL (time-to-live) value in the packet to a specified value |
| **eq**  integer | Match a single TTL value |
| **gt**  integer | Match TTL greater than this number |
| **lt**  integer | Match TTL lesser than this number |
| **neq**  integer | Match TTL not equal to this value |
| **vlan**  string | Vlan options |
| **name**  string / required | Name of the acl-list |
| **standard**  boolean | standard access-list or not  **Choices:**   - `false` - `true` |
| **afi**  string / required | The Address Family Indicator (AFI) for the Access Control Lists (ACL).  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section access-list**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_acls_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F

## [Examples](eos_acls_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# show running-config | section access-list
# ip access-list test1
#    10 permit ip 10.10.10.0/24 any ttl eq 200
#    20 permit ip 10.30.10.0/24 host 10.20.10.1
#    30 deny tcp host 10.10.20.1 eq finger www any syn log
#    40 permit ip any any
# ipv6 access-list test2
#     10 deny icmpv6 any any reject-route hop-limit eq 20

- name: Merge provided configuration with device configuration
  arista.eos.eos_acls:
    config:
      - afi: ipv4
        acls:
          - name: test1
            aces:
              - sequence: 35
                grant: deny
                protocol: ospf
                source:
                  subnet_address: 20.0.0.0/8
                destination:
                  any: true
    state: merged

# After state:
# ------------
#
# show running-config | section access-list
# ip access-list test1
#    10 permit ip 10.10.10.0/24 any ttl eq 200
#    20 permit ip 10.30.10.0/24 host 10.20.10.1
#    30 deny tcp host 10.10.20.1 eq finger www any syn log
#    35 deny ospf 20.0.0.0/8 any
#    40 permit ip any any
# ipv6 access-list test2
#     10 deny icmpv6 any any reject-route hop-limit eq 20

# Using merged

# Before state:
# -------------
# show running-config | section access-list
# ip access-list test1
#    10 permit ip 10.10.10.0/24 any ttl eq 200
#    20 permit ip 10.30.10.0/24 host 10.20.10.1
#    30 deny tcp host 10.10.20.1 eq finger www any syn log
#    40 permit ip any any
# ipv6 access-list test2
#     10 deny icmpv6 any any reject-route hop-limit eq 20

- name: Merge to update the given configuration with an existing ace
  arista.eos.eos_acls:
    config:
      - afi: ipv4
        acls:
          - name: test1
            aces:
              - sequence: 35
                log: true
                ttl:
                  eq: 33
    state: merged

# After state:
# ------------
#
# show running-config | section access-list
# ip access-list test1
#    10 permit ip 10.10.10.0/24 any ttl eq 200
#    20 permit ip 10.30.10.0/24 host 10.20.10.1
#    30 deny tcp host 10.10.20.1 eq finger www any syn log
#    35 deny ospf 20.0.0.0/8 any ttl eq 33 log
#    40 permit ip any any
# ipv6 access-list test2
#     10 deny icmpv6 any any reject-route hop-limit eq 20

# Using replaced

# Before state:
# -------------
# show running-config | section access-list
# ip access-list test1
#    10 permit ip 10.10.10.0/24 any ttl eq 200
#    20 permit ip 10.30.10.0/24 host 10.20.10.1
#    30 deny tcp host 10.10.20.1 eq finger www any syn log
#    40 permit ip any any
# !
# ip access-list test3
#    10 permit ip 35.33.0.0/16 any log
# !
# ipv6 access-list test2
#     10 deny icmpv6 any any reject-route hop-limit eq 20

- name: Replace device configuration with provided configuration
  arista.eos.eos_acls:
    config:
      - afi: ipv4
        acls:
          - name: test1
            aces:
              - sequence: 35
                grant: permit
                protocol: ospf
                source:
                  subnet_address: 20.0.0.0/8
                destination:
                  any: true
    state: replaced

# After state:
# ------------
#
# show running-config | section access-list
# ip access-list test1
#    35 permit ospf 20.0.0.0/8 any
# !
# ip access-list test3
#    10 permit ip 35.33.0.0/16 any log
# !
# ipv6 access-list test2
#     10 deny icmpv6 any any reject-route hop-limit eq 20

# Using overridden

# Before state:
# -------------
# show running-config | section access-list
# ip access-list test1
#    10 permit ip 10.10.10.0/24 any ttl eq 200
#    20 permit ip 10.30.10.0/24 host 10.20.10.1
#    30 deny tcp host 10.10.20.1 eq finger www any syn log
#    40 permit ip any any
# !
# ip access-list test3
#    10 permit ip 35.33.0.0/16 any log
# !
# ipv6 access-list test2
#     10 deny icmpv6 any any reject-route hop-limit eq 20

- name: override device configuration with  provided configuration
  arista.eos.eos_acls:
    config:
      - afi: ipv4
        acls:
          - name: test1
            aces:
              - sequence: 35
                grant: permit
                protocol: ospf
                source:
                  subnet_address: 20.0.0.0/8
                destination:
                  any: true
    state: overridden

# After state:
# ------------
#
# show running-config | section access-list
# ip access-list test1
#    35 permit ospf 20.0.0.0/8 any
# !

# Using deleted:

# Before state:
# -------------
# show running-config | section access-list
# ip access-list test1
#    10 permit ip 10.10.10.0/24 any ttl eq 200
#    20 permit ip 10.30.10.0/24 host 10.20.10.1
#    30 deny tcp host 10.10.20.1 eq finger www any syn log
#    40 permit ip any any
# ipv6 access-list test2
#     10 deny icmpv6 any any reject-route hop-limit eq 20

# !

- name: Delete provided configuration
  arista.eos.eos_acls:
    config:
      - afi: ipv4
        acls:
          - name: test1
    state: deleted

# After state:
# ------------
#
# show running-config | section access-list

# ipv6 access-list test2
#     10 deny icmpv6 any any reject-route hop-limit eq 20

# using gathered

# ip access-list test1
#    35 deny ospf 20.0.0.0/8 any
# ip access-list test2
#    40 permit vlan 55 0xE2 icmpv6 any any log

- name: Gather the existing configuration
  arista.eos.eos_acls:
    state: gathered

# returns:

#  arista.eos.eos_acls:
#    config:
#      - afi: "ipv4"
#        acls:
#          - name: test1
#            aces:
#            - sequence: 35
#              grant: "deny"
#              protocol: "ospf"
#              source:
#                subnet_address: 20.0.0.0/8
#              destination:
#                any: true
#      - afi: "ipv6"
#         acls:
#           - name: test2
#             aces:
#               - sequence: 40
#                 grant: "permit"
#                 vlan: "55 0xE2"
#                 protocol: "icmpv6"
#                 log: true
#                 source:
#                   any: true
#                 destination:
#                   any: true

# using rendered

- name: Delete provided configuration
  arista.eos.eos_acls:
    config:
      - afi: ipv4
        acls:
          - name: test1
            aces:
              - sequence: 35
                grant: deny
                protocol: ospf
                source:
                  subnet_address: 20.0.0.0/8
                destination:
                  any: true
      - afi: ipv6
        acls:
          - name: test2
            aces:
              - sequence: 40
                grant: permit
                vlan: 55 0xE2
                protocol: icmpv6
                log: true
                source:
                  any: true
                destination:
                  any: true
    state: rendered

# returns:

# ip access-list test1
#    35 deny ospf 20.0.0.0/8 any
# ip access-list test2
#    40 permit vlan 55 0xE2 icmpv6 any any log

# Using Parsed

# parsed_acls.cfg

# ipv6 access-list standard test2
#    10 permit any log
# !
# ip access-list test1
#    35 deny ospf 20.0.0.0/8 any
#    45 remark Run by ansible
#    55 permit tcp any any
# !

- name: parse configs
  arista.eos.eos_acls:
    running_config: "{{ lookup('file', './parsed_acls.cfg') }}"
    state: parsed

# returns
# "parsed": [
#         {
#             "acls": [
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "any": true
#                             },
#                             "grant": "deny",
#                             "protocol": "ospf",
#                             "sequence": 35,
#                             "source": {
#                                 "subnet_address": "20.0.0.0/8"
#                             }
#                         },
#                         {
#                             "remark": "Run by ansible",
#                             "sequence": 45
#                         },
#                         {
#                             "destination": {
#                                 "any": true
#                             },
#                             "grant": "permit",
#                             "protocol": "tcp",
#                             "sequence": 55,
#                             "source": {
#                                 "any": true
#                             }
#                         }
#                     ],
#                     "name": "test1"
#                 }
#             ],
#             "afi": "ipv4"
#         },
#         {
#             "acls": [
#                 {
#                     "aces": [
#                         {
#                             "grant": "permit",
#                             "log": true,
#                             "sequence": 10,
#                             "source": {
#                                 "any": true
#                             }
#                         }
#                     ],
#                     "name": "test2",
#                     "standard": true
#                 }
#             ],
#             "afi": "ipv6"
#         }
#     ]
```

## [Return Values](eos_acls_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["ipv6 access-list standard test2", "10 permit any log", "ip access-list test1", "35 deny ospf 20.0.0.0/8 any", "45 remark Run by ansible", "55 permit tcp any any"]` |

### Authors

- Gomathiselvi S (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
