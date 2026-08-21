---
collection: kernel
version: "6.8"
title: "Family mptcp_pm netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/mptcp_pm.html
fetched_at: 2026-08-21T03:49:17+00:00
---
# [Family `mptcp_pm` netlink specification](mptcp_pm.md#id9)

Contents

- [Family `mptcp_pm` netlink specification](mptcp_pm.md#family-mptcp-pm-netlink-specification)

  - [Summary](mptcp_pm.md#summary)
  - [Operations](mptcp_pm.md#operations)

    - [unspec](mptcp_pm.md#unspec)
    - [add-addr](mptcp_pm.md#add-addr)
    - [del-addr](mptcp_pm.md#del-addr)
    - [get-addr](mptcp_pm.md#get-addr)
    - [flush-addrs](mptcp_pm.md#flush-addrs)
    - [set-limits](mptcp_pm.md#set-limits)
    - [get-limits](mptcp_pm.md#get-limits)
    - [set-flags](mptcp_pm.md#set-flags)
    - [announce](mptcp_pm.md#announce)
    - [remove](mptcp_pm.md#remove)
    - [subflow-create](mptcp_pm.md#subflow-create)
    - [subflow-destroy](mptcp_pm.md#subflow-destroy)
  - [Definitions](mptcp_pm.md#definitions)

    - [event-type](mptcp_pm.md#event-type)
  - [Attribute sets](mptcp_pm.md#attribute-sets)

    - [address](mptcp_pm.md#address)

      - [unspec (`unused`)](mptcp_pm.md#unspec-unused)
      - [family (`u16`)](mptcp_pm.md#family-u16)
      - [id (`u8`)](mptcp_pm.md#id-u8)
      - [addr4 (`u32`)](mptcp_pm.md#addr4-u32)
      - [addr6 (`binary`)](mptcp_pm.md#addr6-binary)
      - [port (`u16`)](mptcp_pm.md#port-u16)
      - [flags (`u32`)](mptcp_pm.md#flags-u32)
      - [if-idx (`s32`)](mptcp_pm.md#if-idx-s32)
    - [subflow-attribute](mptcp_pm.md#subflow-attribute)

      - [unspec (`unused`)](mptcp_pm.md#id1)
      - [token-rem (`u32`)](mptcp_pm.md#token-rem-u32)
      - [token-loc (`u32`)](mptcp_pm.md#token-loc-u32)
      - [relwrite-seq (`u32`)](mptcp_pm.md#relwrite-seq-u32)
      - [map-seq (`u64`)](mptcp_pm.md#map-seq-u64)
      - [map-sfseq (`u32`)](mptcp_pm.md#map-sfseq-u32)
      - [ssn-offset (`u32`)](mptcp_pm.md#ssn-offset-u32)
      - [map-datalen (`u16`)](mptcp_pm.md#map-datalen-u16)
      - [flags (`u32`)](mptcp_pm.md#id2)
      - [id-rem (`u8`)](mptcp_pm.md#id-rem-u8)
      - [id-loc (`u8`)](mptcp_pm.md#id-loc-u8)
      - [pad (`pad`)](mptcp_pm.md#pad-pad)
    - [endpoint](mptcp_pm.md#endpoint)

      - [addr (`nest`)](mptcp_pm.md#addr-nest)
    - [attr](mptcp_pm.md#attr)

      - [unspec (`unused`)](mptcp_pm.md#id3)
      - [addr (`nest`)](mptcp_pm.md#id4)
      - [rcv-add-addrs (`u32`)](mptcp_pm.md#rcv-add-addrs-u32)
      - [subflows (`u32`)](mptcp_pm.md#subflows-u32)
      - [token (`u32`)](mptcp_pm.md#token-u32)
      - [loc-id (`u8`)](mptcp_pm.md#loc-id-u8)
      - [addr-remote (`nest`)](mptcp_pm.md#addr-remote-nest)
    - [event-attr](mptcp_pm.md#event-attr)

      - [unspec (`unused`)](mptcp_pm.md#id5)
      - [token (`u32`)](mptcp_pm.md#id6)
      - [family (`u16`)](mptcp_pm.md#id7)
      - [loc-id (`u8`)](mptcp_pm.md#id8)
      - [rem-id (`u8`)](mptcp_pm.md#rem-id-u8)
      - [saddr4 (`u32`)](mptcp_pm.md#saddr4-u32)
      - [saddr6 (`binary`)](mptcp_pm.md#saddr6-binary)
      - [daddr4 (`u32`)](mptcp_pm.md#daddr4-u32)
      - [daddr6 (`binary`)](mptcp_pm.md#daddr6-binary)
      - [sport (`u16`)](mptcp_pm.md#sport-u16)
      - [dport (`u16`)](mptcp_pm.md#dport-u16)
      - [backup (`u8`)](mptcp_pm.md#backup-u8)
      - [error (`u8`)](mptcp_pm.md#error-u8)
      - [flags (`u16`)](mptcp_pm.md#flags-u16)
      - [timeout (`u32`)](mptcp_pm.md#timeout-u32)
      - [if_idx (`u32`)](mptcp_pm.md#if-idx-u32)
      - [reset-reason (`u32`)](mptcp_pm.md#reset-reason-u32)
      - [reset-flags (`u32`)](mptcp_pm.md#reset-flags-u32)
      - [server-side (`u8`)](mptcp_pm.md#server-side-u8)

## [Summary](mptcp_pm.md#id10)

Multipath TCP.

## [Operations](mptcp_pm.md#id11)

### [unspec](mptcp_pm.md#id12)

unused

value
:   0

### [add-addr](mptcp_pm.md#id13)

Add endpoint

attribute-set
:   endpoint

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`addr`]

### [del-addr](mptcp_pm.md#id14)

Delete endpoint

attribute-set
:   endpoint

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`addr`]

### [get-addr](mptcp_pm.md#id15)

Get endpoint information

attribute-set
:   endpoint

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`addr`]

    **reply**
    :   attributes
        :   [`addr`]

dump
:   **reply**
    :   attributes
        :   [`addr`]

### [flush-addrs](mptcp_pm.md#id16)

flush addresses

attribute-set
:   endpoint

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`addr`]

### [set-limits](mptcp_pm.md#id17)

Set protocol limits

attribute-set
:   attr

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`rcv-add-addrs`, `subflows`]

### [get-limits](mptcp_pm.md#id18)

Get protocol limits

attribute-set
:   attr

dont-validate
:   ['strict']

do
:   **request**
    :   attributes
        :   [`rcv-add-addrs`, `subflows`]

    **reply**
    :   attributes
        :   [`rcv-add-addrs`, `subflows`]

### [set-flags](mptcp_pm.md#id19)

Change endpoint flags

attribute-set
:   attr

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`addr`, `token`, `addr-remote`]

### [announce](mptcp_pm.md#id20)

announce new sf

attribute-set
:   attr

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`addr`, `token`]

### [remove](mptcp_pm.md#id21)

announce removal

attribute-set
:   attr

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`token`, `loc-id`]

### [subflow-create](mptcp_pm.md#id22)

todo

attribute-set
:   attr

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`addr`, `token`, `addr-remote`]

### [subflow-destroy](mptcp_pm.md#id23)

todo

attribute-set
:   attr

dont-validate
:   ['strict']

flags
:   ['uns-admin-perm']

do
:   **request**
    :   attributes
        :   [`addr`, `token`, `addr-remote`]

## [Definitions](mptcp_pm.md#id24)

### [event-type](mptcp_pm.md#id25)

type
:   enum

enum-name
:   mptcp-event-type

name-prefix
:   mptcp-event-

entries
:   unspec
    :   unused event

    created
    :   token, family, saddr4 | saddr6, daddr4 | daddr6, sport, dport A new MPTCP connection has been created. It is the good time to allocate memory and send ADD_ADDR if needed. Depending on the traffic-patterns it can take a long time until the MPTCP_EVENT_ESTABLISHED is sent.

    established
    :   token, family, saddr4 | saddr6, daddr4 | daddr6, sport, dport A MPTCP connection is established (can start new subflows).

    closed
    :   token A MPTCP connection has stopped.

    announced
    :   token, rem_id, family, daddr4 | daddr6 [, dport] A new address has been announced by the peer.

    removed
    :   token, rem_id An address has been lost by the peer.

    sub-established
    :   token, family, loc_id, rem_id, saddr4 | saddr6, daddr4 | daddr6, sport, dport, backup, if_idx [, error] A new subflow has been established. 'error' should not be set.

    sub-closed
    :   token, family, loc_id, rem_id, saddr4 | saddr6, daddr4 | daddr6, sport, dport, backup, if_idx [, error] A subflow has been closed. An error (copy of sk_err) could be set if an error has been detected for this subflow.

    sub-priority
    :   token, family, loc_id, rem_id, saddr4 | saddr6, daddr4 | daddr6, sport, dport, backup, if_idx [, error] The priority of a subflow has changed. 'error' should not be set.

    listener-created
    :   family, sport, saddr4 | saddr6 A new PM listener is created.

    listener-closed
    :   family, sport, saddr4 | saddr6 A PM listener is closed.

## [Attribute sets](mptcp_pm.md#id26)

### [address](mptcp_pm.md#id27)

#### [unspec (`unused`)](mptcp_pm.md#id28)

value
:   0

#### [family (`u16`)](mptcp_pm.md#id29)

#### [id (`u8`)](mptcp_pm.md#id30)

#### [addr4 (`u32`)](mptcp_pm.md#id31)

byte-order
:   big-endian

#### [addr6 (`binary`)](mptcp_pm.md#id32)

#### [port (`u16`)](mptcp_pm.md#id33)

byte-order
:   big-endian

#### [flags (`u32`)](mptcp_pm.md#id34)

#### [if-idx (`s32`)](mptcp_pm.md#id35)

### [subflow-attribute](mptcp_pm.md#id36)

#### [unspec (`unused`)](mptcp_pm.md#id37)

value
:   0

#### [token-rem (`u32`)](mptcp_pm.md#id38)

#### [token-loc (`u32`)](mptcp_pm.md#id39)

#### [relwrite-seq (`u32`)](mptcp_pm.md#id40)

#### [map-seq (`u64`)](mptcp_pm.md#id41)

#### [map-sfseq (`u32`)](mptcp_pm.md#id42)

#### [ssn-offset (`u32`)](mptcp_pm.md#id43)

#### [map-datalen (`u16`)](mptcp_pm.md#id44)

#### [flags (`u32`)](mptcp_pm.md#id45)

#### [id-rem (`u8`)](mptcp_pm.md#id46)

#### [id-loc (`u8`)](mptcp_pm.md#id47)

#### [pad (`pad`)](mptcp_pm.md#id48)

### [endpoint](mptcp_pm.md#id49)

#### [addr (`nest`)](mptcp_pm.md#id50)

nested-attributes
:   address

### [attr](mptcp_pm.md#id51)

#### [unspec (`unused`)](mptcp_pm.md#id52)

value
:   0

#### [addr (`nest`)](mptcp_pm.md#id53)

nested-attributes
:   address

#### [rcv-add-addrs (`u32`)](mptcp_pm.md#id54)

#### [subflows (`u32`)](mptcp_pm.md#id55)

#### [token (`u32`)](mptcp_pm.md#id56)

#### [loc-id (`u8`)](mptcp_pm.md#id57)

#### [addr-remote (`nest`)](mptcp_pm.md#id58)

nested-attributes
:   address

### [event-attr](mptcp_pm.md#id59)

#### [unspec (`unused`)](mptcp_pm.md#id60)

value
:   0

#### [token (`u32`)](mptcp_pm.md#id61)

#### [family (`u16`)](mptcp_pm.md#id62)

#### [loc-id (`u8`)](mptcp_pm.md#id63)

#### [rem-id (`u8`)](mptcp_pm.md#id64)

#### [saddr4 (`u32`)](mptcp_pm.md#id65)

byte-order
:   big-endian

#### [saddr6 (`binary`)](mptcp_pm.md#id66)

#### [daddr4 (`u32`)](mptcp_pm.md#id67)

byte-order
:   big-endian

#### [daddr6 (`binary`)](mptcp_pm.md#id68)

#### [sport (`u16`)](mptcp_pm.md#id69)

byte-order
:   big-endian

#### [dport (`u16`)](mptcp_pm.md#id70)

byte-order
:   big-endian

#### [backup (`u8`)](mptcp_pm.md#id71)

#### [error (`u8`)](mptcp_pm.md#id72)

#### [flags (`u16`)](mptcp_pm.md#id73)

#### [timeout (`u32`)](mptcp_pm.md#id74)

#### [if_idx (`u32`)](mptcp_pm.md#id75)

#### [reset-reason (`u32`)](mptcp_pm.md#id76)

#### [reset-flags (`u32`)](mptcp_pm.md#id77)

#### [server-side (`u8`)](mptcp_pm.md#id78)
