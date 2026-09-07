---
collection: ceph
version: "20.2.4"
title: "Mount CephFS: Prerequisites"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/cephfs/mount-prerequisites.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Mount CephFS: Prerequisites

You can use CephFS by mounting the file system on a machine or by using
cephfs-shell <!-- unresolved-rst-link: kind=ref target=cephfs-shell -->. A system mount can be performed using [the kernel driver](mount-using-kernel-driver.md) as well as [the FUSE driver](mount-using-fuse.md). Both have their own advantages
and disadvantages. Read the following section to understand more about both of
these ways to mount CephFS.

For Windows CephFS mounts, please check the [ceph-dokan](ceph-dokan.md) page.

## Which CephFS Client?

The FUSE client is the most accessible and the easiest to upgrade to the
version of Ceph used by the storage cluster, while the kernel client will
always gives better performance.

When encountering bugs or performance issues, it is often instructive to
try using the other client, in order to find out whether the bug was
client-specific or not (and then to let the developers know).

## General Pre-requisite for Mounting CephFS
Before mounting CephFS, ensure that the client host (where CephFS has to be
mounted and used) has a copy of the Ceph configuration file (i.e.
``ceph.conf``) and a keyring of the CephX user that has permission to access
the MDS. Both of these files must already be present on the host where the
Ceph MON resides.

1. Generate a minimal conf file for the client host and place it at a
   standard location:

```
# on client host
mkdir -p -m 755 /etc/ceph
ssh {user}@{mon-host} "sudo ceph config generate-minimal-conf" | sudo tee /etc/ceph/ceph.conf
```

   Alternatively, you may copy the conf file. But the above method generates
   a conf with minimal details which is usually sufficient. For more
   information, see [Client Authentication](client-auth.md) and [bootstrap-options](../rados/configuration/ceph-conf.md#bootstrap-options).

1. Ensure that the conf has appropriate permissions:

```
chmod 644 /etc/ceph/ceph.conf
```

1. Create a CephX user and get its secret key:

```
 ssh {user}@{mon-host} "sudo ceph fs authorize cephfs client.foo / rw" | sudo tee /etc/ceph/ceph.client.foo.keyring

In above command, replace ``cephfs`` with the name of your CephFS, ``foo``
by the name you want for your CephX user and ``/`` by the path within your
CephFS for which you want to allow access to the client host and ``rw``
stands for both read and write permissions. Alternatively, you may copy the
Ceph keyring from the MON host to client host at ``/etc/ceph`` but creating
a keyring specific to the client host is better. While creating a CephX
keyring/client, using same client name across multiple machines is perfectly
fine.

.. note:: If you get 2 prompts for password while running above any of 2
          above command, run ``sudo ls`` (or any other trivial command with
          sudo) immediately before these commands.
```

1. Ensure that the keyring has appropriate permissions:

```
chmod 600 /etc/ceph/ceph.client.foo.keyring
```

> **Note:** There might be few more prerequisites for kernel and FUSE mounts
> individually, please check respective mount documents.
