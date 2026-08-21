---
collection: kernel
version: "6.8"
title: "Family fou netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/fou.html
fetched_at: 2026-08-21T03:49:16+00:00
---
# [Family `fou` netlink specification](fou.md#id1)

Contents

- [Family `fou` netlink specification](fou.md#family-fou-netlink-specification)

  - [Summary](fou.md#summary)
  - [Operations](fou.md#operations)

    - [unspec](fou.md#unspec)
    - [add](fou.md#add)
    - [del](fou.md#del)
    - [get](fou.md#get)
  - [Definitions](fou.md#definitions)

    - [encap_type](fou.md#encap-type)
  - [Attribute sets](fou.md#attribute-sets)

    - [fou](fou.md#fou)

      - [unspec (`unused`)](fou.md#unspec-unused)
      - [port (`u16`)](fou.md#port-u16)
      - [af (`u8`)](fou.md#af-u8)
      - [ipproto (`u8`)](fou.md#ipproto-u8)
      - [type (`u8`)](fou.md#type-u8)
      - [remcsum_nopartial (`flag`)](fou.md#remcsum-nopartial-flag)
      - [local_v4 (`u32`)](fou.md#local-v4-u32)
      - [local_v6 (`binary`)](fou.md#local-v6-binary)
      - [peer_v4 (`u32`)](fou.md#peer-v4-u32)
      - [peer_v6 (`binary`)](fou.md#peer-v6-binary)
      - [peer_port (`u16`)](fou.md#peer-port-u16)
      - [ifindex (`s32`)](fou.md#ifindex-s32)

## [Summary](fou.md#id2)

Foo-over-UDP.

## [Operations](fou.md#id3)

### [unspec](fou.md#id4)

unused

value
:   0

### [add](fou.md#id5)

Add port.

attribute-set
:   fou

dont-validate
:   ['strict', 'dump']

flags
:   ['admin-perm']

do
:   **request**
    :   attributes
        :   [`port`, `ipproto`, `type`, `remcsum_nopartial`, `local_v4`, `peer_v4`, `local_v6`, `peer_v6`, `peer_port`, `ifindex`]

### [del](fou.md#id6)

Delete port.

attribute-set
:   fou

dont-validate
:   ['strict', 'dump']

flags
:   ['admin-perm']

do
:   **request**
    :   attributes
        :   [`af`, `ifindex`, `port`, `peer_port`, `local_v4`, `peer_v4`, `local_v6`, `peer_v6`]

### [get](fou.md#id7)

Get tunnel info.

attribute-set
:   fou

dont-validate
:   ['strict', 'dump']

do
:   **request**
    :   attributes
        :   [`af`, `ifindex`, `port`, `peer_port`, `local_v4`, `peer_v4`, `local_v6`, `peer_v6`]

    **reply**
    :   attributes
        :   [`port`, `ipproto`, `type`, `remcsum_nopartial`, `local_v4`, `peer_v4`, `local_v6`, `peer_v6`, `peer_port`, `ifindex`]

dump
:   **reply**
    :   attributes
        :   [`port`, `ipproto`, `type`, `remcsum_nopartial`, `local_v4`, `peer_v4`, `local_v6`, `peer_v6`, `peer_port`, `ifindex`]

## [Definitions](fou.md#id8)

### [encap_type](fou.md#id9)

type
:   enum

name-prefix
:   fou-encap-

enum-name
:   None

entries
:   - `unspec`
    - `direct`
    - `gue`

## [Attribute sets](fou.md#id10)

### [fou](fou.md#id11)

#### [unspec (`unused`)](fou.md#id12)

value
:   0

#### [port (`u16`)](fou.md#id13)

byte-order
:   big-endian

#### [af (`u8`)](fou.md#id14)

#### [ipproto (`u8`)](fou.md#id15)

#### [type (`u8`)](fou.md#id16)

#### [remcsum_nopartial (`flag`)](fou.md#id17)

#### [local_v4 (`u32`)](fou.md#id18)

#### [local_v6 (`binary`)](fou.md#id19)

#### [peer_v4 (`u32`)](fou.md#id20)

#### [peer_v6 (`binary`)](fou.md#id21)

#### [peer_port (`u16`)](fou.md#id22)

byte-order
:   big-endian

#### [ifindex (`s32`)](fou.md#id23)
