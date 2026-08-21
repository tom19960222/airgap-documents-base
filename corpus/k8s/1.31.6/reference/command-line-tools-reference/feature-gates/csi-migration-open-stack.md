---
collection: k8s
version: "1.31.6"
title: "CSIMigrationOpenStack"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/csi-migration-open-stack.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables shims and translation logic to route volume
operations from the Cinder in-tree plugin to Cinder CSI plugin. Supports
falling back to in-tree Cinder plugin for mount operations to nodes that have
the feature disabled or that do not have Cinder CSI plugin installed and
configured. Does not support falling back for provision operations, for those
the CSI plugin must be installed and configured. Requires CSIMigration
feature flag enabled.
