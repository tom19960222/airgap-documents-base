---
collection: kernel
version: "6.17"
title: "Family rt-neigh netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/rt-neigh.html
fetched_at: 2026-09-16T16:40:57+00:00
---
# [Family `rt-neigh` netlink specification](rt-neigh.md#id3)

Contents

- [Family `rt-neigh` netlink specification](rt-neigh.md#family-rt-neigh-netlink-specification)

  - [Summary](rt-neigh.md#summary)
  - [Operations](rt-neigh.md#operations)

    - [newneigh](rt-neigh.md#newneigh)
    - [delneigh](rt-neigh.md#delneigh)
    - [delneigh-ntf](rt-neigh.md#delneigh-ntf)
    - [getneigh](rt-neigh.md#getneigh)
    - [newneigh-ntf](rt-neigh.md#newneigh-ntf)
    - [getneightbl](rt-neigh.md#getneightbl)
    - [setneightbl](rt-neigh.md#setneightbl)
  - [Multicast groups](rt-neigh.md#multicast-groups)
  - [Definitions](rt-neigh.md#definitions)

    - [ndmsg](rt-neigh.md#ndmsg)
    - [ndtmsg](rt-neigh.md#ndtmsg)
    - [nud-state](rt-neigh.md#nud-state)
    - [ntf-flags](rt-neigh.md#ntf-flags)
    - [ntf-ext-flags](rt-neigh.md#ntf-ext-flags)
    - [rtm-type](rt-neigh.md#rtm-type)
    - [nda-cacheinfo](rt-neigh.md#nda-cacheinfo)
    - [ndt-config](rt-neigh.md#ndt-config)
    - [ndt-stats](rt-neigh.md#ndt-stats)
  - [Attribute sets](rt-neigh.md#attribute-sets)

    - [neighbour-attrs](rt-neigh.md#neighbour-attrs)
    - [ndt-attrs](rt-neigh.md#ndt-attrs)
    - [ndtpa-attrs](rt-neigh.md#ndtpa-attrs)

## [Summary](rt-neigh.md#id4)

IP neighbour management over rtnetlink.

## [Operations](rt-neigh.md#id5)

### [newneigh](rt-neigh.md#id6)

Add new neighbour entry

fixed-header:
:   [ndmsg](rt-neigh.md#rt-neigh-definition-ndmsg)

attribute-set:
:   [neighbour-attrs](rt-neigh.md#rt-neigh-attribute-set-neighbour-attrs)

do:
:   **request**
    :   attributes:
        :   [`dst`, `lladdr`, `probes`, `vlan`, `port`, `vni`, `ifindex`, `master`, `protocol`, `nh-id`, `flags-ext`, `fdb-ext-attrs`]

### [delneigh](rt-neigh.md#id7)

Remove an existing neighbour entry

fixed-header:
:   [ndmsg](rt-neigh.md#rt-neigh-definition-ndmsg)

attribute-set:
:   [neighbour-attrs](rt-neigh.md#rt-neigh-attribute-set-neighbour-attrs)

do:
:   **request**
    :   attributes:
        :   [`dst`, `ifindex`]

### [delneigh-ntf](rt-neigh.md#id8)

Notify a neighbour deletion

value:
:   29

notify:
:   getneigh

fixed-header:
:   [ndmsg](rt-neigh.md#rt-neigh-definition-ndmsg)

### [getneigh](rt-neigh.md#id9)

Get or dump neighbour entries

fixed-header:
:   [ndmsg](rt-neigh.md#rt-neigh-definition-ndmsg)

attribute-set:
:   [neighbour-attrs](rt-neigh.md#rt-neigh-attribute-set-neighbour-attrs)

do:
:   **request**
    :   attributes:
        :   [`dst`]

    **reply**
    :   attributes:
        :   [`dst`, `lladdr`, `probes`, `vlan`, `port`, `vni`, `ifindex`, `master`, `protocol`, `nh-id`, `flags-ext`, `fdb-ext-attrs`]

dump:
:   **request**
    :   attributes:
        :   [`ifindex`, `master`]

    **reply**
    :   attributes:
        :   [`dst`, `lladdr`, `probes`, `vlan`, `port`, `vni`, `ifindex`, `master`, `protocol`, `nh-id`, `flags-ext`, `fdb-ext-attrs`]

### [newneigh-ntf](rt-neigh.md#id10)

Notify a neighbour creation

value:
:   28

notify:
:   getneigh

fixed-header:
:   [ndmsg](rt-neigh.md#rt-neigh-definition-ndmsg)

### [getneightbl](rt-neigh.md#id11)

Get or dump neighbour tables

fixed-header:
:   [ndtmsg](rt-neigh.md#rt-neigh-definition-ndtmsg)

attribute-set:
:   [ndt-attrs](rt-neigh.md#rt-neigh-attribute-set-ndt-attrs)

dump:
:   **request**

    **reply**
    :   attributes:
        :   [`name`, `thresh1`, `thresh2`, `thresh3`, `config`, `parms`, `stats`, `gc-interval`]

### [setneightbl](rt-neigh.md#id12)

Set neighbour tables

fixed-header:
:   [ndtmsg](rt-neigh.md#rt-neigh-definition-ndtmsg)

attribute-set:
:   [ndt-attrs](rt-neigh.md#rt-neigh-attribute-set-ndt-attrs)

do:
:   **request**
    :   attributes:
        :   [`name`, `thresh1`, `thresh2`, `thresh3`, `parms`, `gc-interval`]

## [Multicast groups](rt-neigh.md#id13)

- rtnlgrp-neigh

## [Definitions](rt-neigh.md#id14)

### [ndmsg](rt-neigh.md#id15)

type:
:   struct

members:
:   ndm-family (`u8`):

    ndm-pad (`pad`):

    ndm-ifindex (`s32`):

    ndm-state (`u16`):

    ndm-flags (`u8`):

    ndm-type (`u8`):

### [ndtmsg](rt-neigh.md#id16)

type:
:   struct

members:
:   family (`u8`):

### [nud-state](rt-neigh.md#id17)

type:
:   flags

enum-name:
:   None

entries:
:   - `incomplete`
    - `reachable`
    - `stale`
    - `delay`
    - `probe`
    - `failed`
    - `noarp`
    - `permanent`

### [ntf-flags](rt-neigh.md#id18)

type:
:   flags

enum-name:
:   None

entries:
:   - `use`
    - `self`
    - `master`
    - `proxy`
    - `ext-learned`
    - `offloaded`
    - `sticky`
    - `router`

### [ntf-ext-flags](rt-neigh.md#id19)

type:
:   flags

enum-name:
:   None

entries:
:   - `managed`
    - `locked`
    - `ext-validated`

### [rtm-type](rt-neigh.md#id20)

type:
:   enum

enum-name:
:   None

entries:
:   - `unspec`
    - `unicast`
    - `local`
    - `broadcast`
    - `anycast`
    - `multicast`
    - `blackhole`
    - `unreachable`
    - `prohibit`
    - `throw`
    - `nat`
    - `xresolve`

### [nda-cacheinfo](rt-neigh.md#id21)

type:
:   struct

members:
:   confirmed (`u32`):

    used (`u32`):

    updated (`u32`):

    refcnt (`u32`):

### [ndt-config](rt-neigh.md#id22)

type:
:   struct

members:
:   key-len (`u16`):

    entry-size (`u16`):

    entries (`u32`):

    last-flush (`u32`):

    last-rand (`u32`):

    hash-rnd (`u32`):

    hash-mask (`u32`):

    hash-chain-gc (`u32`):

    proxy-qlen (`u32`):

### [ndt-stats](rt-neigh.md#id23)

type:
:   struct

members:
:   allocs (`u64`):

    destroys (`u64`):

    hash-grows (`u64`):

    res-failed (`u64`):

    lookups (`u64`):

    hits (`u64`):

    rcv-probes-mcast (`u64`):

    rcv-probes-ucast (`u64`):

    periodic-gc-runs (`u64`):

    forced-gc-runs (`u64`):

    table-fulls (`u64`):

## [Attribute sets](rt-neigh.md#id24)

### [neighbour-attrs](rt-neigh.md#id25)

#### unspec (`binary`)

value:
:   0

#### dst (`binary`)

display-hint:
:   ipv4

#### lladdr (`binary`)

display-hint:
:   mac

#### cacheinfo (`binary`)

struct:
:   [nda-cacheinfo](rt-neigh.md#rt-neigh-definition-nda-cacheinfo)

#### probes (`u32`)

#### vlan (`u16`)

#### port (`u16`)

#### vni (`u32`)

#### ifindex (`u32`)

#### master (`u32`)

#### link-netnsid (`s32`)

#### src-vni (`u32`)

#### protocol (`u8`)

#### nh-id (`u32`)

#### fdb-ext-attrs (`binary`)

#### flags-ext (`u32`)

enum:
:   [ntf-ext-flags](rt-neigh.md#rt-neigh-definition-ntf-ext-flags)

#### ndm-state-mask (`u16`)

#### ndm-flags-mask (`u8`)

### [ndt-attrs](rt-neigh.md#id26)

#### name (`string`)

#### thresh1 (`u32`)

#### thresh2 (`u32`)

#### thresh3 (`u32`)

#### config (`binary`)

struct:
:   [ndt-config](rt-neigh.md#rt-neigh-definition-ndt-config)

#### parms (`nest`)

nested-attributes:
:   [ndtpa-attrs](rt-neigh.md#rt-neigh-attribute-set-ndtpa-attrs)

#### stats (`binary`)

struct:
:   [ndt-stats](rt-neigh.md#rt-neigh-definition-ndt-stats)

#### gc-interval (`u64`)

#### pad (`pad`)

### [ndtpa-attrs](rt-neigh.md#id27)

#### ifindex (`u32`)

#### refcnt (`u32`)

#### reachable-time (`u64`)

#### base-reachable-time (`u64`)

#### retrans-time (`u64`)

#### gc-staletime (`u64`)

#### delay-probe-time (`u64`)

#### queue-len (`u32`)

#### app-probes (`u32`)

#### ucast-probes (`u32`)

#### mcast-probes (`u32`)

#### anycast-delay (`u64`)

#### proxy-delay (`u64`)

#### proxy-qlen (`u32`)

#### locktime (`u64`)

#### queue-lenbytes (`u32`)

#### mcast-reprobes (`u32`)

#### pad (`pad`)

#### interval-probe-time-ms (`u64`)
