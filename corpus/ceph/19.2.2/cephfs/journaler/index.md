---
collection: ceph
version: "19.2.2"
title: "Journaler"
source_url: https://docs.ceph.com/en/squid/cephfs/journaler/
fetched_at: 2026-07-27T16:40:10+00:00
---
# Journaler

journaler_write_head_interval
:   > Interval in seconds between journal header updates (to help bound
    > replay time)
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `15`

journaler_prefetch_periods
:   > Number of striping periods to prefetch while reading MDS journal
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `10`
    >
    > min:
    > :   `2`

journaler_prezero_periods
:   > Number of striping periods to zero head of MDS journal write position
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `5`
    >
    > min:
    > :   `2`

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
