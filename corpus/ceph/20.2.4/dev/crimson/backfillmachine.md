---
collection: ceph
version: "20.2.4"
title: "BackfillMachine"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/dev/crimson/backfillmachine.rst
fetched_at: 2026-08-18T01:32:45Z
---
# BackfillMachine

In Crimson, backfill is implemented with [Boost State Chart](https://www.boost.org/doc/libs/1_86_0/libs/statechart/doc/).

.. //TODO: Once the implementation is settled:
..         * Explain exceptional states once we finish working on this code
..         * Explain example happy path flow (code walkthorugh?)
..         * https://tracker.ceph.com/issues/68728

A sample of the recent state model:

> **Note:** ``Cancelled`` and ``Crushed`` states are not included in the
> following graph in order to make it easier to follow:
>
> * **Any** state is able to transit into ``Crushed``.
>
> * **Any** state (except from ``Initial`` and ``Waiting``) can transit into ``Cancelled``

![](https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/dev/crimson/crimson_backfillmachine.svg)

In similarly to [/dev/peering](../peering.md) a copy of the latest BackfillMachine
state model can be genereated using the [gen_state_diagram.py](https://github.com/ceph/ceph/blob/master/doc/scripts/gen_state_diagram.py)
