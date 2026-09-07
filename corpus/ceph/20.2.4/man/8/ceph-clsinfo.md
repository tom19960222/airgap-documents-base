---
collection: ceph
version: "20.2.4"
title: "ceph-clsinfo -- show class object information"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/man/8/ceph-clsinfo.rst
fetched_at: 2026-08-18T01:32:45Z
---
:orphan:

# ceph-clsinfo -- show class object information

.. program:: ceph-clsinfo

## Synopsis

| **ceph-clsinfo** [ *options* ] ... *filename*

## Description

**ceph-clsinfo** can show name, version, and architecture information
about a specific class object.

## Options

.. option:: -n, --name

   Shows the class name

.. option:: -v, --version

   Shows the class version

.. option:: -a, --arch

   Shows the class architecture

## Availability

**ceph-clsinfo** is part of Ceph, a massively scalable, open-source, distributed storage system. Please
refer to the Ceph documentation at https://docs.ceph.com for more
information.

## See also

[ceph](../../install/clone-source.md)\(8)
