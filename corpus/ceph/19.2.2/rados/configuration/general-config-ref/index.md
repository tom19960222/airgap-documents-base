---
collection: ceph
version: "19.2.2"
title: "General Config Reference"
source_url: https://docs.ceph.com/en/squid/rados/configuration/general-config-ref/
fetched_at: 2026-07-27T16:39:36+00:00
---
# General Config Reference

admin_socket
:   > The socket for executing administrative commands on a daemon,
    > irrespective of whether Ceph Monitors have established a quorum.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `/var/run/ceph/$cluster-$name.asok`

pid_file
:   > The file in which the mon, osd or mds will write its PID. For
    > instance, `/var/run/$cluster/$type.$id.pid` will create
    > /var/run/ceph/mon.a.pid for the `mon` with id `a` running in the
    > `ceph` cluster. The `pid file` is removed when the daemon stops
    > gracefully. If the process is not daemonized (i.e. runs with the
    > `-f` or `-d` option), the `pid file` is not created.
    >
    > type:
    > :   `str`

chdir
:   > The directory Ceph daemons change to once they are up and running.
    > Default `/` directory recommended.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   `daemonize`

fatal_signal_handlers
:   > If set, we will install signal handlers for SEGV, ABRT, BUS, ILL, FPE,
    > XCPU, XFSZ, SYS signals to generate a useful log message
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

max_open_files
:   If set, when the [Ceph Storage Cluster](../../../glossary/index.md#term-Ceph-Storage-Cluster) starts, Ceph sets
    the max open FDs at the OS level (i.e., the max # of file
    descriptors). A suitably large value prevents Ceph Daemons from running out
    of file descriptors.

    Type:
    :   64-bit Integer

    Required:
    :   No

    Default:
    :   `0`

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
