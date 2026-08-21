---
collection: k8s
version: "1.31.6"
title: "SeparateTaintEvictionController"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/separate-taint-eviction-controller.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables running `TaintEvictionController`,
that performs [Taint-based Evictions](/docs/concepts/scheduling-eviction/taint-and-toleration/#taint-based-evictions),
in a controller separated from `NodeLifecycleController`. When this feature is
enabled, users can optionally disable Taint-based Eviction setting the
`--controllers=-taint-eviction-controller` flag on the `kube-controller-manager`.
