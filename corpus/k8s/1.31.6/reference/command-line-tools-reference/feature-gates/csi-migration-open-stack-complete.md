---
collection: k8s
version: "1.31.6"
title: "CSIMigrationOpenStackComplete"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/csi-migration-open-stack-complete.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Stops registering the Cinder in-tree plugin in
kubelet and volume controllers and enables shims and translation logic to route
volume operations from the Cinder in-tree plugin to Cinder CSI plugin.
Requires CSIMigration and CSIMigrationOpenStack feature flags enabled and Cinder
CSI plugin installed and configured on all nodes in the cluster. This flag has
been deprecated in favor of the `InTreePluginOpenStackUnregister` feature flag
which prevents the registration of in-tree openstack cinder plugin.
