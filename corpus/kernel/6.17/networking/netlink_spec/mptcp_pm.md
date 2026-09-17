---
collection: kernel
version: "6.17"
title: "Family mptcp_pm netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/mptcp_pm.html
fetched_at: 2026-09-16T16:40:49+00:00
---
# [Family `mptcp_pm` netlink specification](mptcp_pm.md#id10)

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
    - [subflow-attribute](mptcp_pm.md#subflow-attribute)
    - [endpoint](mptcp_pm.md#endpoint)
    - [attr](mptcp_pm.md#attr)
    - [event-attr](mptcp_pm.md#event-attr)

## [Summary](mptcp_pm.md#id11)

Multipath TCP.

## [Operations](mptcp_pm.md#id12)

### [unspec](mptcp_pm.md#id13)

unused

value:
:   0

### [add-addr](mptcp_pm.md#id14)

Add endpoint

attribute-set:
:   [endpoint](mptcp_pm.md#mptcp-pm-attribute-set-endpoint)

dont-validate:
:   [‘strict’]

flags:
:   [`uns-admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`addr`]

### [del-addr](mptcp_pm.md#id15)

Delete endpoint

attribute-set:
:   [endpoint](mptcp_pm.md#mptcp-pm-attribute-set-endpoint)

dont-validate:
:   [‘strict’]

flags:
:   [`uns-admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`addr`]

### [get-addr](mptcp_pm.md#id16)

Get endpoint information

attribute-set:
:   [attr](mptcp_pm.md#mptcp-pm-attribute-set-attr)

dont-validate:
:   [‘strict’]

do:
:   **request**
    :   attributes:
        :   [`addr`, `token`]

    **reply**
    :   attributes:
        :   [`addr`]

dump:
:   **reply**
    :   attributes:
        :   [`addr`]

### [flush-addrs](mptcp_pm.md#id17)

Flush addresses

attribute-set:
:   [endpoint](mptcp_pm.md#mptcp-pm-attribute-set-endpoint)

dont-validate:
:   [‘strict’]

flags:
:   [`uns-admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`addr`]

### [set-limits](mptcp_pm.md#id18)

Set protocol limits

attribute-set:
:   [attr](mptcp_pm.md#mptcp-pm-attribute-set-attr)

dont-validate:
:   [‘strict’]

flags:
:   [`uns-admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`rcv-add-addrs`, `subflows`]

### [get-limits](mptcp_pm.md#id19)

Get protocol limits

attribute-set:
:   [attr](mptcp_pm.md#mptcp-pm-attribute-set-attr)

dont-validate:
:   [‘strict’]

do:
:   **request**
    :   attributes:
        :   [`rcv-add-addrs`, `subflows`]

    **reply**
    :   attributes:
        :   [`rcv-add-addrs`, `subflows`]

### [set-flags](mptcp_pm.md#id20)

Change endpoint flags

attribute-set:
:   [attr](mptcp_pm.md#mptcp-pm-attribute-set-attr)

dont-validate:
:   [‘strict’]

flags:
:   [`uns-admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`addr`, `token`, `addr-remote`]

### [announce](mptcp_pm.md#id21)

Announce new address

attribute-set:
:   [attr](mptcp_pm.md#mptcp-pm-attribute-set-attr)

dont-validate:
:   [‘strict’]

flags:
:   [`uns-admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`addr`, `token`]

### [remove](mptcp_pm.md#id22)

Announce removal

attribute-set:
:   [attr](mptcp_pm.md#mptcp-pm-attribute-set-attr)

dont-validate:
:   [‘strict’]

flags:
:   [`uns-admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`token`, `loc-id`]

### [subflow-create](mptcp_pm.md#id23)

Create subflow

attribute-set:
:   [attr](mptcp_pm.md#mptcp-pm-attribute-set-attr)

dont-validate:
:   [‘strict’]

flags:
:   [`uns-admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`addr`, `token`, `addr-remote`]

### [subflow-destroy](mptcp_pm.md#id24)

Destroy subflow

attribute-set:
:   [attr](mptcp_pm.md#mptcp-pm-attribute-set-attr)

dont-validate:
:   [‘strict’]

flags:
:   [`uns-admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`addr`, `token`, `addr-remote`]

## [Definitions](mptcp_pm.md#id25)

### [event-type](mptcp_pm.md#id26)

type:
:   enum

enum-name:
:   mptcp-event-type

name-prefix:
:   mptcp-event-

entries:
:   unspec:
    :   unused event

    created:
    :   A new MPTCP connection has been created. It is the good time to allocate memory and send ADD_ADDR if needed. Depending on the traffic-patterns it can take a long time until the MPTCP_EVENT_ESTABLISHED is sent. Attributes: token, family, saddr4 | saddr6, daddr4 | daddr6, sport, dport, server-side, [flags].

    established:
    :   A MPTCP connection is established (can start new subflows). Attributes: token, family, saddr4 | saddr6, daddr4 | daddr6, sport, dport, server-side, [flags].

    closed:
    :   A MPTCP connection has stopped. Attribute: token.

    announced:
    :   A new address has been announced by the peer. Attributes: token, rem_id, family, daddr4 | daddr6 [, dport].

    removed:
    :   An address has been lost by the peer. Attributes: token, rem_id.

    sub-established:
    :   A new subflow has been established. ‘error’ should not be set. Attributes: token, family, loc_id, rem_id, saddr4 | saddr6, daddr4 | daddr6, sport, dport, backup, if-idx [, error].

    sub-closed:
    :   A subflow has been closed. An error (copy of sk_err) could be set if an error has been detected for this subflow. Attributes: token, family, loc_id, rem_id, saddr4 | saddr6, daddr4 | daddr6, sport, dport, backup, if-idx [, error].

    sub-priority:
    :   The priority of a subflow has changed. ‘error’ should not be set. Attributes: token, family, loc_id, rem_id, saddr4 | saddr6, daddr4 | daddr6, sport, dport, backup, if-idx [, error].

    listener-created:
    :   A new PM listener is created. Attributes: family, sport, saddr4 | saddr6.

    listener-closed:
    :   A PM listener is closed. Attributes: family, sport, saddr4 | saddr6.

## [Attribute sets](mptcp_pm.md#id27)

### [address](mptcp_pm.md#id28)

#### unspec (`unused`)

value:
:   0

#### family (`u16`)

#### id (`u8`)

#### addr4 (`u32`)

byte-order:
:   big-endian

#### addr6 (`binary`)

#### port (`u16`)

#### flags (`u32`)

#### if-idx (`s32`)

### [subflow-attribute](mptcp_pm.md#id29)

#### unspec (`unused`)

value:
:   0

#### token-rem (`u32`)

#### token-loc (`u32`)

#### relwrite-seq (`u32`)

#### map-seq (`u64`)

#### map-sfseq (`u32`)

#### ssn-offset (`u32`)

#### map-datalen (`u16`)

#### flags (`u32`)

#### id-rem (`u8`)

#### id-loc (`u8`)

#### pad (`pad`)

### [endpoint](mptcp_pm.md#id30)

#### addr (`nest`)

nested-attributes:
:   [address](mptcp_pm.md#mptcp-pm-attribute-set-address)

### [attr](mptcp_pm.md#id31)

#### unspec (`unused`)

value:
:   0

#### addr (`nest`)

nested-attributes:
:   [address](mptcp_pm.md#mptcp-pm-attribute-set-address)

#### rcv-add-addrs (`u32`)

#### subflows (`u32`)

#### token (`u32`)

#### loc-id (`u8`)

#### addr-remote (`nest`)

nested-attributes:
:   [address](mptcp_pm.md#mptcp-pm-attribute-set-address)

### [event-attr](mptcp_pm.md#id32)

#### unspec (`unused`)

value:
:   0

#### token (`u32`)

#### family (`u16`)

#### loc-id (`u8`)

#### rem-id (`u8`)

#### saddr4 (`u32`)

byte-order:
:   big-endian

#### saddr6 (`binary`)

#### daddr4 (`u32`)

byte-order:
:   big-endian

#### daddr6 (`binary`)

#### sport (`u16`)

byte-order:
:   big-endian

#### dport (`u16`)

byte-order:
:   big-endian

#### backup (`u8`)

#### error (`u8`)

#### flags (`u16`)

#### timeout (`u32`)

#### if-idx (`s32`)

#### reset-reason (`u32`)

#### reset-flags (`u32`)

#### server-side (`u8`)
