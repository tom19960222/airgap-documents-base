---
collection: k8s
version: "1.31.6"
title: "PodReadyToStartContainersCondition"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/pod-ready-to-start-containers.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable the kubelet to mark the [PodReadyToStartContainers](/docs/concepts/workloads/pods/pod-lifecycle/#pod-has-network) condition on pods.

This feature gate was previously known as `PodHasNetworkCondition`, and the associated condition was
named `PodHasNetwork`.
