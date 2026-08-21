---
collection: k8s
version: "1.31.6"
title: "GracefulNodeShutdown"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/graceful-node-shutdown.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables support for graceful shutdown in kubelet.
During a system shutdown, kubelet will attempt to detect the shutdown event
and gracefully terminate pods running on the node. See
[Graceful Node Shutdown](/docs/concepts/architecture/nodes/#graceful-node-shutdown)
for more details.
