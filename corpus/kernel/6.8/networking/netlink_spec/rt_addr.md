---
collection: kernel
version: "6.8"
title: "Family rt-addr netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/rt_addr.html
fetched_at: 2026-08-21T03:49:21+00:00
---
# [Family `rt-addr` netlink specification](rt_addr.md#id1)

Contents

- [Family `rt-addr` netlink specification](rt_addr.md#family-rt-addr-netlink-specification)

  - [Summary](rt_addr.md#summary)
  - [Operations](rt_addr.md#operations)

    - [newaddr](rt_addr.md#newaddr)
    - [deladdr](rt_addr.md#deladdr)
    - [getaddr](rt_addr.md#getaddr)
  - [Multicast groups](rt_addr.md#multicast-groups)
  - [Definitions](rt_addr.md#definitions)

    - [ifaddrmsg](rt_addr.md#ifaddrmsg)
    - [ifa-cacheinfo](rt_addr.md#ifa-cacheinfo)
    - [ifa-flags](rt_addr.md#ifa-flags)
  - [Attribute sets](rt_addr.md#attribute-sets)

    - [addr-attrs](rt_addr.md#addr-attrs)

      - [ifa-address (`binary`)](rt_addr.md#ifa-address-binary)
      - [ifa-local (`binary`)](rt_addr.md#ifa-local-binary)
      - [ifa-label (`string`)](rt_addr.md#ifa-label-string)
      - [ifa-broadcast (`binary`)](rt_addr.md#ifa-broadcast-binary)
      - [ifa-anycast (`binary`)](rt_addr.md#ifa-anycast-binary)
      - [ifa-cacheinfo (`binary`)](rt_addr.md#ifa-cacheinfo-binary)
      - [ifa-multicast (`binary`)](rt_addr.md#ifa-multicast-binary)
      - [ifa-flags (`u32`)](rt_addr.md#ifa-flags-u32)
      - [ifa-rt-priority (`u32`)](rt_addr.md#ifa-rt-priority-u32)
      - [ifa-target-netnsid (`binary`)](rt_addr.md#ifa-target-netnsid-binary)
      - [ifa-proto (`u8`)](rt_addr.md#ifa-proto-u8)

## [Summary](rt_addr.md#id2)

Address configuration over rtnetlink.

## [Operations](rt_addr.md#id3)

### [newaddr](rt_addr.md#id4)

Add new address

attribute-set
:   addr-attrs

do
:   **request**
    :   attributes
        :   [`ifa-family`, `ifa-flags`, `ifa-prefixlen`, `ifa-scope`, `ifa-index`, `ifa-address`, `ifa-label`, `ifa-local`, `ifa-cacheinfo`]

### [deladdr](rt_addr.md#id5)

Remove address

attribute-set
:   addr-attrs

do
:   **request**
    :   attributes
        :   [`ifa-family`, `ifa-flags`, `ifa-prefixlen`, `ifa-scope`, `ifa-index`, `ifa-address`, `ifa-local`]

### [getaddr](rt_addr.md#id6)

Dump address information.

attribute-set
:   addr-attrs

dump
:   **request**
    :   attributes
        :   [`ifa-index`]

    **reply**
    :   attributes
        :   [`ifa-family`, `ifa-flags`, `ifa-prefixlen`, `ifa-scope`, `ifa-index`, `ifa-address`, `ifa-label`, `ifa-local`, `ifa-cacheinfo`]

## [Multicast groups](rt_addr.md#id7)

- rtnlgrp-ipv4-ifaddr
- rtnlgrp-ipv6-ifaddr

## [Definitions](rt_addr.md#id8)

### [ifaddrmsg](rt_addr.md#id9)

type
:   struct

members
:   ifa-family

    ifa-prefixlen

    ifa-flags

    ifa-scope

    ifa-index

### [ifa-cacheinfo](rt_addr.md#id10)

type
:   struct

members
:   ifa-prefered

    ifa-valid

    cstamp

    tstamp

### [ifa-flags](rt_addr.md#id11)

type
:   flags

entries
:   secondary

    nodad

    optimistic

    dadfailed

    homeaddress

    deprecated

    tentative

    permanent

    managetempaddr

    noprefixroute

    mcautojoin

    stable-privacy

## [Attribute sets](rt_addr.md#id12)

### [addr-attrs](rt_addr.md#id13)

#### [ifa-address (`binary`)](rt_addr.md#id14)

display-hint
:   ipv4

#### [ifa-local (`binary`)](rt_addr.md#id15)

display-hint
:   ipv4

#### [ifa-label (`string`)](rt_addr.md#id16)

#### [ifa-broadcast (`binary`)](rt_addr.md#id17)

display-hint
:   ipv4

#### [ifa-anycast (`binary`)](rt_addr.md#id18)

#### [ifa-cacheinfo (`binary`)](rt_addr.md#id19)

struct
:   ifa-cacheinfo

#### [ifa-multicast (`binary`)](rt_addr.md#id20)

#### [ifa-flags (`u32`)](rt_addr.md#id21)

enum
:   ifa-flags

enum-as-flags
:   True

#### [ifa-rt-priority (`u32`)](rt_addr.md#id22)

#### [ifa-target-netnsid (`binary`)](rt_addr.md#id23)

#### [ifa-proto (`u8`)](rt_addr.md#id24)
