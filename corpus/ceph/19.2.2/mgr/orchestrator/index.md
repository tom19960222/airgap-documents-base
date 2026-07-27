---
collection: ceph
version: "19.2.2"
title: "Orchestrator CLI"
source_url: https://docs.ceph.com/en/squid/mgr/orchestrator/
fetched_at: 2026-07-27T16:40:13+00:00
---
# Orchestrator CLI

This module provides a command line interface (CLI) for orchestrator modules.
Orchestrator modules are `ceph-mgr` plugins that interface with external
orchestration services.

## Definition of Terms

The orchestrator CLI unifies multiple external orchestrators, so we need a
common nomenclature for the orchestrator module:

|  |  |
| --- | --- |
| *host* | hostname (not the DNS name) of the physical host. Not the podname, container name, or hostname inside the container. |
| *service type* | The type of the service. e.g., nfs, mds, osd, mon, rgw, mgr, iscsi |
| *service* | A logical service. Typically comprised of multiple service instances on multiple hosts for HA   - `fs_name` for mds type - `rgw_zone` for rgw type - `ganesha_cluster_id` for nfs type |
| *daemon* | A single instance of a service. Usually a daemon, but maybe not (e.g., might be a kernel service like LIO or knfsd or whatever)  This identifier should uniquely identify the instance. |

Here is how the names relate:

- A *service* has a specific *service type*.
- A *daemon* is a physical instance of a *service type*.

> **Note:**
>
> Orchestrator modules might implement only a subset of the commands listed
> below. The implementation of the commands may differ between modules.

## Status

```
ceph orch status [--detail]
```

This command shows the current orchestrator mode and its high-level status
(whether the orchestrator plugin is available and operational).

## Stateless services (MDS/RGW/NFS/rbd-mirror/iSCSI)

> **Note:**
>
> The orchestrator will not configure the services. See the relevant
> documentation for details about how to configure particular services.

The `name` parameter identifies the kind of the group of instances. The
following short list explains the meaning of the `name` parameter:

- A CephFS file system identifies a group of MDS daemons.
- A zone name identifies a group of RGWs.

Creating/growing/shrinking/removing services:

```
ceph orch apply mds <fs_name> [--placement=<placement>] [--dry-run]
ceph orch apply rgw <name> [--realm=<realm>] [--zone=<zone>] [--port=<port>] [--ssl] [--placement=<placement>] [--dry-run]
ceph orch apply nfs <name> <pool> [--namespace=<namespace>] [--placement=<placement>] [--dry-run]
ceph orch rm <service_name> [--force]
```

where `placement` is a [Daemon Placement](../../cephadm/services/index.md#orchestrator-cli-placement-spec).

e.g., `ceph orch apply mds myfs --placement="3 host1 host2 host3"`

Service Commands:

```
ceph orch <start|stop|restart|redeploy|reconfig> <service_name>
```

> **Note:**
>
> These commands apply only to cephadm containerized daemons.

## Options

start
:   Start the daemon on the corresponding host.

stop
:   Stop the daemon on the corresponding host.

restart
:   Restart the daemon on the corresponding host.

redeploy
:   Redeploy the Ceph daemon on the corresponding host. This will recreate the daemon directory
    structure under `/var/lib/ceph/<fsid>/<daemon-name>` (if it doesn’t exist), refresh its
    configuration files, regenerate its unit-files and restarts the systemd daemon.

reconfig
:   Reconfigure the daemon on the corresponding host. This will refresh configuration files then restart the daemon.

    > **Note:**
    >
    > this command assumes the daemon directory `/var/lib/ceph/<fsid>/<daemon-name>` already exists.

## Configuring the Orchestrator CLI

Enable the orchestrator by using the `set backend` command to select the orchestrator module that will be used:

```
ceph orch set backend <module>
```

### Example - Configuring the Orchestrator CLI

For example, to enable the Rook orchestrator module and use it with the CLI:

```
ceph mgr module enable rook
ceph orch set backend rook
```

Confirm that the backend is properly configured:

```
ceph orch status
```

### Disable the Orchestrator

To disable the orchestrator, use the empty string `""`:

```
ceph orch set backend ""
ceph mgr module disable rook
```

## Current Implementation Status

This is an overview of the current implementation status of the orchestrators.

| Command | Rook | Cephadm |
| --- | --- | --- |
| apply iscsi | ⚪ | ✔ |
| apply mds | ✔ | ✔ |
| apply mgr | ⚪ | ✔ |
| apply mon | ✔ | ✔ |
| apply nfs | ✔ | ✔ |
| apply osd | ✔ | ✔ |
| apply rbd-mirror | ✔ | ✔ |
| apply cephfs-mirror | ⚪ | ✔ |
| apply grafana | ⚪ | ✔ |
| apply prometheus | ❌ | ✔ |
| apply alertmanager | ❌ | ✔ |
| apply node-exporter | ❌ | ✔ |
| apply rgw | ✔ | ✔ |
| apply container | ⚪ | ✔ |
| apply snmp-gateway | ❌ | ✔ |
| host add | ⚪ | ✔ |
| host ls | ✔ | ✔ |
| host rm | ⚪ | ✔ |
| host maintenance enter | ❌ | ✔ |
| host maintenance exit | ❌ | ✔ |
| daemon status | ⚪ | ✔ |
| daemon {stop,start,…} | ⚪ | ✔ |
| device {ident,fault}-(on,off} | ⚪ | ✔ |
| device ls | ✔ | ✔ |
| iscsi add | ⚪ | ✔ |
| mds add | ⚪ | ✔ |
| nfs add | ⚪ | ✔ |
| rbd-mirror add | ⚪ | ✔ |
| rgw add | ⚪ | ✔ |
| ls | ✔ | ✔ |
| ps | ✔ | ✔ |
| status | ✔ | ✔ |
| upgrade | ❌ | ✔ |

where

- ⚪ = not yet implemented
- ❌ = not applicable
- ✔ = implemented

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
