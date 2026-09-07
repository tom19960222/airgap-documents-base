---
collection: ceph
version: "20.2.4"
title: "ceph-debugpack -- ceph debug packer utility"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/man/8/ceph-debugpack.rst
fetched_at: 2026-08-18T01:32:45Z
---
:orphan:

# ceph-debugpack -- ceph debug packer utility

.. program:: ceph-debugpack

## Synopsis

| **ceph-debugpack** [ *options* ] *filename.tar.gz*

## Description

**ceph-debugpack** will build a tarball containing various items that are
useful for debugging crashes. The resulting tarball can be shared with
Ceph developers when debugging a problem.

The tarball will include the binaries for ceph-mds, ceph-osd, and ceph-mon, radosgw, any
log files, the ceph.conf configuration file, any core files we can
find, and (if the system is running) dumps of the current cluster state
as reported by 'ceph report'.

## Options

.. option:: -c ceph.conf, --conf=ceph.conf

   Use *ceph.conf* configuration file instead of the default
   ``/etc/ceph/ceph.conf`` to determine monitor addresses during
   startup.

## Availability

**ceph-debugpack** is part of Ceph, a massively scalable, open-source, distributed storage system. Please
refer to the Ceph documentation at https://docs.ceph.com for more
information.

## See also

[ceph](../../install/clone-source.md)\(8)
[ceph-post-file](ceph-post-file.md)\(8)
