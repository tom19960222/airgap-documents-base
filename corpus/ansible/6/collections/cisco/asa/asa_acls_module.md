---
collection: ansible
version: "6"
title: "cisco.asa.asa_acls module – Access-Lists resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/asa/asa_acls_module.html
fetched_at: 2026-07-27T16:50:45+00:00
---
# cisco.asa.asa_acls module – Access-Lists resource module

> **Note:**
>
> This module is part of the [cisco.asa collection](https://galaxy.ansible.com/cisco/asa) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.asa`.
>
> To use it in a playbook, specify: `cisco.asa.asa_acls`.

New in cisco.asa 1.0.0

- [Synopsis](asa_acls_module.md#synopsis)
- [Parameters](asa_acls_module.md#parameters)
- [Notes](asa_acls_module.md#notes)
- [Examples](asa_acls_module.md#examples)
- [Return Values](asa_acls_module.md#return-values)

## [Synopsis](asa_acls_module.md#id1)

- This module configures and manages the named or numbered ACLs on ASA platforms.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](asa_acls_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of ACL options. |
| **acls**  list / elements=dictionary | A list of Access Control Lists (ACL). |
| **aces**  list / elements=dictionary | The entries within the ACL. |
| **destination**  dictionary | Specify the packet destination. |
| **address**  string | Host address to match, or any single host address. |
| **any**  boolean | Match any destination address.  Choices:   - `false` - `true` |
| **any4**  boolean | Match any ipv4 destination address.  Choices:   - `false` - `true` |
| **any6**  boolean | Match any ipv6 destination address.  Choices:   - `false` - `true` |
| **host**  string | A single destination host |
| **interface**  string | Use interface address as destination address |
| **netmask**  string | Netmask for destination IP address, valid with IPV4 address. |
| **object_group**  string | Network object-group for destination address |
| **port_protocol**  dictionary | Specify the destination port along with protocol.  Note, Valid with TCP/UDP protocol_options |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Port range operator |
| **end**  integer | Specify the end of the port range. |
| **start**  integer | Specify the start of the port range. |
| **service_object_group**  string | Service object-group for destination port |
| **grant**  string | Specify the action.  Choices:   - `"permit"` - `"deny"` |
| **inactive**  boolean | Keyword for disabling an ACL element.  Choices:   - `false` - `true` |
| **line**  integer | Use this to specify line number at which ACE should be entered.  Existing ACE can be updated based on the input line number.  It’s not a required param in case of configuring the acl, but in case of Delete operation it’s required, else Delete operation won’t work as expected.  Refer to vendor documentation for valid values. |
| **log**  string | Log matches against this entry.  Choices:   - `"default"` - `"alerts"` - `"critical"` - `"debugging"` - `"disable"` - `"emergencies"` - `"errors"` - `"informational"` - `"interval"` - `"notifications"` - `"warnings"` |
| **protocol**  string | Specify the protocol to match.  Refer to vendor documentation for valid values. |
| **protocol_options**  dictionary | protocol type. |
| **ahp**  boolean | Authentication Header Protocol.  Choices:   - `false` - `true` |
| **eigrp**  boolean | Cisco’s EIGRP routing protocol.  Choices:   - `false` - `true` |
| **esp**  boolean | Encapsulation Security Payload.  Choices:   - `false` - `true` |
| **gre**  boolean | Cisco’s GRE tunneling.  Choices:   - `false` - `true` |
| **icmp**  dictionary | Internet Control Message Protocol. |
| **alternate_address**  boolean | Alternate address  Choices:   - `false` - `true` |
| **conversion_error**  boolean | Datagram conversion  Choices:   - `false` - `true` |
| **echo**  boolean | Echo (ping)  Choices:   - `false` - `true` |
| **echo_reply**  boolean | Echo reply  Choices:   - `false` - `true` |
| **information_reply**  boolean | Information replies  Choices:   - `false` - `true` |
| **information_request**  boolean | Information requests  Choices:   - `false` - `true` |
| **mask_reply**  boolean | Mask replies  Choices:   - `false` - `true` |
| **mask_request**  boolean | mask_request  Choices:   - `false` - `true` |
| **mobile_redirect**  boolean | Mobile host redirect  Choices:   - `false` - `true` |
| **parameter_problem**  boolean | All parameter problems  Choices:   - `false` - `true` |
| **redirect**  boolean | All redirects  Choices:   - `false` - `true` |
| **router_advertisement**  boolean | Router discovery advertisements  Choices:   - `false` - `true` |
| **router_solicitation**  boolean | Router discovery solicitations  Choices:   - `false` - `true` |
| **source_quench**  boolean | Source quenches  Choices:   - `false` - `true` |
| **source_route_failed**  boolean | Source route  Choices:   - `false` - `true` |
| **time_exceeded**  boolean | All time exceededs  Choices:   - `false` - `true` |
| **timestamp_reply**  boolean | Timestamp replies  Choices:   - `false` - `true` |
| **timestamp_request**  boolean | Timestamp requests  Choices:   - `false` - `true` |
| **traceroute**  boolean | Traceroute  Choices:   - `false` - `true` |
| **unreachable**  boolean | All unreachables  Choices:   - `false` - `true` |
| **icmp6**  dictionary | Internet Control Message Protocol. |
| **echo**  boolean | Echo (ping)  Choices:   - `false` - `true` |
| **echo_reply**  boolean | Echo reply  Choices:   - `false` - `true` |
| **membership_query**  boolean | Membership query  Choices:   - `false` - `true` |
| **membership_reduction**  boolean | Membership reduction  Choices:   - `false` - `true` |
| **membership_report**  boolean | Membership report  Choices:   - `false` - `true` |
| **neighbor_advertisement**  boolean | Neighbor advertisement  Choices:   - `false` - `true` |
| **neighbor_redirect**  boolean | Neighbor redirect  Choices:   - `false` - `true` |
| **neighbor_solicitation**  boolean | Neighbor_solicitation  Choices:   - `false` - `true` |
| **packet_too_big**  boolean | Packet too big  Choices:   - `false` - `true` |
| **parameter_problem**  boolean | Parameter problem  Choices:   - `false` - `true` |
| **router_advertisement**  boolean | Router discovery advertisements  Choices:   - `false` - `true` |
| **router_renumbering**  boolean | Router renumbering  Choices:   - `false` - `true` |
| **router_solicitation**  boolean | Router solicitation  Choices:   - `false` - `true` |
| **time_exceeded**  boolean | Time exceeded  Choices:   - `false` - `true` |
| **unreachable**  boolean | All unreachables  Choices:   - `false` - `true` |
| **igmp**  boolean | Internet Gateway Message Protocol.  Choices:   - `false` - `true` |
| **igrp**  boolean | Internet Gateway Routing Protocol.  Choices:   - `false` - `true` |
| **ip**  boolean | Any Internet Protocol.  Choices:   - `false` - `true` |
| **ipinip**  boolean | IP in IP tunneling.  Choices:   - `false` - `true` |
| **ipsec**  boolean | IP Security.  Choices:   - `false` - `true` |
| **nos**  boolean | KA9Q NOS compatible IP over IP tunneling.  Choices:   - `false` - `true` |
| **ospf**  boolean | OSPF routing protocol.  Choices:   - `false` - `true` |
| **pcp**  boolean | Payload Compression Protocol.  Choices:   - `false` - `true` |
| **pim**  boolean | Protocol Independent Multicast.  Choices:   - `false` - `true` |
| **pptp**  boolean | Point-to-Point Tunneling Protocol.  Choices:   - `false` - `true` |
| **protocol_number**  integer | An IP protocol number |
| **sctp**  boolean | Stream Control Transmission Protocol.  Choices:   - `false` - `true` |
| **snp**  boolean | Simple Network Protocol.  Choices:   - `false` - `true` |
| **tcp**  boolean | Match TCP packet flags  Choices:   - `false` - `true` |
| **udp**  boolean | User Datagram Protocol.  Choices:   - `false` - `true` |
| **remark**  string | Specify a comment (remark) for the access-list after this keyword |
| **source**  dictionary | Specify the packet source. |
| **address**  string | Source network address. |
| **any**  boolean | Match any source address.  Choices:   - `false` - `true` |
| **any4**  boolean | Match any ipv4 source address.  Choices:   - `false` - `true` |
| **any6**  boolean | Match any ipv6 source address.  Choices:   - `false` - `true` |
| **host**  string | A single source host |
| **interface**  string | Use interface address as source address |
| **netmask**  string | Netmask for source IP address, valid with IPV4 address. |
| **object_group**  string | Network object-group for source address |
| **port_protocol**  dictionary | Specify the destination port along with protocol.  Note, Valid with TCP/UDP protocol_options |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Port range operator |
| **end**  integer | Specify the end of the port range. |
| **start**  integer | Specify the start of the port range. |
| **time_range**  string | Specify a time-range. |
| **acl_type**  string | ACL type  Choices:   - `"extended"` - `"standard"` |
| **name**  string / required | The name or the number of the ACL. |
| **rename**  string | Rename an existing access-list.  If input to rename param is given, it’ll take preference over other parameters and only rename config will be matched and computed against. |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. |
| **state**  string | The state of the configuration after module completion  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](asa_acls_module.md#id3)

> **Note:**
>
> - Tested against Cisco ASA Version 9.10(1)11
> - This module works with connection `network_cli`. See [ASA Platform Options](../network/user_guide/platform_asa.md).

## [Examples](asa_acls_module.md#id4)

```yaml+jinja
# Using merged
# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 2 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list R1_traffic; 1 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3

- name: Merge provided configuration with device configuration
  cisco.asa.asa_acls:
    config:
      acls:
        - name: temp_access
          acl_type: extended
          aces:
          - grant: deny
            line: 1
            protocol_options:
              tcp: true
            source:
              address: 192.0.2.0
              netmask: 255.255.255.0
            destination:
              address: 192.0.3.0
              netmask: 255.255.255.0
              port_protocol:
                eq: www
            log: default
          - grant: deny
            line: 2
            protocol_options:
              igrp: true
            source:
              address: 198.51.100.0
              netmask: 255.255.255.0
            destination:
              address: 198.51.110.0
              netmask: 255.255.255.0
            time_range: temp
          - grant: deny
            line: 3
            protocol_options:
              tcp: true
            source:
              interface: management
            destination:
              interface: management
              port_protocol:
                eq: www
            log: warnings
          - grant: deny
            line: 4
            protocol_options:
              tcp: true
            source:
              object_group: test_og_network
            destination:
              object_group: test_network_og
              port_protocol:
                eq: www
            log: default
        - name: global_access
          acl_type: extended
          aces:
          - line: 3
            remark: test global access
          - grant: deny
            line: 4
            protocol_options:
              tcp: true
            source:
              any: true
            destination:
              any: true
              port_protocol:
                eq: www
            log: errors
        - name: R1_traffic
          aces:
          - line: 1
            remark: test_v6_acls
          - grant: deny
            line: 2
            protocol_options:
              tcp: true
            source:
              address: 2001:db8:0:3::/64
              port_protocol:
                eq: www
            destination:
              address: 2001:fc8:0:4::/64
              port_protocol:
                eq: telnet
            inactive: true
    state: merged

# Commands fired:
# ---------------
# access-list global_access line 3 remark test global access
# access-list global_access line 4 extended deny tcp any any eq www log errors interval 300
# access-list R1_traffic line 1 remark test_v6_acls
# access-list R1_traffic line 2 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive
# access-list temp_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default
# access-list temp_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp inactive
# access-list temp_access line 2 extended deny tcp interface management interface management
#                         eq www log warnings
# access-list test_access line 3 extended deny tcp object-group test_og_network object-group test_network_og
#                         eq www log default

# After state:
# ------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 remark test global access (hitcnt=0) 0xae78337e
# access-list global_access line 4 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1 remark test_v6_acls
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae
# access-list test_access line 3
#                         extended deny tcp interface management interface management eq www log warnings
#                         interval 300 (hitcnt=0) 0x78aa233d
# access-list test_access line 2 extended deny tcp object-group test_og_network object-group test_network_og
#                         eq www log default (hitcnt=0) 0x477aec1e
#    access-list test_access line 2 extended deny tcp 192.0.2.0 255.255.255.0 host 192.0.3.1 eq www
#                            log default (hitcnt=0) 0xdc7edff8
#    access-list test_access line 2 extended deny tcp 192.0.2.0 255.255.255.0 host 192.0.3.2 eq www
#                            log default (hitcnt=0) 0x7b0e9fde
#    access-list test_access line 2 extended deny tcp 198.51.100.0 255.255.255.0 2001:db8:3::/64 eq www
#                            log default (hitcnt=0) 0x97c75adc

# Using Merged to Rename ACLs
# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 2 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list R1_traffic; 1 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3

- name: Rename ACL with different name using Merged state
  cisco.asa.asa_acls:
    config:
      acls:
        - name: global_access
          rename: global_access_renamed
        - name: R1_traffic
          rename: R1_traffic_renamed
    state: merged

# Commands fired:
# ---------------
# access-list global_access rename global_access_renamed
# access-list R1_traffic rename R1_traffic_renamed

# After state:
# -------------
#
# vasa#sh access-lists
# access-list global_access_renamed; 2 elements; name hash: 0xbd6c87a7
# access-list global_access_renamed line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access_renamed line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list R1_traffic_renamed; 1 elements; name hash: 0xaf40d3c2
# access-list R1_traffic_renamed line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3

# Using replaced

# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

- name: Replaces device configuration of listed acl with provided configuration
  cisco.asa.asa_acls:
    config:
      acls:
        - name: global_access
          acl_type: extended
          aces:
          - grant: deny
            line: 1
            protocol_options:
              tcp: true
            source:
              address: 192.0.4.0
              netmask: 255.255.255.0
              port_protocol:
                eq: telnet
            destination:
              address: 192.0.5.0
              netmask: 255.255.255.0
              port_protocol:
                eq: www
    state: replaced

# Commands fired:
# ---------------
# no access-list global_access line 3 extended deny tcp any any eq www log errors interval 300
# no access-list global_access line 2 extended deny tcp any any eq telnet
# no access-list global_access line 1 extended permit icmp any any log disable
# access-list global_access line 1 extended deny tcp 192.0.4.0 255.255.255.0 eq telnet 192.0.5.0 255.255.255.0 eq www

# After state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 1 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended deny tcp 192.0.4.0 255.255.255.0 eq telnet
#                           192.0.5.0 255.255.255.0 eq www (hitcnt=0) 0x3e5b2757
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

# Using overridden

# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

- name: Override device configuration of all acl with provided configuration
  cisco.asa.asa_acls:
    config:
      acls:
        - name: global_access
          acl_type: extended
          aces:
          - grant: deny
            line: 1
            protocol_options:
              tcp: true
            source:
              address: 192.0.4.0
              netmask: 255.255.255.0
              port_protocol:
                eq: telnet
            destination:
              address: 192.0.5.0
              netmask: 255.255.255.0
              port_protocol:
                eq: www
    state: overridden

# Commands fired:
# ---------------
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 time-range temp
# no access-list temp_access line 1
#                            extended grant deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default
# no access-list R1_traffic line 2
#                           extended grant deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive
# no access-list R1_traffic line 1
#                           extended grant deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www log errors
# no access-list global_access line 3 extended grant deny tcp any any eq www log errors
# no access-list global_access line 2 extended grant deny tcp any any eq telnet
# no access-list global_access line 1 extended grant permit icmp any any log disable
# access-list global_access line 4 extended deny tcp 192.0.4.0 255.255.255.0 eq telnet 192.0.5.0 255.255.255.0 eq www

# After state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 1 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630

# Using Deleted

# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

- name: "Delete module attributes of given acl (Note: This won't delete ALL of the ACLs configured)"
  cisco.asa.asa_acls:
    config:
      acls:
        - name: temp_access
        - name: global_access
    state: deleted

# Commands fired:
# ---------------
# no access-list temp_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                            time-range temp inactive
# no access-list temp_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                            log default
# no access-list global_access line 3 extended deny tcp any any eq www log errors interval 300
# no access-list global_access line 2 extended deny tcp any any eq telnet
# no access-list global_access line 1 extended permit icmp any any log disable

# After state:
# -------------
#
# vasa#sh access-lists
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432

# Using Deleted without any config passed
#"(NOTE: This will delete all of configured resource module attributes)"

# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

- name: 'Delete ALL ACLs in one go (Note: This WILL delete the ALL of configured ACLs)'
  cisco.asa.asa_acls:
    state: deleted

# Commands fired:
# ---------------
# no access-list global_access line 1 extended permit icmp any any log disable
# no access-list global_access line 2 extended deny tcp any any eq telnet
# no access-list global_access line 3 extended deny tcp any any eq www log errors interval 300
# no access-list R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                           log errors interval 300
# no access-list R1_traffic line 2 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive
# no access-list temp_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default
# no access-list temp_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                            time-range temp inactive

# After state:
# -------------
#
# vasa#sh access-lists

# Using Gathered

# Before state:
# -------------
#
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

- name: Gather listed ACLs with provided configurations
  cisco.asa.asa_acls:
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
#                                 "any": true
#                             },
#                             "grant": "permit",
#                             "line": 1,
#                             "log": "disable",
#                             "protocol": "icmp",
#                             "source": {
#                                 "any": true
#                             }
#                         },
#                         {
#                             "destination": {
#                                 "any": true,
#                                 "port_protocol": {
#                                     "eq": "telnet"
#                                 }
#                             },
#                             "grant": "deny",
#                             "line": 2,
#                             "protocol": "tcp",
#                             "protocol_options": {
#                                 "tcp": true
#                             },
#                             "source": {
#                                 "any": true
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "global_access"
#                 },
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "address": "2001:fc8:0:4::/64",
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 }
#                             },
#                             "grant": "deny",
#                             "line": 1,
#                             "log": "errors",
#                             "protocol": "tcp",
#                             "protocol_options": {
#                                 "tcp": true
#                             },
#                             "source": {
#                                 "address": "2001:db8:0:3::/64",
#                                 "port_protocol": {
#                                     "eq": "telnet"
#                                 }
#                             }
#                         },
#                         {
#                             "destination": {
#                                 "address": "2001:fc8:0:4::/64",
#                                 "port_protocol": {
#                                     "eq": "telnet"
#                                 }
#                             },
#                             "grant": "deny",
#                             "inactive": true,
#                             "line": 2,
#                             "protocol": "tcp",
#                             "protocol_options": {
#                                 "tcp": true
#                             },
#                             "source": {
#                                 "address": "2001:db8:0:3::/64",
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 }
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "R1_traffic"
#                 },
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "address": "192.0.3.0",
#                                 "netmask": "255.255.255.0",
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 }
#                             },
#                             "grant": "deny",
#                             "line": 1,
#                             "log": "default",
#                             "protocol": "tcp",
#                             "protocol_options": {
#                                 "tcp": true
#                             },
#                             "source": {
#                                 "address": "192.0.2.0",
#                                 "netmask": "255.255.255.0"
#                             }
#                         },
#                         {
#                             "destination": {
#                                 "address": "198.51.110.0",
#                                 "netmask": "255.255.255.0"
#                             },
#                             "grant": "deny",
#                             "inactive": true,
#                             "line": 2,
#                             "protocol": "igrp",
#                             "protocol_options": {
#                                 "igrp": true
#                             },
#                             "source": {
#                                 "address": "198.51.100.0",
#                                 "netmask": "255.255.255.0"
#                             },
#                             "time_range": "temp"
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "temp_access"
#                 }
#             ]
#         }
#     ]

# Using Rendered

- name: Rendered the provided configuration with the exisiting running configuration
  cisco.asa.asa_acls:
  config:
    acls:
      - name: temp_access
        acl_type: extended
        aces:
        - grant: deny
          line: 1
          protocol_options:
            tcp: true
          source:
            address: 192.0.2.0
            netmask: 255.255.255.0
          destination:
            address: 192.0.3.0
            netmask: 255.255.255.0
            port_protocol:
              eq: www
          log: default
        - grant: deny
          line: 2
          protocol_options:
            igrp: true
          source:
            address: 198.51.100.0
            netmask: 255.255.255.0
          destination:
            address: 198.51.110.0
            netmask: 255.255.255.0
          time_range: temp
      - name: R1_traffic
        aces:
        - grant: deny
          protocol_options:
            tcp: true
          source:
            address: 2001:db8:0:3::/64
            port_protocol:
              eq: www
          destination:
            address: 2001:fc8:0:4::/64
            port_protocol:
              eq: telnet
          inactive: true
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "access-list temp_access line 1
#                                  extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0
#                                  eq www log default"
#         "access-list temp_access line 2
#                                  extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                                  time-range temp"
#         "access-list R1_traffic
#                      deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive"
#     ]

# Using Parsed

# parsed.cfg
#
# access-list test_access; 2 elements; name hash: 0xaf1b712e
# access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default
# access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors
# access-list test_R1_traffic; 1 elements; name hash: 0xaf40d3c2
# access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive

- name: Parse the commands for provided configuration
  cisco.asa.asa_acls:
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
#                                 "address": "192.0.3.0",
#                                 "netmask": "255.255.255.0",
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 }
#                             },
#                             "grant": "deny",
#                             "line": 1,
#                             "log": "default",
#                             "protocol": "tcp",
#                             "protocol_options": {
#                                 "tcp": true
#                             },
#                             "source": {
#                                 "address": "192.0.2.0",
#                                 "netmask": "255.255.255.0"
#                             }
#                         },
#                         {
#                             "destination": {
#                                 "address": "198.51.110.0",
#                                 "netmask": "255.255.255.0"
#                             },
#                             "grant": "deny",
#                             "line": 2,
#                             "log": "errors",
#                             "protocol": "igrp",
#                             "protocol_options": {
#                                 "igrp": true
#                             },
#                             "source": {
#                                 "address": "198.51.100.0",
#                                 "netmask": "255.255.255.0"
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "test_access"
#                 },
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "address": "2001:fc8:0:4::/64",
#                                 "port_protocol": {
#                                     "eq": "telnet"
#                                 }
#                             },
#                             "grant": "deny",
#                             "inactive": true,
#                             "line": 1,
#                             "protocol": "tcp",
#                             "protocol_options": {
#                                 "tcp": true
#                             },
#                             "source": {
#                                 "address": "2001:db8:0:3::/64",
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 }
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "test_R1_TRAFFIC"
#                 }
#             ]
#         }
#     ]
```

## [Return Values](asa_acls_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device  Returned: always  Sample: `["access-list global_access line 1 extended permit icmp any any log disable"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.asa/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.asa)
