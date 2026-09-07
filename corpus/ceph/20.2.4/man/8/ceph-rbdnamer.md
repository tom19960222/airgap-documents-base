---
collection: ceph
version: "20.2.4"
title: "ceph-rbdnamer -- udev helper to name RBD devices"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/man/8/ceph-rbdnamer.rst
fetched_at: 2026-08-18T01:32:45Z
---
:orphan:

# ceph-rbdnamer -- udev helper to name RBD devices

.. program:: ceph-rbdnamer

# Synopsis

| **ceph-rbdnamer** *num*

# Description

**ceph-rbdnamer** prints the pool, namespace, image and snapshot names
for a given RBD device to stdout. It is used by `udev` device manager
to set up RBD device symlinks. The appropriate `udev` rules are
provided in a file named `50-rbd.rules`.

# Availability

**ceph-rbdnamer** is part of Ceph, a massively scalable, open-source, distributed storage system.  Please
refer to the Ceph documentation at https://docs.ceph.com for more
information.

# See also

rbd\(8),
ceph\(8)
