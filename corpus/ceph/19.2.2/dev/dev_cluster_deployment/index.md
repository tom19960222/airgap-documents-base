---
collection: ceph
version: "19.2.2"
title: "Deploying a development cluster"
source_url: https://docs.ceph.com/en/squid/dev/dev_cluster_deployment/
fetched_at: 2026-07-27T16:41:18+00:00
---
# Deploying a development cluster

In order to develop on ceph, a Ceph utility,
*vstart.sh*, allows you to deploy fake local cluster for development purpose.

## Usage

It allows to deploy a fake local cluster on your machine for development purpose. It starts rgw, mon, osd and/or mds, or all of them if not specified.

To start your development cluster, type the following:

```
vstart.sh [OPTIONS]...
```

In order to stop the cluster, you can type:

```
./stop.sh
```

## Options

-b, --bluestore
:   Use bluestore as the objectstore backend for osds.

--cache <pool>
:   Set a cache-tier for the specified pool.

-d, --debug
:   Launch in debug mode.

-e
:   Create an erasure pool.

--hitset <pool> <hit_set_type>
:   Enable hitset tracking.

-i ip_address
:   Bind to the specified *ip_address* instead of guessing and resolve from hostname.

-k
:   Keep old configuration files instead of overwriting these.

-K, --kstore
:   Use kstore as the osd objectstore backend.

-l, --localhost
:   Use localhost instead of hostname.

-m ip[:port]
:   Specifies monitor *ip* address and *port*.

--memstore
:   Use memstore as the objectstore backend for osds

--multimds <count>
:   Allow multimds with maximum active count.

-n, --new
:   Create a new cluster.

-N, --not-new
:   Reuse existing cluster config (default).

--nodaemon
:   Use ceph-run as wrapper for mon/osd/mds.

--nolockdep
:   Disable lockdep

-o <config>
:   Add *config* to all sections in the ceph configuration.

--rgw_port <port>
:   Specify ceph rgw http listen port.

--rgw_frontend <frontend>
:   Specify the rgw frontend configuration (default is civetweb).

--rgw_compression <compression_type>
:   Specify the rgw compression plugin (default is disabled).

--smallmds
:   Configure mds with small limit cache size.

--short
:   Short object names only; necessary for ext4 dev

--valgrind[_{osd,mds,mon}] 'valgrind_toolname [args...]'
:   Launch the osd/mds/mon/all the ceph binaries using valgrind with the specified tool and arguments.

--without-dashboard
:   Do not run using mgr dashboard.

-x
:   Enable cephx (on by default).

-X
:   Disable cephx.

## Environment variables

{OSD,MDS,MON,RGW}

These environment variables will contains the number of instances of the desired ceph process you want to start.

Example:

```
OSD=3 MON=3 RGW=1 vstart.sh
```

# Deploying multiple development clusters on the same machine

In order to bring up multiple ceph clusters on the same machine, *mstart.sh* a
small wrapper around the above *vstart* can help.

## Usage

To start multiple clusters, you would run mstart for each cluster you would want
to deploy, and it will start monitors, rgws for each cluster on different ports
allowing you to run multiple mons, rgws etc. on the same cluster. Invoke it in
the following way:

```
mstart.sh <cluster-name> <vstart options>
```

For eg:

```
./mstart.sh cluster1 -n
```

For stopping the cluster, you do:

```
./mstop.sh <cluster-name>
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
