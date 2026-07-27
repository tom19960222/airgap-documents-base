---
collection: ceph
version: "19.2.2"
title: "Scrub internals and diagnostics"
source_url: https://docs.ceph.com/en/squid/dev/osd_internals/scrub/
fetched_at: 2026-07-27T16:43:09+00:00
---
# Scrub internals and diagnostics

## Scrubbing Behavior Table

| Flags | none | noscrub | nodeep_scrub | noscrub/nodeep_scrub |
| --- | --- | --- | --- | --- |
| Periodic tick | S | X | S | X |
| Periodic tick after osd_deep_scrub_interval | D | D | S | X |
| Initiated scrub | S | S | S | S |
| Initiated scrub after osd_deep_scrub_interval | D | D | S | S |
| Initiated deep scrub | D | D | D | D |

- X = Do nothing
- S = Do regular scrub
- D = Do deep scrub

## State variables

- Periodic tick state is `!must_scrub && !must_deep_scrub && !time_for_deep`
- Periodic tick after `osd_deep_scrub_interval state is !must_scrub && !must_deep_scrub && time_for_deep`
- Initiated scrub state is `must_scrub && !must_deep_scrub && !time_for_deep`
- Initiated scrub after `osd_deep_scrub_interval` state is `must_scrub && !must_deep_scrub && time_for_deep`
- Initiated deep scrub state is `must_scrub && must_deep_scrub`

## Scrub Reservations

An OSD daemon command dumps total local and remote reservations:

```
ceph daemon osd.<id> dump_scrub_reservations
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
