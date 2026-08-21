---
collection: k8s
version: "1.31.6"
title: "PodAndContainerStatsFromCRI"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/pod-and-container-stats-from-cri.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Configure the kubelet to gather container and pod stats from the CRI container runtime rather than gathering them from cAdvisor.
As of 1.26, this also includes gathering metrics from CRI and emitting them over `/metrics/cadvisor` (rather than having cAdvisor emit them directly).
