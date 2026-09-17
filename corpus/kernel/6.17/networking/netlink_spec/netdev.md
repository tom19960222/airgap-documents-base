---
collection: kernel
version: "6.17"
title: "Family netdev netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/netdev.html
fetched_at: 2026-09-16T16:40:50+00:00
---
# [Family `netdev` netlink specification](netdev.md#id11)

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
    - [qstats-get](netdev.md#qstats-get)
    - [bind-rx](netdev.md#bind-rx)
    - [napi-set](netdev.md#napi-set)
    - [bind-tx](netdev.md#bind-tx)
  - [Multicast groups](netdev.md#multicast-groups)
  - [Definitions](netdev.md#definitions)

    - [xdp-act](netdev.md#xdp-act)
    - [xdp-rx-metadata](netdev.md#xdp-rx-metadata)
    - [xsk-flags](netdev.md#xsk-flags)
    - [queue-type](netdev.md#queue-type)
    - [qstats-scope](netdev.md#qstats-scope)
    - [napi-threaded](netdev.md#napi-threaded)
  - [Attribute sets](netdev.md#attribute-sets)

    - [dev](netdev.md#dev)
    - [io-uring-provider-info](netdev.md#io-uring-provider-info)
    - [page-pool](netdev.md#page-pool)
    - [page-pool-info](netdev.md#page-pool-info)
    - [page-pool-stats](netdev.md#page-pool-stats)
    - [napi](netdev.md#napi)
    - [xsk-info](netdev.md#xsk-info)
    - [queue](netdev.md#queue)
    - [qstats](netdev.md#qstats)
    - [queue-id](netdev.md#queue-id)
    - [dmabuf](netdev.md#dmabuf)

## [Summary](netdev.md#id12)

netdev configuration over generic netlink.

## [Operations](netdev.md#id13)

### [dev-get](netdev.md#id14)

Get / dump information about a netdev.

attribute-set:
:   [dev](netdev.md#netdev-attribute-set-dev)

do:
:   **request**
    :   attributes:
        :   [`ifindex`]

    **reply**
    :   attributes:
        :   [`ifindex`, `xdp-features`, `xdp-zc-max-segs`, `xdp-rx-metadata-features`, `xsk-features`]

dump:
:   **reply**
    :   attributes:
        :   [`ifindex`, `xdp-features`, `xdp-zc-max-segs`, `xdp-rx-metadata-features`, `xsk-features`]

### [dev-add-ntf](netdev.md#id15)

Notification about device appearing.

notify:
:   dev-get

mcgrp:
:   mgmt

### [dev-del-ntf](netdev.md#id16)

Notification about device disappearing.

notify:
:   dev-get

mcgrp:
:   mgmt

### [dev-change-ntf](netdev.md#id17)

Notification about device configuration being changed.

notify:
:   dev-get

mcgrp:
:   mgmt

### [page-pool-get](netdev.md#id18)

Get / dump information about Page Pools.
(Only Page Pools associated with a net_device can be listed.)

attribute-set:
:   [page-pool](netdev.md#netdev-attribute-set-page-pool)

config-cond:
:   page-pool

do:
:   **request**
    :   attributes:
        :   [`id`]

    **reply**
    :   attributes:
        :   [`id`, `ifindex`, `napi-id`, `inflight`, `inflight-mem`, `detach-time`, `dmabuf`, `io-uring`]

dump:
:   **reply**
    :   attributes:
        :   [`id`, `ifindex`, `napi-id`, `inflight`, `inflight-mem`, `detach-time`, `dmabuf`, `io-uring`]

### [page-pool-add-ntf](netdev.md#id19)

Notification about page pool appearing.

notify:
:   page-pool-get

mcgrp:
:   page-pool

config-cond:
:   page-pool

### [page-pool-del-ntf](netdev.md#id20)

Notification about page pool disappearing.

notify:
:   page-pool-get

mcgrp:
:   page-pool

config-cond:
:   page-pool

### [page-pool-change-ntf](netdev.md#id21)

Notification about page pool configuration being changed.

notify:
:   page-pool-get

mcgrp:
:   page-pool

config-cond:
:   page-pool

### [page-pool-stats-get](netdev.md#id22)

Get page pool statistics.

attribute-set:
:   [page-pool-stats](netdev.md#netdev-attribute-set-page-pool-stats)

config-cond:
:   page-pool-stats

do:
:   **request**
    :   attributes:
        :   [`info`]

    **reply**
    :   attributes:
        :   [`info`, `alloc-fast`, `alloc-slow`, `alloc-slow-high-order`, `alloc-empty`, `alloc-refill`, `alloc-waive`, `recycle-cached`, `recycle-cache-full`, `recycle-ring`, `recycle-ring-full`, `recycle-released-refcnt`]

dump:
:   **reply**
    :   attributes:
        :   [`info`, `alloc-fast`, `alloc-slow`, `alloc-slow-high-order`, `alloc-empty`, `alloc-refill`, `alloc-waive`, `recycle-cached`, `recycle-cache-full`, `recycle-ring`, `recycle-ring-full`, `recycle-released-refcnt`]

### [queue-get](netdev.md#id23)

Get queue information from the kernel. Only configured queues will be reported (as opposed to all available hardware queues).

attribute-set:
:   [queue](netdev.md#netdev-attribute-set-queue)

do:
:   **request**
    :   attributes:
        :   [`ifindex`, `type`, `id`]

    **reply**
    :   attributes:
        :   [`id`, `type`, `napi-id`, `ifindex`, `dmabuf`, `io-uring`, `xsk`]

dump:
:   **request**
    :   attributes:
        :   [`ifindex`]

    **reply**
    :   attributes:
        :   [`id`, `type`, `napi-id`, `ifindex`, `dmabuf`, `io-uring`, `xsk`]

### [napi-get](netdev.md#id24)

Get information about NAPI instances configured on the system.

attribute-set:
:   [napi](netdev.md#netdev-attribute-set-napi)

do:
:   **request**
    :   attributes:
        :   [`id`]

    **reply**
    :   attributes:
        :   [`id`, `ifindex`, `irq`, `pid`, `defer-hard-irqs`, `gro-flush-timeout`, `irq-suspend-timeout`, `threaded`]

dump:
:   **request**
    :   attributes:
        :   [`ifindex`]

    **reply**
    :   attributes:
        :   [`id`, `ifindex`, `irq`, `pid`, `defer-hard-irqs`, `gro-flush-timeout`, `irq-suspend-timeout`, `threaded`]

### [qstats-get](netdev.md#id25)

Get / dump fine grained statistics. Which statistics are reported
depends on the device and the driver, and whether the driver stores
software counters per-queue.

attribute-set:
:   [qstats](netdev.md#netdev-attribute-set-qstats)

dump:
:   **request**
    :   attributes:
        :   [`ifindex`, `scope`]

    **reply**
    :   attributes:
        :   [`ifindex`, `queue-type`, `queue-id`, `rx-packets`, `rx-bytes`, `tx-packets`, `tx-bytes`]

### [bind-rx](netdev.md#id26)

Bind dmabuf to netdev

attribute-set:
:   [dmabuf](netdev.md#netdev-attribute-set-dmabuf)

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`ifindex`, `fd`, `queues`]

    **reply**
    :   attributes:
        :   [`id`]

### [napi-set](netdev.md#id27)

Set configurable NAPI instance settings.

attribute-set:
:   [napi](netdev.md#netdev-attribute-set-napi)

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`id`, `defer-hard-irqs`, `gro-flush-timeout`, `irq-suspend-timeout`, `threaded`]

### [bind-tx](netdev.md#id28)

Bind dmabuf to netdev for TX

attribute-set:
:   [dmabuf](netdev.md#netdev-attribute-set-dmabuf)

do:
:   **request**
    :   attributes:
        :   [`ifindex`, `fd`]

    **reply**
    :   attributes:
        :   [`id`]

## [Multicast groups](netdev.md#id29)

- mgmt
- page-pool

## [Definitions](netdev.md#id30)

### [xdp-act](netdev.md#id31)

type:
:   flags

entries:
:   basic:
    :   XDP features set supported by all drivers (XDP_ABORTED, XDP_DROP, XDP_PASS, XDP_TX)

    redirect:
    :   The netdev supports XDP_REDIRECT

    ndo-xmit:
    :   This feature informs if netdev implements ndo_xdp_xmit callback.

    xsk-zerocopy:
    :   This feature informs if netdev supports AF_XDP in zero copy mode.

    hw-offload:
    :   This feature informs if netdev supports XDP hw offloading.

    rx-sg:
    :   This feature informs if netdev implements non-linear XDP buffer support in the driver napi callback.

    ndo-xmit-sg:
    :   This feature informs if netdev implements non-linear XDP buffer support in ndo_xdp_xmit callback.

### [xdp-rx-metadata](netdev.md#id32)

type:
:   flags

entries:
:   timestamp:
    :   Device is capable of exposing receive HW timestamp via [`bpf_xdp_metadata_rx_timestamp()`](../xdp-rx-metadata.md#c.bpf_xdp_metadata_rx_timestamp "bpf_xdp_metadata_rx_timestamp").

    hash:
    :   Device is capable of exposing receive packet hash via [`bpf_xdp_metadata_rx_hash()`](../xdp-rx-metadata.md#c.bpf_xdp_metadata_rx_hash "bpf_xdp_metadata_rx_hash").

    vlan-tag:
    :   Device is capable of exposing receive packet VLAN tag via [`bpf_xdp_metadata_rx_vlan_tag()`](../xdp-rx-metadata.md#c.bpf_xdp_metadata_rx_vlan_tag "bpf_xdp_metadata_rx_vlan_tag").

### [xsk-flags](netdev.md#id33)

type:
:   flags

entries:
:   tx-timestamp:
    :   HW timestamping egress packets is supported by the driver.

    tx-checksum:
    :   L3 checksum HW offload is supported by the driver.

    tx-launch-time-fifo:
    :   Launch time HW offload is supported by the driver.

### [queue-type](netdev.md#id34)

type:
:   enum

entries:
:   - `rx`
    - `tx`

### [qstats-scope](netdev.md#id35)

type:
:   flags

entries:
:   - `queue`

### [napi-threaded](netdev.md#id36)

type:
:   enum

entries:
:   - `disabled`
    - `enabled`

## [Attribute sets](netdev.md#id37)

### [dev](netdev.md#id38)

#### ifindex (`u32`)

doc:
:   netdev ifindex

#### pad (`pad`)

#### xdp-features (`u64`)

doc:
:   Bitmask of enabled xdp-features.

enum:
:   [xdp-act](netdev.md#netdev-definition-xdp-act)

#### xdp-zc-max-segs (`u32`)

doc:
:   max fragment count supported by ZC driver

#### xdp-rx-metadata-features (`u64`)

doc:
:   Bitmask of supported XDP receive metadata features. See [XDP RX Metadata](../xdp-rx-metadata.md) for more details.

enum:
:   [xdp-rx-metadata](netdev.md#netdev-definition-xdp-rx-metadata)

#### xsk-features (`u64`)

doc:
:   Bitmask of enabled AF_XDP features.

enum:
:   [xsk-flags](netdev.md#netdev-definition-xsk-flags)

### [io-uring-provider-info](netdev.md#id39)

### [page-pool](netdev.md#id40)

#### id (`uint`)

doc:
:   Unique ID of a Page Pool instance.

#### ifindex (`u32`)

doc:
:   ifindex of the netdev to which the pool belongs. May be reported as 0 if the page pool was allocated for a netdev which got destroyed already (page pools may outlast their netdevs because they wait for all memory to be returned).

#### napi-id (`uint`)

doc:
:   Id of NAPI using this Page Pool instance.

#### inflight (`uint`)

doc:
:   Number of outstanding references to this page pool (allocated but yet to be freed pages). Allocated pages may be held in socket receive queues, driver receive ring, page pool recycling ring, the page pool cache, etc.

#### inflight-mem (`uint`)

doc:
:   Amount of memory held by inflight pages.

#### detach-time (`uint`)

doc:
:   Seconds in CLOCK_BOOTTIME of when Page Pool was detached by the driver. Once detached Page Pool can no longer be used to allocate memory. Page Pools wait for all the memory allocated from them to be freed before truly disappearing. “Detached” Page Pools cannot be “re-attached”, they are just waiting to disappear. Attribute is absent if Page Pool has not been detached, and can still be used to allocate new memory.

#### dmabuf (`u32`)

doc:
:   ID of the dmabuf this page-pool is attached to.

#### io-uring (`nest`)

doc:
:   io-uring memory provider information.

nested-attributes:
:   [io-uring-provider-info](netdev.md#netdev-attribute-set-io-uring-provider-info)

### [page-pool-info](netdev.md#id41)

#### id

#### ifindex

### [page-pool-stats](netdev.md#id42)

#### info (`nest`)

doc:
:   Page pool identifying information.

nested-attributes:
:   [page-pool-info](netdev.md#netdev-attribute-set-page-pool-info)

#### alloc-fast (`uint`)

value:
:   8

#### alloc-slow (`uint`)

#### alloc-slow-high-order (`uint`)

#### alloc-empty (`uint`)

#### alloc-refill (`uint`)

#### alloc-waive (`uint`)

#### recycle-cached (`uint`)

#### recycle-cache-full (`uint`)

#### recycle-ring (`uint`)

#### recycle-ring-full (`uint`)

#### recycle-released-refcnt (`uint`)

### [napi](netdev.md#id43)

#### ifindex (`u32`)

doc:
:   ifindex of the netdevice to which NAPI instance belongs.

#### id (`u32`)

doc:
:   ID of the NAPI instance.

#### irq (`u32`)

doc:
:   The associated interrupt vector number for the napi

#### pid (`u32`)

doc:
:   PID of the napi thread, if NAPI is configured to operate in threaded mode. If NAPI is not in threaded mode (i.e. uses normal softirq context), the attribute will be absent.

#### defer-hard-irqs (`u32`)

doc:
:   The number of consecutive empty polls before IRQ deferral ends and hardware IRQs are re-enabled.

#### gro-flush-timeout (`uint`)

doc:
:   The timeout, in nanoseconds, of when to trigger the NAPI watchdog timer which schedules NAPI processing. Additionally, a non-zero value will also prevent GRO from flushing recent super-frames at the end of a NAPI cycle. This may add receive latency in exchange for reducing the number of frames processed by the network stack.

#### irq-suspend-timeout (`uint`)

doc:
:   The timeout, in nanoseconds, of how long to suspend irq processing, if event polling finds events

#### threaded (`u32`)

doc:
:   Whether the NAPI is configured to operate in threaded polling mode. If this is set to enabled then the NAPI context operates in threaded polling mode.

enum:
:   [napi-threaded](netdev.md#netdev-definition-napi-threaded)

### [xsk-info](netdev.md#id44)

### [queue](netdev.md#id45)

#### id (`u32`)

doc:
:   Queue index; most queue types are indexed like a C array, with indexes starting at 0 and ending at queue count - 1. Queue indexes are scoped to an interface and queue type.

#### ifindex (`u32`)

doc:
:   ifindex of the netdevice to which the queue belongs.

#### type (`u32`)

doc:
:   Queue type as rx, tx. Each queue type defines a separate ID space. XDP TX queues allocated in the kernel are not linked to NAPIs and thus not listed. AF_XDP queues will have more information set in the xsk attribute.

enum:
:   [queue-type](netdev.md#netdev-definition-queue-type)

#### napi-id (`u32`)

doc:
:   ID of the NAPI instance which services this queue.

#### dmabuf (`u32`)

doc:
:   ID of the dmabuf attached to this queue, if any.

#### io-uring (`nest`)

doc:
:   io_uring memory provider information.

nested-attributes:
:   [io-uring-provider-info](netdev.md#netdev-attribute-set-io-uring-provider-info)

#### xsk (`nest`)

doc:
:   XSK information for this queue, if any.

nested-attributes:
:   [xsk-info](netdev.md#netdev-attribute-set-xsk-info)

### [qstats](netdev.md#id46)

#### ifindex (`u32`)

doc:
:   ifindex of the netdevice to which stats belong.

#### queue-type (`u32`)

doc:
:   Queue type as rx, tx, for queue-id.

enum:
:   [queue-type](netdev.md#netdev-definition-queue-type)

#### queue-id (`u32`)

doc:
:   Queue ID, if stats are scoped to a single queue instance.

#### scope (`uint`)

doc:
:   What object type should be used to iterate over the stats.

enum:
:   [qstats-scope](netdev.md#netdev-definition-qstats-scope)

#### rx-packets (`uint`)

doc:
:   Number of wire packets successfully received and passed to the stack. For drivers supporting XDP, XDP is considered the first layer of the stack, so packets consumed by XDP are still counted here.

value:
:   8

#### rx-bytes (`uint`)

doc:
:   Successfully received bytes, see rx-packets.

#### tx-packets (`uint`)

doc:
:   Number of wire packets successfully sent. Packet is considered to be successfully sent once it is in device memory (usually this means the device has issued a DMA completion for the packet).

#### tx-bytes (`uint`)

doc:
:   Successfully sent bytes, see tx-packets.

#### rx-alloc-fail (`uint`)

doc:
:   Number of times skb or buffer allocation failed on the Rx datapath. Allocation failure may, or may not result in a packet drop, depending on driver implementation and whether system recovers quickly.

#### rx-hw-drops (`uint`)

doc:
:   Number of all packets which entered the device, but never left it, including but not limited to: packets dropped due to lack of buffer space, processing errors, explicit or implicit policies and packet filters.

#### rx-hw-drop-overruns (`uint`)

doc:
:   Number of packets dropped due to transient lack of resources, such as buffer space, host descriptors etc.

#### rx-csum-complete (`uint`)

doc:
:   Number of packets that were marked as CHECKSUM_COMPLETE.

#### rx-csum-unnecessary (`uint`)

doc:
:   Number of packets that were marked as CHECKSUM_UNNECESSARY.

#### rx-csum-none (`uint`)

doc:
:   Number of packets that were not checksummed by device.

#### rx-csum-bad (`uint`)

doc:
:   Number of packets with bad checksum. The packets are not discarded, but still delivered to the stack.

#### rx-hw-gro-packets (`uint`)

doc:
:   Number of packets that were coalesced from smaller packets by the device. Counts only packets coalesced with the HW-GRO netdevice feature, LRO-coalesced packets are not counted.

#### rx-hw-gro-bytes (`uint`)

doc:
:   See rx-hw-gro-packets.

#### rx-hw-gro-wire-packets (`uint`)

doc:
:   Number of packets that were coalesced to bigger packetss with the HW-GRO netdevice feature. LRO-coalesced packets are not counted.

#### rx-hw-gro-wire-bytes (`uint`)

doc:
:   See rx-hw-gro-wire-packets.

#### rx-hw-drop-ratelimits (`uint`)

doc:
:   Number of the packets dropped by the device due to the received packets bitrate exceeding the device rate limit.

#### tx-hw-drops (`uint`)

doc:
:   Number of packets that arrived at the device but never left it, encompassing packets dropped for reasons such as processing errors, as well as those affected by explicitly defined policies and packet filtering criteria.

#### tx-hw-drop-errors (`uint`)

doc:
:   Number of packets dropped because they were invalid or malformed.

#### tx-csum-none (`uint`)

doc:
:   Number of packets that did not require the device to calculate the checksum.

#### tx-needs-csum (`uint`)

doc:
:   Number of packets that required the device to calculate the checksum. This counter includes the number of GSO wire packets for which device calculated the L4 checksum.

#### tx-hw-gso-packets (`uint`)

doc:
:   Number of packets that necessitated segmentation into smaller packets by the device.

#### tx-hw-gso-bytes (`uint`)

doc:
:   See tx-hw-gso-packets.

#### tx-hw-gso-wire-packets (`uint`)

doc:
:   Number of wire-sized packets generated by processing tx-hw-gso-packets

#### tx-hw-gso-wire-bytes (`uint`)

doc:
:   See tx-hw-gso-wire-packets.

#### tx-hw-drop-ratelimits (`uint`)

doc:
:   Number of the packets dropped by the device due to the transmit packets bitrate exceeding the device rate limit.

#### tx-stop (`uint`)

doc:
:   Number of times driver paused accepting new tx packets from the stack to this queue, because the queue was full. Note that if BQL is supported and enabled on the device the networking stack will avoid queuing a lot of data at once.

#### tx-wake (`uint`)

doc:
:   Number of times driver re-started accepting send requests to this queue from the stack.

### [queue-id](netdev.md#id47)

#### id

#### type

### [dmabuf](netdev.md#id48)

#### ifindex (`u32`)

doc:
:   netdev ifindex to bind the dmabuf to.

#### queues (`nest`)

doc:
:   receive queues to bind the dmabuf to.

nested-attributes:
:   [queue-id](netdev.md#netdev-attribute-set-queue-id)

multi-attr:
:   True

#### fd (`u32`)

doc:
:   dmabuf file descriptor to bind.

#### id (`u32`)

doc:
:   id of the dmabuf binding
