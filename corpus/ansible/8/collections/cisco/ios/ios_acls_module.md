---
collection: ansible
version: "8"
title: "cisco.ios.ios_acls module – Resource module to configure ACLs."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_acls_module.html
fetched_at: 2026-07-28T01:26:03+00:00
---
# cisco.ios.ios_acls module – Resource module to configure ACLs.

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
> To use it in a playbook, specify: `cisco.ios.ios_acls`.

New in cisco.ios 1.0.0

- [Synopsis](ios_acls_module.md#synopsis)
- [Parameters](ios_acls_module.md#parameters)
- [Notes](ios_acls_module.md#notes)
- [Examples](ios_acls_module.md#examples)
- [Return Values](ios_acls_module.md#return-values)

## [Synopsis](ios_acls_module.md#id1)

- This module configures and manages the named or numbered ACLs on IOS platforms.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: acls

## [Parameters](ios_acls_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of ACL configuration options. |
| **acls**  list / elements=dictionary | A list of Access Control Lists (ACL) attributes. |
| **aces**  list / elements=dictionary | The entries within the ACL. |
| **destination**  dictionary | Specify the packet destination. |
| **address**  string | Host address to match, or any single host address. |
| **any**  boolean | Match any source address.  **Choices:**   - `false` - `true` |
| **host**  string | A single destination host |
| **object_group**  string | Destination network object group |
| **port_protocol**  dictionary | Specify the destination port along with protocol.  Note, Valid with TCP/UDP protocol_options |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Port group. |
| **end**  integer | Specify the end of the port range. |
| **start**  integer | Specify the start of the port range. |
| **wildcard_bits**  string | Destination wildcard bits, valid with IPV4 address. |
| **dscp**  string | Match packets with given dscp value. |
| **enable_fragments**  boolean | Enable non-initial fragments.  **Choices:**   - `false` - `true` |
| **evaluate**  string | Evaluate an access list |
| **fragments**  string | Check non-initial fragments.  This option is DEPRECATED and is replaced with enable_fragments which accepts bool as input this attribute will be removed after 2024-01-01. |
| **grant**  string | Specify the action.  **Choices:**   - `"permit"` - `"deny"` |
| **log**  dictionary | Log matches against this entry. |
| **set**  boolean | Enable Log matches against this entry  **Choices:**   - `false` - `true` |
| **user_cookie**  string | User defined cookie (max of 64 char) |
| **log_input**  dictionary | Log matches against this entry, including input interface. |
| **set**  boolean | Enable Log matches against this entry, including input interface.  **Choices:**   - `false` - `true` |
| **user_cookie**  string | User defined cookie (max of 64 char) |
| **option**  dictionary | Match packets with given IP Options value.  Valid only for named acls. |
| **add_ext**  boolean | Match packets with Address Extension Option (147).  **Choices:**   - `false` - `true` |
| **any_options**  boolean | Match packets with ANY Option.  **Choices:**   - `false` - `true` |
| **com_security**  boolean | Match packets with Commercial Security Option (134).  **Choices:**   - `false` - `true` |
| **dps**  boolean | Match packets with Dynamic Packet State Option (151).  **Choices:**   - `false` - `true` |
| **encode**  boolean | Match packets with Encode Option (15).  **Choices:**   - `false` - `true` |
| **eool**  boolean | Match packets with End of Options (0).  **Choices:**   - `false` - `true` |
| **ext_ip**  boolean | Match packets with Extended IP Option (145).  **Choices:**   - `false` - `true` |
| **ext_security**  boolean | Match packets with Extended Security Option (133).  **Choices:**   - `false` - `true` |
| **finn**  boolean | Match packets with Experimental Flow Control Option (205).  **Choices:**   - `false` - `true` |
| **imitd**  boolean | Match packets with IMI Traffic Desriptor Option (144).  **Choices:**   - `false` - `true` |
| **lsr**  boolean | Match packets with Loose Source Route Option (131).  **Choices:**   - `false` - `true` |
| **mtup**  boolean | Match packets with MTU Probe Option (11).  **Choices:**   - `false` - `true` |
| **mtur**  boolean | Match packets with MTU Reply Option (12).  **Choices:**   - `false` - `true` |
| **no_op**  boolean | Match packets with No Operation Option (1).  **Choices:**   - `false` - `true` |
| **nsapa**  boolean | Match packets with NSAP Addresses Option (150).  **Choices:**   - `false` - `true` |
| **record_route**  boolean | Match packets with Record Route Option (7).  **Choices:**   - `false` - `true` |
| **router_alert**  boolean | Match packets with Router Alert Option (148).  **Choices:**   - `false` - `true` |
| **sdb**  boolean | Match packets with Selective Directed Broadcast Option (149).  **Choices:**   - `false` - `true` |
| **security**  boolean | Match packets with Basic Security Option (130).  **Choices:**   - `false` - `true` |
| **ssr**  boolean | Match packets with Strict Source Routing Option (137).  **Choices:**   - `false` - `true` |
| **stream_id**  boolean | Match packets with Stream ID Option (136).  **Choices:**   - `false` - `true` |
| **timestamp**  boolean | Match packets with Time Stamp Option (68).  **Choices:**   - `false` - `true` |
| **traceroute**  boolean | Match packets with Trace Route Option (82).  **Choices:**   - `false` - `true` |
| **ump**  boolean | Match packets with Upstream Multicast Packet Option (152).  **Choices:**   - `false` - `true` |
| **visa**  boolean | Match packets with Experimental Access Control Option (142).  **Choices:**   - `false` - `true` |
| **zsu**  boolean | Match packets with Experimental Measurement Option (10).  **Choices:**   - `false` - `true` |
| **precedence**  string | Match packets with given precedence value. |
| **protocol**  string | Specify the protocol to match.  Refer to vendor documentation for valid values. |
| **protocol_options**  dictionary | protocol type. |
| **ahp**  boolean | Authentication Header Protocol.  **Choices:**   - `false` - `true` |
| **eigrp**  boolean | Cisco’s EIGRP routing protocol.  **Choices:**   - `false` - `true` |
| **esp**  boolean | Encapsulation Security Payload.  **Choices:**   - `false` - `true` |
| **gre**  boolean | Cisco’s GRE tunneling.  **Choices:**   - `false` - `true` |
| **hbh**  boolean | Hop by Hop options header. Valid for IPV6  **Choices:**   - `false` - `true` |
| **icmp**  dictionary | Internet Control Message Protocol. |
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
| **mask_request**  boolean | mask_request  **Choices:**   - `false` - `true` |
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
| **igmp**  dictionary | Internet Gateway Message Protocol. |
| **dvmrp**  boolean | Distance Vector Multicast Routing Protocol(2)  **Choices:**   - `false` - `true` |
| **host_query**  boolean | IGMP Membership Query(0)  **Choices:**   - `false` - `true` |
| **mtrace_resp**  boolean | Multicast Traceroute Response(7)  **Choices:**   - `false` - `true` |
| **mtrace_route**  boolean | Multicast Traceroute(8)  **Choices:**   - `false` - `true` |
| **pim**  boolean | Protocol Independent Multicast(3)  **Choices:**   - `false` - `true` |
| **trace**  boolean | Multicast trace(4)  **Choices:**   - `false` - `true` |
| **v1host_report**  boolean | IGMPv1 Membership Report(1)  **Choices:**   - `false` - `true` |
| **v2host_report**  boolean | IGMPv2 Membership Report(5)  **Choices:**   - `false` - `true` |
| **v2leave_group**  boolean | IGMPv2 Leave Group(6)  **Choices:**   - `false` - `true` |
| **v3host_report**  boolean | IGMPv3 Membership Report(9)  **Choices:**   - `false` - `true` |
| **ip**  boolean | Any Internet Protocol.  **Choices:**   - `false` - `true` |
| **ipinip**  boolean | IP in IP tunneling.  **Choices:**   - `false` - `true` |
| **ipv6**  boolean | Any IPv6.  **Choices:**   - `false` - `true` |
| **nos**  boolean | KA9Q NOS compatible IP over IP tunneling.  **Choices:**   - `false` - `true` |
| **ospf**  boolean | OSPF routing protocol.  **Choices:**   - `false` - `true` |
| **pcp**  boolean | Payload Compression Protocol.  **Choices:**   - `false` - `true` |
| **pim**  boolean | Protocol Independent Multicast.  **Choices:**   - `false` - `true` |
| **protocol_number**  integer | An IP protocol number |
| **sctp**  boolean | Stream Control Transmission Protocol.  **Choices:**   - `false` - `true` |
| **tcp**  dictionary | Match TCP packet flags |
| **ack**  boolean | Match on the ACK bit  **Choices:**   - `false` - `true` |
| **established**  boolean | Match established connections  **Choices:**   - `false` - `true` |
| **fin**  boolean | Match on the FIN bit  **Choices:**   - `false` - `true` |
| **psh**  boolean | Match on the PSH bit  **Choices:**   - `false` - `true` |
| **rst**  boolean | Match on the RST bit  **Choices:**   - `false` - `true` |
| **syn**  boolean | Match on the SYN bit  **Choices:**   - `false` - `true` |
| **urg**  boolean | Match on the URG bit  **Choices:**   - `false` - `true` |
| **udp**  boolean | User Datagram Protocol.  **Choices:**   - `false` - `true` |
| **remarks**  list / elements=string | The remarks/description of the ACL. |
| **sequence**  integer | Sequence Number for the Access Control Entry(ACE).  Refer to vendor documentation for valid values. |
| **source**  dictionary | Specify the packet source. |
| **address**  string | Source network address. |
| **any**  boolean | Match any source address.  **Choices:**   - `false` - `true` |
| **host**  string | A single source host |
| **object_group**  string | Source network object group |
| **port_protocol**  dictionary | Specify the source port along with protocol.  Note, Valid with TCP/UDP protocol_options |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Port group. |
| **end**  integer | Specify the end of the port range. |
| **start**  integer | Specify the start of the port range. |
| **wildcard_bits**  string | Source wildcard bits, valid with IPV4 address. |
| **time_range**  string | Specify a time-range. |
| **tos**  dictionary | Match packets with given TOS value.  Note, DSCP and TOS are mutually exclusive |
| **max_reliability**  boolean | Match packets with max reliable TOS (2).  **Choices:**   - `false` - `true` |
| **max_throughput**  boolean | Match packets with max throughput TOS (4).  **Choices:**   - `false` - `true` |
| **min_delay**  boolean | Match packets with min delay TOS (8).  **Choices:**   - `false` - `true` |
| **min_monetary_cost**  boolean | Match packets with min monetary cost TOS (1).  **Choices:**   - `false` - `true` |
| **normal**  boolean | Match packets with normal TOS (0).  **Choices:**   - `false` - `true` |
| **service_value**  integer | Type of service value |
| **ttl**  dictionary | Match packets with given TTL value. |
| **eq**  integer | Match only packets on a given TTL number. |
| **gt**  integer | Match only packets with a greater TTL number. |
| **lt**  integer | Match only packets with a lower TTL number. |
| **neq**  integer | Match only packets not on a given TTL number. |
| **range**  dictionary | Match only packets in the range of TTLs. |
| **end**  integer | Specify the end of the port range. |
| **start**  integer | Specify the start of the port range. |
| **acl_type**  string | ACL type  Note, it’s mandatory and required for Named ACL, but for Numbered ACL it’s not mandatory.  **Choices:**   - `"extended"` - `"standard"` |
| **name**  string / required | The name or the number of the ACL. |
| **afi**  string / required | The Address Family Indicator (AFI) for the Access Control Lists (ACL).  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **sh access-list**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The state *merged* is the default state which merges the want and have config, but for ACL module as the IOS platform doesn’t allow update of ACE over an pre-existing ACE sequence in ACL, same way ACLs resource module will error out for respective scenario and only addition of new ACE over new sequence will be allowed with merge state.  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of commands *show access-list* and *show running-config | include ip(v6*\* access-list|remark) executed on device. Config data from both the commands should be kept together one after another for the parsers to pick the commands correctly. For state *parsed* active connection to remote host is not required.  The state *overridden*, modify/add the ACLs defined, deleted all other ACLs.  The state *replaced*, modify/add only the ACEs of the ACLs defined only. It does not perform any other change on the device.  The state *deleted*, deletes only the specified ACLs, or all if not specified.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](ios_acls_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - Module behavior is not idempotent when sequence for aces are not mentioned
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_acls_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# vios#sh access-lists
# Extended IP access list 100
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 echo dscp ef ttl eq 10

- name: Merge provided configuration with device configuration
  cisco.ios.ios_acls:
    config:
      - afi: ipv4
        acls:
          - name: 100
            aces:
              - sequence: 10
                protocol_options:
                  icmp:
                    traceroute: true
    state: merged

# After state:
# ------------
#
# Play Execution fails, with error:
# Cannot update existing sequence 10 of ACLs 100 with state merged.
# Please use state replaced or overridden.

# Before state:
# -------------
#
# vios#sh access-lists
# Extended IP access list 110
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 echo dscp ef ttl eq 10

- name: Merge provided configuration with device configuration
  cisco.ios.ios_acls:
    config:
      - afi: ipv4
        acls:
          - name: std_acl
            acl_type: standard
            aces:
              - grant: deny
                source:
                  address: 192.168.1.200
              - grant: deny
                source:
                  address: 192.168.2.0
                  wildcard_bits: 0.0.0.255
          - name: 110
            aces:
              - sequence: 10
                protocol_options:
                  icmp:
                    traceroute: true
              - grant: deny
                protocol_options:
                  tcp:
                    ack: true
                source:
                  host: 198.51.100.0
                destination:
                  host: 198.51.110.0
                  port_protocol:
                    eq: telnet
          - name: test
            acl_type: extended
            aces:
              - grant: deny
                protocol_options:
                  tcp:
                    fin: true
                source:
                  address: 192.0.2.0
                  wildcard_bits: 0.0.0.255
                destination:
                  address: 192.0.3.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: www
                option:
                  traceroute: true
                ttl:
                  eq: 10
          - name: 123
            aces:
              - remarks:
                  - "remarks for extended ACL 1"
                  - "check ACL"
              - grant: deny
                protocol_options:
                  tcp:
                    ack: true
                source:
                  address: 198.51.100.0
                  wildcard_bits: 0.0.0.255
                destination:
                  address: 198.51.101.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: telnet
                tos:
                  service_value: 12
              - grant: deny
                protocol_options:
                  tcp:
                    ack: true
                source:
                  address: 192.0.3.0
                  wildcard_bits: 0.0.0.255
                destination:
                  address: 192.0.4.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: www
                dscp: ef
                ttl:
                  lt: 20
      - afi: ipv6
        acls:
          - name: R1_TRAFFIC
            aces:
              - grant: deny
                protocol_options:
                  tcp:
                    ack: true
                source:
                  any: true
                  port_protocol:
                    eq: www
                destination:
                  any: true
                  port_protocol:
                    eq: telnet
                dscp: af11
    state: merged

# Commands fired:
# ---------------
#
# - ip access-list standard std_acl
# - deny 192.168.1.200
# - deny 192.168.2.0 0.0.0.255
# - ip access-list extended 110
# - 10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
# - deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
# - ip access-list extended test
# - deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
# - ip access-list extended 123
# - deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
# - deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
# - remark remarks for extended ACL 1
# - remark check ACL
# - ipv6 access-list R1_TRAFFIC
# - deny tcp any eq www any eq telnet ack dscp af11

# After state:
# ------------
#
# vios#sh access-lists
# Standard IP access list std_acl
#    10 deny   192.168.1.200
#    20 deny   192.168.2.0, wildcard bits 0.0.0.255
# Extended IP access list 100
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 echo dscp ef ttl eq 10
# Extended IP access list 110
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
#    20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
# Extended IP access list 123
#    10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
#    20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
# Extended IP access list test
#    10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
# IPv6 access list R1_TRAFFIC
#    deny tcp any eq www any eq telnet ack dscp af11 sequence 10

# Using replaced

# Before state:
# -------------
#
# vios#sh access-lists
# Standard IP access list std_acl
#    10 deny   192.168.1.200
#    20 deny   192.168.2.0, wildcard bits 0.0.0.255
# Extended IP access list 110
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
#    20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
# Extended IP access list 123
#    10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
#    20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
# Extended IP access list test
#    10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
# IPv6 access list R1_TRAFFIC
#    deny tcp any eq www any eq telnet ack dscp af11 sequence 10

- name: Replaces device configuration of listed acls with provided configuration
  cisco.ios.ios_acls:
    config:
      - afi: ipv4
        acls:
          - name: 110
            aces:
              - grant: deny
                protocol_options:
                  tcp:
                    syn: true
                source:
                  address: 192.0.2.0
                  wildcard_bits: 0.0.0.255
                destination:
                  address: 192.0.3.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: www
                dscp: ef
                ttl:
                  eq: 10
          - name: 150
            aces:
              - grant: deny
                sequence: 20
                protocol_options:
                  tcp:
                    syn: true
                source:
                  address: 198.51.100.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: telnet
                destination:
                  address: 198.51.110.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: telnet
                dscp: ef
                ttl:
                  eq: 10
    state: replaced

# Commands fired:
# ---------------
#
# - no ip access-list extended 110
# - ip access-list extended 110
# - deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www syn dscp ef ttl eq 10
# - ip access-list extended 150
# - 20 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn dscp ef ttl eq 10

# After state:
# -------------
#
# vios#sh access-lists
# Standard IP access list std_acl
#    10 deny   192.168.1.200
#    20 deny   192.168.2.0, wildcard bits 0.0.0.255
# Extended IP access list 110
#    10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www syn dscp ef ttl eq 10
# Extended IP access list 123
#    10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
#    20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
# Extended IP access list 150
#    20 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn dscp ef ttl eq 10
# Extended IP access list test
#    10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
# IPv6 access list R1_TRAFFIC
#    deny tcp any eq www any eq telnet ack dscp af11 sequence 10

# Using overridden

# Before state:
# -------------
#
# vios#sh access-lists
# Standard IP access list std_acl
#    10 deny   192.168.1.200
#    20 deny   192.168.2.0, wildcard bits 0.0.0.255
# Extended IP access list 110
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
#    20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
# Extended IP access list 123
#    10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
#    20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
# Extended IP access list test
#    10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
# IPv6 access list R1_TRAFFIC
#    deny tcp any eq www any eq telnet ack dscp af11 sequence 10

- name: Override device configuration of all acls with provided configuration
  cisco.ios.ios_acls:
    config:
      - afi: ipv4
        acls:
          - name: 110
            aces:
              - grant: deny
                sequence: 20
                protocol_options:
                  tcp:
                    ack: true
                source:
                  address: 198.51.100.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: telnet
                destination:
                  address: 198.51.110.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: www
                dscp: ef
                ttl:
                  eq: 10
          - name: 150
            aces:
              - grant: deny
                sequence: 10
                protocol_options:
                  tcp:
                    syn: true
                source:
                  address: 198.51.100.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: telnet
                destination:
                  address: 198.51.110.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: telnet
                dscp: ef
                ttl:
                  eq: 10
    state: overridden

# Commands fired:
# ---------------
#
# - no ip access-list standard std_acl
# - no ip access-list extended 110
# - no ip access-list extended 123
# - no ip access-list extended 150
# - no ip access-list extended test
# - no ipv6 access-list R1_TRAFFIC
# - ip access-list extended 150
# - 10 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn dscp ef ttl eq 10
# - ip access-list extended 110
# - 20 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq www ack dscp ef ttl eq 10

# After state:
# -------------
#
# vios#sh access-lists
# Extended IP access list 110
#    20 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq www ack dscp ef ttl eq 10
# Extended IP access list 150
#    10 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn dscp ef ttl eq 10

# Using Deleted

# Before state:
# -------------
#
# vios#sh access-lists
# Standard IP access list std_acl
#    10 deny   192.168.1.200
#    20 deny   192.168.2.0, wildcard bits 0.0.0.255
# Extended IP access list 110
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
#    20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
# Extended IP access list 123
#    10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
#    20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
# Extended IP access list test
#    10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
# IPv6 access list R1_TRAFFIC
#    deny tcp any eq www any eq telnet ack dscp af11 sequence 10

- name: "Delete ACLs (Note: This won't delete the all configured ACLs)"
  cisco.ios.ios_acls:
    config:
      - afi: ipv4
        acls:
          - name: test
            acl_type: extended
          - name: 110
      - afi: ipv6
        acls:
          - name: R1_TRAFFIC
    state: deleted

# Commands fired:
# ---------------
#
# - no ip access-list extended test
# - no ip access-list extended 110
# - no ipv6 access-list R1_TRAFFIC

# After state:
# -------------
#
# vios#sh access-lists
# Standard IP access list std_acl
#    10 deny   192.168.1.200
#    20 deny   192.168.2.0, wildcard bits 0.0.0.255
# Extended IP access list 123
#    10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
#    20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20

# Before state:
# -------------
#
# vios#sh access-lists
# Standard IP access list std_acl
#    10 deny   192.168.1.200
#    20 deny   192.168.2.0, wildcard bits 0.0.0.255
# Extended IP access list 110
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
#    20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
# Extended IP access list 123
#    10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
#    20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
# Extended IP access list test
#    10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
# IPv6 access list R1_TRAFFIC
#    deny tcp any eq www any eq telnet ack dscp af11 sequence 10

- name: "Delete ACLs based on AFI (Note: This won't delete the all configured ACLs)"
  cisco.ios.ios_acls:
    config:
      - afi: ipv4
    state: deleted

# Commands fired:
# ---------------
#
# - no ip access-list standard std_acl
# - no ip access-list extended test
# - no ip access-list extended 110
# - no ip access-list extended 123

# After state:
# -------------
#
# vios#sh access-lists
# IPv6 access list R1_TRAFFIC
#    deny tcp any eq www any eq telnet ack dscp af11 sequence 10

# Using Deleted without any config passed
#"(NOTE: This will delete all of configured ACLs)"

# Before state:
# -------------
#
# vios#sh access-lists
# Standard IP access list std_acl
#    10 deny   192.168.1.200
#    20 deny   192.168.2.0, wildcard bits 0.0.0.255
# Extended IP access list 110
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
#    20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
# Extended IP access list 123
#    10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
#    20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
# Extended IP access list test
#    10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
# IPv6 access list R1_TRAFFIC
#    deny tcp any eq www any eq telnet ack dscp af11 sequence 10

- name:
    "Delete ALL of configured ACLs (Note: This WILL delete the all configured
    ACLs)"
  cisco.ios.ios_acls:
    state: deleted

# Commands fired:
# ---------------
#
# - no ip access-list extended test
# - no ip access-list extended 110
# - no ip access-list extended 123
# - no ip access-list extended test
# - no ipv6 access-list R1_TRAFFIC

# After state:
# -------------
#
# vios#sh access-lists

# Using Gathered

# Before state:
# -------------
#
# vios#sh access-lists
# Standard IP access list std_acl
#    10 deny   192.168.1.200
#    20 deny   192.168.2.0, wildcard bits 0.0.0.255
# Extended IP access list 110
#    10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
#    20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
# Extended IP access list 123
#    10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
#    20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
# Extended IP access list test
#    10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
# IPv6 access list R1_TRAFFIC
#    deny tcp any eq www any eq telnet ack dscp af11 sequence 10

- name: Gather listed acls with provided configurations
  cisco.ios.ios_acls:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "acls": [
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "address": "192.0.3.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "dscp": "ef",
#                             "grant": "deny",
#                             "protocol_options": {
#                                 "icmp": {
#                                     "echo": true
#                                 }
#                             },
#                             "sequence": 10,
#                             "source": {
#                                 "address": "192.0.2.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "ttl": {
#                                 "eq": 10
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "110"
#                 },
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "address": "198.51.101.0",
#                                 "port_protocol": {
#                                     "eq": "telnet"
#                                 },
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "grant": "deny",
#                             "protocol_options": {
#                                 "tcp": {
#                                     "ack": true
#                                 }
#                             },
#                             "sequence": 10,
#                             "source": {
#                                 "address": "198.51.100.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "tos": {
#                                 "service_value": 12
#                             }
#                         },
#                         {
#                             "destination": {
#                                 "address": "192.0.4.0",
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 },
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "dscp": "ef",
#                             "grant": "deny",
#                             "protocol_options": {
#                                 "tcp": {
#                                     "ack": true
#                                 }
#                             },
#                             "sequence": 20,
#                             "source": {
#                                 "address": "192.0.3.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "ttl": {
#                                 "lt": 20
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "123"
#                 },
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "address": "192.0.3.0",
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 },
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "grant": "deny",
#                             "option": {
#                                 "traceroute": true
#                             },
#                             "protocol_options": {
#                                 "tcp": {
#                                     "fin": true
#                                 }
#                             },
#                             "sequence": 10,
#                             "source": {
#                                 "address": "192.0.2.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "ttl": {
#                                 "eq": 10
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "test_acl"
#                 }
#             ],
#             "afi": "ipv4"
#         },
#         {
#             "acls": [
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "any": true,
#                                 "port_protocol": {
#                                     "eq": "telnet"
#                                 }
#                             },
#                             "dscp": "af11",
#                             "grant": "deny",
#                             "protocol_options": {
#                                 "tcp": {
#                                     "ack": true
#                                 }
#                             },
#                             "sequence": 10,
#                             "source": {
#                                 "any": true,
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 }
#                             }
#                         }
#                     ],
#                     "name": "R1_TRAFFIC"
#                 }
#             ],
#             "afi": "ipv6"
#         }
#     ]

# Using Rendered

- name: Rendered the provided configuration with the existing running configuration
  cisco.ios.ios_acls:
    config:
      - afi: ipv4
        acls:
          - name: 110
            aces:
              - grant: deny
                sequence: 10
                protocol_options:
                  tcp:
                    syn: true
                source:
                  address: 192.0.2.0
                  wildcard_bits: 0.0.0.255
                destination:
                  address: 192.0.3.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: www
                dscp: ef
                ttl:
                  eq: 10
          - name: 150
            aces:
              - grant: deny
                protocol_options:
                  tcp:
                    syn: true
                source:
                  address: 198.51.100.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: telnet
                destination:
                  address: 198.51.110.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: telnet
                dscp: ef
                ttl:
                  eq: 10
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "ip access-list extended 110",
#         "10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www syn dscp ef ttl eq 10",
#         "ip access-list extended 150",
#         "deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn dscp ef ttl eq 10"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# IPv6 access-list R1_TRAFFIC
# deny tcp any eq www any eq telnet ack dscp af11

- name: Parse the commands for provided configuration
  cisco.ios.ios_acls:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "acls": [
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "any": true,
#                                 "port_protocol": {
#                                     "eq": "telnet"
#                                 }
#                             },
#                             "dscp": "af11",
#                             "grant": "deny",
#                             "protocol_options": {
#                                 "tcp": {
#                                     "ack": true
#                                 }
#                             },
#                             "source": {
#                                 "any": true,
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 }
#                             }
#                         }
#                     ],
#                     "name": "R1_TRAFFIC"
#                 }
#             ],
#             "afi": "ipv6"
#         }
#     ]
```

## [Return Values](ios_acls_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["ip access-list extended 110", "deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 echo dscp ef ttl eq 10", "permit ip host 2.2.2.2 host 3.3.3.3"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["ip access-list extended test", "permit ip host 2.2.2.2 host 3.3.3.3", "permit tcp host 1.1.1.1 host 5.5.5.5 eq www"]` |

### Authors

- Sumit Jaiswal (@justjais)
- Sagar Paul (@KB-perByte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
