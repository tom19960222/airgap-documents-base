---
collection: k8s
version: "1.31.6"
title: "MaxUnavailableStatefulSet"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/max-unavailable-stateful-set.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables setting the `maxUnavailable` field for the
[rolling update strategy](/docs/concepts/workloads/controllers/statefulset/#rolling-updates)
of a StatefulSet. The field specifies the maximum number of Pods
that can be unavailable during the update.
