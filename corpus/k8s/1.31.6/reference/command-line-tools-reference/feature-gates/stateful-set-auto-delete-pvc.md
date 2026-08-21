---
collection: k8s
version: "1.31.6"
title: "StatefulSetAutoDeletePVC"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/stateful-set-auto-delete-pvc.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Allows the use of the optional `.spec.persistentVolumeClaimRetentionPolicy` field, 
providing control over the deletion of PVCs in a StatefulSet's lifecycle.
See
[PersistentVolumeClaim retention](/docs/concepts/workloads/controllers/statefulset/#persistentvolumeclaim-retention)
for more details.
