---
collection: k8s
version: "1.31.6"
title: "CSIMigrationRBD"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/csi-migration-rbd.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables shims and translation logic to route volume
operations from the RBD in-tree plugin to Ceph RBD CSI plugin. Requires
CSIMigration and csiMigrationRBD feature flags enabled and Ceph CSI plugin
installed and configured in the cluster.

This feature gate was deprecated in favor of the `InTreePluginRBDUnregister` feature gate,
which prevents the registration of in-tree RBD plugin.
