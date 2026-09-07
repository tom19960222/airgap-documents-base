---
collection: ceph
version: "20.2.4"
title: "ceph-run -- restart daemon on core dump"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/man/8/ceph-run.rst
fetched_at: 2026-08-18T01:32:45Z
---
:orphan:

# ceph-run -- restart daemon on core dump

.. program:: ceph-run

## Synopsis

| **ceph-run** *command* ...

## Description

**ceph-run** is a simple wrapper that will restart a daemon if it exits
with a signal indicating it crashed and possibly core dumped (that is,
signals 3, 4, 5, 6, 8, or 11).

The command should run the daemon in the foreground. For Ceph daemons,
that means the ``-f`` option.

## Options

None

## Availability

**ceph-run** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at https://docs.ceph.com for more information.

## See also

[ceph](../../install/clone-source.md)\(8),
[ceph-mon](ceph-mon.md)\(8),
[ceph-mds](ceph-mds.md)\(8),
[ceph-osd](ceph-osd.md)\(8)
