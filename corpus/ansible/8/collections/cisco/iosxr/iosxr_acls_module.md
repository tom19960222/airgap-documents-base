---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_acls module – Resource module to configure ACLs."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_acls_module.html
fetched_at: 2026-07-28T01:26:34+00:00
---
# cisco.iosxr.iosxr_acls module – Resource module to configure ACLs.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_acls`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_acls_module.md#synopsis)
- [Parameters](iosxr_acls_module.md#parameters)
- [Examples](iosxr_acls_module.md#examples)
- [Return Values](iosxr_acls_module.md#return-values)

## [Synopsis](iosxr_acls_module.md#id1)

- This module manages Access Control Lists (ACLs) on devices running IOS-XR.

Aliases: acls

## [Parameters](iosxr_acls_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of dictionaries specifying ACL configurations. |
| **acls**  list / elements=dictionary | A list of Access Control Lists (ACLs). |
| **aces**  list / elements=dictionary | List of Access Control Entries (ACEs) for this Access Control List (ACL). |
| **authen**  boolean | Match if authentication header is present.  **Choices:**   - `false` - `true` |
| **capture**  boolean | Capture matched packet.  **Choices:**   - `false` - `true` |
| **destination**  dictionary | Specifies the packet destination. |
| **address**  string | The destination IP address to match. |
| **any**  boolean | Match any destination address.  **Choices:**   - `false` - `true` |
| **host**  string | The host IP address to match. |
| **net_group**  string | Name of net-group. |
| **port_group**  string | Name of port-group. |
| **port_protocol**  dictionary | Specify the source port or protocol. |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Match only packets in the range of port numbers |
| **end**  string | Specify the end of the port range |
| **start**  string | Specify the start of the port range |
| **prefix**  string | Destination network prefix. |
| **wildcard_bits**  string | The Wildcard bits to apply to destination address. |
| **destopts**  boolean | Match if destination opts header is present.  **Choices:**   - `false` - `true` |
| **dscp**  dictionary | Match packets with given DSCP value. |
| **eq**  string | Match only packets on a given dscp value |
| **gt**  string | Match only packets with a greater dscp value |
| **lt**  string | Match only packets with a lower dscp value |
| **neq**  string | Match only packets not on a given dscp value |
| **range**  dictionary | Match only packets in the range of dscp values |
| **end**  string | End of the dscp range |
| **start**  string | Start of the dscp range |
| **fragments**  boolean | Check non-intial fragments.  **Choices:**   - `false` - `true` |
| **grant**  string | Forward or drop packets matching the Access Control Entry (ACE).  **Choices:**   - `"permit"` - `"deny"` |
| **hop_by_hop**  boolean | Match if hop-by-hop opts header is present.  **Choices:**   - `false` - `true` |
| **icmp_off**  boolean | Enable/disable the ICMP message for this entry.  **Choices:**   - `false` - `true` |
| **line**  aliases: ace  string | An ACE excluding the sequence number.  This key is mutually exclusive with all the other attributes except ‘sequence’.  When used with other attributes, the value of this key will get precedence and the other keys will be ignored.  This should only be used when an attribute doesn’t exist in the argspec but is valid for the device.  For fact gathering, any ACE that is not fully parsed, will show up as a value of this attribute, excluding the sequence number, which will be populated as value of the sequence key. |
| **log**  boolean | Enable/disable log matches against this entry.  **Choices:**   - `false` - `true` |
| **log_input**  boolean | Enable/disable log matches against this entry, including input interface.  **Choices:**   - `false` - `true` |
| **packet_length**  dictionary | Match packets given packet length. |
| **eq**  integer | Match only packets on a given packet length |
| **gt**  integer | Match only packets with a greater packet length |
| **lt**  integer | Match only packets with a lower packet length |
| **neq**  integer | Match only packets not on a given packet length |
| **range**  dictionary | Match only packets in the range of packet lengths |
| **end**  integer | End of the packet length range |
| **start**  integer | Start of the packet length range |
| **precedence**  string | Match packets with given precedence value |
| **protocol**  string | Specify the protocol to match.  Refer to vendor documentation for valid values. |
| **protocol_options**  dictionary | Additional suboptions for the protocol. |
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
| **icmpv6**  dictionary | Internet Control Message Protocol settings for IPv6. |
| **address_unreachable**  boolean | Address Unreachable  **Choices:**   - `false` - `true` |
| **administratively_prohibited**  boolean | Administratively Prohibited  **Choices:**   - `false` - `true` |
| **beyond_scope_of_source_address**  boolean | Administratively Prohibited  **Choices:**   - `false` - `true` |
| **destination_unreachable**  boolean | Destination Unreachable  **Choices:**   - `false` - `true` |
| **echo**  boolean | Echo  **Choices:**   - `false` - `true` |
| **echo_reply**  boolean | Echo Reply  **Choices:**   - `false` - `true` |
| **erroneous_header_field**  boolean | Erroneous Header Field  **Choices:**   - `false` - `true` |
| **group_membership_query**  boolean | Group Membership Query  **Choices:**   - `false` - `true` |
| **group_membership_report**  boolean | Group Membership Report  **Choices:**   - `false` - `true` |
| **group_membership_termination**  boolean | Group Membership Termination  **Choices:**   - `false` - `true` |
| **host_unreachable**  boolean | Host Unreachable  **Choices:**   - `false` - `true` |
| **nd_na**  boolean | Neighbor Discovery - Neighbor Advertisement  **Choices:**   - `false` - `true` |
| **nd_ns**  boolean | Neighbor Discovery - Neighbor Solicitation  **Choices:**   - `false` - `true` |
| **neighbor_redirect**  boolean | Neighbor Redirect  **Choices:**   - `false` - `true` |
| **no_route_to_destination**  boolean | No Route To Destination  **Choices:**   - `false` - `true` |
| **node_information_request_is_refused**  boolean | Node Information Request Is Refused  **Choices:**   - `false` - `true` |
| **node_information_successful_reply**  boolean | Node Information Successful Reply  **Choices:**   - `false` - `true` |
| **packet_too_big**  boolean | Packet Too Big  **Choices:**   - `false` - `true` |
| **parameter_problem**  boolean | Parameter Problem  **Choices:**   - `false` - `true` |
| **port_unreachable**  boolean | Port Unreachable  **Choices:**   - `false` - `true` |
| **query_subject_is_domainname**  boolean | Query Subject Is Domain name  **Choices:**   - `false` - `true` |
| **query_subject_is_IPv4address**  boolean | Query Subject Is IPv4 address  **Choices:**   - `false` - `true` |
| **query_subject_is_IPv6address**  boolean | Query Subject Is IPv6 address  **Choices:**   - `false` - `true` |
| **reassembly_timeout**  boolean | Reassembly Timeout  **Choices:**   - `false` - `true` |
| **redirect**  boolean | Redirect  **Choices:**   - `false` - `true` |
| **router_advertisement**  boolean | Router Advertisement  **Choices:**   - `false` - `true` |
| **router_renumbering**  boolean | Router Renumbering  **Choices:**   - `false` - `true` |
| **router_solicitation**  boolean | Router Solicitation  **Choices:**   - `false` - `true` |
| **rr_command**  boolean | RR Command  **Choices:**   - `false` - `true` |
| **rr_result**  boolean | RR Result  **Choices:**   - `false` - `true` |
| **rr_seqnum_reset**  boolean | RR Seqnum Reset  **Choices:**   - `false` - `true` |
| **time_exceeded**  boolean | Time Exceeded  **Choices:**   - `false` - `true` |
| **ttl_exceeded**  boolean | TTL Exceeded  **Choices:**   - `false` - `true` |
| **unknown_query_type**  boolean | Unknown Query Type  **Choices:**   - `false` - `true` |
| **unreachable**  boolean | Unreachable  **Choices:**   - `false` - `true` |
| **unrecognized_next_header**  boolean | Unrecognized Next Header  **Choices:**   - `false` - `true` |
| **unrecognized_option**  boolean | Unrecognized Option  **Choices:**   - `false` - `true` |
| **whoareyou_reply**  boolean | Whoareyou Reply  **Choices:**   - `false` - `true` |
| **whoareyou_request**  boolean | Whoareyou Request  **Choices:**   - `false` - `true` |
| **igmp**  dictionary | Internet Group Management Protocol (IGMP) settings. |
| **dvmrp**  boolean | Match Distance Vector Multicast Routing Protocol  **Choices:**   - `false` - `true` |
| **host_query**  boolean | Match Host Query  **Choices:**   - `false` - `true` |
| **host_report**  boolean | Match Host Report  **Choices:**   - `false` - `true` |
| **mtrace**  boolean | Match mtrace  **Choices:**   - `false` - `true` |
| **mtrace_response**  boolean | Match mtrace response  **Choices:**   - `false` - `true` |
| **pim**  boolean | Match Protocol Independent Multicast  **Choices:**   - `false` - `true` |
| **trace**  boolean | Multicast trace  **Choices:**   - `false` - `true` |
| **tcp**  dictionary | Match TCP packet flags |
| **ack**  boolean | Match on the ACK bit  **Choices:**   - `false` - `true` |
| **established**  boolean | Match established connections  **Choices:**   - `false` - `true` |
| **fin**  boolean | Match on the FIN bit  **Choices:**   - `false` - `true` |
| **psh**  boolean | Match on the PSH bit  **Choices:**   - `false` - `true` |
| **rst**  boolean | Match on the RST bit  **Choices:**   - `false` - `true` |
| **syn**  boolean | Match on the SYN bit  **Choices:**   - `false` - `true` |
| **urg**  boolean | Match on the URG bit  **Choices:**   - `false` - `true` |
| **remark**  string | Comments or a description for the access list. |
| **routing**  boolean | Match if routing header is present.  **Choices:**   - `false` - `true` |
| **sequence**  integer | Sequence number for the Access Control Entry (ACE). |
| **source**  dictionary | Specifies the packet source. |
| **address**  string | The source IP address to match. |
| **any**  boolean | Match any source address.  **Choices:**   - `false` - `true` |
| **host**  string | The host IP address to match. |
| **net_group**  string | Name of net-group. |
| **port_group**  string | Name of port-group. |
| **port_protocol**  dictionary | Specify the source port or protocol. |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Match only packets in the range of port numbers |
| **end**  string | Specify the end of the port range |
| **start**  string | Specify the start of the port range |
| **prefix**  string | Source network prefix. |
| **wildcard_bits**  string | The Wildcard bits to apply to source address. |
| **ttl**  dictionary | Match against specified TTL value. |
| **eq**  integer | Match only packets with exact TTL value. |
| **gt**  integer | Match only packets with a greater TTL value. |
| **lt**  integer | Match only packets with a lower TTL value. |
| **neq**  integer | Match only packets that won’t have the given TTL value. |
| **range**  dictionary | Match only packets in the range of given TTL values. |
| **end**  integer | End of the TTL range. |
| **start**  integer | Start of the TTL range. |
| **name**  string | The name of the Access Control List (ACL). |
| **afi**  string / required | The Address Family Indicator (AFI) for the Access Control Lists (ACL).  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command **show running-config router static**. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Examples](iosxr_acls_module.md#id3)

```yaml+jinja
# Using merged to add new ACLs

# Before state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:07:45.767 UTC
# RP/0/RP0/CPU0:ios#

- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_acls:
    config:
    - afi: ipv6
      acls:
      - name: acl6_1
        aces:
        - sequence: 10
          grant: deny
          protocol: tcp
          source:
            prefix: 2001:db8:1234::/48
            port_protocol:
              range:
                start: ftp
                end: telnet
          destination:
            any: true
          protocol_options:
            tcp:
              syn: true
          ttl:
            range:
              start: 180
              end: 250
          routing: true
          authen: true
          log: true

        - sequence: 20
          grant: permit
          protocol: icmpv6
          source:
            any: true
          destination:
            any: true
          protocol_options:
            icmpv6:
              router_advertisement: true
          precedence: network
          destopts: true

    - afi: ipv4
      acls:
      - name: acl_1
        aces:
        - sequence: 16
          remark: TEST_ACL_1_REMARK

        - sequence: 21
          grant: permit
          protocol: tcp
          source:
            host: 192.0.2.10
            port_protocol:
              range:
                start: pop3
                end: 121
          destination:
            address: 198.51.100.0
            wildcard_bits: 0.0.0.15
          protocol_options:
            tcp:
              rst: true

        - sequence: 23
          grant: deny
          protocol: icmp
          source:
            any: true
          destination:
            prefix: 198.51.100.0/28
          protocol_options:
            icmp:
              reassembly_timeout: true
          dscp:
            lt: af12

      - name: acl_2
        aces:
        - sequence: 10
          remark: TEST_ACL_2_REMARK
    state: merged

# After state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:22:57.021 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp host 192.0.2.10 range pop3 121 198.51.100.0 0.0.0.15 rst
#  23 deny icmp any 198.51.100.0 0.0.0.15 reassembly-timeout dscp lt af12
# ipv4 access-list acl_2
#  10 remark TEST_ACL_2_REMARK
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

# Using merged to update existing ACLs

# Before state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:22:57.021 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp host 192.0.2.10 range pop3 121 198.51.100.0 0.0.0.15 rst
#  23 deny icmp any 198.51.100.0 0.0.0.15 reassembly-timeout dscp lt af12
# ipv4 access-list acl_2
#  10 remark TEST_ACL_2_REMARK
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

- name: Update existing ACEs
  cisco.iosxr.iosxr_acls:
    config:
    - afi: ipv4
      acls:
      - name: acl_1
        aces:
        - sequence: 21
          source:
            prefix: 198.51.100.32/28
            port_protocol:
              range:
                start: pop3
                end: 121
          protocol_options:
            tcp:
              syn: true

        - sequence: 23
          protocol_options:
            icmp:
              router_advertisement: true
          dscp:
            eq: af23

# After state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:47:18.711 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp 198.51.100.32 0.0.0.15 range pop3 121 198.51.100.0 0.0.0.15 syn
#  23 deny icmp any 198.51.100.0 0.0.0.15 router-advertisement dscp eq af23
# ipv4 access-list acl_2
#  10 remark TEST_ACL_2_REMARK
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

# Using replaced to replace a whole ACL

# Before state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:22:57.021 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp host 192.0.2.10 range pop3 121 198.51.100.0 0.0.0.15 rst
#  23 deny icmp any 198.51.100.0 0.0.0.15 reassembly-timeout dscp lt af12
# ipv4 access-list acl_2
#  10 remark TEST_ACL_2_REMARK
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

- name: Replace device configurations of listed ACL with provided configurations
  cisco.iosxr.iosxr_acls:
    config:
    - afi: ipv4
      acls:
      - name: acl_2
        aces:
        - sequence: 11
          grant: permit
          protocol: igmp
          source:
            host: 198.51.100.130
          destination:
            any: true
          ttl:
            eq: 100

        - sequence: 12
          grant: deny
          source:
            any: true
          destination:
            any: true
          protocol: icmp
    state: replaced

# After state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 06:19:51.496 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp 198.51.100.32 0.0.0.15 range pop3 121 198.51.100.0 0.0.0.15 syn
#  23 deny icmp any 198.51.100.0 0.0.0.15 router-advertisement dscp eq af23
# ipv4 access-list acl_2
#  11 permit igmp host 198.51.100.130 any ttl eq 100
#  12 deny icmp any any
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

# Using overridden to override all ACLs in the device

# Before state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:22:57.021 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp host 192.0.2.10 range pop3 121 198.51.100.0 0.0.0.15 rst
#  23 deny icmp any 198.51.100.0 0.0.0.15 reassembly-timeout dscp lt af12
# ipv4 access-list acl_2
#  10 remark TEST_ACL_2_REMARK
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

- name: Overridde all ACLs configuration with provided configuration
  cisco.iosxr.iosxr_acls:
    config:
    - afi: ipv4
      acls:
      - name: acl_1
        aces:
        - sequence: 10
          grant: permit
          source:
            any: true
          destination:
            any: true
          protocol: tcp

      - name: acl_2
        aces:
        - sequence: 20
          grant: permit
          source:
            any: true
          destination:
            any: true
          protocol: igmp
    state: overridden

# After state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 06:31:22.178 UTC
# ipv4 access-list acl_1
#  10 permit tcp any any
# ipv4 access-list acl_2
#  20 permit igmp any any

# Using deleted to delete an entire ACL

# Before state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:22:57.021 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp host 192.0.2.10 range pop3 121 198.51.100.0 0.0.0.15 rst
#  23 deny icmp any 198.51.100.0 0.0.0.15 reassembly-timeout dscp lt af12
# ipv4 access-list acl_2
#  10 remark TEST_ACL_2_REMARK
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

- name: Delete a single ACL
  cisco.iosxr.iosxr_acls:
    config:
    - afi: ipv6
      acls:
      - name: acl6_1
    state: deleted

# After state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:22:57.021 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp host 192.0.2.10 range pop3 121 198.51.100.0 0.0.0.15 rst
#  23 deny icmp any 198.51.100.0 0.0.0.15 reassembly-timeout dscp lt af12
# ipv4 access-list acl_2
#  10 remark TEST_ACL_2_REMARK

# Using deleted to delete all ACLs under one AFI

# Before state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:22:57.021 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp host 192.0.2.10 range pop3 121 198.51.100.0 0.0.0.15 rst
#  23 deny icmp any 198.51.100.0 0.0.0.15 reassembly-timeout dscp lt af12
# ipv4 access-list acl_2
#  10 remark TEST_ACL_2_REMARK
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

- name: Delete all ACLs under one AFI
  cisco.iosxr.iosxr_acls:
    config:
    - afi: ipv4
    state: deleted

# After state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:22:57.021 UTC
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

# Using deleted to delete all ACLs from the device

# Before state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:22:57.021 UTC
# ipv4 access-list acl_1
#  16 remark TEST_ACL_1_REMARK
#  21 permit tcp host 192.0.2.10 range pop3 121 198.51.100.0 0.0.0.15 rst
#  23 deny icmp any 198.51.100.0 0.0.0.15 reassembly-timeout dscp lt af12
# ipv4 access-list acl_2
#  10 remark TEST_ACL_2_REMARK
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network destopts

- name: Delete all ACLs from the device
  cisco.iosxr.iosxr_acls:
    state: deleted

# After state:
# -------------

# RP/0/RP0/CPU0:ios#sh access-lists afi-all
# Thu Feb 20 05:07:45.767 UTC
# RP/0/RP0/CPU0:ios#

# Using gathered to gather ACL facts from the device

- name: Gather ACL interfaces facts using gathered state
  cisco.iosxr.iosxr_acls:
    state: gathered

# Task Output (redacted)
# -----------------------
#

# "gathered": [
#    {
#        "acls": [
#            {
#                "aces": [
#                    {
#                        "remark": "TEST_ACL_1_REMARK",
#                        "sequence": 16
#                    },
#                    {
#                        "destination": {
#                            "address": "198.51.100.0",
#                            "wildcard_bits": "0.0.0.15"
#                        },
#                        "grant": "permit",
#                        "protocol": "tcp",
#                        "protocol_options": {
#                            "tcp": {
#                                "rst": true
#                            }
#                        },
#                        "sequence": 21,
#                        "source": {
#                            "host": "192.0.2.10",
#                            "port_protocol": {
#                                "range": {
#                                    "end": "121",
#                                    "start": "pop3"
#                                }
#                            }
#                        }
#                    },
#                    {
#                        "destination": {
#                            "address": "198.51.100.0",
#                            "wildcard_bits": "0.0.0.15"
#                        },
#                        "dscp": {
#                            "lt": "af12"
#                        },
#                        "grant": "deny",
#                        "protocol": "icmp",
#                        "protocol_options": {
#                            "icmp": {
#                                "reassembly_timeout": true
#                            }
#                        },
#                        "sequence": 23,
#                        "source": {
#                            "any": true
#                        }
#                    }
#                ],
#                "name": "acl_1"
#            },
#            {
#                "aces": [
#                    {
#                        "remark": "TEST_ACL_2_REMARK",
#                        "sequence": 10
#                    }
#                ],
#                "name": "acl_2"
#            }
#        ],
#        "afi": "ipv4"
#    },
#    {
#        "acls": [
#            {
#                "aces": [
#                    {
#                        "authen": true,
#                        "destination": {
#                            "any": true
#                        },
#                        "grant": "deny",
#                        "log": true,
#                        "protocol": "tcp",
#                        "protocol_options": {
#                            "tcp": {
#                                "syn": true
#                            }
#                        },
#                        "routing": true,
#                        "sequence": 10,
#                        "source": {
#                            "port_protocol": {
#                                "range": {
#                                   "end": "telnet",
#                                   "start": "ftp"
#                                }
#                            },
#                            "prefix": "2001:db8:1234::/48"
#                        },
#                        "ttl": {
#                            "range": {
#                                "end": 250,
#                                "start": 180
#                            }
#                        }
#                    },
#                    {
#                        "destination": {
#                            "any": true
#                        },
#                        "destopts": true,
#                        "grant": "permit",
#                        "precedence": "network",
#                        "protocol": "icmpv6",
#                        "protocol_options": {
#                            "icmpv6": {
#                                "router_advertisement": true
#                            }
#                        },
#                        "sequence": 20,
#                        "source": {
#                            "any": true
#                        }
#                    }
#                ],
#                "name": "acl6_1"
#            }
#        ],
#        "afi": "ipv6"
#    }
#  ]

# Using rendered

- name: Render platform specific commands (without connecting to the device)
  cisco.iosxr.iosxr_acls:
    config:
    - afi: ipv4
      acls:
      - name: acl_2
        aces:
        - sequence: 11
          grant: permit
          protocol: igmp
          source:
            host: 198.51.100.130
          destination:
            any: true
          ttl:
            eq: 100

        - sequence: 12
          grant: deny
          source:
            any: true
          destination:
            any: true
          protocol: icmp
    state: rendered

# Task Output (redacted)
# -----------------------

# "rendered": [
#    "ipv4 access-list acl_2",
#    "11 permit igmp host 198.51.100.130 any ttl eq 100",
#    "12 deny icmp any any"

# Using parsed

# parsed.cfg
# ------------
#
# ipv4 access-list acl_1
#  10 remark TEST_ACL_2_REMARK
# ipv4 access-list acl_2
#  11 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 authen routing log
#  21 permit icmpv6 any any router-advertisement precedence network packet-length eq 576 destopts
# ipv6 access-list acl6_1
#  10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 routing authen log
#  20 permit icmpv6 any any router-advertisement precedence network packet-length eq 576 destopts

- name: Parse externally provided ACL config to agnostic model
  cisco.iosxr.iosxr_acls:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task Output (redacted)
# -----------------------
#  "parsed": [
#        {
#            "acls": [
#                {
#                    "aces": [
#                      {
#                            "remark": "TEST_ACL_2_REMARK",
#                            "sequence": 10
#                        }
#                    ],
#                   "name": "acl_1"
#                },
#                {
#                    "aces": [
#                        {
#                            "authen": true,
#                            "destination": {
#                                "any": true
#                            },
#                            "grant": "deny",
#                            "log": true,
#                            "protocol": "tcp",
#                            "protocol_options": {
#                                "tcp": {
#                                    "syn": true
#                                }
#                            },
#                            "routing": true,
#                            "sequence": 11,
#                            "source": {
#                                "port_protocol": {
#                                    "range": {
#                                        "end": "telnet",
#                                        "start": "ftp"
#                                    }
#                                },
#                                "prefix": "2001:db8:1234::/48"
#                            },
#                            "ttl": {
#                                "range": {
#                                    "end": 250,
#                                    "start": 180
#                                }
#                            }
#                        },
#                        {
#                            "destination": {
#                                "any": true
#                            },
#                            "destopts": true,
#                            "grant": "permit",
#                            "packet_length": {
#                                "eq": 576
#                            },
#                            "precedence": "network",
#                            "protocol": "icmpv6",
#                            "protocol_options": {
#                                "icmpv6": {
#                                    "router_advertisement": true
#                                }
#                            },
#                            "sequence": 21,
#                            "source": {
#                                "any": true
#                            }
#                        }
#                    ],
#                    "name": "acl_2"
#                }
#            ],
#            "afi": "ipv4"
#        },
#        {
#            "acls": [
#                {
#                    "aces": [
#                        {
#                            "authen": true,
#                            "destination": {
#                                "any": true
#                            },
#                            "grant": "deny",
#                            "log": true,
#                            "protocol": "tcp",
#                            "protocol_options": {
#                                "tcp": {
#                                    "syn": true
#                                }
#                            },
#                            "routing": true,
#                            "sequence": 10,
#                            "source": {
#                                "port_protocol": {
#                                    "range": {
#                                        "end": "telnet",
#                                        "start": "ftp"
#                                    }
#                                },
#                                "prefix": "2001:db8:1234::/48"
#                            },
#                            "ttl": {
#                                "range": {
#                                    "end": 250,
#                                    "start": 180
#                                }
#                            }
#                        },
#                        {
#                            "destination": {
#                                "any": true
#                            },
#                            "destopts": true,
#                            "grant": "permit",
#                            "packet_length": {
#                                "eq": 576
#                            },
#                            "precedence": "network",
#                            "protocol": "icmpv6",
#                            "protocol_options": {
#                                "icmpv6": {
#                                    "router_advertisement": true
#                                }
#                            },
#                            "sequence": 20,
#                            "source": {
#                                "any": true
#                            }
#                        }
#                    ],
#                    "name": "acl6_1"
#                }
#            ],
#            "afi": "ipv6"
#        }
#    ]
```

## [Return Values](iosxr_acls_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["ipv6 access-list acl6_1", "10 deny tcp 2001:db8:1234::/48 range ftp telnet any syn ttl range 180 250 authen routing log", "20 permit icmpv6 any any router-advertisement precedence network destopts", "ipv4 access-list acl_1", "16 remark TEST_ACL_1_REMARK", "21 permit tcp host 192.0.2.10 range pop3 121 198.51.100.0 0.0.0.15 rst", "23 deny icmp any 198.51.100.0 0.0.0.15 reassembly-timeout dscp lt af12"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
