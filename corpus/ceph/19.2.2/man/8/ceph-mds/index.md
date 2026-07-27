---
collection: ceph
version: "19.2.2"
title: "ceph-mds -- ceph metadata server daemon"
source_url: https://docs.ceph.com/en/squid/man/8/ceph-mds/
fetched_at: 2026-07-27T16:39:54+00:00
---
# ceph-mds -- ceph metadata server daemon

## Synopsis

**ceph-mds** -i <*ID*> [flags]

## Description

**ceph-mds** is the metadata server daemon for the Ceph distributed file
system. One or more instances of ceph-mds collectively manage the file
system namespace, coordinating access to the shared OSD cluster.

Each ceph-mds daemon instance should have a unique name. The name is used
to identify daemon instances in the ceph.conf.

Once the daemon has started, the monitor cluster will normally assign
it a logical rank, or put it in a standby pool to take over for
another daemon that crashes. Some of the specified options can cause
other behaviors.

## Options

-f, --foreground
:   Foreground: do not daemonize after startup (run in foreground). Do
    not generate a pid file. Useful when run via [ceph-run](../ceph-run/index.md)(8).

-d
:   Debug mode: like `-f`, but also send all log output to stderr.

--setuser userorgid
:   Set uid after starting. If a username is specified, the user
    record is looked up to get a uid and a gid, and the gid is also set
    as well, unless --setgroup is also specified.

--setgroup grouporgid
:   Set gid after starting. If a group name is specified the group
    record is looked up to get a gid.

-c ceph.conf, --conf=ceph.conf
:   Use *ceph.conf* configuration file instead of the default
    `/etc/ceph/ceph.conf` to determine monitor addresses during
    startup.

-m monaddress[:port]
:   Connect to specified monitor (instead of looking through
    `ceph.conf`).

--id/-i ID
:   Set ID portion of the MDS name. The ID should not start with a numeric digit.

--name/-n TYPE.ID
:   Set the MDS name of the format TYPE.ID. The TYPE is obviously ‘mds’.
    The ID should not start with a numeric digit.

## Availability

**ceph-mds** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at
<https://docs.ceph.com> for more information.

## See also

[ceph](../ceph/index.md)(8),
[ceph-mon](../ceph-mon/index.md)(8),
[ceph-osd](../ceph-osd/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
