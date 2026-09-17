---
collection: csi-addons
version: "0.14.0"
title: "VolumeReplicationClass"
source_url: https://github.com/csi-addons/kubernetes-csi-addons/blob/621cfdc3b7d36922a8d328324643540eeac2671d/docs/volumereplicationclass.md
fetched_at: 2026-01-12T14:50:51Z
---
# VolumeReplicationClass

VolumeReplicationClass is a cluster scoped resource that contains driver related configuration parameters.

`provisioner` is name of the storage provisioner.

`parameters` contains key-value pairs that are passed down to the driver. Users can add their own key-value pairs. Keys with `replication.storage.openshift.io/` prefix are reserved by operator and not passed down to the driver.

## Reserved parameter keys

- `replication.storage.openshift.io/replication-secret-name`
- `replication.storage.openshift.io/replication-secret-namespace`

```yaml
apiVersion: replication.storage.openshift.io/v1alpha1
kind: VolumeReplicationClass
metadata:
  name: volumereplicationclass-sample
spec:
  provisioner: example.provisioner.io
  parameters:
    replication.storage.openshift.io/replication-secret-name: secret-name
    replication.storage.openshift.io/replication-secret-namespace: secret-namespace
    # schedulingInterval is a vendor specific parameter. It is used to set the
    # replication scheduling interval for storage volumes that are replication
    # enabled using related VolumeReplication resource
    schedulingInterval: 1m
```
