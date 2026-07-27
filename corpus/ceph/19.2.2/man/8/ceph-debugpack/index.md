---
collection: ceph
version: "19.2.2"
title: "ceph-debugpack -- ceph debug packer utility"
source_url: https://docs.ceph.com/en/squid/man/8/ceph-debugpack/
fetched_at: 2026-07-27T16:41:59+00:00
---
# ceph-debugpack -- ceph debug packer utility

## Synopsis

**ceph-debugpack** [ *options* ] *filename.tar.gz*

## Description

**ceph-debugpack** will build a tarball containing various items that are
useful for debugging crashes. The resulting tarball can be shared with
Ceph developers when debugging a problem.

The tarball will include the binaries for ceph-mds, ceph-osd, and ceph-mon, radosgw, any
log files, the ceph.conf configuration file, any core files we can
find, and (if the system is running) dumps of the current cluster state
as reported by ‘ceph report’.

## Options

-c ceph.conf, --conf=ceph.conf
:   Use *ceph.conf* configuration file instead of the default
    `/etc/ceph/ceph.conf` to determine monitor addresses during
    startup.

## Availability

**ceph-debugpack** is part of Ceph, a massively scalable, open-source, distributed storage system. Please
refer to the Ceph documentation at <https://docs.ceph.com> for more
information.

## See also

[ceph](../ceph/index.md)(8)
[ceph-post-file](../ceph-post-file/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
