---
collection: kernel
version: "6.8"
title: "Family netdev netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/netdev.html
fetched_at: 2026-08-21T03:49:18+00:00
---
# [Family `netdev` netlink specification](netdev.md#id5)

Contents

- [Family `netdev` netlink specification](netdev.md#family-netdev-netlink-specification)

  - [Summary](netdev.md#summary)
  - [Operations](netdev.md#operations)

    - [dev-get](netdev.md#dev-get)
    - [dev-add-ntf](netdev.md#dev-add-ntf)
    - [dev-del-ntf](netdev.md#dev-del-ntf)
    - [dev-change-ntf](netdev.md#dev-change-ntf)
    - [page-pool-get](netdev.md#page-pool-get)
    - [page-pool-add-ntf](netdev.md#page-pool-add-ntf)
    - [page-pool-del-ntf](netdev.md#page-pool-del-ntf)
    - [page-pool-change-ntf](netdev.md#page-pool-change-ntf)
    - [page-pool-stats-get](netdev.md#page-pool-stats-get)
    - [queue-get](netdev.md#queue-get)
    - [napi-get](netdev.md#napi-get)
  - [Multicast groups](netdev.md#multicast-groups)
  - [Definitions](netdev.md#definitions)

    - [xdp-act](netdev.md#xdp-act)
    - [xdp-rx-metadata](netdev.md#xdp-rx-metadata)
    - [xsk-flags](netdev.md#xsk-flags)
    - [queue-type](netdev.md#queue-type)
  - [Attribute sets](netdev.md#attribute-sets)

    - [dev](netdev.md#dev)

      - [ifindex (`u32`)](netdev.md#ifindex-u32)
      - [pad (`pad`)](netdev.md#pad-pad)
      - [xdp-features (`u64`)](netdev.md#xdp-features-u64)
      - [xdp-zc-max-segs (`u32`)](netdev.md#xdp-zc-max-segs-u32)
      - [xdp-rx-metadata-features (`u64`)](netdev.md#xdp-rx-metadata-features-u64)
      - [xsk-features (`u64`)](netdev.md#xsk-features-u64)
    - [page-pool](netdev.md#page-pool)

      - [id (`uint`)](netdev.md#id-uint)
      - [ifindex (`u32`)](netdev.md#id1)
      - [napi-id (`uint`)](netdev.md#napi-id-uint)
      - [inflight (`uint`)](netdev.md#inflight-uint)
      - [inflight-mem (`uint`)](netdev.md#inflight-mem-uint)
      - [detach-time (`uint`)](netdev.md#detach-time-uint)
    - [page-pool-info](netdev.md#page-pool-info)

      - [id](netdev.md#id)
      - [ifindex](netdev.md#ifindex)
    - [page-pool-stats](netdev.md#page-pool-stats)

      - [info (`nest`)](netdev.md#info-nest)
      - [alloc-fast (`uint`)](netdev.md#alloc-fast-uint)
      - [alloc-slow (`uint`)](netdev.md#alloc-slow-uint)
      - [alloc-slow-high-order (`uint`)](netdev.md#alloc-slow-high-order-uint)
      - [alloc-empty (`uint`)](netdev.md#alloc-empty-uint)
      - [alloc-refill (`uint`)](netdev.md#alloc-refill-uint)
      - [alloc-waive (`uint`)](netdev.md#alloc-waive-uint)
      - [recycle-cached (`uint`)](netdev.md#recycle-cached-uint)
      - [recycle-cache-full (`uint`)](netdev.md#recycle-cache-full-uint)
      - [recycle-ring (`uint`)](netdev.md#recycle-ring-uint)
      - [recycle-ring-full (`uint`)](netdev.md#recycle-ring-full-uint)
      - [recycle-released-refcnt (`uint`)](netdev.md#recycle-released-refcnt-uint)
    - [napi](netdev.md#napi)

      - [ifindex (`u32`)](netdev.md#id2)
      - [id (`u32`)](netdev.md#id-u32)
      - [irq (`u32`)](netdev.md#irq-u32)
      - [pid (`u32`)](netdev.md#pid-u32)
    - [queue](netdev.md#queue)

      - [id (`u32`)](netdev.md#id3)
      - [ifindex (`u32`)](netdev.md#id4)
      - [type (`u32`)](netdev.md#type-u32)
      - [napi-id (`u32`)](netdev.md#napi-id-u32)

## [Summary](netdev.md#id6)

netdev configuration over generic netlink.

## [Operations](netdev.md#id7)

### [dev-get](netdev.md#id8)

Get / dump information about a netdev.

attribute-set
:   dev

do
:   **request**
    :   attributes
        :   [`ifindex`]

    **reply**
    :   attributes
        :   [`ifindex`, `xdp-features`, `xdp-zc-max-segs`, `xdp-rx-metadata-features`, `xsk-features`]

dump
:   **reply**
    :   attributes
        :   [`ifindex`, `xdp-features`, `xdp-zc-max-segs`, `xdp-rx-metadata-features`, `xsk-features`]

### [dev-add-ntf](netdev.md#id9)

Notification about device appearing.

notify
:   dev-get

mcgrp
:   mgmt

### [dev-del-ntf](netdev.md#id10)

Notification about device disappearing.

notify
:   dev-get

mcgrp
:   mgmt

### [dev-change-ntf](netdev.md#id11)

Notification about device configuration being changed.

notify
:   dev-get

mcgrp
:   mgmt

### [page-pool-get](netdev.md#id12)

Get / dump information about Page Pools.(Only Page Pools associated with a net_device can be listed.)

attribute-set
:   page-pool

config-cond
:   page-pool

do
:   **request**
    :   attributes
        :   [`id`]

    **reply**
    :   attributes
        :   [`id`, `ifindex`, `napi-id`, `inflight`, `inflight-mem`, `detach-time`]

dump
:   **reply**
    :   attributes
        :   [`id`, `ifindex`, `napi-id`, `inflight`, `inflight-mem`, `detach-time`]

### [page-pool-add-ntf](netdev.md#id13)

Notification about page pool appearing.

notify
:   page-pool-get

mcgrp
:   page-pool

config-cond
:   page-pool

### [page-pool-del-ntf](netdev.md#id14)

Notification about page pool disappearing.

notify
:   page-pool-get

mcgrp
:   page-pool

config-cond
:   page-pool

### [page-pool-change-ntf](netdev.md#id15)

Notification about page pool configuration being changed.

notify
:   page-pool-get

mcgrp
:   page-pool

config-cond
:   page-pool

### [page-pool-stats-get](netdev.md#id16)

Get page pool statistics.

attribute-set
:   page-pool-stats

config-cond
:   page-pool-stats

do
:   **request**
    :   attributes
        :   [`info`]

    **reply**
    :   attributes
        :   [`info`, `alloc-fast`, `alloc-slow`, `alloc-slow-high-order`, `alloc-empty`, `alloc-refill`, `alloc-waive`, `recycle-cached`, `recycle-cache-full`, `recycle-ring`, `recycle-ring-full`, `recycle-released-refcnt`]

dump
:   **reply**
    :   attributes
        :   [`info`, `alloc-fast`, `alloc-slow`, `alloc-slow-high-order`, `alloc-empty`, `alloc-refill`, `alloc-waive`, `recycle-cached`, `recycle-cache-full`, `recycle-ring`, `recycle-ring-full`, `recycle-released-refcnt`]

### [queue-get](netdev.md#id17)

Get queue information from the kernel. Only configured queues will be reported (as opposed to all available hardware queues).

attribute-set
:   queue

do
:   **request**
    :   attributes
        :   [`ifindex`, `type`, `id`]

    **reply**
    :   attributes
        :   [`id`, `type`, `napi-id`, `ifindex`]

dump
:   **request**
    :   attributes
        :   [`ifindex`]

    **reply**
    :   attributes
        :   [`id`, `type`, `napi-id`, `ifindex`]

### [napi-get](netdev.md#id18)

Get information about NAPI instances configured on the system.

attribute-set
:   napi

do
:   **request**
    :   attributes
        :   [`id`]

    **reply**
    :   attributes
        :   [`id`, `ifindex`, `irq`, `pid`]

dump
:   **request**
    :   attributes
        :   [`ifindex`]

    **reply**
    :   attributes
        :   [`id`, `ifindex`, `irq`, `pid`]

## [Multicast groups](netdev.md#id19)

- mgmt
- page-pool

## [Definitions](netdev.md#id20)

### [xdp-act](netdev.md#id21)

type
:   flags

entries
:   basic
    :   XDP features set supported by all drivers (XDP_ABORTED, XDP_DROP, XDP_PASS, XDP_TX)

    redirect
    :   The netdev supports XDP_REDIRECT

    ndo-xmit
    :   This feature informs if netdev implements ndo_xdp_xmit callback.

    xsk-zerocopy
    :   This feature informs if netdev supports AF_XDP in zero copy mode.

    hw-offload
    :   This feature informs if netdev supports XDP hw offloading.

    rx-sg
    :   This feature informs if netdev implements non-linear XDP buffer support in the driver napi callback.

    ndo-xmit-sg
    :   This feature informs if netdev implements non-linear XDP buffer support in ndo_xdp_xmit callback.

### [xdp-rx-metadata](netdev.md#id22)

type
:   flags

entries
:   timestamp
    :   Device is capable of exposing receive HW timestamp via [`bpf_xdp_metadata_rx_timestamp()`](../xdp-rx-metadata.md#c.bpf_xdp_metadata_rx_timestamp "bpf_xdp_metadata_rx_timestamp").

    hash
    :   Device is capable of exposing receive packet hash via [`bpf_xdp_metadata_rx_hash()`](../xdp-rx-metadata.md#c.bpf_xdp_metadata_rx_hash "bpf_xdp_metadata_rx_hash").

    vlan-tag
    :   Device is capable of exposing receive packet VLAN tag via [`bpf_xdp_metadata_rx_vlan_tag()`](../xdp-rx-metadata.md#c.bpf_xdp_metadata_rx_vlan_tag "bpf_xdp_metadata_rx_vlan_tag").

### [xsk-flags](netdev.md#id23)

type
:   flags

entries
:   tx-timestamp
    :   HW timestamping egress packets is supported by the driver.

    tx-checksum
    :   L3 checksum HW offload is supported by the driver.

### [queue-type](netdev.md#id24)

type
:   enum

entries
:   - `rx`
    - `tx`

## [Attribute sets](netdev.md#id25)

### [dev](netdev.md#id26)

#### [ifindex (`u32`)](netdev.md#id27)

doc
:   netdev ifindex

#### [pad (`pad`)](netdev.md#id28)

#### [xdp-features (`u64`)](netdev.md#id29)

doc
:   Bitmask of enabled xdp-features.

enum
:   xdp-act

#### [xdp-zc-max-segs (`u32`)](netdev.md#id30)

doc
:   max fragment count supported by ZC driver

#### [xdp-rx-metadata-features (`u64`)](netdev.md#id31)

doc
:   Bitmask of supported XDP receive metadata features. See [XDP RX Metadata](../xdp-rx-metadata.md) for more details.

enum
:   xdp-rx-metadata

#### [xsk-features (`u64`)](netdev.md#id32)

doc
:   Bitmask of enabled AF_XDP features.

enum
:   xsk-flags

### [page-pool](netdev.md#id33)

#### [id (`uint`)](netdev.md#id34)

doc
:   Unique ID of a Page Pool instance.

#### [ifindex (`u32`)](netdev.md#id35)

doc
:   ifindex of the netdev to which the pool belongs.May be reported as 0 if the page pool was allocated for a netdevwhich got destroyed already (page pools may outlast their netdevsbecause they wait for all memory to be returned).

#### [napi-id (`uint`)](netdev.md#id36)

doc
:   Id of NAPI using this Page Pool instance.

#### [inflight (`uint`)](netdev.md#id37)

doc
:   Number of outstanding references to this page pool (allocatedbut yet to be freed pages). Allocated pages may be held insocket receive queues, driver receive ring, page pool recyclingring, the page pool cache, etc.

#### [inflight-mem (`uint`)](netdev.md#id38)

doc
:   Amount of memory held by inflight pages.

#### [detach-time (`uint`)](netdev.md#id39)

doc
:   Seconds in CLOCK_BOOTTIME of when Page Pool was detached bythe driver. Once detached Page Pool can no longer be used toallocate memory.Page Pools wait for all the memory allocated from them to be freedbefore truly disappearing. "Detached" Page Pools cannot be"re-attached", they are just waiting to disappear.Attribute is absent if Page Pool has not been detached, andcan still be used to allocate new memory.

### [page-pool-info](netdev.md#id40)

#### [id](netdev.md#id41)

#### [ifindex](netdev.md#id42)

### [page-pool-stats](netdev.md#id43)

#### [info (`nest`)](netdev.md#id44)

doc
:   Page pool identifying information.

nested-attributes
:   page-pool-info

#### [alloc-fast (`uint`)](netdev.md#id45)

value
:   8

#### [alloc-slow (`uint`)](netdev.md#id46)

#### [alloc-slow-high-order (`uint`)](netdev.md#id47)

#### [alloc-empty (`uint`)](netdev.md#id48)

#### [alloc-refill (`uint`)](netdev.md#id49)

#### [alloc-waive (`uint`)](netdev.md#id50)

#### [recycle-cached (`uint`)](netdev.md#id51)

#### [recycle-cache-full (`uint`)](netdev.md#id52)

#### [recycle-ring (`uint`)](netdev.md#id53)

#### [recycle-ring-full (`uint`)](netdev.md#id54)

#### [recycle-released-refcnt (`uint`)](netdev.md#id55)

### [napi](netdev.md#id56)

#### [ifindex (`u32`)](netdev.md#id57)

doc
:   ifindex of the netdevice to which NAPI instance belongs.

#### [id (`u32`)](netdev.md#id58)

doc
:   ID of the NAPI instance.

#### [irq (`u32`)](netdev.md#id59)

doc
:   The associated interrupt vector number for the napi

#### [pid (`u32`)](netdev.md#id60)

doc
:   PID of the napi thread, if NAPI is configured to operate in threaded mode. If NAPI is not in threaded mode (i.e. uses normal softirq context), the attribute will be absent.

### [queue](netdev.md#id61)

#### [id (`u32`)](netdev.md#id62)

doc
:   Queue index; most queue types are indexed like a C array, with indexes starting at 0 and ending at queue count - 1. Queue indexes are scoped to an interface and queue type.

#### [ifindex (`u32`)](netdev.md#id63)

doc
:   ifindex of the netdevice to which the queue belongs.

#### [type (`u32`)](netdev.md#id64)

doc
:   Queue type as rx, tx. Each queue type defines a separate ID space.

enum
:   queue-type

#### [napi-id (`u32`)](netdev.md#id65)

doc
:   ID of the NAPI instance which services this queue.
