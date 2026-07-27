---
collection: ceph
version: "19.2.2"
title: "Ceph Manager Daemon"
source_url: https://docs.ceph.com/en/squid/mgr/
fetched_at: 2026-07-27T16:38:47+00:00
---
# Ceph Manager Daemon

The [Ceph Manager](../glossary/index.md#term-Ceph-Manager) daemon (ceph-mgr) runs alongside monitor daemons,
to provide additional monitoring and interfaces to external monitoring
and management systems.

Since the 12.x (*luminous*) Ceph release, the ceph-mgr daemon is required for
normal operations. The ceph-mgr daemon is an optional component in
the 11.x (*kraken*) Ceph release.

By default, the manager daemon requires no additional configuration, beyond
ensuring it is running. If there is no mgr daemon running, you will
see a health warning to that effect, and some of the other information
in the output of ceph status will be missing or stale until a mgr is started.

Use your normal deployment tools, such as ceph-ansible or cephadm, to
set up ceph-mgr daemons on each of your mon nodes. It is not mandatory
to place mgr daemons on the same nodes as mons, but it is almost always
sensible.

- [ceph-mgr administrator’s guide](administrator/index.md)
- [Interpreting Manager Daemon Status](administrator/index.md#interpreting-manager-daemon-status)
- [Writing modules](modules/index.md)
- [Writing orchestrator plugins](orchestrator_modules/index.md)
- [Dashboard module](dashboard/index.md)
- [Ceph RESTful API](ceph_api/index.md)
- [Alerts module](alerts/index.md)
- [DiskPrediction module](diskprediction/index.md)
- [Local pool module](localpool/index.md)
- [RESTful module](restful/index.md)
- [Zabbix module](zabbix/index.md)
- [Prometheus module](prometheus/index.md)
- [Influx module](influx/index.md)
- [Hello module](hello/index.md)
- [Telegraf module](telegraf/index.md)
- [Telemetry module](telemetry/index.md)
- [Iostat module](iostat/index.md)
- [Crash module](crash/index.md)
- [Insights module](insights/index.md)
- [Orchestrator module](orchestrator/index.md)
- [Rook module](rook/index.md)
- [RGW module](rgw/index.md)
- [MDS Autoscaler module](mds_autoscaler/index.md)
- [NFS module](nfs/index.md)
- [Progress Module](progress/index.md)
- [CLI API Commands module](cli_api/index.md)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
