---
collection: ceph
version: "19.2.2"
title: "MDS Service"
source_url: https://docs.ceph.com/en/squid/cephadm/services/mds/
fetched_at: 2026-07-27T16:39:22+00:00
---
# MDS Service

## Deploy CephFS

One or more MDS daemons is required to use the [CephFS](../../../glossary/index.md#term-CephFS) file system.
These are created automatically if the newer `ceph fs volume`
interface is used to create a new file system. For more information,
see [FS volumes and subvolumes](../../../cephfs/fs-volumes/index.md#fs-volumes-and-subvolumes).

For example:

```
ceph fs volume create <fs_name> --placement="<placement spec>"
```

where `fs_name` is the name of the CephFS and `placement` is a
[Daemon Placement](../index.md#orchestrator-cli-placement-spec). For example, to place
MDS daemons for the new `foo` volume on hosts labeled with `mds`:

```
ceph fs volume create foo --placement="label:mds"
```

You can also update the placement after-the-fact via:

```
ceph orch apply mds foo 'mds-[012]'
```

For manually deploying MDS daemons, use this specification:

```yaml
service_type: mds
service_id: fs_name
placement:
  count: 3
  label: mds
```

The specification can then be applied using:

```
ceph orch apply -i mds.yaml
```

See [Stateless services (MDS/RGW/NFS/rbd-mirror/iSCSI)](../../../mgr/orchestrator/index.md#orchestrator-cli-stateless-services) for manually deploying
MDS daemons on the CLI.

## Further Reading

- [Ceph File System](../../../cephfs/index.md#ceph-file-system)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
