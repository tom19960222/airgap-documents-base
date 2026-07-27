---
collection: ceph
version: "19.2.2"
title: "ceph-syn -- ceph synthetic workload generator"
source_url: https://docs.ceph.com/en/squid/man/8/ceph-syn/
fetched_at: 2026-07-27T16:42:01+00:00
---
# ceph-syn -- ceph synthetic workload generator

## Synopsis

**ceph-syn** [ -m *monaddr*:*port* ] --syn *command* *…*

## Description

**ceph-syn** is a simple synthetic workload generator for the Ceph
distributed file system. It uses the userspace client library to
generate simple workloads against a currently running file system. The
file system need not be mounted via ceph-fuse(8) or the kernel client.

One or more `--syn` command arguments specify the particular
workload, as documented below.

## Options

-d
:   Detach from console and daemonize after startup.

-c ceph.conf, --conf=ceph.conf
:   Use *ceph.conf* configuration file instead of the default
    `/etc/ceph/ceph.conf` to determine monitor addresses during
    startup.

-m monaddress[:port]
:   Connect to specified monitor (instead of looking through
    `ceph.conf`).

--num_client num
:   Run num different clients, each in a separate thread.

--syn workloadspec
:   Run the given workload. May be specified as many times as
    needed. Workloads will normally run sequentially.

## Workloads

Each workload should be preceded by `--syn` on the command
line. This is not a complete list.

**mknap** *path* *snapname*
:   Create a snapshot called *snapname* on *path*.

**rmsnap** *path* *snapname*
:   Delete snapshot called *snapname* on *path*.

**rmfile** *path*
:   Delete/unlink *path*.

**writefile** *sizeinmb* *blocksize*
:   Create a file, named after our client id, that is *sizeinmb* MB by
    writing *blocksize* chunks.

**readfile** *sizeinmb* *blocksize*
:   Read file, named after our client id, that is *sizeinmb* MB by
    writing *blocksize* chunks.

**rw** *sizeinmb* *blocksize*
:   Write file, then read it back, as above.

**makedirs** *numsubdirs* *numfiles* *depth*
:   Create a hierarchy of directories that is *depth* levels deep. Give
    each directory *numsubdirs* subdirectories and *numfiles* files.

**walk**
:   Recursively walk the file system (like find).

## Availability

**ceph-syn** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at <https://docs.ceph.com> for more information.

## See also

[ceph](../ceph/index.md)(8),
[ceph-fuse](../ceph-fuse/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
