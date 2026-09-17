---
collection: kernel
version: "6.17"
title: "Family rt-addr netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/rt-addr.html
fetched_at: 2026-09-16T16:40:56+00:00
---
# [Family `rt-addr` netlink specification](rt-addr.md#id1)

Contents

- [Family `rt-addr` netlink specification](rt-addr.md#family-rt-addr-netlink-specification)

  - [Summary](rt-addr.md#summary)
  - [Operations](rt-addr.md#operations)

    - [newaddr](rt-addr.md#newaddr)
    - [deladdr](rt-addr.md#deladdr)
    - [getaddr](rt-addr.md#getaddr)
    - [getmulticast](rt-addr.md#getmulticast)
  - [Multicast groups](rt-addr.md#multicast-groups)
  - [Definitions](rt-addr.md#definitions)

    - [ifaddrmsg](rt-addr.md#ifaddrmsg)
    - [ifa-cacheinfo](rt-addr.md#ifa-cacheinfo)
    - [ifa-flags](rt-addr.md#ifa-flags)
  - [Attribute sets](rt-addr.md#attribute-sets)

    - [addr-attrs](rt-addr.md#addr-attrs)

## [Summary](rt-addr.md#id2)

Address configuration over rtnetlink.

## [Operations](rt-addr.md#id3)

### [newaddr](rt-addr.md#id4)

Add new address

attribute-set:
:   [addr-attrs](rt-addr.md#rt-addr-attribute-set-addr-attrs)

do:
:   **request**
    :   attributes:
        :   [`address`, `label`, `local`, `cacheinfo`]

### [deladdr](rt-addr.md#id5)

Remove address

attribute-set:
:   [addr-attrs](rt-addr.md#rt-addr-attribute-set-addr-attrs)

do:
:   **request**
    :   attributes:
        :   [`address`, `local`]

### [getaddr](rt-addr.md#id6)

Dump address information.

attribute-set:
:   [addr-attrs](rt-addr.md#rt-addr-attribute-set-addr-attrs)

dump:
:   **request**
    :   attributes:
        :   []

    **reply**
    :   attributes:
        :   [`address`, `label`, `local`, `cacheinfo`]

### [getmulticast](rt-addr.md#id7)

Get / dump IPv4/IPv6 multicast addresses.

attribute-set:
:   [addr-attrs](rt-addr.md#rt-addr-attribute-set-addr-attrs)

fixed-header:
:   [ifaddrmsg](rt-addr.md#rt-addr-definition-ifaddrmsg)

do:
:   **request**
    :   attributes:
        :   []

    **reply**
    :   attributes:
        :   [`multicast`, `cacheinfo`]

dump:
:   **request**
    :   attributes:
        :   []

    **reply**
    :   attributes:
        :   [`multicast`, `cacheinfo`]

## [Multicast groups](rt-addr.md#id8)

- rtnlgrp-ipv4-ifaddr
- rtnlgrp-ipv6-ifaddr

## [Definitions](rt-addr.md#id9)

### [ifaddrmsg](rt-addr.md#id10)

type:
:   struct

members:
:   ifa-family (`u8`):

    ifa-prefixlen (`u8`):

    ifa-flags (`u8`):

    ifa-scope (`u8`):

    ifa-index (`u32`):

### [ifa-cacheinfo](rt-addr.md#id11)

type:
:   struct

members:
:   ifa-prefered (`u32`):

    ifa-valid (`u32`):

    cstamp (`u32`):

    tstamp (`u32`):

### [ifa-flags](rt-addr.md#id12)

type:
:   flags

name-prefix:
:   ifa-f-

enum-name:
:   None

entries:
:   secondary:

    nodad:

    optimistic:

    dadfailed:

    homeaddress:

    deprecated:

    tentative:

    permanent:

    managetempaddr:

    noprefixroute:

    mcautojoin:

    stable-privacy:

## [Attribute sets](rt-addr.md#id13)

### [addr-attrs](rt-addr.md#id14)

#### address (`binary`)

display-hint:
:   ipv4

#### local (`binary`)

display-hint:
:   ipv4

#### label (`string`)

#### broadcast (`binary`)

display-hint:
:   ipv4

#### anycast (`binary`)

#### cacheinfo (`binary`)

struct:
:   [ifa-cacheinfo](rt-addr.md#rt-addr-definition-ifa-cacheinfo)

#### multicast (`binary`)

#### flags (`u32`)

enum:
:   [ifa-flags](rt-addr.md#rt-addr-definition-ifa-flags)

enum-as-flags:
:   True

#### rt-priority (`u32`)

#### target-netnsid (`binary`)

#### proto (`u8`)
