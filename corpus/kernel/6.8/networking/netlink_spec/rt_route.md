---
collection: kernel
version: "6.8"
title: "Family rt-route netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/rt_route.html
fetched_at: 2026-08-21T03:49:22+00:00
---
# [Family `rt-route` netlink specification](rt_route.md#id1)

Contents

- [Family `rt-route` netlink specification](rt_route.md#family-rt-route-netlink-specification)

  - [Summary](rt_route.md#summary)
  - [Operations](rt_route.md#operations)

    - [getroute](rt_route.md#getroute)
    - [newroute](rt_route.md#newroute)
    - [delroute](rt_route.md#delroute)
  - [Definitions](rt_route.md#definitions)

    - [rtm-type](rt_route.md#rtm-type)
    - [rtmsg](rt_route.md#rtmsg)
    - [rta-cacheinfo](rt_route.md#rta-cacheinfo)
  - [Attribute sets](rt_route.md#attribute-sets)

    - [route-attrs](rt_route.md#route-attrs)

      - [rta-dst (`binary`)](rt_route.md#rta-dst-binary)
      - [rta-src (`binary`)](rt_route.md#rta-src-binary)
      - [rta-iif (`u32`)](rt_route.md#rta-iif-u32)
      - [rta-oif (`u32`)](rt_route.md#rta-oif-u32)
      - [rta-gateway (`binary`)](rt_route.md#rta-gateway-binary)
      - [rta-priority (`u32`)](rt_route.md#rta-priority-u32)
      - [rta-prefsrc (`binary`)](rt_route.md#rta-prefsrc-binary)
      - [rta-metrics (`nest`)](rt_route.md#rta-metrics-nest)
      - [rta-multipath (`binary`)](rt_route.md#rta-multipath-binary)
      - [rta-protoinfo (`binary`)](rt_route.md#rta-protoinfo-binary)
      - [rta-flow (`u32`)](rt_route.md#rta-flow-u32)
      - [rta-cacheinfo (`binary`)](rt_route.md#rta-cacheinfo-binary)
      - [rta-session (`binary`)](rt_route.md#rta-session-binary)
      - [rta-mp-algo (`binary`)](rt_route.md#rta-mp-algo-binary)
      - [rta-table (`u32`)](rt_route.md#rta-table-u32)
      - [rta-mark (`u32`)](rt_route.md#rta-mark-u32)
      - [rta-mfc-stats (`binary`)](rt_route.md#rta-mfc-stats-binary)
      - [rta-via (`binary`)](rt_route.md#rta-via-binary)
      - [rta-newdst (`binary`)](rt_route.md#rta-newdst-binary)
      - [rta-pref (`u8`)](rt_route.md#rta-pref-u8)
      - [rta-encap-type (`u16`)](rt_route.md#rta-encap-type-u16)
      - [rta-encap (`binary`)](rt_route.md#rta-encap-binary)
      - [rta-expires (`u32`)](rt_route.md#rta-expires-u32)
      - [rta-pad (`binary`)](rt_route.md#rta-pad-binary)
      - [rta-uid (`u32`)](rt_route.md#rta-uid-u32)
      - [rta-ttl-propagate (`u8`)](rt_route.md#rta-ttl-propagate-u8)
      - [rta-ip-proto (`u8`)](rt_route.md#rta-ip-proto-u8)
      - [rta-sport (`u16`)](rt_route.md#rta-sport-u16)
      - [rta-dport (`u16`)](rt_route.md#rta-dport-u16)
      - [rta-nh-id (`u32`)](rt_route.md#rta-nh-id-u32)
    - [rta-metrics](rt_route.md#rta-metrics)

      - [rtax-unspec (`unused`)](rt_route.md#rtax-unspec-unused)
      - [rtax-lock (`u32`)](rt_route.md#rtax-lock-u32)
      - [rtax-mtu (`u32`)](rt_route.md#rtax-mtu-u32)
      - [rtax-window (`u32`)](rt_route.md#rtax-window-u32)
      - [rtax-rtt (`u32`)](rt_route.md#rtax-rtt-u32)
      - [rtax-rttvar (`u32`)](rt_route.md#rtax-rttvar-u32)
      - [rtax-ssthresh (`u32`)](rt_route.md#rtax-ssthresh-u32)
      - [rtax-cwnd (`u32`)](rt_route.md#rtax-cwnd-u32)
      - [rtax-advmss (`u32`)](rt_route.md#rtax-advmss-u32)
      - [rtax-reordering (`u32`)](rt_route.md#rtax-reordering-u32)
      - [rtax-hoplimit (`u32`)](rt_route.md#rtax-hoplimit-u32)
      - [rtax-initcwnd (`u32`)](rt_route.md#rtax-initcwnd-u32)
      - [rtax-features (`u32`)](rt_route.md#rtax-features-u32)
      - [rtax-rto-min (`u32`)](rt_route.md#rtax-rto-min-u32)
      - [rtax-initrwnd (`u32`)](rt_route.md#rtax-initrwnd-u32)
      - [rtax-quickack (`u32`)](rt_route.md#rtax-quickack-u32)
      - [rtax-cc-algo (`string`)](rt_route.md#rtax-cc-algo-string)
      - [rtax-fastopen-no-cookie (`u32`)](rt_route.md#rtax-fastopen-no-cookie-u32)

## [Summary](rt_route.md#id2)

Route configuration over rtnetlink.

## [Operations](rt_route.md#id3)

### [getroute](rt_route.md#id4)

Dump route information.

attribute-set
:   route-attrs

fixed-header
:   rtmsg

do
:   **request**
    :   attributes
        :   [`rtm-family`, `rta-src`, `rtm-src-len`, `rta-dst`, `rtm-dst-len`, `rta-iif`, `rta-oif`, `rta-ip-proto`, `rta-sport`, `rta-dport`, `rta-mark`, `rta-uid`]

    **reply**
    :   attributes
        :   [`rtm-family`, `rtm-dst-len`, `rtm-src-len`, `rtm-tos`, `rtm-table`, `rtm-protocol`, `rtm-scope`, `rtm-type`, `rtm-flags`, `rta-dst`, `rta-src`, `rta-iif`, `rta-oif`, `rta-gateway`, `rta-priority`, `rta-prefsrc`, `rta-metrics`, `rta-multipath`, `rta-flow`, `rta-cacheinfo`, `rta-table`, `rta-mark`, `rta-mfc-stats`, `rta-via`, `rta-newdst`, `rta-pref`, `rta-encap-type`, `rta-encap`, `rta-expires`, `rta-pad`, `rta-uid`, `rta-ttl-propagate`, `rta-ip-proto`, `rta-sport`, `rta-dport`, `rta-nh-id`]

dump
:   **request**
    :   attributes
        :   [`rtm-family`]

    **reply**
    :   attributes
        :   [`rtm-family`, `rtm-dst-len`, `rtm-src-len`, `rtm-tos`, `rtm-table`, `rtm-protocol`, `rtm-scope`, `rtm-type`, `rtm-flags`, `rta-dst`, `rta-src`, `rta-iif`, `rta-oif`, `rta-gateway`, `rta-priority`, `rta-prefsrc`, `rta-metrics`, `rta-multipath`, `rta-flow`, `rta-cacheinfo`, `rta-table`, `rta-mark`, `rta-mfc-stats`, `rta-via`, `rta-newdst`, `rta-pref`, `rta-encap-type`, `rta-encap`, `rta-expires`, `rta-pad`, `rta-uid`, `rta-ttl-propagate`, `rta-ip-proto`, `rta-sport`, `rta-dport`, `rta-nh-id`]

### [newroute](rt_route.md#id5)

Create a new route

attribute-set
:   route-attrs

fixed-header
:   rtmsg

do
:   **request**
    :   attributes
        :   [`rtm-family`, `rtm-dst-len`, `rtm-src-len`, `rtm-tos`, `rtm-table`, `rtm-protocol`, `rtm-scope`, `rtm-type`, `rtm-flags`, `rta-dst`, `rta-src`, `rta-iif`, `rta-oif`, `rta-gateway`, `rta-priority`, `rta-prefsrc`, `rta-metrics`, `rta-multipath`, `rta-flow`, `rta-cacheinfo`, `rta-table`, `rta-mark`, `rta-mfc-stats`, `rta-via`, `rta-newdst`, `rta-pref`, `rta-encap-type`, `rta-encap`, `rta-expires`, `rta-pad`, `rta-uid`, `rta-ttl-propagate`, `rta-ip-proto`, `rta-sport`, `rta-dport`, `rta-nh-id`]

### [delroute](rt_route.md#id6)

Delete an existing route

attribute-set
:   route-attrs

fixed-header
:   rtmsg

do
:   **request**
    :   attributes
        :   [`rtm-family`, `rtm-dst-len`, `rtm-src-len`, `rtm-tos`, `rtm-table`, `rtm-protocol`, `rtm-scope`, `rtm-type`, `rtm-flags`, `rta-dst`, `rta-src`, `rta-iif`, `rta-oif`, `rta-gateway`, `rta-priority`, `rta-prefsrc`, `rta-metrics`, `rta-multipath`, `rta-flow`, `rta-cacheinfo`, `rta-table`, `rta-mark`, `rta-mfc-stats`, `rta-via`, `rta-newdst`, `rta-pref`, `rta-encap-type`, `rta-encap`, `rta-expires`, `rta-pad`, `rta-uid`, `rta-ttl-propagate`, `rta-ip-proto`, `rta-sport`, `rta-dport`, `rta-nh-id`]

## [Definitions](rt_route.md#id7)

### [rtm-type](rt_route.md#id8)

name-prefix
:   rtn-

type
:   enum

entries
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

### [rtmsg](rt_route.md#id9)

type
:   struct

members
:   rtm-family

    rtm-dst-len

    rtm-src-len

    rtm-tos

    rtm-table

    rtm-protocol

    rtm-scope

    rtm-type

    rtm-flags

### [rta-cacheinfo](rt_route.md#id10)

type
:   struct

members
:   rta-clntref

    rta-lastuse

    rta-expires

    rta-error

    rta-used

## [Attribute sets](rt_route.md#id11)

### [route-attrs](rt_route.md#id12)

#### [rta-dst (`binary`)](rt_route.md#id13)

display-hint
:   ipv4

#### [rta-src (`binary`)](rt_route.md#id14)

display-hint
:   ipv4

#### [rta-iif (`u32`)](rt_route.md#id15)

#### [rta-oif (`u32`)](rt_route.md#id16)

#### [rta-gateway (`binary`)](rt_route.md#id17)

display-hint
:   ipv4

#### [rta-priority (`u32`)](rt_route.md#id18)

#### [rta-prefsrc (`binary`)](rt_route.md#id19)

display-hint
:   ipv4

#### [rta-metrics (`nest`)](rt_route.md#id20)

nested-attributes
:   rta-metrics

#### [rta-multipath (`binary`)](rt_route.md#id21)

#### [rta-protoinfo (`binary`)](rt_route.md#id22)

#### [rta-flow (`u32`)](rt_route.md#id23)

#### [rta-cacheinfo (`binary`)](rt_route.md#id24)

struct
:   rta-cacheinfo

#### [rta-session (`binary`)](rt_route.md#id25)

#### [rta-mp-algo (`binary`)](rt_route.md#id26)

#### [rta-table (`u32`)](rt_route.md#id27)

#### [rta-mark (`u32`)](rt_route.md#id28)

#### [rta-mfc-stats (`binary`)](rt_route.md#id29)

#### [rta-via (`binary`)](rt_route.md#id30)

#### [rta-newdst (`binary`)](rt_route.md#id31)

#### [rta-pref (`u8`)](rt_route.md#id32)

#### [rta-encap-type (`u16`)](rt_route.md#id33)

#### [rta-encap (`binary`)](rt_route.md#id34)

#### [rta-expires (`u32`)](rt_route.md#id35)

#### [rta-pad (`binary`)](rt_route.md#id36)

#### [rta-uid (`u32`)](rt_route.md#id37)

#### [rta-ttl-propagate (`u8`)](rt_route.md#id38)

#### [rta-ip-proto (`u8`)](rt_route.md#id39)

#### [rta-sport (`u16`)](rt_route.md#id40)

#### [rta-dport (`u16`)](rt_route.md#id41)

#### [rta-nh-id (`u32`)](rt_route.md#id42)

### [rta-metrics](rt_route.md#id43)

#### [rtax-unspec (`unused`)](rt_route.md#id44)

value
:   0

#### [rtax-lock (`u32`)](rt_route.md#id45)

#### [rtax-mtu (`u32`)](rt_route.md#id46)

#### [rtax-window (`u32`)](rt_route.md#id47)

#### [rtax-rtt (`u32`)](rt_route.md#id48)

#### [rtax-rttvar (`u32`)](rt_route.md#id49)

#### [rtax-ssthresh (`u32`)](rt_route.md#id50)

#### [rtax-cwnd (`u32`)](rt_route.md#id51)

#### [rtax-advmss (`u32`)](rt_route.md#id52)

#### [rtax-reordering (`u32`)](rt_route.md#id53)

#### [rtax-hoplimit (`u32`)](rt_route.md#id54)

#### [rtax-initcwnd (`u32`)](rt_route.md#id55)

#### [rtax-features (`u32`)](rt_route.md#id56)

#### [rtax-rto-min (`u32`)](rt_route.md#id57)

#### [rtax-initrwnd (`u32`)](rt_route.md#id58)

#### [rtax-quickack (`u32`)](rt_route.md#id59)

#### [rtax-cc-algo (`string`)](rt_route.md#id60)

#### [rtax-fastopen-no-cookie (`u32`)](rt_route.md#id61)
