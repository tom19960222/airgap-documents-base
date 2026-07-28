---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_acls module – ACLs resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_acls_module.html
fetched_at: 2026-07-28T01:38:27+00:00
---
# cisco.nxos.nxos_acls module – ACLs resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_acls`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_acls_module.md#synopsis)
- [Parameters](nxos_acls_module.md#parameters)
- [Notes](nxos_acls_module.md#notes)
- [Examples](nxos_acls_module.md#examples)
- [Return Values](nxos_acls_module.md#return-values)

## [Synopsis](nxos_acls_module.md#id1)

- Manage named IP ACLs on the Cisco NX-OS platform

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: acls

## [Parameters](nxos_acls_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of ACL options. |
| **acls**  list / elements=dictionary | A list of the ACLs. |
| **aces**  list / elements=dictionary | The entries within the ACL. |
| **destination**  dictionary | Specify the packet destination. |
| **address**  string | Destination network address. |
| **any**  boolean | Any destination address.  **Choices:**   - `false` - `true` |
| **host**  string | Host IP address. |
| **port_protocol**  dictionary | Specify the destination port or protocol (only for TCP and UDP). |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Match only packets in the range of port numbers. |
| **end**  string | Specify the end of the port range. |
| **start**  string | Specify the start of the port range. |
| **prefix**  string | Destination network prefix. Only for prefixes of value less than 31 for ipv4 and 127 for ipv6. Prefixes of 32 (ipv4) and 128 (ipv6) should be given in the ‘host’ key. |
| **wildcard_bits**  string | Destination wildcard bits. |
| **dscp**  string | Match packets with given DSCP value. |
| **fragments**  boolean | Check non-initial fragments.  **Choices:**   - `false` - `true` |
| **grant**  string | Action to be applied on the rule.  **Choices:**   - `"permit"` - `"deny"` |
| **log**  boolean | Log matches against this entry.  **Choices:**   - `false` - `true` |
| **precedence**  string | Match packets with given precedence value. |
| **protocol**  string | Specify the protocol. |
| **protocol_options**  dictionary | All possible suboptions for the protocol chosen. |
| **icmp**  dictionary | ICMP protocol options. |
| **administratively_prohibited**  boolean | Administratively prohibited  **Choices:**   - `false` - `true` |
| **alternate_address**  boolean | Alternate address  **Choices:**   - `false` - `true` |
| **conversion_error**  boolean | Datagram conversion  **Choices:**   - `false` - `true` |
| **dod_host_prohibited**  boolean | Host prohibited  **Choices:**   - `false` - `true` |
| **dod_net_prohibited**  boolean | Net prohibited  **Choices:**   - `false` - `true` |
| **echo**  boolean | Echo (ping)  **Choices:**   - `false` - `true` |
| **echo_reply**  boolean | Echo reply  **Choices:**   - `false` - `true` |
| **echo_request**  boolean | Echo request (ping)  **Choices:**   - `false` - `true` |
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
| **time_exceeded**  boolean | All time exceeded.  **Choices:**   - `false` - `true` |
| **timestamp_reply**  boolean | Timestamp replies  **Choices:**   - `false` - `true` |
| **timestamp_request**  boolean | Timestamp requests  **Choices:**   - `false` - `true` |
| **traceroute**  boolean | Traceroute  **Choices:**   - `false` - `true` |
| **ttl_exceeded**  boolean | TTL exceeded  **Choices:**   - `false` - `true` |
| **unreachable**  boolean | All unreachables  **Choices:**   - `false` - `true` |
| **icmpv6**  dictionary | ICMPv6 protocol options. |
| **beyond_scope**  boolean | Destination beyond scope.  **Choices:**   - `false` - `true` |
| **destination_unreachable**  boolean | Destination address is unreachable.  **Choices:**   - `false` - `true` |
| **echo_reply**  boolean | Echo reply.  **Choices:**   - `false` - `true` |
| **echo_request**  boolean | Echo request (ping).  **Choices:**   - `false` - `true` |
| **fragments**  boolean | Check non-initial fragments.  **Choices:**   - `false` - `true` |
| **header**  boolean | Parameter header problem.  **Choices:**   - `false` - `true` |
| **hop_limit**  boolean | Hop limit exceeded in transit.  **Choices:**   - `false` - `true` |
| **mld_query**  boolean | Multicast Listener Discovery Query.  **Choices:**   - `false` - `true` |
| **mld_reduction**  boolean | Multicast Listener Discovery Reduction.  **Choices:**   - `false` - `true` |
| **mld_report**  boolean | Multicast Listener Discovery Report.  **Choices:**   - `false` - `true` |
| **mldv2**  boolean | Multicast Listener Discovery Protocol.  **Choices:**   - `false` - `true` |
| **nd_na**  boolean | Neighbor discovery neighbor advertisements.  **Choices:**   - `false` - `true` |
| **nd_ns**  boolean | Neighbor discovery neighbor solicitations.  **Choices:**   - `false` - `true` |
| **next_header**  boolean | Parameter next header problems.  **Choices:**   - `false` - `true` |
| **no_admin**  boolean | Administration prohibited destination.  **Choices:**   - `false` - `true` |
| **no_route**  boolean | No route to destination.  **Choices:**   - `false` - `true` |
| **packet_too_big**  boolean | Packet too big.  **Choices:**   - `false` - `true` |
| **parameter_option**  boolean | Parameter option problems.  **Choices:**   - `false` - `true` |
| **parameter_problem**  boolean | All parameter problems.  **Choices:**   - `false` - `true` |
| **port_unreachable**  boolean | Port unreachable.  **Choices:**   - `false` - `true` |
| **reassembly_timeout**  boolean | Reassembly timeout.  **Choices:**   - `false` - `true` |
| **renum_command**  boolean | Router renumbering command.  **Choices:**   - `false` - `true` |
| **renum_result**  boolean | Router renumbering result.  **Choices:**   - `false` - `true` |
| **renum_seq_number**  boolean | Router renumbering sequence number reset.  **Choices:**   - `false` - `true` |
| **router_advertisement**  boolean | Neighbor discovery router advertisements.  **Choices:**   - `false` - `true` |
| **router_renumbering**  boolean | All router renumbering.  **Choices:**   - `false` - `true` |
| **router_solicitation**  boolean | Neighbor discovery router solicitations.  **Choices:**   - `false` - `true` |
| **telemetry_path**  boolean | IPT enabled.  **Choices:**   - `false` - `true` |
| **telemetry_queue**  boolean | Flow of interest for BDC/HDC.  **Choices:**   - `false` - `true` |
| **time_exceeded**  boolean | All time exceeded.  **Choices:**   - `false` - `true` |
| **unreachable**  boolean | All unreachable.  **Choices:**   - `false` - `true` |
| **igmp**  dictionary | IGMP protocol options. |
| **dvmrp**  boolean | Distance Vector Multicast Routing Protocol  **Choices:**   - `false` - `true` |
| **host_query**  boolean | Host Query  **Choices:**   - `false` - `true` |
| **host_report**  boolean | Host Report  **Choices:**   - `false` - `true` |
| **tcp**  dictionary | TCP flags. |
| **ack**  boolean | Match on the ACK bit  **Choices:**   - `false` - `true` |
| **established**  boolean | Match established connections  **Choices:**   - `false` - `true` |
| **fin**  boolean | Match on the FIN bit  **Choices:**   - `false` - `true` |
| **psh**  boolean | Match on the PSH bit  **Choices:**   - `false` - `true` |
| **rst**  boolean | Match on the RST bit  **Choices:**   - `false` - `true` |
| **syn**  boolean | Match on the SYN bit  **Choices:**   - `false` - `true` |
| **urg**  boolean | Match on the URG bit  **Choices:**   - `false` - `true` |
| **remark**  string | Access list entry comment. |
| **sequence**  integer | Sequence number. |
| **source**  dictionary | Specify the packet source. |
| **address**  string | Source network address. |
| **any**  boolean | Any source address.  **Choices:**   - `false` - `true` |
| **host**  string | Host IP address. |
| **port_protocol**  dictionary | Specify the destination port or protocol (only for TCP and UDP). |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Match only packets in the range of port numbers. |
| **end**  string | Specify the end of the port range. |
| **start**  string | Specify the start of the port range. |
| **prefix**  string | Source network prefix. Only for prefixes of mask value less than 31 for ipv4 and 127 for ipv6. Prefixes of mask 32 (ipv4) and 128 (ipv6) should be given in the ‘host’ key. |
| **wildcard_bits**  string | Source wildcard bits. |
| **name**  string / required | Name of the ACL. |
| **afi**  string / required | The Address Family Indicator (AFI) for the ACL.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘ip(v6**\* access-list).  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  **Choices:**   - `"deleted"` - `"gathered"` - `"merged"` ← (default) - `"overridden"` - `"rendered"` - `"replaced"` - `"parsed"` |

## [Notes](nxos_acls_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - As NX-OS allows configuring a rule again with different sequence numbers, the user is expected to provide sequence numbers for the access control entries to preserve idempotency. If no sequence number is given, the rule will be added as a new rule by the device.

## [Examples](nxos_acls_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#

- name: Merge new ACLs configuration
  cisco.nxos.nxos_acls:
    config:
    - afi: ipv4
      acls:
      - name: ACL1v4
        aces:
        - grant: deny
          destination:
            address: 192.0.2.64
            wildcard_bits: 0.0.0.255
          source:
            any: true
            port_protocol:
              lt: 55
          protocol: tcp
          protocol_options:
            tcp:
              ack: true
              fin: true
          sequence: 50

    - afi: ipv6
      acls:
      - name: ACL1v6
        aces:
        - grant: permit
          sequence: 10
          source:
            any: true
          destination:
            prefix: 2001:db8:12::/32
          protocol: sctp
    state: merged

# After state:
# ------------
#
# ip access-list ACL1v4
#  50 deny tcp any lt 55 192.0.2.64 0.0.0.255 ack fin
# ipv6 access-list ACL1v6
#  10 permit sctp any any

# Using replaced

# Before state:
# ----------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Replace existing ACL configuration with provided configuration
  cisco.nxos.nxos_acls:
    config:
    - afi: ipv4
    - afi: ipv6
      acls:
      - name: ACL1v6
        aces:
        - sequence: 20
          grant: permit
          source:
            any: true
          destination:
            any: true
          protocol: pip

        - remark: Replaced ACE

      - name: ACL2v6
    state: replaced

# After state:
# ---------------
#
# ipv6 access-list ACL1v6
#   20 permit pip any any
#   30 remark Replaced ACE
# ipv6 access-list ACL2v6

# Using overridden

# Before state:
# ----------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Override existing configuration with provided configuration
  cisco.nxos.nxos_acls:
    config:
    - afi: ipv4
      acls:
      - name: NewACL
        aces:
        - grant: deny
          source:
            address: 192.0.2.0
            wildcard_bits: 0.0.255.255
          destination:
            any: true
          protocol: eigrp
        - remark: Example for overridden state
    state: overridden

# After state:
# ------------
#
# ip access-list NewACL
#   10 deny eigrp 192.0.2.0 0.0.255.255 any
#   20 remark Example for overridden state

# Using deleted:
#
# Before state:
# -------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Delete all ACLs
  cisco.nxos.nxos_acls:
    config:
    state: deleted

# After state:
# -----------
#

# Before state:
# -------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Delete all ACLs in given AFI
  cisco.nxos.nxos_acls:
    config:
    - afi: ipv4
    state: deleted

# After state:
# ------------
#
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

# Before state:
# -------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ipv6 access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ipv6 access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Delete specific ACLs
  cisco.nxos.nxos_acls:
    config:
    - afi: ipv4
      acls:
      - name: ACL1v4
      - name: ACL2v4
    - afi: ipv6
      acls:
      - name: ACL1v6
    state: deleted

# After state:
# ------------
# ipv6 access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

# Using parsed

- name: Parse given config to structured data
  cisco.nxos.nxos_acls:
    running_config: |
      ip access-list ACL1v4
        50 deny tcp any lt 55 192.0.2.64 0.0.0.255 ack fin
      ipv6 access-list ACL1v6
        10 permit sctp any any
    state: parsed

# returns:
# parsed:
# - afi: ipv4
#   acls:
#     - name: ACL1v4
#       aces:
#         - grant: deny
#           destination:
#             address: 192.0.2.64
#             wildcard_bits: 0.0.0.255
#           source:
#             any: true
#             port_protocol:
#               lt: 55
#           protocol: tcp
#           protocol_options:
#             tcp:
#               ack: true
#               fin: true
#           sequence: 50
#
# - afi: ipv6
#   acls:
#     - name: ACL1v6
#       aces:
#         - grant: permit
#           sequence: 10
#           source:
#             any: true
#           destination:
#             prefix: 2001:db8:12::/32
#           protocol: sctp

# Using gathered:

# Before state:
# ------------
#
# ip access-list ACL1v4
#  50 deny tcp any lt 55 192.0.2.64 0.0.0.255 ack fin
# ipv6 access-list ACL1v6
#  10 permit sctp any any

- name: Gather existing configuration
  cisco.nxos.nxos_acls:
    state: gathered

# returns:
# gathered:
# - afi: ipv4
#   acls:
#     - name: ACL1v4
#       aces:
#         - grant: deny
#           destination:
#             address: 192.0.2.64
#             wildcard_bits: 0.0.0.255
#           source:
#             any: true
#             port_protocol:
#               lt: 55
#           protocol: tcp
#           protocol_options:
#             tcp:
#               ack: true
#               fin: true
#           sequence: 50

# - afi: ipv6
#   acls:
#     - name: ACL1v6
#       aces:
#         - grant: permit
#           sequence: 10
#           source:
#             any: true
#           destination:
#             prefix: 2001:db8:12::/32
#           protocol: sctp

# Using rendered

- name: Render required configuration to be pushed to the device
  cisco.nxos.nxos_acls:
    config:
    - afi: ipv4
      acls:
      - name: ACL1v4
        aces:
        - grant: deny
          destination:
            address: 192.0.2.64
            wildcard_bits: 0.0.0.255
          source:
            any: true
            port_protocol:
              lt: 55
          protocol: tcp
          protocol_options:
            tcp:
              ack: true
              fin: true
          sequence: 50

    - afi: ipv6
      acls:
      - name: ACL1v6
        aces:
        - grant: permit
          sequence: 10
          source:
            any: true
          destination:
            prefix: 2001:db8:12::/32
          protocol: sctp
    state: rendered

# returns:
# rendered:
#  ip access-list ACL1v4
#   50 deny tcp any lt 55 192.0.2.64 0.0.0.255 ack fin
#  ipv6 access-list ACL1v6
#   10 permit sctp any any
```

## [Return Values](nxos_acls_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["ip access-list ACL1v4", "10 permit ip any any precedence critical log", "20 deny tcp any lt smtp host 192.0.2.64 ack fin"]` |

### Authors

- Adharsh Srivats Rangarajan (@adharshsrivatsr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
