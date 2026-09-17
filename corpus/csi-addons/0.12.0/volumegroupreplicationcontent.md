---
collection: csi-addons
version: "0.12.0"
title: "VolumeGroupReplicationContent"
source_url: https://github.com/csi-addons/kubernetes-csi-addons/blob/57383f123ba4500174f945b919e81f41b61541d9/docs/volumegroupreplicationcontent.md
fetched_at: 2025-03-03T16:21:53+01:00
---
# VolumeGroupReplicationContent

VolumeGroupReplicationContent is a cluster scoped resource that contains volume grouping related information.

`volumeGroupReplicationRef` contains object reference of the volumeGroupReplication resource that created this resource.

`volumeGroupReplicationHandle` (optional) is an existing (but new) group replication ID.

`volumeGroupReplicationClassName` is the name of the VolumeGroupReplicationClass that contains the driver related info
for volume grouping.

`source` (optional) contains the VolumeGroupReplicationContentSource struct.

- `VolumeHandles` is the list of volume handles that this resource is responsible for grouping.

```yaml
apiVersion: replication.storage.openshift.io/v1alpha1
kind: VolumeGroupReplicationContent
metadata:
  name: volumegroupreplicationcontent-sample
spec:
  volumeGroupReplicationRef:
    kind: VolumeGroupReplication
    name: volumegroupreplication-sample
    namespace: default
  volumeGroupReplicationClassName: volumegroupreplicationclass-sample
  provisioner: example.provisioner.io
  source:
    volumeHandles:
      - myPersistentVolumeHandle
      - myPersistentVolumeHandle1
      - myPersistentVolumeHandle2
```
