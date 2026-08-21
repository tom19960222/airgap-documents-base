---
collection: k8s
version: "1.31.6"
title: "KubeletPodResourcesDynamicResources"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/kubelet-pod-resources-dynamic-resources.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Extend the kubelet's pod resources gRPC endpoint to
to include resources allocated in `ResourceClaims` via `DynamicResourceAllocation` API.
See [resource allocation reporting](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#monitoring-device-plugin-resources) for more details.
with information about the allocatable resources, enabling clients to properly
track the free compute resources on a node.
