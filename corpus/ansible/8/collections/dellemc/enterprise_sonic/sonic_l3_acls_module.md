---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_l3_acls module – Manage Layer 3 access control lists (ACL) configurations on SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_l3_acls_module.html
fetched_at: 2026-07-28T02:03:39+00:00
---
# dellemc.enterprise_sonic.sonic_l3_acls module – Manage Layer 3 access control lists (ACL) configurations on SONiC

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_l3_acls`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_l3_acls_module.md#synopsis)
- [Parameters](sonic_l3_acls_module.md#parameters)
- [Examples](sonic_l3_acls_module.md#examples)
- [Return Values](sonic_l3_acls_module.md#return-values)

## [Synopsis](sonic_l3_acls_module.md#id1)

- This module provides configuration management of Layer 3 access control lists (ACL) in devices running SONiC.

## [Parameters](sonic_l3_acls_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies Layer 3 ACL configurations. |
| **acls**  list / elements=dictionary | List of ACL configuration for the given address family. |
| **name**  string / required | Specifies the ACL name. |
| **remark**  string | Specifies remark for the ACL. |
| **rules**  list / elements=dictionary | List of rules with the ACL.  *sequence_num*, *action*, *protocol*, *source* & *destination* are required for adding a new rule.  If *state=deleted*, options other than *sequence_num* are not considered. |
| **action**  string | Specifies the action taken on the matched packet.  **Choices:**   - `"deny"` - `"discard"` - `"do-not-nat"` - `"permit"` - `"transit"` |
| **destination**  dictionary | Specifies the destination of the packet.  *any*, *host* and *prefix* are mutually exclusive. |
| **any**  boolean | Match any destination network address.  **Choices:**   - `false` - `true` |
| **host**  string | Network address of a single destination host. |
| **port_number**  dictionary | Specifies the destination port (valid only for TCP or UDP)  Only one suboption can be specified for port_number in a rule. |
| **eq**  integer | Match packets with destination port equal to the given port number.  The range is from 0 to 65535. |
| **gt**  integer | Match packets with destination port greater than the given port number.  The range is from 0 to 65534. |
| **lt**  integer | Match packets with destination port lesser than the given port number.  The range is from 1 to 65535. |
| **range**  dictionary | Match packets with destination port in the given range.  *begin* and *end* are required together. |
| **begin**  integer | Specifies the beginning of the port range.  The range is from 0 to 65534. |
| **end**  integer | Specifies the end of the port range.  The range is from 1 to 65535. |
| **prefix**  string | Destination network prefix in the format A.B.C.D/mask (ipv4) or A::B/mask (ipv6). |
| **dscp**  dictionary | Match packets using DSCP value.  Only one suboption can be specified for dscp in a rule. |
| **af11**  boolean | Match packets with AF11 DSCP (001010 - Decimal value 10).  **Choices:**   - `false` - `true` |
| **af12**  boolean | Match packets with AF12 DSCP (001100 - Decimal value 12).  **Choices:**   - `false` - `true` |
| **af13**  boolean | Match packets with AF13 DSCP (001110 - Decimal value 14).  **Choices:**   - `false` - `true` |
| **af21**  boolean | Match packets with AF21 DSCP (010010 - Decimal value 18).  **Choices:**   - `false` - `true` |
| **af22**  boolean | Match packets with AF22 DSCP (010100 - Decimal value 20).  **Choices:**   - `false` - `true` |
| **af23**  boolean | Match packets with AF23 DSCP (010110 - Decimal value 22).  **Choices:**   - `false` - `true` |
| **af31**  boolean | Match packets with AF31 DSCP (011010 - Decimal value 26).  **Choices:**   - `false` - `true` |
| **af32**  boolean | Match packets with AF32 DSCP (011100 - Decimal value 28).  **Choices:**   - `false` - `true` |
| **af33**  boolean | Match packets with AF33 DSCP (011110 - Decimal value 30).  **Choices:**   - `false` - `true` |
| **af41**  boolean | Match packets with AF41 DSCP (100010 - Decimal value 34).  **Choices:**   - `false` - `true` |
| **af42**  boolean | Match packets with AF42 DSCP (100100 - Decimal value 36).  **Choices:**   - `false` - `true` |
| **af43**  boolean | Match packets with AF43 DSCP (100110 - Decimal value 38).  **Choices:**   - `false` - `true` |
| **cs1**  boolean | Match packets with CS1 DSCP (001000 - Decimal value 8).  **Choices:**   - `false` - `true` |
| **cs2**  boolean | Match packets with CS2 DSCP (010000 - Decimal value 16).  **Choices:**   - `false` - `true` |
| **cs3**  boolean | Match packets with CS3 DSCP (011000 - Decimal value 24).  **Choices:**   - `false` - `true` |
| **cs4**  boolean | Match packets with CS4 DSCP (100000 - Decimal value 32).  **Choices:**   - `false` - `true` |
| **cs5**  boolean | Match packets with CS5 DSCP (101000 - Decimal value 40).  **Choices:**   - `false` - `true` |
| **cs6**  boolean | Match packets with CS6 DSCP (110000 - Decimal value 48).  **Choices:**   - `false` - `true` |
| **cs7**  boolean | Match packets with CS7 DSCP (111000 - Decimal value 56).  **Choices:**   - `false` - `true` |
| **default**  boolean | Match packets with CS0 DSCP (000000 - Decimal value 0).  **Choices:**   - `false` - `true` |
| **ef**  boolean | Match packets with EF DSCP (101110 - Decimal value 46).  **Choices:**   - `false` - `true` |
| **value**  integer | Match packets with given DSCP value.  The range is from 0 to 63. |
| **voice_admit**  boolean | Match packets with VOICE-ADMIT DSCP (101100 - Decimal value 44).  **Choices:**   - `false` - `true` |
| **protocol**  dictionary | Specifies the protocol to match.  Only one suboption can be specified for protocol in a rule. |
| **name**  string | Match packets with the given protocol.  `ip` - Match any IPv4 packets.  `ipv6` - Match any IPv6 packets.  `icmp` - Match ICMP packets.  `icmpv6` - Match ICMPv6 packets.  `tcp` - Match TCP packets.  `udp` - Match UDP packets.  `ip` and `icmp` are valid only for IPv4 ACLs.  `ipv6` and `icmpv6` are valid only for IPv6 ACLs.  **Choices:**   - `"ip"` - `"ipv6"` - `"icmp"` - `"icmpv6"` - `"tcp"` - `"udp"` |
| **number**  integer | Match packets with given protocol number.  The range is from 0 to 255. |
| **protocol_options**  dictionary | Specifies the additional packet match options for the chosen protocol.  *icmp*, *icmpv6* and *tcp* are mutually exclusive. |
| **icmp**  dictionary | Packet match options for ICMP. |
| **code**  integer | Match packets with given ICMP code.  The range is from 0 to 255. |
| **type**  integer | Match packets with given ICMP type.  The range is from 0 to 255. |
| **icmpv6**  dictionary | Packet match options for ICMPv6. |
| **code**  integer | Match packets with given ICMPv6 code.  The range is from 0 to 255. |
| **type**  integer | Match packets with given ICMPv6 type.  The range is from 0 to 255. |
| **tcp**  dictionary | Packet match options for TCP.  *established* and other TCP flag options are mutually exclusive. |
| **ack**  boolean | Match packets with ACK flag set.  **Choices:**   - `false` - `true` |
| **established**  boolean | Match packets which are part of established TCP session.  **Choices:**   - `false` - `true` |
| **fin**  boolean | Match packets with FIN flag set.  **Choices:**   - `false` - `true` |
| **not_ack**  boolean | Match packets with ACK flag cleared.  **Choices:**   - `false` - `true` |
| **not_fin**  boolean | Match packets with FIN flag cleared.  **Choices:**   - `false` - `true` |
| **not_psh**  boolean | Match packets with PSH flag cleared.  **Choices:**   - `false` - `true` |
| **not_rst**  boolean | Match packets with RST flag cleared.  **Choices:**   - `false` - `true` |
| **not_syn**  boolean | Match packets with SYN flag cleared.  **Choices:**   - `false` - `true` |
| **not_urg**  boolean | Match packets with URG flag cleared.  **Choices:**   - `false` - `true` |
| **psh**  boolean | Match packets with PSH flag set.  **Choices:**   - `false` - `true` |
| **rst**  boolean | Match packets with RST flag set.  **Choices:**   - `false` - `true` |
| **syn**  boolean | Match packets with SYN flag set.  **Choices:**   - `false` - `true` |
| **urg**  boolean | Match packets with URG flag set.  **Choices:**   - `false` - `true` |
| **remark**  string | Specifies remark for the ACL rule. |
| **sequence_num**  integer / required | Specifies the sequence number of the rule.  The range is from 1 to 65535. |
| **source**  dictionary | Specifies the source of the packet.  *any*, *host* and *prefix* are mutually exclusive. |
| **any**  boolean | Match any source network address.  **Choices:**   - `false` - `true` |
| **host**  string | Network address of a single source host. |
| **port_number**  dictionary | Specifies the source port (valid only for TCP or UDP)  Only one suboption can be specified for port_number in a rule. |
| **eq**  integer | Match packets with source port equal to the given port number.  The range is from 0 to 65535. |
| **gt**  integer | Match packets with source port greater than the given port number.  The range is from 0 to 65534. |
| **lt**  integer | Match packets with source port lesser than the given port number.  The range is from 1 to 65535. |
| **range**  dictionary | Match packets with source port in the given range.  *begin* and *end* are required together. |
| **begin**  integer | Specifies the beginning of the port range.  The range is from 0 to 65534. |
| **end**  integer | Specifies the end of the port range.  The range is from 1 to 65535. |
| **prefix**  string | Source network prefix in the format A.B.C.D/mask (ipv4) or A::B/mask (ipv6). |
| **vlan_id**  integer | Match packets with the given VLAN ID value. |
| **address_family**  string / required | Specifies the address family of the ACLs.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **state**  string | The state of the configuration after module completion.  `merged` - Merges provided L3 ACL configuration with on-device configuration.  `replaced` - Replaces on-device configuration of the specified L3 ACLs with provided configuration.  `overridden` - Overrides all on-device L3 ACL configurations with the provided configuration.  `deleted` - Deletes on-device L3 ACL configuration.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Examples](sonic_l3_acls_module.md#id3)

```yaml+jinja
# Using merged
#
# Before State:
# -------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test
#  seq 1 permit ip host 192.168.1.2 any
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit ipv6 host 192:168:1::2 any
# sonic#

  - name: Merge provided Layer 3 ACL configurations
    dellemc.enterprise_sonic.sonic_l3_acls:
      config:
        - address_family: 'ipv4'
          acls:
          - name: 'test'
            rules:
            - sequence_num: 2
              action: 'permit'
              protocol:
                name: 'icmp'
              source:
                any: true
              destination:
                host: '192.168.1.2'
              protocol_options:
                icmp:
                  type: 8
            - sequence_num: 3
              action: 'deny'
              protocol:
                number: 2
              source:
                any: true
              destination:
                any: true
            - sequence_num: 4
              action: 'deny'
              protocol:
                name: 'ip'
              source:
                any: true
              destination:
                any: true
              vlan_id: 10
              remark: 'Vlan10'
          - name: 'test1'
            remark: 'test_ip_acl'
            rules:
            - sequence_num: 1
              action: 'permit'
              protocol:
                name: 'tcp'
              source:
                prefix: '10.0.0.0/8'
              destination:
                any: true
            - sequence_num: 2
              action: 'deny'
              protocol:
                name: 'udp'
              source:
                any: true
              destination:
                prefix: '20.1.0.0/16'
                port_number:
                  gt: 1024
            - sequence_num: 3
              action: 'deny'
              protocol:
                name: 'ip'
              source:
                any: true
              destination:
                any: true
              dscp:
                value: 63
        - address_family: 'ipv6'
          acls:
          - name: 'testv6'
            rules:
            - sequence_num: 2
              action: 'deny'
              protocol:
                name: 'icmpv6'
              source:
                any: true
              destination:
                any: true
          - name: 'testv6-1'
            remark: 'test_ipv6_acl'
            rules:
            - sequence_num: 1
              action: 'permit'
              protocol:
                name: 'ipv6'
              source:
                prefix: '1000::/16'
              destination:
                any: true
              dscp:
                af22: true
            - sequence_num: 2
              action: 'deny'
              protocol:
                name: 'tcp'
              source:
                any: true
              destination:
                prefix: '2000::1000:0/112'
                port_number:
                  range:
                    begin: 100
                    end: 1000
            - sequence_num: 3
              action: 'permit'
              protocol:
                name: 'tcp'
              source:
                any: true
              destination:
                any: true
              protocol_options:
                tcp:
                  established: true
            - sequence_num: 4
              action: 'deny'
              protocol:
                name: 'udp'
              source:
                any: true
                port_number:
                  eq: 3000
              destination:
                any: true
      state: merged

# After State:
# ------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test
#  seq 1 permit ip host 192.168.1.2 any
#  seq 2 permit icmp any host 192.168.1.2 type 8
#  seq 3 deny 2 any any
#  seq 4 deny ip any any vlan 10 remark Vlan10
# !
# ip access-list test1
#  remark test_ip_acl
#  seq 1 permit tcp 10.0.0.0/8 any
#  seq 2 deny udp any 20.1.0.0/16 gt 1024
#  seq 3 deny ip any any dscp 63
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit ipv6 host 192:168:1::2 any
#  seq 2 deny icmpv6 any any
# !
# ipv6 access-list testv6-1
#  remark test_ipv6_acl
#  seq 1 permit ipv6 1000::/16 any dscp af22
#  seq 2 deny tcp any 2000::1000:0/112 range 100 1000
#  seq 3 permit tcp any any established
#  seq 4 deny udp any eq 3000 any
# sonic#

# Using replaced
#
# Before State:
# -------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test
#  seq 1 permit ip host 192.168.1.2 any
#  seq 2 permit icmp any host 192.168.1.2 type 8
#  seq 3 deny 2 any any
#  seq 4 deny ip any any vlan 10 remark Vlan10
# !
# ip access-list test1
#  remark test_ip_acl
#  seq 1 permit tcp 10.0.0.0/8 any
#  seq 2 deny udp any 20.1.0.0/16 gt 1024
#  seq 3 deny ip any any dscp 63
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit tcp host 3000::1 any established
#  seq 2 permit udp any any
#  seq 3 deny icmpv6 any any
# !
# ipv6 access-list testv6-1
#  remark test_ipv6_acl
#  seq 1 permit ipv6 1000::/16 any dscp af22
#  seq 2 deny tcp any 2000::1000:0/112 range 100 1000
#  seq 3 permit tcp any any established
#  seq 4 deny udp any eq 3000 any
# sonic#

  - name: Replace device configuration of specified Layer 3 ACLs with provided configuration
    dellemc.enterprise_sonic.sonic_l3_acls:
      config:
        - address_family: 'ipv4'
          acls:
          - name: 'test2'
            rules:
            - sequence_num: 1
              action: 'permit'
              protocol:
                name: 'tcp'
              source:
                prefix: '192.168.1.0/24'
              destination:
                any: true
        - address_family: 'ipv6'
          acls:
          - name: 'testv6'
            rules:
            - sequence_num: 1
              action: 'permit'
              protocol:
                name: 'tcp'
              source:
                host: '3000::1'
              destination:
                any: true
              protocol_options:
                tcp:
                  ack: true
                  syn: true
                  fin: true
            - sequence_num: 2
              action: 'deny'
              protocol:
                name: 'ipv6'
              source:
                any: true
              destination:
                any: true
      state: replaced

# After State:
# ------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test
#  seq 1 permit ip host 192.168.1.2 any
#  seq 2 permit icmp any host 192.168.1.3 type 8
#  seq 3 deny 2 any any
#  seq 4 deny ip any any vlan 10 remark Vlan10
# !
# ip access-list test1
#  remark test_ip_acl
#  seq 1 permit tcp 10.0.0.0/8 any
#  seq 2 deny udp any 20.1.0.0/16 gt 1024
#  seq 3 deny ip any any dscp 63
# !
# ip access-list test2
#  seq 1 permit tcp 192.168.1.0/24 any
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit tcp host 3000::1 any fin syn ack
#  seq 2 deny ipv6 any any
# !
# ipv6 access-list testv6-1
#  remark test_ipv6_acl
#  seq 1 permit ipv6 1000::/16 any dscp af22
#  seq 2 deny tcp any 2000::1000:0/112 range 100 1000
#  seq 3 permit tcp any any established
#  seq 4 deny udp any eq 3000 any
# sonic#

# Using overridden
#
# Before State:
# -------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test
#  seq 1 permit ip host 192.168.1.2 any
#  seq 2 permit icmp any host 192.168.1.3 type 8
#  seq 3 deny 2 any any
#  seq 4 deny ip any any vlan 10 remark Vlan10
# !
# ip access-list test1
#  remark test_ip_acl
#  seq 1 permit tcp 10.0.0.0/8 any
#  seq 2 deny udp any 20.1.0.0/16 gt 1024
#  seq 3 deny ip any any dscp 63
# !
# ip access-list test2
#  seq 1 permit tcp 192.168.1.0/24 any
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit tcp 3000::/16 any
#  seq 2 deny ipv6 any any
# !
# ipv6 access-list testv6-1
#  remark test_ipv6_acl
#  seq 1 permit ipv6 1000::/16 any dscp af22
#  seq 2 deny tcp any 2000::1000:0/112 range 100 1000
#  seq 3 permit tcp any any established
#  seq 4 deny udp any eq 3000 any
# sonic#

  - name: Override device configuration of all Layer 3 ACLs with provided configuration
    dellemc.enterprise_sonic.sonic_l3_acls:
      config:
        - address_family: 'ipv4'
          acls:
          - name: 'test_acl'
            rules:
            - sequence_num: 1
              action: 'permit'
              protocol:
                name: 'ip'
              source:
                prefix: '100.1.1.0/24'
              destination:
                prefix: '100.1.2.0/24'
            - sequence_num: 2
              action: 'deny'
              protocol:
                name: 'udp'
              source:
                any: true
              destination:
                any: true
      state: overridden

# After State:
# ------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test_acl
#  seq 1 permit ip 100.1.1.0/24 100.1.2.0/24
#  seq 2 deny udp any any
# sonic#
# sonic# show running-configuration ipv6 access-list
# sonic#

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test
#  seq 1 permit ip host 192.168.1.2 any
#  seq 2 permit icmp any host 192.168.1.3 type 8
#  seq 3 deny 2 any any
#  seq 4 deny ip any any vlan 10 remark Vlan10
# !
# ip access-list test1
#  remark test_ip_acl
#  seq 1 permit tcp 10.0.0.0/8 any
#  seq 2 deny udp any 20.1.0.0/16 gt 1024
#  seq 3 deny ip any any dscp 63
# !
# ip access-list test2
#  seq 1 permit tcp 192.168.1.0/24 any
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit tcp 3000::/16 any
#  seq 2 deny ipv6 any any
# !
# ipv6 access-list testv6-1
#  remark test_ipv6_acl
#  seq 1 permit ipv6 1000::/16 any dscp af22
#  seq 2 deny tcp any 2000::1000:0/112 range 100 1000
#  seq 3 permit tcp any any established
#  seq 4 deny udp any eq 3000 any
# sonic#

  - name: Delete specified Layer 3 ACLs, ACL remark and ACL rule entries
    dellemc.enterprise_sonic.sonic_l3_acls:
      config:
        - address_family: 'ipv4'
          acls:
          - name: 'test'
            rules:
              - sequence_num: 2
          - name: 'test2'
        - address_family: 'ipv6'
          acls:
          - name: 'testv6-1'
            remark: 'test_ipv6_acl'
            rules:
              - sequence_num: 3
      state: deleted

# After State:
# ------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test
#  seq 1 permit ip host 192.168.1.2 any
#  seq 3 deny 2 any any
#  seq 4 deny ip any any vlan 10 remark Vlan10
# !
# ip access-list test1
#  remark test_ip_acl
#  seq 1 permit tcp 10.0.0.0/8 any
#  seq 2 deny udp any 20.1.0.0/16 gt 1024
#  seq 3 deny ip any any dscp 63
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit tcp 3000::/16 any
#  seq 2 deny ipv6 any any
# !
# ipv6 access-list testv6-1
#  seq 1 permit ipv6 1000::/16 any dscp af22
#  seq 2 deny tcp any 2000::1000:0/112 range 100 1000
#  seq 4 deny udp any eq 3000 any
# sonic#

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test
#  seq 1 permit ip host 192.168.1.2 any
#  seq 2 permit icmp any host 192.168.1.3 type 8
#  seq 3 deny 2 any any
#  seq 4 deny ip any any vlan 10 remark Vlan10
# !
# ip access-list test1
#  remark test_ip_acl
#  seq 1 permit tcp 10.0.0.0/8 any
#  seq 2 deny udp any 20.1.0.0/16 gt 1024
#  seq 3 deny ip any any dscp 63
# !
# ip access-list test2
#  seq 1 permit tcp 192.168.1.0/24 any
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit tcp 3000::/16 any
#  seq 2 deny ipv6 any any
# !
# ipv6 access-list testv6-1
#  remark test_ipv6_acl
#  seq 1 permit ipv6 1000::/16 any dscp af22
#  seq 2 deny tcp any 2000::1000:0/112 range 100 1000
#  seq 3 permit tcp any any established
#  seq 4 deny udp any eq 3000 any
# sonic#

  - name: Delete all Layer 3 ACLs for an address-family
    dellemc.enterprise_sonic.sonic_l3_acls:
      config:
        - address_family: 'ipv4'
      state: deleted

# After State:
# ------------
#
# sonic# show running-configuration ip access-list
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit tcp 3000::/16 any
#  seq 2 deny ipv6 any any
# !
# ipv6 access-list testv6-1
#  remark test_ipv6_acl
#  seq 1 permit ipv6 1000::/16 any dscp af22
#  seq 2 deny tcp any 2000::1000:0/112 range 100 1000
#  seq 3 permit tcp any any established
#  seq 4 deny udp any eq 3000 any
# sonic#

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration ip access-list
# !
# ip access-list test
#  seq 1 permit ip host 192.168.1.2 any
#  seq 2 permit icmp any host 192.168.1.3 type 8
#  seq 3 deny 2 any any
#  seq 4 deny ip any any vlan 10 remark Vlan10
# !
# ip access-list test1
#  remark test_ip_acl
#  seq 1 permit tcp 10.0.0.0/8 any
#  seq 2 deny udp any 20.1.0.0/16 gt 1024
#  seq 3 deny ip any any dscp 63
# !
# ip access-list test2
#  seq 1 permit tcp 192.168.1.0/24 any
# sonic#
# sonic# show running-configuration ipv6 access-list
# !
# ipv6 access-list testv6
#  seq 1 permit tcp 3000::/16 any
#  seq 2 deny ipv6 any any
# !
# ipv6 access-list testv6-1
#  remark test_ipv6_acl
#  seq 1 permit ipv6 1000::/16 any dscp af22
#  seq 2 deny tcp any 2000::1000:0/112 range 100 1000
#  seq 3 permit tcp any any established
#  seq 4 deny udp any eq 3000 any
# sonic#

  - name: Delete all Layer 3 ACL configurations
    dellemc.enterprise_sonic.sonic_l3_acls:
      config:
      state: deleted

# After State:
# ------------
#
# sonic# show running-configuration ip access-list
# sonic#
# sonic# show running-configuration ipv6 access-list
# sonic#
```

## [Return Values](sonic_l3_acls_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Arun Saravanan Balachandran (@ArunSaravananBalachandran)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
