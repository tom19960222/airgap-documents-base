---
collection: kernel
version: "6.17"
title: "Family rt-link netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/rt-link.html
fetched_at: 2026-09-16T16:40:57+00:00
---
# [Family `rt-link` netlink specification](rt-link.md#id62)

Contents

- [Family `rt-link` netlink specification](rt-link.md#family-rt-link-netlink-specification)

  - [Summary](rt-link.md#summary)
  - [Operations](rt-link.md#operations)

    - [newlink](rt-link.md#newlink)
    - [newlink-ntf](rt-link.md#newlink-ntf)
    - [dellink](rt-link.md#dellink)
    - [getlink](rt-link.md#getlink)
    - [setlink](rt-link.md#setlink)
    - [getstats](rt-link.md#getstats)
  - [Multicast groups](rt-link.md#multicast-groups)
  - [Definitions](rt-link.md#definitions)

    - [ifinfo-flags](rt-link.md#ifinfo-flags)
    - [vlan-protocols](rt-link.md#vlan-protocols)
    - [rtgenmsg](rt-link.md#rtgenmsg)
    - [ifinfomsg](rt-link.md#ifinfomsg)
    - [ifla-bridge-id](rt-link.md#ifla-bridge-id)
    - [ifla-cacheinfo](rt-link.md#ifla-cacheinfo)
    - [rtnl-link-stats](rt-link.md#rtnl-link-stats)
    - [rtnl-link-stats64](rt-link.md#rtnl-link-stats64)
    - [rtnl-link-ifmap](rt-link.md#rtnl-link-ifmap)
    - [ipv4-devconf](rt-link.md#ipv4-devconf)
    - [ipv6-devconf](rt-link.md#ipv6-devconf)
    - [ifla-icmp6-stats](rt-link.md#ifla-icmp6-stats)
    - [ifla-inet6-stats](rt-link.md#ifla-inet6-stats)
    - [br-boolopt-multi](rt-link.md#br-boolopt-multi)
    - [if-stats-msg](rt-link.md#if-stats-msg)
    - [ifla-vlan-flags](rt-link.md#ifla-vlan-flags)
    - [vlan-flags](rt-link.md#vlan-flags)
    - [ifla-vlan-qos-mapping](rt-link.md#ifla-vlan-qos-mapping)
    - [ifla-geneve-port-range](rt-link.md#ifla-geneve-port-range)
    - [ifla-vf-mac](rt-link.md#ifla-vf-mac)
    - [ifla-vf-vlan](rt-link.md#ifla-vf-vlan)
    - [ifla-vf-tx-rate](rt-link.md#ifla-vf-tx-rate)
    - [ifla-vf-spoofchk](rt-link.md#ifla-vf-spoofchk)
    - [ifla-vf-link-state](rt-link.md#ifla-vf-link-state)
    - [ifla-vf-link-state-enum](rt-link.md#ifla-vf-link-state-enum)
    - [ifla-vf-rate](rt-link.md#ifla-vf-rate)
    - [ifla-vf-rss-query-en](rt-link.md#ifla-vf-rss-query-en)
    - [ifla-vf-trust](rt-link.md#ifla-vf-trust)
    - [ifla-vf-guid](rt-link.md#ifla-vf-guid)
    - [ifla-vf-vlan-info](rt-link.md#ifla-vf-vlan-info)
    - [rtext-filter](rt-link.md#rtext-filter)
    - [netkit-policy](rt-link.md#netkit-policy)
    - [netkit-mode](rt-link.md#netkit-mode)
    - [netkit-scrub](rt-link.md#netkit-scrub)
    - [ovpn-mode](rt-link.md#ovpn-mode)
  - [Attribute sets](rt-link.md#attribute-sets)

    - [link-attrs](rt-link.md#link-attrs)
    - [prop-list-link-attrs](rt-link.md#prop-list-link-attrs)
    - [af-spec-attrs](rt-link.md#af-spec-attrs)
    - [vfinfo-list-attrs](rt-link.md#vfinfo-list-attrs)
    - [vfinfo-attrs](rt-link.md#vfinfo-attrs)
    - [vf-stats-attrs](rt-link.md#vf-stats-attrs)
    - [vf-vlan-attrs](rt-link.md#vf-vlan-attrs)
    - [vf-ports-attrs](rt-link.md#vf-ports-attrs)
    - [port-self-attrs](rt-link.md#port-self-attrs)
    - [linkinfo-attrs](rt-link.md#linkinfo-attrs)
    - [linkinfo-bond-attrs](rt-link.md#linkinfo-bond-attrs)
    - [bond-ad-info-attrs](rt-link.md#bond-ad-info-attrs)
    - [bond-slave-attrs](rt-link.md#bond-slave-attrs)
    - [linkinfo-bridge-attrs](rt-link.md#linkinfo-bridge-attrs)
    - [linkinfo-brport-attrs](rt-link.md#linkinfo-brport-attrs)
    - [linkinfo-gre-attrs](rt-link.md#linkinfo-gre-attrs)
    - [linkinfo-gre6-attrs](rt-link.md#linkinfo-gre6-attrs)
    - [linkinfo-vti-attrs](rt-link.md#linkinfo-vti-attrs)
    - [linkinfo-vti6-attrs](rt-link.md#linkinfo-vti6-attrs)
    - [linkinfo-geneve-attrs](rt-link.md#linkinfo-geneve-attrs)
    - [linkinfo-iptun-attrs](rt-link.md#linkinfo-iptun-attrs)
    - [linkinfo-ip6tnl-attrs](rt-link.md#linkinfo-ip6tnl-attrs)
    - [linkinfo-tun-attrs](rt-link.md#linkinfo-tun-attrs)
    - [linkinfo-vlan-attrs](rt-link.md#linkinfo-vlan-attrs)
    - [ifla-vlan-qos](rt-link.md#ifla-vlan-qos)
    - [linkinfo-vrf-attrs](rt-link.md#linkinfo-vrf-attrs)
    - [xdp-attrs](rt-link.md#xdp-attrs)
    - [ifla-attrs](rt-link.md#ifla-attrs)
    - [ifla6-attrs](rt-link.md#ifla6-attrs)
    - [mctp-attrs](rt-link.md#mctp-attrs)
    - [stats-attrs](rt-link.md#stats-attrs)
    - [link-offload-xstats](rt-link.md#link-offload-xstats)
    - [hw-s-info-one](rt-link.md#hw-s-info-one)
    - [link-dpll-pin-attrs](rt-link.md#link-dpll-pin-attrs)
    - [linkinfo-netkit-attrs](rt-link.md#linkinfo-netkit-attrs)
    - [linkinfo-ovpn-attrs](rt-link.md#linkinfo-ovpn-attrs)
  - [Sub-messages](rt-link.md#sub-messages)

    - [linkinfo-data-msg](rt-link.md#linkinfo-data-msg)
    - [linkinfo-member-data-msg](rt-link.md#linkinfo-member-data-msg)

## [Summary](rt-link.md#id63)

Link configuration over rtnetlink.

## [Operations](rt-link.md#id64)

### [newlink](rt-link.md#id65)

Create a new link.

attribute-set:
:   [link-attrs](rt-link.md#rt-link-attribute-set-link-attrs)

fixed-header:
:   [ifinfomsg](rt-link.md#rt-link-definition-ifinfomsg)

do:
:   **request**
    :   attributes:
        :   [`ifname`, `net-ns-pid`, `net-ns-fd`, `target-netnsid`, `link-netnsid`, `linkinfo`, `group`, `num-tx-queues`, `num-rx-queues`, `address`, `broadcast`, `mtu`, `txqlen`, `operstate`, `linkmode`, `gso-max-size`, `gso-max-segs`, `gro-max-size`, `gso-ipv4-max-size`, `gro-ipv4-max-size`, `af-spec`]

### [newlink-ntf](rt-link.md#id66)

Notify that a link has been created

value:
:   16

notify:
:   getlink

fixed-header:
:   [ifinfomsg](rt-link.md#rt-link-definition-ifinfomsg)

### [dellink](rt-link.md#id67)

Delete an existing link.

attribute-set:
:   [link-attrs](rt-link.md#rt-link-attribute-set-link-attrs)

fixed-header:
:   [ifinfomsg](rt-link.md#rt-link-definition-ifinfomsg)

do:
:   **request**
    :   attributes:
        :   [`ifname`]

### [getlink](rt-link.md#id68)

Get / dump information about a link.

attribute-set:
:   [link-attrs](rt-link.md#rt-link-attribute-set-link-attrs)

fixed-header:
:   [ifinfomsg](rt-link.md#rt-link-definition-ifinfomsg)

do:
:   **request**
    :   attributes:
        :   [`ifname`, `alt-ifname`, `ext-mask`, `target-netnsid`]

    **reply**
    :   attributes:
        :   [`address`, `broadcast`, `ifname`, `mtu`, `link`, `qdisc`, `stats`, `cost`, `priority`, `master`, `wireless`, `protinfo`, `txqlen`, `map`, `weight`, `operstate`, `linkmode`, `linkinfo`, `net-ns-pid`, `ifalias`, `num-vf`, `vfinfo-list`, `stats64`, `vf-ports`, `port-self`, `af-spec`, `group`, `net-ns-fd`, `ext-mask`, `promiscuity`, `num-tx-queues`, `num-rx-queues`, `carrier`, `phys-port-id`, `carrier-changes`, `phys-switch-id`, `link-netnsid`, `phys-port-name`, `proto-down`, `gso-max-segs`, `gso-max-size`, `pad`, `xdp`, `event`, `new-netnsid`, `target-netnsid`, `carrier-up-count`, `carrier-down-count`, `new-ifindex`, `min-mtu`, `max-mtu`, `prop-list`, `perm-address`, `proto-down-reason`, `parent-dev-name`, `parent-dev-bus-name`, `gro-max-size`, `tso-max-size`, `tso-max-segs`, `allmulti`, `devlink-port`, `gso-ipv4-max-size`, `gro-ipv4-max-size`]

dump:
:   **request**
    :   attributes:
        :   [`target-netnsid`, `ext-mask`, `master`, `linkinfo`]

    **reply**
    :   attributes:
        :   [`address`, `broadcast`, `ifname`, `mtu`, `link`, `qdisc`, `stats`, `cost`, `priority`, `master`, `wireless`, `protinfo`, `txqlen`, `map`, `weight`, `operstate`, `linkmode`, `linkinfo`, `net-ns-pid`, `ifalias`, `num-vf`, `vfinfo-list`, `stats64`, `vf-ports`, `port-self`, `af-spec`, `group`, `net-ns-fd`, `ext-mask`, `promiscuity`, `num-tx-queues`, `num-rx-queues`, `carrier`, `phys-port-id`, `carrier-changes`, `phys-switch-id`, `link-netnsid`, `phys-port-name`, `proto-down`, `gso-max-segs`, `gso-max-size`, `pad`, `xdp`, `event`, `new-netnsid`, `target-netnsid`, `carrier-up-count`, `carrier-down-count`, `new-ifindex`, `min-mtu`, `max-mtu`, `prop-list`, `perm-address`, `proto-down-reason`, `parent-dev-name`, `parent-dev-bus-name`, `gro-max-size`, `tso-max-size`, `tso-max-segs`, `allmulti`, `devlink-port`, `gso-ipv4-max-size`, `gro-ipv4-max-size`]

### [setlink](rt-link.md#id69)

Set information about a link.

attribute-set:
:   [link-attrs](rt-link.md#rt-link-attribute-set-link-attrs)

fixed-header:
:   [ifinfomsg](rt-link.md#rt-link-definition-ifinfomsg)

do:
:   **request**
    :   attributes:
        :   [`address`, `broadcast`, `ifname`, `mtu`, `link`, `qdisc`, `stats`, `cost`, `priority`, `master`, `wireless`, `protinfo`, `txqlen`, `map`, `weight`, `operstate`, `linkmode`, `linkinfo`, `net-ns-pid`, `ifalias`, `num-vf`, `vfinfo-list`, `stats64`, `vf-ports`, `port-self`, `af-spec`, `group`, `net-ns-fd`, `ext-mask`, `promiscuity`, `num-tx-queues`, `num-rx-queues`, `carrier`, `phys-port-id`, `carrier-changes`, `phys-switch-id`, `link-netnsid`, `phys-port-name`, `proto-down`, `gso-max-segs`, `gso-max-size`, `pad`, `xdp`, `event`, `new-netnsid`, `target-netnsid`, `carrier-up-count`, `carrier-down-count`, `new-ifindex`, `min-mtu`, `max-mtu`, `prop-list`, `perm-address`, `proto-down-reason`, `parent-dev-name`, `parent-dev-bus-name`, `gro-max-size`, `tso-max-size`, `tso-max-segs`, `allmulti`, `devlink-port`, `gso-ipv4-max-size`, `gro-ipv4-max-size`]

### [getstats](rt-link.md#id70)

Get / dump link stats.

attribute-set:
:   [stats-attrs](rt-link.md#rt-link-attribute-set-stats-attrs)

fixed-header:
:   [if-stats-msg](rt-link.md#rt-link-definition-if-stats-msg)

do:
:   **request**

    **reply**
    :   attributes:
        :   [`link-64`, `link-xstats`, `link-xstats-slave`, `link-offload-xstats`, `af-spec`]

dump:
:   **request**

    **reply**
    :   attributes:
        :   [`link-64`, `link-xstats`, `link-xstats-slave`, `link-offload-xstats`, `af-spec`]

## [Multicast groups](rt-link.md#id71)

- rtnlgrp-link
- rtnlgrp-stats

## [Definitions](rt-link.md#id72)

### [ifinfo-flags](rt-link.md#id73)

type:
:   flags

header:
:   linux/if.h

enum-name:
:   net-device-flags

name-prefix:
:   iff-

entries:
:   up:

    broadcast:

    debug:

    loopback:

    point-to-point:

    no-trailers:

    running:

    no-arp:

    promisc:

    all-multi:

    master:

    slave:

    multicast:

    portsel:

    auto-media:

    dynamic:

    lower-up:

    dormant:

    echo:

### [vlan-protocols](rt-link.md#id74)

type:
:   enum

enum-name:
:   None

entries:
:   8021q:

    8021ad:

### [rtgenmsg](rt-link.md#id75)

type:
:   struct

members:
:   family (`u8`):

### [ifinfomsg](rt-link.md#id76)

type:
:   struct

members:
:   ifi-family (`u8`):

    ifi-type (`u16`):

    ifi-index (`s32`):

    ifi-flags (`u32`):

    ifi-change (`u32`):

### [ifla-bridge-id](rt-link.md#id77)

type:
:   struct

members:
:   prio (`u16`):

    addr (`binary`):

### [ifla-cacheinfo](rt-link.md#id78)

type:
:   struct

members:
:   max-reasm-len (`u32`):

    tstamp (`u32`):

    reachable-time (`s32`):

    retrans-time (`u32`):

### [rtnl-link-stats](rt-link.md#id79)

type:
:   struct

members:
:   rx-packets (`u32`):

    tx-packets (`u32`):

    rx-bytes (`u32`):

    tx-bytes (`u32`):

    rx-errors (`u32`):

    tx-errors (`u32`):

    rx-dropped (`u32`):

    tx-dropped (`u32`):

    multicast (`u32`):

    collisions (`u32`):

    rx-length-errors (`u32`):

    rx-over-errors (`u32`):

    rx-crc-errors (`u32`):

    rx-frame-errors (`u32`):

    rx-fifo-errors (`u32`):

    rx-missed-errors (`u32`):

    tx-aborted-errors (`u32`):

    tx-carrier-errors (`u32`):

    tx-fifo-errors (`u32`):

    tx-heartbeat-errors (`u32`):

    tx-window-errors (`u32`):

    rx-compressed (`u32`):

    tx-compressed (`u32`):

    rx-nohandler (`u32`):

### [rtnl-link-stats64](rt-link.md#id80)

type:
:   struct

members:
:   rx-packets (`u64`):

    tx-packets (`u64`):

    rx-bytes (`u64`):

    tx-bytes (`u64`):

    rx-errors (`u64`):

    tx-errors (`u64`):

    rx-dropped (`u64`):

    tx-dropped (`u64`):

    multicast (`u64`):

    collisions (`u64`):

    rx-length-errors (`u64`):

    rx-over-errors (`u64`):

    rx-crc-errors (`u64`):

    rx-frame-errors (`u64`):

    rx-fifo-errors (`u64`):

    rx-missed-errors (`u64`):

    tx-aborted-errors (`u64`):

    tx-carrier-errors (`u64`):

    tx-fifo-errors (`u64`):

    tx-heartbeat-errors (`u64`):

    tx-window-errors (`u64`):

    rx-compressed (`u64`):

    tx-compressed (`u64`):

    rx-nohandler (`u64`):

    rx-otherhost-dropped (`u64`):

### [rtnl-link-ifmap](rt-link.md#id81)

type:
:   struct

members:
:   mem-start (`u64`):

    mem-end (`u64`):

    base-addr (`u64`):

    irq (`u16`):

    dma (`u8`):

    port (`u8`):

### [ipv4-devconf](rt-link.md#id82)

enum-name:
:   None

type:
:   enum

entries:
:   forwarding:

    mc-forwarding:

    proxy-arp:

    accept-redirects:

    secure-redirects:

    send-redirects:

    shared-media:

    rp-filter:

    accept-source-route:

    bootp-relay:

    log-martians:

    tag:

    arpfilter:

    medium-id:

    noxfrm:

    nopolicy:

    force-igmp-version:

    arp-announce:

    arp-ignore:

    promote-secondaries:

    arp-accept:

    arp-notify:

    accept-local:

    src-vmark:

    proxy-arp-pvlan:

    route-localnet:

    igmpv2-unsolicited-report-interval:

    igmpv3-unsolicited-report-interval:

    ignore-routes-with-linkdown:

    drop-unicast-in-l2-multicast:

    drop-gratuitous-arp:

    bc-forwarding:

    arp-evict-nocarrier:

### [ipv6-devconf](rt-link.md#id83)

enum-name:
:   None

type:
:   enum

entries:
:   forwarding:

    hoplimit:

    mtu6:

    accept-ra:

    accept-redirects:

    autoconf:

    dad-transmits:

    rtr-solicits:

    rtr-solicit-interval:

    rtr-solicit-delay:

    use-tempaddr:

    temp-valid-lft:

    temp-prefered-lft:

    regen-max-retry:

    max-desync-factor:

    max-addresses:

    force-mld-version:

    accept-ra-defrtr:

    accept-ra-pinfo:

    accept-ra-rtr-pref:

    rtr-probe-interval:

    accept-ra-rt-info-max-plen:

    proxy-ndp:

    optimistic-dad:

    accept-source-route:

    mc-forwarding:

    disable-ipv6:

    accept-dad:

    force-tllao:

    ndisc-notify:

    mldv1-unsolicited-report-interval:

    mldv2-unsolicited-report-interval:

    suppress-frag-ndisc:

    accept-ra-from-local:

    use-optimistic:

    accept-ra-mtu:

    stable-secret:

    use-oif-addrs-only:

    accept-ra-min-hop-limit:

    ignore-routes-with-linkdown:

    drop-unicast-in-l2-multicast:

    drop-unsolicited-na:

    keep-addr-on-down:

    rtr-solicit-max-interval:

    seg6-enabled:

    seg6-require-hmac:

    enhanced-dad:

    addr-gen-mode:

    disable-policy:

    accept-ra-rt-info-min-plen:

    ndisc-tclass:

    rpl-seg-enabled:

    ra-defrtr-metric:

    ioam6-enabled:

    ioam6-id:

    ioam6-id-wide:

    ndisc-evict-nocarrier:

    accept-untracked-na:

### [ifla-icmp6-stats](rt-link.md#id84)

enum-name:
:   None

type:
:   enum

entries:
:   num:

    inmsgs:

    inerrors:

    outmsgs:

    outerrors:

    csumerrors:

    ratelimithost:

### [ifla-inet6-stats](rt-link.md#id85)

enum-name:
:   None

type:
:   enum

entries:
:   num:

    inpkts:

    inoctets:

    indelivers:

    outforwdatagrams:

    outpkts:

    outoctets:

    inhdrerrors:

    intoobigerrors:

    innoroutes:

    inaddrerrors:

    inunknownprotos:

    intruncatedpkts:

    indiscards:

    outdiscards:

    outnoroutes:

    reasmtimeout:

    reasmreqds:

    reasmoks:

    reasmfails:

    fragoks:

    fragfails:

    fragcreates:

    inmcastpkts:

    outmcastpkts:

    inbcastpkts:

    outbcastpkts:

    inmcastoctets:

    outmcastoctets:

    inbcastoctets:

    outbcastoctets:

    csumerrors:

    noectpkts:

    ect1-pkts:

    ect0-pkts:

    cepkts:

    reasm-overlaps:

### [br-boolopt-multi](rt-link.md#id86)

type:
:   struct

header:
:   linux/if_bridge.h

members:
:   optval (`u32`):

    optmask (`u32`):

### [if-stats-msg](rt-link.md#id87)

type:
:   struct

members:
:   family (`u8`):

    ifindex (`u32`):

    filter-mask (`u32`):

### [ifla-vlan-flags](rt-link.md#id88)

type:
:   struct

members:
:   flags (`u32`):

    mask (`u32`):

### [vlan-flags](rt-link.md#id89)

type:
:   flags

enum-name:
:   None

entries:
:   - `reorder-hdr`
    - `gvrp`
    - `loose-binding`
    - `mvrp`
    - `bridge-binding`

### [ifla-vlan-qos-mapping](rt-link.md#id90)

type:
:   struct

members:
:   from (`u32`):

    to (`u32`):

### [ifla-geneve-port-range](rt-link.md#id91)

type:
:   struct

members:
:   low (`u16`):

    high (`u16`):

### [ifla-vf-mac](rt-link.md#id92)

type:
:   struct

members:
:   vf (`u32`):

    mac (`binary`):

### [ifla-vf-vlan](rt-link.md#id93)

type:
:   struct

members:
:   vf (`u32`):

    vlan (`u32`):

    qos (`u32`):

### [ifla-vf-tx-rate](rt-link.md#id94)

type:
:   struct

members:
:   vf (`u32`):

    rate (`u32`):

### [ifla-vf-spoofchk](rt-link.md#id95)

type:
:   struct

members:
:   vf (`u32`):

    setting (`u32`):

### [ifla-vf-link-state](rt-link.md#id96)

type:
:   struct

members:
:   vf (`u32`):

    link-state (`u32`):

### [ifla-vf-link-state-enum](rt-link.md#id97)

type:
:   enum

enum-name:
:   None

entries:
:   - `auto`
    - `enable`
    - `disable`

### [ifla-vf-rate](rt-link.md#id98)

type:
:   struct

members:
:   vf (`u32`):

    min-tx-rate (`u32`):

    max-tx-rate (`u32`):

### [ifla-vf-rss-query-en](rt-link.md#id99)

type:
:   struct

members:
:   vf (`u32`):

    setting (`u32`):

### [ifla-vf-trust](rt-link.md#id100)

type:
:   struct

members:
:   vf (`u32`):

    setting (`u32`):

### [ifla-vf-guid](rt-link.md#id101)

type:
:   struct

members:
:   vf (`u32`):

    guid (`u64`):

### [ifla-vf-vlan-info](rt-link.md#id102)

type:
:   struct

members:
:   vf (`u32`):

    vlan (`u32`):

    qos (`u32`):

    vlan-proto (`u32`):

### [rtext-filter](rt-link.md#id103)

type:
:   flags

enum-name:
:   None

entries:
:   - `vf`
    - `brvlan`
    - `brvlan-compressed`
    - `skip-stats`
    - `mrp`
    - `cfm-config`
    - `cfm-status`
    - `mst`

### [netkit-policy](rt-link.md#id104)

type:
:   enum

enum-name:
:   None

entries:
:   forward:

    blackhole:

### [netkit-mode](rt-link.md#id105)

type:
:   enum

enum-name:
:   netkit-mode

entries:
:   l2:

    l3:

### [netkit-scrub](rt-link.md#id106)

type:
:   enum

enum-name:
:   None

entries:
:   none:

    default:

### [ovpn-mode](rt-link.md#id107)

enum-name:
:   ovpn-mode

name-prefix:
:   ovpn-mode

type:
:   enum

entries:
:   - `p2p`
    - `mp`

## [Attribute sets](rt-link.md#id108)

### [link-attrs](rt-link.md#id109)

#### address (`binary`)

display-hint:
:   mac

#### broadcast (`binary`)

display-hint:
:   mac

#### ifname (`string`)

#### mtu (`u32`)

#### link (`u32`)

#### qdisc (`string`)

#### stats (`binary`)

struct:
:   [rtnl-link-stats](rt-link.md#rt-link-definition-rtnl-link-stats)

#### cost (`string`)

#### priority (`string`)

#### master (`u32`)

#### wireless (`string`)

#### protinfo (`string`)

#### txqlen (`u32`)

#### map (`binary`)

struct:
:   [rtnl-link-ifmap](rt-link.md#rt-link-definition-rtnl-link-ifmap)

#### weight (`u32`)

#### operstate (`u8`)

#### linkmode (`u8`)

#### linkinfo (`nest`)

nested-attributes:
:   [linkinfo-attrs](rt-link.md#rt-link-attribute-set-linkinfo-attrs)

#### net-ns-pid (`u32`)

#### ifalias (`string`)

#### num-vf (`u32`)

#### vfinfo-list (`nest`)

nested-attributes:
:   [vfinfo-list-attrs](rt-link.md#rt-link-attribute-set-vfinfo-list-attrs)

#### stats64 (`binary`)

struct:
:   [rtnl-link-stats64](rt-link.md#rt-link-definition-rtnl-link-stats64)

#### vf-ports (`nest`)

nested-attributes:
:   [vf-ports-attrs](rt-link.md#rt-link-attribute-set-vf-ports-attrs)

#### port-self (`nest`)

nested-attributes:
:   [port-self-attrs](rt-link.md#rt-link-attribute-set-port-self-attrs)

#### af-spec (`nest`)

nested-attributes:
:   [af-spec-attrs](rt-link.md#rt-link-attribute-set-af-spec-attrs)

#### group (`u32`)

#### net-ns-fd (`u32`)

#### ext-mask (`u32`)

enum:
:   [rtext-filter](rt-link.md#rt-link-definition-rtext-filter)

enum-as-flags:
:   True

#### promiscuity (`u32`)

#### num-tx-queues (`u32`)

#### num-rx-queues (`u32`)

#### carrier (`u8`)

#### phys-port-id (`binary`)

#### carrier-changes (`u32`)

#### phys-switch-id (`binary`)

#### link-netnsid (`s32`)

#### phys-port-name (`string`)

#### proto-down (`u8`)

#### gso-max-segs (`u32`)

#### gso-max-size (`u32`)

#### pad (`pad`)

#### xdp (`nest`)

nested-attributes:
:   [xdp-attrs](rt-link.md#rt-link-attribute-set-xdp-attrs)

#### event (`u32`)

#### new-netnsid (`s32`)

#### target-netnsid (`s32`)

#### carrier-up-count (`u32`)

#### carrier-down-count (`u32`)

#### new-ifindex (`s32`)

#### min-mtu (`u32`)

#### max-mtu (`u32`)

#### prop-list (`nest`)

nested-attributes:
:   [prop-list-link-attrs](rt-link.md#rt-link-attribute-set-prop-list-link-attrs)

#### alt-ifname (`string`)

#### perm-address (`binary`)

display-hint:
:   mac

#### proto-down-reason (`string`)

#### parent-dev-name (`string`)

#### parent-dev-bus-name (`string`)

#### gro-max-size (`u32`)

#### tso-max-size (`u32`)

#### tso-max-segs (`u32`)

#### allmulti (`u32`)

#### devlink-port (`binary`)

#### gso-ipv4-max-size (`u32`)

#### gro-ipv4-max-size (`u32`)

#### dpll-pin (`nest`)

nested-attributes:
:   [link-dpll-pin-attrs](rt-link.md#rt-link-attribute-set-link-dpll-pin-attrs)

#### max-pacing-offload-horizon (`uint`)

doc:
:   EDT offload horizon supported by the device (in nsec).

#### netns-immutable (`u8`)

### [prop-list-link-attrs](rt-link.md#id110)

#### alt-ifname

multi-attr:
:   True

### [af-spec-attrs](rt-link.md#id111)

#### inet (`nest`)

value:
:   2

nested-attributes:
:   [ifla-attrs](rt-link.md#rt-link-attribute-set-ifla-attrs)

#### inet6 (`nest`)

value:
:   10

nested-attributes:
:   [ifla6-attrs](rt-link.md#rt-link-attribute-set-ifla6-attrs)

#### mctp (`nest`)

value:
:   45

nested-attributes:
:   [mctp-attrs](rt-link.md#rt-link-attribute-set-mctp-attrs)

### [vfinfo-list-attrs](rt-link.md#id112)

#### info (`nest`)

nested-attributes:
:   [vfinfo-attrs](rt-link.md#rt-link-attribute-set-vfinfo-attrs)

multi-attr:
:   True

### [vfinfo-attrs](rt-link.md#id113)

#### mac (`binary`)

struct:
:   [ifla-vf-mac](rt-link.md#rt-link-definition-ifla-vf-mac)

#### vlan (`binary`)

struct:
:   [ifla-vf-vlan](rt-link.md#rt-link-definition-ifla-vf-vlan)

#### tx-rate (`binary`)

struct:
:   [ifla-vf-tx-rate](rt-link.md#rt-link-definition-ifla-vf-tx-rate)

#### spoofchk (`binary`)

struct:
:   [ifla-vf-spoofchk](rt-link.md#rt-link-definition-ifla-vf-spoofchk)

#### link-state (`binary`)

struct:
:   [ifla-vf-link-state](rt-link.md#rt-link-definition-ifla-vf-link-state)

#### rate (`binary`)

struct:
:   [ifla-vf-rate](rt-link.md#rt-link-definition-ifla-vf-rate)

#### rss-query-en (`binary`)

struct:
:   [ifla-vf-rss-query-en](rt-link.md#rt-link-definition-ifla-vf-rss-query-en)

#### stats (`nest`)

nested-attributes:
:   [vf-stats-attrs](rt-link.md#rt-link-attribute-set-vf-stats-attrs)

#### trust (`binary`)

struct:
:   [ifla-vf-trust](rt-link.md#rt-link-definition-ifla-vf-trust)

#### ib-node-guid (`binary`)

struct:
:   [ifla-vf-guid](rt-link.md#rt-link-definition-ifla-vf-guid)

#### ib-port-guid (`binary`)

struct:
:   [ifla-vf-guid](rt-link.md#rt-link-definition-ifla-vf-guid)

#### vlan-list (`nest`)

nested-attributes:
:   [vf-vlan-attrs](rt-link.md#rt-link-attribute-set-vf-vlan-attrs)

#### broadcast (`binary`)

### [vf-stats-attrs](rt-link.md#id114)

#### rx-packets (`u64`)

value:
:   0

#### tx-packets (`u64`)

#### rx-bytes (`u64`)

#### tx-bytes (`u64`)

#### broadcast (`u64`)

#### multicast (`u64`)

#### pad (`pad`)

#### rx-dropped (`u64`)

#### tx-dropped (`u64`)

### [vf-vlan-attrs](rt-link.md#id115)

#### info (`binary`)

struct:
:   [ifla-vf-vlan-info](rt-link.md#rt-link-definition-ifla-vf-vlan-info)

multi-attr:
:   True

### [vf-ports-attrs](rt-link.md#id116)

### [port-self-attrs](rt-link.md#id117)

### [linkinfo-attrs](rt-link.md#id118)

#### kind (`string`)

#### data (`sub-message`)

sub-message:
:   [linkinfo-data-msg](rt-link.md#rt-link-sub-message-linkinfo-data-msg)

selector:
:   kind

#### xstats (`binary`)

#### slave-kind (`string`)

#### slave-data (`sub-message`)

sub-message:
:   [linkinfo-member-data-msg](rt-link.md#rt-link-sub-message-linkinfo-member-data-msg)

selector:
:   slave-kind

### [linkinfo-bond-attrs](rt-link.md#id119)

#### mode (`u8`)

#### active-slave (`u32`)

#### miimon (`u32`)

#### updelay (`u32`)

#### downdelay (`u32`)

#### use-carrier (`u8`)

#### arp-interval (`u32`)

#### arp-ip-target (`indexed-array`)

sub-type:
:   u32

byte-order:
:   big-endian

display-hint:
:   ipv4

#### arp-validate (`u32`)

#### arp-all-targets (`u32`)

#### primary (`u32`)

#### primary-reselect (`u8`)

#### fail-over-mac (`u8`)

#### xmit-hash-policy (`u8`)

#### resend-igmp (`u32`)

#### num-peer-notif (`u8`)

#### all-slaves-active (`u8`)

#### min-links (`u32`)

#### lp-interval (`u32`)

#### packets-per-slave (`u32`)

#### ad-lacp-rate (`u8`)

#### ad-select (`u8`)

#### ad-info (`nest`)

nested-attributes:
:   [bond-ad-info-attrs](rt-link.md#rt-link-attribute-set-bond-ad-info-attrs)

#### ad-actor-sys-prio (`u16`)

#### ad-user-port-key (`u16`)

#### ad-actor-system (`binary`)

display-hint:
:   mac

#### tlb-dynamic-lb (`u8`)

#### peer-notif-delay (`u32`)

#### ad-lacp-active (`u8`)

#### missed-max (`u8`)

#### ns-ip6-target (`indexed-array`)

sub-type:
:   binary

display-hint:
:   ipv6

#### coupled-control (`u8`)

### [bond-ad-info-attrs](rt-link.md#id120)

#### aggregator (`u16`)

#### num-ports (`u16`)

#### actor-key (`u16`)

#### partner-key (`u16`)

#### partner-mac (`binary`)

display-hint:
:   mac

### [bond-slave-attrs](rt-link.md#id121)

#### state (`u8`)

#### mii-status (`u8`)

#### link-failure-count (`u32`)

#### perm-hwaddr (`binary`)

display-hint:
:   mac

#### queue-id (`u16`)

#### ad-aggregator-id (`u16`)

#### ad-actor-oper-port-state (`u8`)

#### ad-partner-oper-port-state (`u16`)

#### prio (`u32`)

### [linkinfo-bridge-attrs](rt-link.md#id122)

#### forward-delay (`u32`)

#### hello-time (`u32`)

#### max-age (`u32`)

#### ageing-time (`u32`)

#### stp-state (`u32`)

#### priority (`u16`)

#### vlan-filtering (`u8`)

#### vlan-protocol (`u16`)

#### group-fwd-mask (`u16`)

#### root-id (`binary`)

struct:
:   [ifla-bridge-id](rt-link.md#rt-link-definition-ifla-bridge-id)

#### bridge-id (`binary`)

struct:
:   [ifla-bridge-id](rt-link.md#rt-link-definition-ifla-bridge-id)

#### root-port (`u16`)

#### root-path-cost (`u32`)

#### topology-change (`u8`)

#### topology-change-detected (`u8`)

#### hello-timer (`u64`)

#### tcn-timer (`u64`)

#### topology-change-timer (`u64`)

#### gc-timer (`u64`)

#### group-addr (`binary`)

display-hint:
:   mac

#### fdb-flush (`binary`)

#### mcast-router (`u8`)

#### mcast-snooping (`u8`)

#### mcast-query-use-ifaddr (`u8`)

#### mcast-querier (`u8`)

#### mcast-hash-elasticity (`u32`)

#### mcast-hash-max (`u32`)

#### mcast-last-member-cnt (`u32`)

#### mcast-startup-query-cnt (`u32`)

#### mcast-last-member-intvl (`u64`)

#### mcast-membership-intvl (`u64`)

#### mcast-querier-intvl (`u64`)

#### mcast-query-intvl (`u64`)

#### mcast-query-response-intvl (`u64`)

#### mcast-startup-query-intvl (`u64`)

#### nf-call-iptables (`u8`)

#### nf-call-ip6tables (`u8`)

#### nf-call-arptables (`u8`)

#### vlan-default-pvid (`u16`)

#### pad (`pad`)

#### vlan-stats-enabled (`u8`)

#### mcast-stats-enabled (`u8`)

#### mcast-igmp-version (`u8`)

#### mcast-mld-version (`u8`)

#### vlan-stats-per-port (`u8`)

#### multi-boolopt (`binary`)

struct:
:   [br-boolopt-multi](rt-link.md#rt-link-definition-br-boolopt-multi)

#### mcast-querier-state (`binary`)

#### fdb-n-learned (`u32`)

#### fdb-max-learned (`u32`)

### [linkinfo-brport-attrs](rt-link.md#id123)

#### state (`u8`)

#### priority (`u16`)

#### cost (`u32`)

#### mode (`flag`)

#### guard (`flag`)

#### protect (`flag`)

#### fast-leave (`flag`)

#### learning (`flag`)

#### unicast-flood (`flag`)

#### proxyarp (`flag`)

#### learning-sync (`flag`)

#### proxyarp-wifi (`flag`)

#### root-id (`binary`)

struct:
:   [ifla-bridge-id](rt-link.md#rt-link-definition-ifla-bridge-id)

#### bridge-id (`binary`)

struct:
:   [ifla-bridge-id](rt-link.md#rt-link-definition-ifla-bridge-id)

#### designated-port (`u16`)

#### designated-cost (`u16`)

#### id (`u16`)

#### no (`u16`)

#### topology-change-ack (`u8`)

#### config-pending (`u8`)

#### message-age-timer (`u64`)

#### forward-delay-timer (`u64`)

#### hold-timer (`u64`)

#### flush (`flag`)

#### multicast-router (`u8`)

#### pad (`pad`)

#### mcast-flood (`flag`)

#### mcast-to-ucast (`flag`)

#### vlan-tunnel (`flag`)

#### bcast-flood (`flag`)

#### group-fwd-mask (`u16`)

#### neigh-suppress (`flag`)

#### isolated (`flag`)

#### backup-port (`u32`)

#### mrp-ring-open (`flag`)

#### mrp-in-open (`flag`)

#### mcast-eht-hosts-limit (`u32`)

#### mcast-eht-hosts-cnt (`u32`)

#### locked (`flag`)

#### mab (`flag`)

#### mcast-n-groups (`u32`)

#### mcast-max-groups (`u32`)

#### neigh-vlan-suppress (`flag`)

#### backup-nhid (`u32`)

### [linkinfo-gre-attrs](rt-link.md#id124)

#### link (`u32`)

#### iflags (`u16`)

byte-order:
:   big-endian

#### oflags (`u16`)

byte-order:
:   big-endian

#### ikey (`u32`)

byte-order:
:   big-endian

#### okey (`u32`)

byte-order:
:   big-endian

#### local (`binary`)

display-hint:
:   ipv4

#### remote (`binary`)

display-hint:
:   ipv4

#### ttl (`u8`)

#### tos (`u8`)

#### pmtudisc (`u8`)

#### encap-limit (`u8`)

#### flowinfo (`u32`)

byte-order:
:   big-endian

#### flags (`u32`)

#### encap-type (`u16`)

#### encap-flags (`u16`)

#### encap-sport (`u16`)

byte-order:
:   big-endian

#### encap-dport (`u16`)

byte-order:
:   big-endian

#### collect-metadata (`flag`)

#### ignore-df (`u8`)

#### fwmark (`u32`)

#### erspan-index (`u32`)

#### erspan-ver (`u8`)

#### erspan-dir (`u8`)

#### erspan-hwid (`u16`)

### [linkinfo-gre6-attrs](rt-link.md#id125)

#### link

#### iflags

#### oflags

#### ikey

#### okey

#### local

display-hint:
:   ipv6

#### remote

display-hint:
:   ipv6

#### ttl

#### encap-limit

#### flowinfo

#### flags

#### encap-type

#### encap-flags

#### encap-sport

#### encap-dport

#### collect-metadata

#### fwmark

#### erspan-index

#### erspan-ver

#### erspan-dir

#### erspan-hwid

### [linkinfo-vti-attrs](rt-link.md#id126)

#### link (`u32`)

#### ikey (`u32`)

byte-order:
:   big-endian

#### okey (`u32`)

byte-order:
:   big-endian

#### local (`binary`)

display-hint:
:   ipv4

#### remote (`binary`)

display-hint:
:   ipv4

#### fwmark (`u32`)

### [linkinfo-vti6-attrs](rt-link.md#id127)

#### link

#### ikey

#### okey

#### local

display-hint:
:   ipv6

#### remote

display-hint:
:   ipv6

#### fwmark

### [linkinfo-geneve-attrs](rt-link.md#id128)

#### id (`u32`)

#### remote (`binary`)

display-hint:
:   ipv4

#### ttl (`u8`)

#### tos (`u8`)

#### port (`u16`)

byte-order:
:   big-endian

#### collect-metadata (`flag`)

#### remote6 (`binary`)

display-hint:
:   ipv6

#### udp-csum (`u8`)

#### udp-zero-csum6-tx (`u8`)

#### udp-zero-csum6-rx (`u8`)

#### label (`u32`)

byte-order:
:   big-endian

#### ttl-inherit (`u8`)

#### df (`u8`)

#### inner-proto-inherit (`flag`)

#### port-range (`binary`)

struct:
:   [ifla-geneve-port-range](rt-link.md#rt-link-definition-ifla-geneve-port-range)

### [linkinfo-iptun-attrs](rt-link.md#id129)

#### link (`u32`)

#### local (`binary`)

display-hint:
:   ipv4

#### remote (`binary`)

display-hint:
:   ipv4

#### ttl (`u8`)

#### tos (`u8`)

#### encap-limit (`u8`)

#### flowinfo (`u32`)

byte-order:
:   big-endian

#### flags (`u16`)

byte-order:
:   big-endian

#### proto (`u8`)

#### pmtudisc (`u8`)

#### 6rd-prefix (`binary`)

display-hint:
:   ipv6

#### 6rd-relay-prefix (`binary`)

display-hint:
:   ipv4

#### 6rd-prefixlen (`u16`)

#### 6rd-relay-prefixlen (`u16`)

#### encap-type (`u16`)

#### encap-flags (`u16`)

#### encap-sport (`u16`)

byte-order:
:   big-endian

#### encap-dport (`u16`)

byte-order:
:   big-endian

#### collect-metadata (`flag`)

#### fwmark (`u32`)

### [linkinfo-ip6tnl-attrs](rt-link.md#id130)

#### link

#### local

display-hint:
:   ipv6

#### remote

display-hint:
:   ipv6

#### ttl

#### encap-limit

#### flowinfo

#### flags (`u32`)

#### proto

#### encap-type

#### encap-flags

#### encap-sport

#### encap-dport

#### collect-metadata

#### fwmark

### [linkinfo-tun-attrs](rt-link.md#id131)

#### owner (`u32`)

#### group (`u32`)

#### type (`u8`)

#### pi (`u8`)

#### vnet-hdr (`u8`)

#### persist (`u8`)

#### multi-queue (`u8`)

#### num-queues (`u32`)

#### num-disabled-queues (`u32`)

### [linkinfo-vlan-attrs](rt-link.md#id132)

#### id (`u16`)

#### flags (`binary`)

struct:
:   [ifla-vlan-flags](rt-link.md#rt-link-definition-ifla-vlan-flags)

#### egress-qos (`nest`)

nested-attributes:
:   [ifla-vlan-qos](rt-link.md#rt-link-attribute-set-ifla-vlan-qos)

#### ingress-qos (`nest`)

nested-attributes:
:   [ifla-vlan-qos](rt-link.md#rt-link-attribute-set-ifla-vlan-qos)

#### protocol (`u16`)

enum:
:   [vlan-protocols](rt-link.md#rt-link-definition-vlan-protocols)

byte-order:
:   big-endian

### [ifla-vlan-qos](rt-link.md#id133)

#### mapping (`binary`)

multi-attr:
:   True

struct:
:   [ifla-vlan-qos-mapping](rt-link.md#rt-link-definition-ifla-vlan-qos-mapping)

### [linkinfo-vrf-attrs](rt-link.md#id134)

#### table (`u32`)

### [xdp-attrs](rt-link.md#id135)

#### fd (`s32`)

#### attached (`u8`)

#### flags (`u32`)

#### prog-id (`u32`)

#### drv-prog-id (`u32`)

#### skb-prog-id (`u32`)

#### hw-prog-id (`u32`)

#### expected-fd (`s32`)

### [ifla-attrs](rt-link.md#id136)

#### conf (`binary`)

sub-type:
:   u32

doc:
:   u32 indexed by ipv4-devconf - 1 on output, on input it’s a nest

### [ifla6-attrs](rt-link.md#id137)

#### flags (`u32`)

#### conf (`binary`)

sub-type:
:   u32

doc:
:   u32 indexed by ipv6-devconf - 1 on output, on input it’s a nest

#### stats (`binary`)

sub-type:
:   u64

#### mcast (`binary`)

#### cacheinfo (`binary`)

struct:
:   [ifla-cacheinfo](rt-link.md#rt-link-definition-ifla-cacheinfo)

#### icmp6stats (`binary`)

sub-type:
:   u64

#### token (`binary`)

#### addr-gen-mode (`u8`)

#### ra-mtu (`u32`)

### [mctp-attrs](rt-link.md#id138)

#### net (`u32`)

#### phys-binding (`u8`)

### [stats-attrs](rt-link.md#id139)

#### link-64 (`binary`)

struct:
:   [rtnl-link-stats64](rt-link.md#rt-link-definition-rtnl-link-stats64)

#### link-xstats (`binary`)

#### link-xstats-slave (`binary`)

#### link-offload-xstats (`nest`)

nested-attributes:
:   [link-offload-xstats](rt-link.md#rt-link-attribute-set-link-offload-xstats)

#### af-spec (`binary`)

### [link-offload-xstats](rt-link.md#id140)

#### cpu-hit (`binary`)

#### hw-s-info (`indexed-array`)

sub-type:
:   nest

nested-attributes:
:   [hw-s-info-one](rt-link.md#rt-link-attribute-set-hw-s-info-one)

#### l3-stats (`binary`)

### [hw-s-info-one](rt-link.md#id141)

#### request (`u8`)

#### used (`u8`)

### [link-dpll-pin-attrs](rt-link.md#id142)

#### id (`u32`)

### [linkinfo-netkit-attrs](rt-link.md#id143)

#### peer-info (`binary`)

#### primary (`u8`)

#### policy (`u32`)

enum:
:   [netkit-policy](rt-link.md#rt-link-definition-netkit-policy)

#### peer-policy (`u32`)

enum:
:   [netkit-policy](rt-link.md#rt-link-definition-netkit-policy)

#### mode (`u32`)

enum:
:   [netkit-mode](rt-link.md#rt-link-definition-netkit-mode)

#### scrub (`u32`)

enum:
:   [netkit-scrub](rt-link.md#rt-link-definition-netkit-scrub)

#### peer-scrub (`u32`)

enum:
:   [netkit-scrub](rt-link.md#rt-link-definition-netkit-scrub)

#### headroom (`u16`)

#### tailroom (`u16`)

### [linkinfo-ovpn-attrs](rt-link.md#id144)

#### mode (`u8`)

enum:
:   [ovpn-mode](rt-link.md#rt-link-definition-ovpn-mode)

## [Sub-messages](rt-link.md#id145)

### [linkinfo-data-msg](rt-link.md#id146)

- **bond**
  :   attribute-set:
      :   [linkinfo-bond-attrs](rt-link.md#rt-link-attribute-set-linkinfo-bond-attrs)
- **bridge**
  :   attribute-set:
      :   [linkinfo-bridge-attrs](rt-link.md#rt-link-attribute-set-linkinfo-bridge-attrs)
- **erspan**
  :   attribute-set:
      :   [linkinfo-gre-attrs](rt-link.md#rt-link-attribute-set-linkinfo-gre-attrs)
- **gre**
  :   attribute-set:
      :   [linkinfo-gre-attrs](rt-link.md#rt-link-attribute-set-linkinfo-gre-attrs)
- **gretap**
  :   attribute-set:
      :   [linkinfo-gre-attrs](rt-link.md#rt-link-attribute-set-linkinfo-gre-attrs)
- **ip6gre**
  :   attribute-set:
      :   [linkinfo-gre6-attrs](rt-link.md#rt-link-attribute-set-linkinfo-gre6-attrs)
- **geneve**
  :   attribute-set:
      :   [linkinfo-geneve-attrs](rt-link.md#rt-link-attribute-set-linkinfo-geneve-attrs)
- **ipip**
  :   attribute-set:
      :   [linkinfo-iptun-attrs](rt-link.md#rt-link-attribute-set-linkinfo-iptun-attrs)
- **ip6tnl**
  :   attribute-set:
      :   [linkinfo-ip6tnl-attrs](rt-link.md#rt-link-attribute-set-linkinfo-ip6tnl-attrs)
- **sit**
  :   attribute-set:
      :   [linkinfo-iptun-attrs](rt-link.md#rt-link-attribute-set-linkinfo-iptun-attrs)
- **tun**
  :   attribute-set:
      :   [linkinfo-tun-attrs](rt-link.md#rt-link-attribute-set-linkinfo-tun-attrs)
- **vlan**
  :   attribute-set:
      :   [linkinfo-vlan-attrs](rt-link.md#rt-link-attribute-set-linkinfo-vlan-attrs)
- **vrf**
  :   attribute-set:
      :   [linkinfo-vrf-attrs](rt-link.md#rt-link-attribute-set-linkinfo-vrf-attrs)
- **vti**
  :   attribute-set:
      :   [linkinfo-vti-attrs](rt-link.md#rt-link-attribute-set-linkinfo-vti-attrs)
- **vti6**
  :   attribute-set:
      :   [linkinfo-vti6-attrs](rt-link.md#rt-link-attribute-set-linkinfo-vti6-attrs)
- **netkit**
  :   attribute-set:
      :   [linkinfo-netkit-attrs](rt-link.md#rt-link-attribute-set-linkinfo-netkit-attrs)
- **ovpn**
  :   attribute-set:
      :   [linkinfo-ovpn-attrs](rt-link.md#rt-link-attribute-set-linkinfo-ovpn-attrs)

### [linkinfo-member-data-msg](rt-link.md#id147)

- **bridge**
  :   attribute-set:
      :   [linkinfo-brport-attrs](rt-link.md#rt-link-attribute-set-linkinfo-brport-attrs)
- **bond**
  :   attribute-set:
      :   [bond-slave-attrs](rt-link.md#rt-link-attribute-set-bond-slave-attrs)
