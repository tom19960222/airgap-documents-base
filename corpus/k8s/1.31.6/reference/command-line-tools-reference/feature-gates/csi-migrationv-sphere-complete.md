---
collection: k8s
version: "1.31.6"
title: "CSIMigrationvSphereComplete"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/csi-migrationv-sphere-complete.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Stops registering the vSphere in-tree plugin in kubelet
and volume controllers and enables shims and translation logic to route volume operations
from the vSphere in-tree plugin to vSphere CSI plugin. Requires CSIMigration and
CSIMigrationvSphere feature flags enabled and vSphere CSI plugin installed and
configured on all nodes in the cluster. This flag has been deprecated in favor
of the `InTreePluginvSphereUnregister` feature flag which prevents the
registration of in-tree vsphere plugin.
