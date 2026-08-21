---
collection: kernel
version: "6.8"
title: "Family ovs_flow netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/ovs_flow.html
fetched_at: 2026-08-21T03:49:19+00:00
---
# [Family `ovs_flow` netlink specification](ovs_flow.md#id3)

Contents

- [Family `ovs_flow` netlink specification](ovs_flow.md#family-ovs-flow-netlink-specification)

  - [Summary](ovs_flow.md#summary)
  - [Operations](ovs_flow.md#operations)

    - [get](ovs_flow.md#get)
    - [new](ovs_flow.md#new)
  - [Multicast groups](ovs_flow.md#multicast-groups)
  - [Definitions](ovs_flow.md#definitions)

    - [ovs-header](ovs_flow.md#ovs-header)
    - [ovs-flow-stats](ovs_flow.md#ovs-flow-stats)
    - [ovs-key-ethernet](ovs_flow.md#ovs-key-ethernet)
    - [ovs-key-mpls](ovs_flow.md#ovs-key-mpls)
    - [ovs-key-ipv4](ovs_flow.md#ovs-key-ipv4)
    - [ovs-key-ipv6](ovs_flow.md#ovs-key-ipv6)
    - [ovs-key-ipv6-exthdrs](ovs_flow.md#ovs-key-ipv6-exthdrs)
    - [ovs-frag-type](ovs_flow.md#ovs-frag-type)
    - [ovs-key-tcp](ovs_flow.md#ovs-key-tcp)
    - [ovs-key-udp](ovs_flow.md#ovs-key-udp)
    - [ovs-key-sctp](ovs_flow.md#ovs-key-sctp)
    - [ovs-key-icmp](ovs_flow.md#ovs-key-icmp)
    - [ovs-key-arp](ovs_flow.md#ovs-key-arp)
    - [ovs-key-nd](ovs_flow.md#ovs-key-nd)
    - [ovs-key-ct-tuple-ipv4](ovs_flow.md#ovs-key-ct-tuple-ipv4)
    - [ovs-action-push-vlan](ovs_flow.md#ovs-action-push-vlan)
    - [ovs-ufid-flags](ovs_flow.md#ovs-ufid-flags)
    - [ovs-action-hash](ovs_flow.md#ovs-action-hash)
    - [ovs-hash-alg](ovs_flow.md#ovs-hash-alg)
    - [ovs-action-push-mpls](ovs_flow.md#ovs-action-push-mpls)
    - [ovs-action-add-mpls](ovs_flow.md#ovs-action-add-mpls)
    - [ct-state-flags](ovs_flow.md#ct-state-flags)
  - [Attribute sets](ovs_flow.md#attribute-sets)

    - [flow-attrs](ovs_flow.md#flow-attrs)

      - [key (`nest`)](ovs_flow.md#key-nest)
      - [actions (`nest`)](ovs_flow.md#actions-nest)
      - [stats (`binary`)](ovs_flow.md#stats-binary)
      - [tcp-flags (`u8`)](ovs_flow.md#tcp-flags-u8)
      - [used (`u64`)](ovs_flow.md#used-u64)
      - [clear (`flag`)](ovs_flow.md#clear-flag)
      - [mask (`nest`)](ovs_flow.md#mask-nest)
      - [probe (`binary`)](ovs_flow.md#probe-binary)
      - [ufid (`binary`)](ovs_flow.md#ufid-binary)
      - [ufid-flags (`u32`)](ovs_flow.md#ufid-flags-u32)
      - [pad (`binary`)](ovs_flow.md#pad-binary)
    - [key-attrs](ovs_flow.md#key-attrs)

      - [encap (`nest`)](ovs_flow.md#encap-nest)
      - [priority (`u32`)](ovs_flow.md#priority-u32)
      - [in-port (`u32`)](ovs_flow.md#in-port-u32)
      - [ethernet (`binary`)](ovs_flow.md#ethernet-binary)
      - [vlan (`u16`)](ovs_flow.md#vlan-u16)
      - [ethertype (`u16`)](ovs_flow.md#ethertype-u16)
      - [ipv4 (`binary`)](ovs_flow.md#ipv4-binary)
      - [ipv6 (`binary`)](ovs_flow.md#ipv6-binary)
      - [tcp (`binary`)](ovs_flow.md#tcp-binary)
      - [udp (`binary`)](ovs_flow.md#udp-binary)
      - [icmp (`binary`)](ovs_flow.md#icmp-binary)
      - [icmpv6 (`binary`)](ovs_flow.md#icmpv6-binary)
      - [arp (`binary`)](ovs_flow.md#arp-binary)
      - [nd (`binary`)](ovs_flow.md#nd-binary)
      - [skb-mark (`u32`)](ovs_flow.md#skb-mark-u32)
      - [tunnel (`nest`)](ovs_flow.md#tunnel-nest)
      - [sctp (`binary`)](ovs_flow.md#sctp-binary)
      - [tcp-flags (`u16`)](ovs_flow.md#tcp-flags-u16)
      - [dp-hash (`u32`)](ovs_flow.md#dp-hash-u32)
      - [recirc-id (`u32`)](ovs_flow.md#recirc-id-u32)
      - [mpls (`binary`)](ovs_flow.md#mpls-binary)
      - [ct-state (`u32`)](ovs_flow.md#ct-state-u32)
      - [ct-zone (`u16`)](ovs_flow.md#ct-zone-u16)
      - [ct-mark (`u32`)](ovs_flow.md#ct-mark-u32)
      - [ct-labels (`binary`)](ovs_flow.md#ct-labels-binary)
      - [ct-orig-tuple-ipv4 (`binary`)](ovs_flow.md#ct-orig-tuple-ipv4-binary)
      - [ct-orig-tuple-ipv6 (`binary`)](ovs_flow.md#ct-orig-tuple-ipv6-binary)
      - [nsh (`nest`)](ovs_flow.md#nsh-nest)
      - [packet-type (`u32`)](ovs_flow.md#packet-type-u32)
      - [nd-extensions (`binary`)](ovs_flow.md#nd-extensions-binary)
      - [tunnel-info (`binary`)](ovs_flow.md#tunnel-info-binary)
      - [ipv6-exthdrs (`binary`)](ovs_flow.md#ipv6-exthdrs-binary)
    - [action-attrs](ovs_flow.md#action-attrs)

      - [output (`u32`)](ovs_flow.md#output-u32)
      - [userspace (`nest`)](ovs_flow.md#userspace-nest)
      - [set (`nest`)](ovs_flow.md#set-nest)
      - [push-vlan (`binary`)](ovs_flow.md#push-vlan-binary)
      - [pop-vlan (`flag`)](ovs_flow.md#pop-vlan-flag)
      - [sample (`nest`)](ovs_flow.md#sample-nest)
      - [recirc (`u32`)](ovs_flow.md#recirc-u32)
      - [hash (`binary`)](ovs_flow.md#hash-binary)
      - [push-mpls (`binary`)](ovs_flow.md#push-mpls-binary)
      - [pop-mpls (`u16`)](ovs_flow.md#pop-mpls-u16)
      - [set-masked (`nest`)](ovs_flow.md#set-masked-nest)
      - [ct (`nest`)](ovs_flow.md#ct-nest)
      - [trunc (`u32`)](ovs_flow.md#trunc-u32)
      - [push-eth (`binary`)](ovs_flow.md#push-eth-binary)
      - [pop-eth (`flag`)](ovs_flow.md#pop-eth-flag)
      - [ct-clear (`flag`)](ovs_flow.md#ct-clear-flag)
      - [push-nsh (`nest`)](ovs_flow.md#push-nsh-nest)
      - [pop-nsh (`flag`)](ovs_flow.md#pop-nsh-flag)
      - [meter (`u32`)](ovs_flow.md#meter-u32)
      - [clone (`nest`)](ovs_flow.md#clone-nest)
      - [check-pkt-len (`nest`)](ovs_flow.md#check-pkt-len-nest)
      - [add-mpls (`binary`)](ovs_flow.md#add-mpls-binary)
      - [dec-ttl (`nest`)](ovs_flow.md#dec-ttl-nest)
    - [tunnel-key-attrs](ovs_flow.md#tunnel-key-attrs)

      - [id (`u64`)](ovs_flow.md#id-u64)
      - [ipv4-src (`u32`)](ovs_flow.md#ipv4-src-u32)
      - [ipv4-dst (`u32`)](ovs_flow.md#ipv4-dst-u32)
      - [tos (`u8`)](ovs_flow.md#tos-u8)
      - [ttl (`u8`)](ovs_flow.md#ttl-u8)
      - [dont-fragment (`flag`)](ovs_flow.md#dont-fragment-flag)
      - [csum (`flag`)](ovs_flow.md#csum-flag)
      - [oam (`flag`)](ovs_flow.md#oam-flag)
      - [geneve-opts (`binary`)](ovs_flow.md#geneve-opts-binary)
      - [tp-src (`u16`)](ovs_flow.md#tp-src-u16)
      - [tp-dst (`u16`)](ovs_flow.md#tp-dst-u16)
      - [vxlan-opts (`nest`)](ovs_flow.md#vxlan-opts-nest)
      - [ipv6-src (`binary`)](ovs_flow.md#ipv6-src-binary)
      - [ipv6-dst (`binary`)](ovs_flow.md#ipv6-dst-binary)
      - [pad (`binary`)](ovs_flow.md#id1)
      - [erspan-opts (`binary`)](ovs_flow.md#erspan-opts-binary)
      - [ipv4-info-bridge (`flag`)](ovs_flow.md#ipv4-info-bridge-flag)
    - [check-pkt-len-attrs](ovs_flow.md#check-pkt-len-attrs)

      - [pkt-len (`u16`)](ovs_flow.md#pkt-len-u16)
      - [actions-if-greater (`nest`)](ovs_flow.md#actions-if-greater-nest)
      - [actions-if-less-equal (`nest`)](ovs_flow.md#actions-if-less-equal-nest)
    - [sample-attrs](ovs_flow.md#sample-attrs)

      - [probability (`u32`)](ovs_flow.md#probability-u32)
      - [actions (`nest`)](ovs_flow.md#id2)
    - [userspace-attrs](ovs_flow.md#userspace-attrs)

      - [pid (`u32`)](ovs_flow.md#pid-u32)
      - [userdata (`binary`)](ovs_flow.md#userdata-binary)
      - [egress-tun-port (`u32`)](ovs_flow.md#egress-tun-port-u32)
      - [actions (`flag`)](ovs_flow.md#actions-flag)
    - [ovs-nsh-key-attrs](ovs_flow.md#ovs-nsh-key-attrs)

      - [base (`binary`)](ovs_flow.md#base-binary)
      - [md1 (`binary`)](ovs_flow.md#md1-binary)
      - [md2 (`binary`)](ovs_flow.md#md2-binary)
    - [ct-attrs](ovs_flow.md#ct-attrs)

      - [commit (`flag`)](ovs_flow.md#commit-flag)
      - [zone (`u16`)](ovs_flow.md#zone-u16)
      - [mark (`binary`)](ovs_flow.md#mark-binary)
      - [labels (`binary`)](ovs_flow.md#labels-binary)
      - [helper (`string`)](ovs_flow.md#helper-string)
      - [nat (`nest`)](ovs_flow.md#nat-nest)
      - [force-commit (`flag`)](ovs_flow.md#force-commit-flag)
      - [eventmask (`u32`)](ovs_flow.md#eventmask-u32)
      - [timeout (`string`)](ovs_flow.md#timeout-string)
    - [nat-attrs](ovs_flow.md#nat-attrs)

      - [src (`flag`)](ovs_flow.md#src-flag)
      - [dst (`flag`)](ovs_flow.md#dst-flag)
      - [ip-min (`binary`)](ovs_flow.md#ip-min-binary)
      - [ip-max (`binary`)](ovs_flow.md#ip-max-binary)
      - [proto-min (`u16`)](ovs_flow.md#proto-min-u16)
      - [proto-max (`u16`)](ovs_flow.md#proto-max-u16)
      - [persistent (`flag`)](ovs_flow.md#persistent-flag)
      - [proto-hash (`flag`)](ovs_flow.md#proto-hash-flag)
      - [proto-random (`flag`)](ovs_flow.md#proto-random-flag)
    - [dec-ttl-attrs](ovs_flow.md#dec-ttl-attrs)

      - [action (`nest`)](ovs_flow.md#action-nest)
    - [vxlan-ext-attrs](ovs_flow.md#vxlan-ext-attrs)

      - [gbp (`u32`)](ovs_flow.md#gbp-u32)

## [Summary](ovs_flow.md#id4)

OVS flow configuration over generic netlink.

## [Operations](ovs_flow.md#id5)

### [get](ovs_flow.md#id6)

Get / dump OVS flow configuration and state

value
:   3

attribute-set
:   flow-attrs

do
:   **request**
    :   attributes
        :   [`key`, `ufid`, `ufid-flags`]

    **reply**
    :   attributes
        :   [`key`, `ufid`, `mask`, `stats`, `actions`]

dump
:   **request**
    :   attributes
        :   [`key`, `ufid`, `ufid-flags`]

    **reply**
    :   attributes
        :   [`key`, `ufid`, `mask`, `stats`, `actions`]

### [new](ovs_flow.md#id7)

Create OVS flow configuration in a data path

value
:   1

attribute-set
:   flow-attrs

do
:   **request**
    :   attributes
        :   [`key`, `ufid`, `mask`, `actions`]

## [Multicast groups](ovs_flow.md#id8)

- ovs_flow

## [Definitions](ovs_flow.md#id9)

### [ovs-header](ovs_flow.md#id10)

type
:   struct

doc
:   Header for OVS Generic Netlink messages.

members
:   dp-ifindex
    :   ifindex of local port for datapath (0 to make a request not specificto a datapath).

### [ovs-flow-stats](ovs_flow.md#id11)

type
:   struct

members
:   n-packets
    :   Number of matched packets.

    n-bytes
    :   Number of matched bytes.

### [ovs-key-ethernet](ovs_flow.md#id12)

type
:   struct

members
:   eth-src

    eth-dst

### [ovs-key-mpls](ovs_flow.md#id13)

type
:   struct

members
:   mpls-lse

### [ovs-key-ipv4](ovs_flow.md#id14)

type
:   struct

members
:   ipv4-src

    ipv4-dst

    ipv4-proto

    ipv4-tos

    ipv4-ttl

    ipv4-frag

### [ovs-key-ipv6](ovs_flow.md#id15)

type
:   struct

members
:   ipv6-src

    ipv6-dst

    ipv6-label

    ipv6-proto

    ipv6-tclass

    ipv6-hlimit

    ipv6-frag

### [ovs-key-ipv6-exthdrs](ovs_flow.md#id16)

type
:   struct

members
:   hdrs

### [ovs-frag-type](ovs_flow.md#id17)

name-prefix
:   ovs-frag-type-

enum-name
:   ovs-frag-type

type
:   enum

entries
:   none
    :   Packet is not a fragment.

    first
    :   Packet is a fragment with offset 0.

    later
    :   Packet is a fragment with nonzero offset.

    any

### [ovs-key-tcp](ovs_flow.md#id18)

type
:   struct

members
:   tcp-src

    tcp-dst

### [ovs-key-udp](ovs_flow.md#id19)

type
:   struct

members
:   udp-src

    udp-dst

### [ovs-key-sctp](ovs_flow.md#id20)

type
:   struct

members
:   sctp-src

    sctp-dst

### [ovs-key-icmp](ovs_flow.md#id21)

type
:   struct

members
:   icmp-type

    icmp-code

### [ovs-key-arp](ovs_flow.md#id22)

type
:   struct

members
:   arp-sip

    arp-tip

    arp-op

    arp-sha

    arp-tha

### [ovs-key-nd](ovs_flow.md#id23)

type
:   struct

members
:   nd_target

    nd-sll

    nd-tll

### [ovs-key-ct-tuple-ipv4](ovs_flow.md#id24)

type
:   struct

members
:   ipv4-src

    ipv4-dst

    src-port

    dst-port

    ipv4-proto

### [ovs-action-push-vlan](ovs_flow.md#id25)

type
:   struct

members
:   vlan_tpid
    :   Tag protocol identifier (TPID) to push.

    vlan_tci
    :   Tag control identifier (TCI) to push.

### [ovs-ufid-flags](ovs_flow.md#id26)

name-prefix
:   ovs-ufid-f-

enum-name
:   None

type
:   flags

entries
:   - `omit-key`
    - `omit-mask`
    - `omit-actions`

### [ovs-action-hash](ovs_flow.md#id27)

type
:   struct

members
:   hash-alg
    :   Algorithm used to compute hash prior to recirculation.

    hash-basis
    :   Basis used for computing hash.

### [ovs-hash-alg](ovs_flow.md#id28)

enum-name
:   ovs-hash-alg

type
:   enum

doc
:   Data path hash algorithm for computing Datapath hash. The algorithm type only specifiesthe fields in a flow will be used as part of the hash. Each datapath is free to use itsown hash algorithm. The hash value will be opaque to the user space daemon.

entries
:   - `ovs-hash-alg-l4`

### [ovs-action-push-mpls](ovs_flow.md#id29)

type
:   struct

members
:   mpls-lse
    :   MPLS label stack entry to push

    mpls-ethertype
    :   Ethertype to set in the encapsulating ethernet frame. The only valuesethertype should ever be given are ETH_P_MPLS_UC and ETH_P_MPLS_MC,indicating MPLS unicast or multicast. Other are rejected.

### [ovs-action-add-mpls](ovs_flow.md#id30)

type
:   struct

members
:   mpls-lse
    :   MPLS label stack entry to push

    mpls-ethertype
    :   Ethertype to set in the encapsulating ethernet frame. The only valuesethertype should ever be given are ETH_P_MPLS_UC and ETH_P_MPLS_MC,indicating MPLS unicast or multicast. Other are rejected.

    tun-flags
    :   MPLS tunnel attributes.

### [ct-state-flags](ovs_flow.md#id31)

enum-name
:   None

type
:   flags

name-prefix
:   ovs-cs-f-

entries
:   new
    :   Beginning of a new connection.

    established
    :   Part of an existing connenction

    related
    :   Related to an existing connection.

    reply-dir
    :   Flow is in the reply direction.

    invalid
    :   Could not track the connection.

    tracked
    :   Conntrack has occurred.

    src-nat
    :   Packet's source address/port was mangled by NAT.

    dst-nat
    :   Packet's destination address/port was mangled by NAT.

## [Attribute sets](ovs_flow.md#id32)

### [flow-attrs](ovs_flow.md#id33)

#### [key (`nest`)](ovs_flow.md#id34)

nested-attributes
:   key-attrs

doc
:   Nested attributes specifying the flow key. Always present innotifications. Required for all requests (except dumps).

#### [actions (`nest`)](ovs_flow.md#id35)

nested-attributes
:   action-attrs

doc
:   Nested attributes specifying the actions to take for packets thatmatch the key. Always present in notifications. Required forOVS_FLOW_CMD_NEW requests, optional for OVS_FLOW_CMD_SET requests. AnOVS_FLOW_CMD_SET without OVS_FLOW_ATTR_ACTIONS will not modify theactions. To clear the actions, an OVS_FLOW_ATTR_ACTIONS without anynested attributes must be given.

#### [stats (`binary`)](ovs_flow.md#id36)

struct
:   ovs-flow-stats

doc
:   Statistics for this flow. Present in notifications if the stats wouldbe nonzero. Ignored in requests.

#### [tcp-flags (`u8`)](ovs_flow.md#id37)

doc
:   An 8-bit value giving the ORed value of all of the TCP flags seen onpackets in this flow. Only present in notifications for TCP flows, andonly if it would be nonzero. Ignored in requests.

#### [used (`u64`)](ovs_flow.md#id38)

doc
:   A 64-bit integer giving the time, in milliseconds on the systemmonotonic clock, at which a packet was last processed for thisflow. Only present in notifications if a packet has been processed forthis flow. Ignored in requests.

#### [clear (`flag`)](ovs_flow.md#id39)

doc
:   If present in a OVS_FLOW_CMD_SET request, clears the last-used time,accumulated TCP flags, and statistics for this flow. Otherwiseignored in requests. Never present in notifications.

#### [mask (`nest`)](ovs_flow.md#id40)

nested-attributes
:   key-attrs

doc
:   Nested attributes specifying the mask bits for wildcarded flowmatch. Mask bit value '1' specifies exact match with correspondingflow key bit, while mask bit value '0' specifies a wildcardedmatch. Omitting attribute is treated as wildcarding all correspondingfields. Optional for all requests. If not present, all flow key bitsare exact match bits.

#### [probe (`binary`)](ovs_flow.md#id41)

doc
:   Flow operation is a feature probe, error logging should be suppressed.

#### [ufid (`binary`)](ovs_flow.md#id42)

doc
:   A value between 1-16 octets specifying a unique identifier for theflow. Causes the flow to be indexed by this value rather than thevalue of the OVS_FLOW_ATTR_KEY attribute. Optional for allrequests. Present in notifications if the flow was created with thisattribute.

display-hint
:   uuid

#### [ufid-flags (`u32`)](ovs_flow.md#id43)

enum
:   ovs-ufid-flags

doc
:   A 32-bit value of ORed flags that provide alternative semantics forflow installation and retrieval. Optional for all requests.

#### [pad (`binary`)](ovs_flow.md#id44)

### [key-attrs](ovs_flow.md#id45)

#### [encap (`nest`)](ovs_flow.md#id46)

nested-attributes
:   key-attrs

#### [priority (`u32`)](ovs_flow.md#id47)

#### [in-port (`u32`)](ovs_flow.md#id48)

#### [ethernet (`binary`)](ovs_flow.md#id49)

struct
:   ovs-key-ethernet

doc
:   struct ovs_key_ethernet

#### [vlan (`u16`)](ovs_flow.md#id50)

byte-order
:   big-endian

#### [ethertype (`u16`)](ovs_flow.md#id51)

byte-order
:   big-endian

#### [ipv4 (`binary`)](ovs_flow.md#id52)

struct
:   ovs-key-ipv4

#### [ipv6 (`binary`)](ovs_flow.md#id53)

struct
:   ovs-key-ipv6

doc
:   struct ovs_key_ipv6

#### [tcp (`binary`)](ovs_flow.md#id54)

struct
:   ovs-key-tcp

#### [udp (`binary`)](ovs_flow.md#id55)

struct
:   ovs-key-udp

#### [icmp (`binary`)](ovs_flow.md#id56)

struct
:   ovs-key-icmp

#### [icmpv6 (`binary`)](ovs_flow.md#id57)

struct
:   ovs-key-icmp

#### [arp (`binary`)](ovs_flow.md#id58)

struct
:   ovs-key-arp

doc
:   struct ovs_key_arp

#### [nd (`binary`)](ovs_flow.md#id59)

struct
:   ovs-key-nd

doc
:   struct ovs_key_nd

#### [skb-mark (`u32`)](ovs_flow.md#id60)

#### [tunnel (`nest`)](ovs_flow.md#id61)

nested-attributes
:   tunnel-key-attrs

#### [sctp (`binary`)](ovs_flow.md#id62)

struct
:   ovs-key-sctp

#### [tcp-flags (`u16`)](ovs_flow.md#id63)

byte-order
:   big-endian

#### [dp-hash (`u32`)](ovs_flow.md#id64)

doc
:   Value 0 indicates the hash is not computed by the datapath.

#### [recirc-id (`u32`)](ovs_flow.md#id65)

#### [mpls (`binary`)](ovs_flow.md#id66)

struct
:   ovs-key-mpls

#### [ct-state (`u32`)](ovs_flow.md#id67)

enum
:   ct-state-flags

enum-as-flags
:   True

#### [ct-zone (`u16`)](ovs_flow.md#id68)

doc
:   connection tracking zone

#### [ct-mark (`u32`)](ovs_flow.md#id69)

doc
:   connection tracking mark

#### [ct-labels (`binary`)](ovs_flow.md#id70)

display-hint
:   hex

doc
:   16-octet connection tracking label

#### [ct-orig-tuple-ipv4 (`binary`)](ovs_flow.md#id71)

struct
:   ovs-key-ct-tuple-ipv4

#### [ct-orig-tuple-ipv6 (`binary`)](ovs_flow.md#id72)

doc
:   struct ovs_key_ct_tuple_ipv6

#### [nsh (`nest`)](ovs_flow.md#id73)

nested-attributes
:   ovs-nsh-key-attrs

#### [packet-type (`u32`)](ovs_flow.md#id74)

byte-order
:   big-endian

doc
:   Should not be sent to the kernel

#### [nd-extensions (`binary`)](ovs_flow.md#id75)

doc
:   Should not be sent to the kernel

#### [tunnel-info (`binary`)](ovs_flow.md#id76)

doc
:   struct ip_tunnel_info

#### [ipv6-exthdrs (`binary`)](ovs_flow.md#id77)

struct
:   ovs-key-ipv6-exthdrs

doc
:   struct ovs_key_ipv6_exthdr

### [action-attrs](ovs_flow.md#id78)

#### [output (`u32`)](ovs_flow.md#id79)

doc
:   ovs port number in datapath

#### [userspace (`nest`)](ovs_flow.md#id80)

nested-attributes
:   userspace-attrs

#### [set (`nest`)](ovs_flow.md#id81)

nested-attributes
:   key-attrs

doc
:   Replaces the contents of an existing header. The single nested attribute specifies a header to modify and its value.

#### [push-vlan (`binary`)](ovs_flow.md#id82)

struct
:   ovs-action-push-vlan

doc
:   Push a new outermost 802.1Q or 802.1ad header onto the packet.

#### [pop-vlan (`flag`)](ovs_flow.md#id83)

doc
:   Pop the outermost 802.1Q or 802.1ad header from the packet.

#### [sample (`nest`)](ovs_flow.md#id84)

nested-attributes
:   sample-attrs

doc
:   Probabilistically executes actions, as specified in the nested attributes.

#### [recirc (`u32`)](ovs_flow.md#id85)

doc
:   recirc id

#### [hash (`binary`)](ovs_flow.md#id86)

struct
:   ovs-action-hash

#### [push-mpls (`binary`)](ovs_flow.md#id87)

struct
:   ovs-action-push-mpls

doc
:   Push a new MPLS label stack entry onto the top of the packets MPLSlabel stack. Set the ethertype of the encapsulating frame to eitherETH_P_MPLS_UC or ETH_P_MPLS_MC to indicate the new packet contents.

#### [pop-mpls (`u16`)](ovs_flow.md#id88)

byte-order
:   big-endian

doc
:   ethertype

#### [set-masked (`nest`)](ovs_flow.md#id89)

nested-attributes
:   key-attrs

doc
:   Replaces the contents of an existing header. A nested attributespecifies a header to modify, its value, and a mask. For every bit setin the mask, the corresponding bit value is copied from the value tothe packet header field, rest of the bits are left unchanged. Thenon-masked value bits must be passed in as zeroes. Masking is notsupported for the OVS_KEY_ATTR_TUNNEL attribute.

#### [ct (`nest`)](ovs_flow.md#id90)

nested-attributes
:   ct-attrs

doc
:   Track the connection. Populate the conntrack-related entriesin the flow key.

#### [trunc (`u32`)](ovs_flow.md#id91)

doc
:   struct ovs_action_trunc is a u32 max length

#### [push-eth (`binary`)](ovs_flow.md#id92)

doc
:   struct ovs_action_push_eth

#### [pop-eth (`flag`)](ovs_flow.md#id93)

#### [ct-clear (`flag`)](ovs_flow.md#id94)

#### [push-nsh (`nest`)](ovs_flow.md#id95)

nested-attributes
:   ovs-nsh-key-attrs

doc
:   Push NSH header to the packet.

#### [pop-nsh (`flag`)](ovs_flow.md#id96)

doc
:   Pop the outermost NSH header off the packet.

#### [meter (`u32`)](ovs_flow.md#id97)

doc
:   Run packet through a meter, which may drop the packet, or modify thepacket (e.g., change the DSCP field)

#### [clone (`nest`)](ovs_flow.md#id98)

nested-attributes
:   action-attrs

doc
:   Make a copy of the packet and execute a list of actions withoutaffecting the original packet and key.

#### [check-pkt-len (`nest`)](ovs_flow.md#id99)

nested-attributes
:   check-pkt-len-attrs

doc
:   Check the packet length and execute a set of actions if greater thanthe specified packet length, else execute another set of actions.

#### [add-mpls (`binary`)](ovs_flow.md#id100)

struct
:   ovs-action-add-mpls

doc
:   Push a new MPLS label stack entry at the start of the packet or at thestart of the l3 header depending on the value of l3 tunnel flag in thetun_flags field of this OVS_ACTION_ATTR_ADD_MPLS argument.

#### [dec-ttl (`nest`)](ovs_flow.md#id101)

nested-attributes
:   dec-ttl-attrs

### [tunnel-key-attrs](ovs_flow.md#id102)

#### [id (`u64`)](ovs_flow.md#id103)

byte-order
:   big-endian

value
:   0

#### [ipv4-src (`u32`)](ovs_flow.md#id104)

byte-order
:   big-endian

#### [ipv4-dst (`u32`)](ovs_flow.md#id105)

byte-order
:   big-endian

#### [tos (`u8`)](ovs_flow.md#id106)

#### [ttl (`u8`)](ovs_flow.md#id107)

#### [dont-fragment (`flag`)](ovs_flow.md#id108)

#### [csum (`flag`)](ovs_flow.md#id109)

#### [oam (`flag`)](ovs_flow.md#id110)

#### [geneve-opts (`binary`)](ovs_flow.md#id111)

sub-type
:   u32

#### [tp-src (`u16`)](ovs_flow.md#id112)

byte-order
:   big-endian

#### [tp-dst (`u16`)](ovs_flow.md#id113)

byte-order
:   big-endian

#### [vxlan-opts (`nest`)](ovs_flow.md#id114)

nested-attributes
:   vxlan-ext-attrs

#### [ipv6-src (`binary`)](ovs_flow.md#id115)

doc
:   struct in6_addr source IPv6 address

#### [ipv6-dst (`binary`)](ovs_flow.md#id116)

doc
:   struct in6_addr destination IPv6 address

#### [pad (`binary`)](ovs_flow.md#id117)

#### [erspan-opts (`binary`)](ovs_flow.md#id118)

doc
:   struct erspan_metadata

#### [ipv4-info-bridge (`flag`)](ovs_flow.md#id119)

### [check-pkt-len-attrs](ovs_flow.md#id120)

#### [pkt-len (`u16`)](ovs_flow.md#id121)

#### [actions-if-greater (`nest`)](ovs_flow.md#id122)

nested-attributes
:   action-attrs

#### [actions-if-less-equal (`nest`)](ovs_flow.md#id123)

nested-attributes
:   action-attrs

### [sample-attrs](ovs_flow.md#id124)

#### [probability (`u32`)](ovs_flow.md#id125)

#### [actions (`nest`)](ovs_flow.md#id126)

nested-attributes
:   action-attrs

### [userspace-attrs](ovs_flow.md#id127)

#### [pid (`u32`)](ovs_flow.md#id128)

#### [userdata (`binary`)](ovs_flow.md#id129)

#### [egress-tun-port (`u32`)](ovs_flow.md#id130)

#### [actions (`flag`)](ovs_flow.md#id131)

### [ovs-nsh-key-attrs](ovs_flow.md#id132)

#### [base (`binary`)](ovs_flow.md#id133)

#### [md1 (`binary`)](ovs_flow.md#id134)

#### [md2 (`binary`)](ovs_flow.md#id135)

### [ct-attrs](ovs_flow.md#id136)

#### [commit (`flag`)](ovs_flow.md#id137)

#### [zone (`u16`)](ovs_flow.md#id138)

#### [mark (`binary`)](ovs_flow.md#id139)

#### [labels (`binary`)](ovs_flow.md#id140)

#### [helper (`string`)](ovs_flow.md#id141)

#### [nat (`nest`)](ovs_flow.md#id142)

nested-attributes
:   nat-attrs

#### [force-commit (`flag`)](ovs_flow.md#id143)

#### [eventmask (`u32`)](ovs_flow.md#id144)

#### [timeout (`string`)](ovs_flow.md#id145)

### [nat-attrs](ovs_flow.md#id146)

#### [src (`flag`)](ovs_flow.md#id147)

#### [dst (`flag`)](ovs_flow.md#id148)

#### [ip-min (`binary`)](ovs_flow.md#id149)

#### [ip-max (`binary`)](ovs_flow.md#id150)

#### [proto-min (`u16`)](ovs_flow.md#id151)

#### [proto-max (`u16`)](ovs_flow.md#id152)

#### [persistent (`flag`)](ovs_flow.md#id153)

#### [proto-hash (`flag`)](ovs_flow.md#id154)

#### [proto-random (`flag`)](ovs_flow.md#id155)

### [dec-ttl-attrs](ovs_flow.md#id156)

#### [action (`nest`)](ovs_flow.md#id157)

nested-attributes
:   action-attrs

### [vxlan-ext-attrs](ovs_flow.md#id158)

#### [gbp (`u32`)](ovs_flow.md#id159)
