---
collection: k8s
version: "1.31.6"
title: "CSIMigrationGCE"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/csi-migration-gce.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables shims and translation logic to route volume
operations from the GCE-PD in-tree plugin to PD CSI plugin. Supports falling
back to in-tree GCE plugin for mount operations to nodes that have the
feature disabled or that do not have PD CSI plugin installed and configured.
Does not support falling back for provision operations, for those the CSI
plugin must be installed and configured. Requires CSIMigration feature flag
enabled.
