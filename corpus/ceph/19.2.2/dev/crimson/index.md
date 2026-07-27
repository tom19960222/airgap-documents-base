---
collection: ceph
version: "19.2.2"
title: "Crimson developer documentation"
source_url: https://docs.ceph.com/en/squid/dev/crimson/
fetched_at: 2026-07-27T16:41:36+00:00
---
# Crimson developer documentation

Contents

- [crimson](crimson/index.md)
  - [Building Crimson](crimson/index.md#building-crimson)
  - [Deploying Crimson with cephadm](crimson/index.md#deploying-crimson-with-cephadm)
  - [Crimson CPU allocation](crimson/index.md#crimson-cpu-allocation)
  - [Running Crimson](crimson/index.md#running-crimson)
  - [Object Store Backends](crimson/index.md#object-store-backends)
    - [Native Backends](crimson/index.md#native-backends)
    - [Non-Native Backends](crimson/index.md#non-native-backends)
  - [vstart.sh](crimson/index.md#vstart-sh)
    - [daemonize](crimson/index.md#daemonize)
    - [logging](crimson/index.md#logging)
    - [PG stats reported to mgr](crimson/index.md#pg-stats-reported-to-mgr)
    - [Asock command](crimson/index.md#asock-command)
    - [Prometheus text protocol](crimson/index.md#prometheus-text-protocol)
  - [Profiling Crimson](crimson/index.md#profiling-crimson)
    - [Fio](crimson/index.md#fio)
    - [CBT](crimson/index.md#cbt)
  - [Hacking Crimson](crimson/index.md#hacking-crimson)
    - [Seastar Documents](crimson/index.md#seastar-documents)
  - [Debugging Crimson](crimson/index.md#debugging-crimson)
    - [Debugging with GDB](crimson/index.md#debugging-with-gdb)
    - [Human-readable backtraces with addr2line](crimson/index.md#human-readable-backtraces-with-addr2line)
  - [Code Walkthroughs](crimson/index.md#code-walkthroughs)
- [error handling](error-handling/index.md)
- [osd](osd/index.md)
- [The `ClientRequest` pipeline](pipeline/index.md)
  - [Comparison with the classical OSD](pipeline/index.md#comparison-with-the-classical-osd)
- [PoseidonStore](poseidonstore/index.md)
  - [Key concepts and goals](poseidonstore/index.md#key-concepts-and-goals)
    - [Background](poseidonstore/index.md#background)
    - [Motivation and Key idea](poseidonstore/index.md#motivation-and-key-idea)
    - [Observation](poseidonstore/index.md#observation)
  - [Design](poseidonstore/index.md#design)
    - [I/O procedure](poseidonstore/index.md#i-o-procedure)
    - [Crash consistency](poseidonstore/index.md#crash-consistency)
    - [Comparison](poseidonstore/index.md#comparison)
  - [Detailed Design](poseidonstore/index.md#detailed-design)
    - [WAL](poseidonstore/index.md#wal)
    - [Partition and Reactor thread](poseidonstore/index.md#partition-and-reactor-thread)
    - [Cache](poseidonstore/index.md#cache)
    - [Sharded partitions (with cross-SP transaction)](poseidonstore/index.md#sharded-partitions-with-cross-sp-transaction)
    - [CoW/Clone](poseidonstore/index.md#cow-clone)
  - [Plans](poseidonstore/index.md#plans)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
