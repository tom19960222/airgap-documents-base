---
collection: csi-addons
version: "0.14.0"
title: "VolumeReplication"
source_url: https://github.com/csi-addons/kubernetes-csi-addons/blob/621cfdc3b7d36922a8d328324643540eeac2671d/docs/volumereplication.md
fetched_at: 2026-01-12T14:50:51Z
---
# VolumeReplication

VolumeReplication is a namespaced resource that contains references to storage object to be replicated and VolumeReplicationClass corresponding to the driver providing replication.

`volumeReplicationClass` is the class providing replication.

`replicationState` is the state of the volume being referenced. Possible values are `primary`, `secondary` and `resync`.

- `primary` denotes that the volume is primary
- `secondary` denotes that the volume is secondary
- `resync` denotes that the volume needs to be resynced

`dataSource` contains typed reference to the source being replicated.

- `apiGroup` is the group for the resource being referenced. If apiGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, apiGroup is required.
- `kind` is the kind of resource being replicated. For eg. PersistentVolumeClaim
- `name` is the name of the resource

`replicationHandle` (optional) is an existing (but new) replication ID.

```yaml
apiVersion: replication.storage.openshift.io/v1alpha1
kind: VolumeReplication
metadata:
  name: volumereplication-sample
  namespace: default
spec:
  volumeReplicationClass: volumereplicationclass-sample
  replicationState: primary
  replicationHandle: replicationHandle # optional
  dataSource:
    kind: PersistentVolumeClaim
    name: myPersistentVolumeClaim # should be in same namespace as VolumeReplication
```
