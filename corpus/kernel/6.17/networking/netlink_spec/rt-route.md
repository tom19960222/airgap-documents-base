---
collection: kernel
version: "6.17"
title: "Family rt-route netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/rt-route.html
fetched_at: 2026-09-16T16:40:58+00:00
---
# [Family `rt-route` netlink specification](rt-route.md#id1)

Contents

- [Family `rt-route` netlink specification](rt-route.md#family-rt-route-netlink-specification)

  - [Summary](rt-route.md#summary)
  - [Operations](rt-route.md#operations)

    - [getroute](rt-route.md#getroute)
    - [newroute](rt-route.md#newroute)
    - [delroute](rt-route.md#delroute)
  - [Definitions](rt-route.md#definitions)

    - [rtm-type](rt-route.md#rtm-type)
    - [rtmsg](rt-route.md#rtmsg)
    - [rta-cacheinfo](rt-route.md#rta-cacheinfo)
  - [Attribute sets](rt-route.md#attribute-sets)

    - [route-attrs](rt-route.md#route-attrs)
    - [metrics](rt-route.md#metrics)

## [Summary](rt-route.md#id2)

Route configuration over rtnetlink.

## [Operations](rt-route.md#id3)

### [getroute](rt-route.md#id4)

Dump route information.

attribute-set:
:   [route-attrs](rt-route.md#rt-route-attribute-set-route-attrs)

do:
:   **request**
    :   attributes:
        :   [`src`, `dst`, `iif`, `oif`, `ip-proto`, `sport`, `dport`, `mark`, `uid`, `flowlabel`]

    **reply**
    :   attributes:
        :   [`dst`, `src`, `iif`, `oif`, `gateway`, `priority`, `prefsrc`, `metrics`, `multipath`, `flow`, `cacheinfo`, `table`, `mark`, `mfc-stats`, `via`, `newdst`, `pref`, `encap-type`, `encap`, `expires`, `pad`, `uid`, `ttl-propagate`, `ip-proto`, `sport`, `dport`, `nh-id`, `flowlabel`]

dump:
:   **request**
    :   attributes:
        :   []

    **reply**
    :   attributes:
        :   [`dst`, `src`, `iif`, `oif`, `gateway`, `priority`, `prefsrc`, `metrics`, `multipath`, `flow`, `cacheinfo`, `table`, `mark`, `mfc-stats`, `via`, `newdst`, `pref`, `encap-type`, `encap`, `expires`, `pad`, `uid`, `ttl-propagate`, `ip-proto`, `sport`, `dport`, `nh-id`, `flowlabel`]

### [newroute](rt-route.md#id5)

Create a new route

attribute-set:
:   [route-attrs](rt-route.md#rt-route-attribute-set-route-attrs)

do:
:   **request**
    :   attributes:
        :   [`dst`, `src`, `iif`, `oif`, `gateway`, `priority`, `prefsrc`, `metrics`, `multipath`, `flow`, `cacheinfo`, `table`, `mark`, `mfc-stats`, `via`, `newdst`, `pref`, `encap-type`, `encap`, `expires`, `pad`, `uid`, `ttl-propagate`, `ip-proto`, `sport`, `dport`, `nh-id`, `flowlabel`]

### [delroute](rt-route.md#id6)

Delete an existing route

attribute-set:
:   [route-attrs](rt-route.md#rt-route-attribute-set-route-attrs)

do:
:   **request**
    :   attributes:
        :   [`dst`, `src`, `iif`, `oif`, `gateway`, `priority`, `prefsrc`, `metrics`, `multipath`, `flow`, `cacheinfo`, `table`, `mark`, `mfc-stats`, `via`, `newdst`, `pref`, `encap-type`, `encap`, `expires`, `pad`, `uid`, `ttl-propagate`, `ip-proto`, `sport`, `dport`, `nh-id`, `flowlabel`]

## [Definitions](rt-route.md#id7)

### [rtm-type](rt-route.md#id8)

name-prefix:
:   rtn-

enum-name:
:   None

type:
:   enum

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

### [rtmsg](rt-route.md#id9)

type:
:   struct

members:
:   rtm-family (`u8`):

    rtm-dst-len (`u8`):

    rtm-src-len (`u8`):

    rtm-tos (`u8`):

    rtm-table (`u8`):

    rtm-protocol (`u8`):

    rtm-scope (`u8`):

    rtm-type (`u8`):

    rtm-flags (`u32`):

### [rta-cacheinfo](rt-route.md#id10)

type:
:   struct

members:
:   rta-clntref (`u32`):

    rta-lastuse (`u32`):

    rta-expires (`u32`):

    rta-error (`u32`):

    rta-used (`u32`):

## [Attribute sets](rt-route.md#id11)

### [route-attrs](rt-route.md#id12)

#### dst (`binary`)

display-hint:
:   ipv4

#### src (`binary`)

display-hint:
:   ipv4

#### iif (`u32`)

#### oif (`u32`)

#### gateway (`binary`)

display-hint:
:   ipv4

#### priority (`u32`)

#### prefsrc (`binary`)

display-hint:
:   ipv4

#### metrics (`nest`)

nested-attributes:
:   [metrics](rt-route.md#rt-route-attribute-set-metrics)

#### multipath (`binary`)

#### protoinfo (`binary`)

#### flow (`u32`)

#### cacheinfo (`binary`)

struct:
:   [rta-cacheinfo](rt-route.md#rt-route-definition-rta-cacheinfo)

#### session (`binary`)

#### mp-algo (`binary`)

#### table (`u32`)

#### mark (`u32`)

#### mfc-stats (`binary`)

#### via (`binary`)

#### newdst (`binary`)

#### pref (`u8`)

#### encap-type (`u16`)

#### encap (`binary`)

#### expires (`u32`)

#### pad (`binary`)

#### uid (`u32`)

#### ttl-propagate (`u8`)

#### ip-proto (`u8`)

#### sport (`u16`)

#### dport (`u16`)

#### nh-id (`u32`)

#### flowlabel (`u32`)

byte-order:
:   big-endian

display-hint:
:   hex

### [metrics](rt-route.md#id13)

#### unspec (`unused`)

value:
:   0

#### lock (`u32`)

#### mtu (`u32`)

#### window (`u32`)

#### rtt (`u32`)

#### rttvar (`u32`)

#### ssthresh (`u32`)

#### cwnd (`u32`)

#### advmss (`u32`)

#### reordering (`u32`)

#### hoplimit (`u32`)

#### initcwnd (`u32`)

#### features (`u32`)

#### rto-min (`u32`)

#### initrwnd (`u32`)

#### quickack (`u32`)

#### cc-algo (`string`)

#### fastopen-no-cookie (`u32`)
