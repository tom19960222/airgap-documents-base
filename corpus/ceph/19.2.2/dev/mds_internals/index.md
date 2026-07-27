---
collection: ceph
version: "19.2.2"
title: "MDS developer documentation"
source_url: https://docs.ceph.com/en/squid/dev/mds_internals/
fetched_at: 2026-07-27T16:41:35+00:00
---
# MDS developer documentation

Contents

- [MDS internal data structures](data-structures/index.md)
- [Subtree exports](exports/index.md)
  - [Normal Migration](exports/index.md#normal-migration)
- [Ceph MDS Locker](locking/index.md)
  - [Why use locks?](locking/index.md#why-use-locks)
  - [Lock Types](locking/index.md#lock-types)
  - [Lock Classes](locking/index.md#lock-classes)
  - [Read, Write and Exclusive Locks](locking/index.md#read-write-and-exclusive-locks)
  - [Lock States and Lock State Machine](locking/index.md#lock-states-and-lock-state-machine)
  - [Lock Transition](locking/index.md#lock-transition)
- [MDS Quiesce Protocol](quiesce/index.md)
  - [Mechanism](quiesce/index.md#mechanism)
  - [Inode Quiescelock](quiesce/index.md#inode-quiescelock)
  - [Lookups and Exports](quiesce/index.md#lookups-and-exports)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
