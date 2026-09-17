---
collection: kernel
version: "6.17"
title: "Family tcp_metrics netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/tcp_metrics.html
fetched_at: 2026-09-16T16:41:00+00:00
---
# [Family `tcp_metrics` netlink specification](tcp_metrics.md#id1)

Contents

- [Family `tcp_metrics` netlink specification](tcp_metrics.md#family-tcp-metrics-netlink-specification)

  - [Summary](tcp_metrics.md#summary)
  - [Operations](tcp_metrics.md#operations)

    - [get](tcp_metrics.md#get)
    - [del](tcp_metrics.md#del)
  - [Definitions](tcp_metrics.md#definitions)

    - [tcp-fastopen-cookie-max](tcp_metrics.md#tcp-fastopen-cookie-max)
  - [Attribute sets](tcp_metrics.md#attribute-sets)

    - [tcp-metrics](tcp_metrics.md#tcp-metrics)
    - [metrics](tcp_metrics.md#metrics)

## [Summary](tcp_metrics.md#id2)

Management interface for TCP metrics.

## [Operations](tcp_metrics.md#id3)

### [get](tcp_metrics.md#id4)

Retrieve metrics.

attribute-set:
:   [tcp-metrics](tcp_metrics.md#tcp-metrics-attribute-set-tcp-metrics)

dont-validate:
:   [‘strict’, ‘dump’]

do:
:   **request**
    :   attributes:
        :   [`addr-ipv4`, `addr-ipv6`, `saddr-ipv4`, `saddr-ipv6`]

    **reply**
    :   attributes:
        :   [`addr-ipv4`, `addr-ipv6`, `saddr-ipv4`, `saddr-ipv6`, `age`, `vals`, `fopen-mss`, `fopen-syn-drops`, `fopen-syn-drop-ts`, `fopen-cookie`]

dump:
:   **reply**
    :   attributes:
        :   [`addr-ipv4`, `addr-ipv6`, `saddr-ipv4`, `saddr-ipv6`, `age`, `vals`, `fopen-mss`, `fopen-syn-drops`, `fopen-syn-drop-ts`, `fopen-cookie`]

### [del](tcp_metrics.md#id5)

Delete metrics.

attribute-set:
:   [tcp-metrics](tcp_metrics.md#tcp-metrics-attribute-set-tcp-metrics)

dont-validate:
:   [‘strict’, ‘dump’]

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`addr-ipv4`, `addr-ipv6`, `saddr-ipv4`, `saddr-ipv6`]

## [Definitions](tcp_metrics.md#id6)

### [tcp-fastopen-cookie-max](tcp_metrics.md#id7)

type:
:   const

value:
:   16

## [Attribute sets](tcp_metrics.md#id8)

### [tcp-metrics](tcp_metrics.md#id9)

#### addr-ipv4 (`u32`)

byte-order:
:   big-endian

display-hint:
:   ipv4

#### addr-ipv6 (`binary`)

byte-order:
:   big-endian

display-hint:
:   ipv6

#### age (`u64`)

#### tw-tsval (`u32`)

doc:
:   unused

#### tw-ts-stamp (`s32`)

doc:
:   unused

#### vals (`nest`)

nested-attributes:
:   [metrics](tcp_metrics.md#tcp-metrics-attribute-set-metrics)

#### fopen-mss (`u16`)

#### fopen-syn-drops (`u16`)

#### fopen-syn-drop-ts (`u64`)

#### fopen-cookie (`binary`)

#### saddr-ipv4 (`u32`)

byte-order:
:   big-endian

display-hint:
:   ipv4

#### saddr-ipv6 (`binary`)

byte-order:
:   big-endian

display-hint:
:   ipv6

#### pad (`pad`)

### [metrics](tcp_metrics.md#id10)

#### rtt (`u32`)

doc:
:   Round Trip Time (RTT), in msecs with 3 bits fractional (left-shift by 3 to get the msec value).

#### rttvar (`u32`)

doc:
:   Round Trip Time VARiance (RTT), in msecs with 2 bits fractional (left-shift by 2 to get the msec value).

#### ssthresh (`u32`)

doc:
:   Slow Start THRESHold.

#### cwnd (`u32`)

doc:
:   Congestion Window.

#### reodering (`u32`)

doc:
:   Reodering metric.

#### rtt-us (`u32`)

doc:
:   Round Trip Time (RTT), in usecs, with 3 bits fractional (left-shift by 3 to get the msec value).

#### rttvar-us (`u32`)

doc:
:   Round Trip Time (RTT), in usecs, with 2 bits fractional (left-shift by 3 to get the msec value).
