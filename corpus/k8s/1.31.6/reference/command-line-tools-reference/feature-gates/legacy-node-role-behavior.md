---
collection: k8s
version: "1.31.6"
title: "LegacyNodeRoleBehavior"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/legacy-node-role-behavior.md
fetched_at: 2026-01-16T10:18:07+05:30
---
When disabled, legacy behavior in service load balancers and
node disruption will ignore the `node-role.kubernetes.io/master` label in favor of the
feature-specific labels provided by `NodeDisruptionExclusion` and `ServiceNodeExclusion`.
