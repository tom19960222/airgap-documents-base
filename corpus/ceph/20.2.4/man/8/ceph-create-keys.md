---
collection: ceph
version: "20.2.4"
title: "ceph-create-keys -- ceph keyring generate tool"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/man/8/ceph-create-keys.rst
fetched_at: 2026-08-18T01:32:45Z
---
:orphan:

# ceph-create-keys -- ceph keyring generate tool

.. program:: ceph-create-keys

# Synopsis

| **ceph-create-keys** [-h] [-v] [-t seconds] [--cluster *name*] --id *id*

# Description

ceph-create-keys is a utility to generate bootstrap keyrings using
the given monitor when it is ready.

It creates following auth entities (or users)

``client.admin``

    and its key for your client host.

``client.bootstrap-{osd, rgw, mds}``

    and their keys for bootstrapping corresponding services

To list all users in the cluster:

```
ceph auth ls
```

# Options

.. option:: --cluster

   name of the cluster (default 'ceph').

.. option:: -t

   time out after **seconds** (default: 600) waiting for a response from the monitor

.. option:: -i, --id

   id of a ceph-mon that is coming up. **ceph-create-keys** will wait until it joins quorum.

.. option:: -v, --verbose

   be more verbose.

# Availability

**ceph-create-keys** is part of Ceph, a massively scalable, open-source, distributed storage system.  Please refer
to the Ceph documentation at https://docs.ceph.com for more
information.

# See also

[ceph](../../install/clone-source.md)\(8)
