---
collection: k8s
version: "1.31.6"
title: "NodeSwap"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/node-swap.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable the kubelet to allocate swap memory for Kubernetes workloads on a node.
Must be used with `KubeletConfiguration.failSwapOn` set to false.
For more details, please see [swap memory](/docs/concepts/architecture/nodes/#swap-memory)
