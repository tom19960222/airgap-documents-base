---
collection: csi-addons
version: "0.14.0"
title: "VolumeGroupReplicationContent"
source_url: https://github.com/csi-addons/kubernetes-csi-addons/blob/621cfdc3b7d36922a8d328324643540eeac2671d/docs/volumegroupreplicationcontent.md
fetched_at: 2026-01-12T14:50:51Z
---
# VolumeGroupReplicationContent

VolumeGroupReplicationContent is a cluster scoped resource that contains volume grouping related information.

`volumeGroupAttributes` contains key-value pairs from the VolumeGroupContext field available in the
CreateVolumeGroupResponse returned by the CSI driver.

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
  volumeGroupAttributes:
    clusterID: my-cluster
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
