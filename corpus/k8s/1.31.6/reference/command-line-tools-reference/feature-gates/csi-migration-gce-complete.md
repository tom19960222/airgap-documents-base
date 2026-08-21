---
collection: k8s
version: "1.31.6"
title: "CSIMigrationGCEComplete"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/csi-migration-gce-complete.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Stops registering the GCE-PD in-tree plugin in
kubelet and volume controllers and enables shims and translation logic to
route volume operations from the GCE-PD in-tree plugin to PD CSI plugin.
Requires CSIMigration and CSIMigrationGCE feature flags enabled and PD CSI
plugin installed and configured on all nodes in the cluster. This flag has
been deprecated in favor of the `InTreePluginGCEUnregister` feature flag which
prevents the registration of in-tree GCE PD plugin.
