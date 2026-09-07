---
collection: ceph
version: "20.2.4"
title: "ceph-kvstore-tool -- ceph kvstore manipulation tool"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/man/8/ceph-kvstore-tool.rst
fetched_at: 2026-08-18T01:32:45Z
---
:orphan:

# ceph-kvstore-tool -- ceph kvstore manipulation tool

.. program:: ceph-kvstore-tool

# Synopsis

| **ceph-kvstore-tool** <rocksdb|bluestore-kv> <store path> *command* [args...]

# Description

ceph-kvstore-tool is a kvstore manipulation tool. It allows users to manipulate
RocksDB's data (like OSD's omap) offline.

# Commands

ceph-kvstore-tool utility uses many commands for debugging purpose
which are as follows:

list [prefix]
    Print key of all KV pairs stored with the URL encoded prefix.

list-crc [prefix]
    Print CRC of all KV pairs stored with the URL encoded prefix.

dump [prefix]
    Print key and value of all KV pairs stored with the URL encoded prefix.

exists <prefix> [key]
    Check if there is any KV pair stored with the URL encoded prefix. If key
    is also specified, check for the key with the prefix instead.

get <prefix> <key> [out <file>]
    Get the value of the KV pair stored with the URL encoded prefix and key.
    If file is also specified, write the value to the file.

crc <prefix>
    Get the CRC of the KV pair stored with the URL encoded prefix and key.

get-size [<prefix> <key>]
    Get estimated store size or size of value specified by prefix and key.

set <prefix> <key> [ver <N>|in <file>]
    Set the value of the KV pair stored with the URL encoded prefix and key.
    The value could be *version_t* or text.

rm <prefix>
    Remove the KV pair stored with the URL encoded prefix and key.

rm-prefix
    Remove all KV pairs stored with the URL encoded prefix.

store-copy <path> [num-keys-per-tx]
    Copy all KV pairs to another directory specified by `path`.
    [num-keys-per-tx] is the number of KV pairs copied for a transaction.

store-crc
    Store CRC of all KV pairs to a file specified by `path`.

compact
    Subcommand `compact` is used to compact all data of kvstore. It will open
    the database, and trigger a database's compaction. After compaction, some
    disk space may be released.

compact-prefix
    Compact all entries specified by the URL encoded prefix.

compact-range <prefix> <start>
    Compact some entries specified by the URL encoded prefix and range.

destructive-repair
    Make a (potentially destructive) effort to recover a corrupted database.
    Note that in the case of rocksdb this may corrupt an otherwise uncorrupted
    database--use this only as a last resort!

stats
    Prints statistics from underlying key-value database. This is only for informative purposes.
    Format and information content may vary between releases. For RocksDB information includes
    compactions stats, performance counters, memory usage and internal RocksDB stats.

histogram
    Presents key-value sizes distribution statistics from the underlying KV database.

# Availability

**ceph-kvstore-tool** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at https://docs.ceph.com for more information.

# See also

ceph\(8)
