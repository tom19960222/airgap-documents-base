---
collection: ceph
version: "19.2.2"
title: "PG"
source_url: https://docs.ceph.com/en/squid/dev/osd_internals/pg/
fetched_at: 2026-07-27T16:43:07+00:00
---
# PG

## Concepts

*Peering Interval*
:   See PG::start_peering_interval.
    See PG::acting_up_affected
    See PG::PeeringState::Reset

    A peering interval is a maximal set of contiguous map epochs in which the
    up and acting sets did not change. PG::PeeringMachine represents a
    transition from one interval to another as passing through
    PeeringState::Reset. On PG::PeeringState::AdvMap PG::acting_up_affected can
    cause the pg to transition to Reset.

## Peering Details and Gotchas

For an overview of peering, see [Peering](../../peering.md).

> - PG::flushed defaults to false and is set to false in
>   PG::start_peering_interval. Upon transitioning to PG::PeeringState::Started
>   we send a transaction through the pg op sequencer which, upon complete,
>   sends a FlushedEvt which sets flushed to true. The primary cannot go
>   active until this happens (See PG::PeeringState::WaitFlushedPeering).
>   Replicas can go active but cannot serve ops (writes or reads).
>   This is necessary because we cannot read our ondisk state until unstable
>   transactions from the previous interval have cleared.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
