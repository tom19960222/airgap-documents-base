---
collection: ceph
version: "20.2.4"
title: "Operating a Cluster"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rados/operations/operating.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Operating a Cluster

.. index:: systemd; operating a cluster

## Running Ceph with systemd

In all distributions that support systemd (CentOS 7, Fedora, Debian
Jessie 8 and later, and SUSE), systemd files (and NOT legacy SysVinit scripts)
are used to manage Ceph daemons. Ceph daemons therefore behave like any other daemons
that can be controlled by the ``systemctl`` command, as in the following examples:

```bash
sudo systemctl start ceph.target       # start all daemons
sudo systemctl status ceph-osd@12      # check status of osd.12
```

To list all of the Ceph systemd units on a node, run the following command:

```bash
sudo systemctl status ceph\*.service ceph\*.target
```

### Starting all daemons

To start all of the daemons on a Ceph node (regardless of their type), run the
following command:

```bash
sudo systemctl start ceph.target
```

### Stopping all daemons

To stop all of the daemons on a Ceph node (regardless of their type), run the
following command:

```bash
sudo systemctl stop ceph\*.service ceph\*.target
```

### Starting all daemons by type

To start all of the daemons of a particular type on a Ceph node, run one of the
following commands:

```bash
sudo systemctl start ceph-osd.target
sudo systemctl start ceph-mon.target
sudo systemctl start ceph-mds.target
```

### Stopping all daemons by type

To stop all of the daemons of a particular type on a Ceph node, run one of the
following commands:

```bash
sudo systemctl stop ceph-osd\*.service ceph-osd.target
sudo systemctl stop ceph-mon\*.service ceph-mon.target
sudo systemctl stop ceph-mds\*.service ceph-mds.target
```

### Starting a daemon

To start a specific daemon instance on a Ceph node, run one of the
following commands:

```bash
sudo systemctl start ceph-osd@{id}
sudo systemctl start ceph-mon@{hostname}
sudo systemctl start ceph-mds@{hostname}
```

For example:

```bash
sudo systemctl start ceph-osd@1
sudo systemctl start ceph-mon@ceph-server
sudo systemctl start ceph-mds@ceph-server
```

### Stopping a daemon

To stop a specific daemon instance on a Ceph node, run one of the
following commands:

```bash
sudo systemctl stop ceph-osd@{id}
sudo systemctl stop ceph-mon@{hostname}
sudo systemctl stop ceph-mds@{hostname}
```

For example:

```bash
sudo systemctl stop ceph-osd@1
sudo systemctl stop ceph-mon@ceph-server
sudo systemctl stop ceph-mds@ceph-server
```

.. index:: sysvinit; operating a cluster

## Running Ceph with SysVinit

Each time you start, restart, or stop Ceph daemons, you must specify at least one option and one command.
Likewise, each time you start, restart, or stop your entire cluster, you must specify at least one option and one command.
In both cases, you can also specify a daemon type or a daemon instance. :

```
{commandline} [options] [commands] [daemons]
```

The ``ceph`` options include:

| Option | Shortcut | Description |
| --- | --- | --- |
| ``--verbose`` | ``-v`` | Use verbose logging. |
| ``--valgrind`` | ``N/A`` | (Dev and QA only) Use [Valgrind](http://www.valgrind.org/) debugging. |
| ``--allhosts`` <br> | ``-a`` <br> | Execute on all nodes listed in ``ceph.conf``. <br> Otherwise, it only executes on ``localhost``. |
| ``--restart`` | ``N/A`` | Automatically restart daemon if it core dumps. |
| ``--norestart`` | ``N/A`` | Do not restart a daemon if it core dumps. |
| ``--conf`` | ``-c`` | Use an alternate configuration file. |

The ``ceph`` commands include:

| Command | Description |
| --- | --- |
| ``start`` | Start the daemon(s). |
| ``stop`` | Stop the daemon(s). |
| ``forcestop`` | Force the daemon(s) to stop. Same as ``kill -9``. |
| ``killall`` | Kill all daemons of a particular type. |
| ``cleanlogs`` | Cleans out the log directory. |
| ``cleanalllogs`` | Cleans out **everything** in the log directory. |

The ``[daemons]`` option allows the ``ceph`` service to target specific daemon types
in order to perform subsystem operations. Daemon types include:

- ``mon``
- ``osd``
- ``mds``
