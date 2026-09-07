---
collection: ceph
version: "20.2.4"
title: "ceph-monstore-tool -- ceph monstore manipulation tool"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/man/8/ceph-monstore-tool.rst
fetched_at: 2026-08-18T01:32:45Z
---
:orphan:

# ceph-monstore-tool -- ceph monstore manipulation tool

.. program:: ceph-monstore-tool

## Synopsis

| **ceph-monstore-tool** <store path> <cmd> [args|options]

## Description

ceph-monstore-tool is used to manipulate MonitorDBStore's data
(monmap, osdmap, etc.) offline. It is similar to `ceph-kvstore-tool`.

Note:
    Ceph-specific options take the format `--option-name=VAL`
    DO NOT FORGET THE EQUALS SIGN. ('=')
    for example, `dump-keys --debug-rocksdb=0`

    Command-specific options must be passed after a `--`
    for example, `get monmap -- --version 10 --out /tmp/foo`

## Commands

ceph-monstore-tool uses many commands for debugging purposes:

store-copy
    Copy the store to PATH.

get monmap [-- options]
    Get monmap (version VER if specified) (default: last committed).

get osdmap [-- options]
    Get osdmap (version VER if specified) (default: last committed).

get msdmap [-- options]
    Get msdmap (version VER if specified) (default: last committed).

get mgr [-- options]
    Get mgrmap (version VER if specified) (default: last committed).

get crushmap [-- options]
    Get crushmap (version VER if specified) (default: last committed).

get-key <prefix> <key> [-- options]
    Get key to FILE (default: stdout).

remove-key <prefix> <key> [-- options]
    Remove key.

dump-keys
    Dump store keys to FILE (default: stdout).

dump-paxos [-- options]
    Dump Paxos transactions  (-- -- help for more info).

dump-trace FILE  [-- options]
    Dump contents of trace file FILE (-- --help for more info).

replay-trace FILE  [-- options]
    Replay trace from FILE (-- --help for more info).

random-gen [-- options]
    Add randomly genererated ops to the store (-- --help for more info).

rewrite-crush [-- options]
    Add a rewrite commit to the store

rebuild
    Rebuild store.

## Availability

**ceph-monstore-tool** is part of Ceph, a massively scalable, open-source,
distributed storage system. See the Ceph documentation at
https://docs.ceph.com for more information.

## See also

[ceph](../../install/clone-source.md)\(8)
