---
collection: k8s
version: "1.31.6"
title: "CSIMigrationAzureDiskComplete"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/csi-migration-azure-disk-complete.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Stops registering the Azure-Disk in-tree
plugin in kubelet and volume controllers and enables shims and translation
logic to route volume operations from the Azure-Disk in-tree plugin to
AzureDisk CSI plugin. Requires CSIMigration and CSIMigrationAzureDisk feature
flags enabled and AzureDisk CSI plugin installed and configured on all nodes
in the cluster. This flag has been deprecated in favor of the
`InTreePluginAzureDiskUnregister` feature flag which prevents the registration
of in-tree AzureDisk plugin.
