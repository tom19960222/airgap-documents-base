---
collection: ceph
version: "20.2.4"
title: "MDS Service"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/cephadm/services/mds.rst
fetched_at: 2026-08-18T01:32:45Z
---
# MDS Service

<a id="orchestrator-cli-cephfs"></a>

# Deploy CephFS

One or more MDS daemons is required to use the CephFS file system.
These are created automatically if the newer ``ceph fs volume``
interface is used to create a new file system. For more information,
see [fs-volumes-and-subvolumes](../../cephfs/fs-volumes.md#fs-volumes-and-subvolumes).

For example:

```bash
ceph fs volume create <fs_name> --placement="<placement spec>"
```

where ``fs_name`` is the name of the CephFS and ``placement`` is a
[orchestrator-cli-placement-spec](index.md#orchestrator-cli-placement-spec). For example, to place
MDS daemons for the new ``foo`` volume on hosts labeled with ``mds``:

```bash
ceph fs volume create foo --placement="label:mds"
```

You can also update the placement after-the-fact via:

```bash
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

```bash
ceph orch apply -i mds.yaml
```

See [orchestrator-cli-stateless-services](../../mgr/orchestrator.md#orchestrator-cli-stateless-services) for manually deploying
MDS daemons on the CLI.

# Further Reading

* [ceph-file-system](../../cephfs/index.md#ceph-file-system)
