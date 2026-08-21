---
collection: k8s
version: "1.31.6"
title: "NodeOutOfServiceVolumeDetach"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/node-out-of-service-volume-detach.md
fetched_at: 2026-01-16T10:18:07+05:30
---
When a Node is marked out-of-service using the
`node.kubernetes.io/out-of-service` taint, Pods on the node will be forcefully deleted
 if they can not tolerate this taint, and the volume detach operations for Pods terminating
 on the node will happen immediately. The deleted Pods can recover quickly on different nodes.
