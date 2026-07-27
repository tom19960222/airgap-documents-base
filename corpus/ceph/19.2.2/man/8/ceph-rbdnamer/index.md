---
collection: ceph
version: "19.2.2"
title: "ceph-rbdnamer -- udev helper to name RBD devices"
source_url: https://docs.ceph.com/en/squid/man/8/ceph-rbdnamer/
fetched_at: 2026-07-27T16:40:27+00:00
---
# ceph-rbdnamer -- udev helper to name RBD devices

## Synopsis

**ceph-rbdnamer** *num*

## Description

**ceph-rbdnamer** prints the pool, namespace, image and snapshot names
for a given RBD device to stdout. It is used by udev device manager
to set up RBD device symlinks. The appropriate udev rules are
provided in a file named 50-rbd.rules.

## Availability

**ceph-rbdnamer** is part of Ceph, a massively scalable, open-source, distributed storage system. Please
refer to the Ceph documentation at <https://docs.ceph.com> for more
information.

## See also

[rbd](../rbd/index.md)(8),
[ceph](../ceph/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
