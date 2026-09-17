---
collection: kernel
version: "6.17"
title: "Family fou netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/fou.html
fetched_at: 2026-09-16T16:40:47+00:00
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

    - [encap-type](fou.md#encap-type)
  - [Attribute sets](fou.md#attribute-sets)

    - [fou](fou.md#fou)

## [Summary](fou.md#id2)

Foo-over-UDP.

## [Operations](fou.md#id3)

### [unspec](fou.md#id4)

unused

value:
:   0

### [add](fou.md#id5)

Add port.

attribute-set:
:   [fou](fou.md#fou-attribute-set-fou)

dont-validate:
:   [‘strict’, ‘dump’]

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`port`, `ipproto`, `type`, `remcsum-nopartial`, `local-v4`, `peer-v4`, `local-v6`, `peer-v6`, `peer-port`, `ifindex`]

### [del](fou.md#id6)

Delete port.

attribute-set:
:   [fou](fou.md#fou-attribute-set-fou)

dont-validate:
:   [‘strict’, ‘dump’]

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`af`, `ifindex`, `port`, `peer-port`, `local-v4`, `peer-v4`, `local-v6`, `peer-v6`]

### [get](fou.md#id7)

Get tunnel info.

attribute-set:
:   [fou](fou.md#fou-attribute-set-fou)

dont-validate:
:   [‘strict’, ‘dump’]

do:
:   **request**
    :   attributes:
        :   [`af`, `ifindex`, `port`, `peer-port`, `local-v4`, `peer-v4`, `local-v6`, `peer-v6`]

    **reply**
    :   attributes:
        :   [`port`, `ipproto`, `type`, `remcsum-nopartial`, `local-v4`, `peer-v4`, `local-v6`, `peer-v6`, `peer-port`, `ifindex`]

dump:
:   **reply**
    :   attributes:
        :   [`port`, `ipproto`, `type`, `remcsum-nopartial`, `local-v4`, `peer-v4`, `local-v6`, `peer-v6`, `peer-port`, `ifindex`]

## [Definitions](fou.md#id8)

### [encap-type](fou.md#id9)

type:
:   enum

name-prefix:
:   fou-encap-

enum-name:
:   None

entries:
:   - `unspec`
    - `direct`
    - `gue`

## [Attribute sets](fou.md#id10)

### [fou](fou.md#id11)

#### unspec (`unused`)

value:
:   0

#### port (`u16`)

byte-order:
:   big-endian

#### af (`u8`)

#### ipproto (`u8`)

#### type (`u8`)

#### remcsum-nopartial (`flag`)

#### local-v4 (`u32`)

#### local-v6 (`binary`)

#### peer-v4 (`u32`)

#### peer-v6 (`binary`)

#### peer-port (`u16`)

byte-order:
:   big-endian

#### ifindex (`s32`)
