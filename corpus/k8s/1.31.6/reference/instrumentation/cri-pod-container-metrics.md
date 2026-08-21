---
collection: k8s
version: "1.31.6"
title: "CRI Pod & Container Metrics"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/instrumentation/cri-pod-container-metrics.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

(Feature state: alpha, as of v1.23)

The [kubelet](/docs/reference/command-line-tools-reference/kubelet/) collects pod and
container metrics via [cAdvisor](https://github.com/google/cadvisor). As an alpha feature,
Kubernetes lets you configure the collection of pod and container
metrics via the Container Runtime Interface (CRI). You
must enable the `PodAndContainerStatsFromCRI` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) and
use a compatible CRI implementation (containerd >= 1.6.0, CRI-O >= 1.23.0) to
use the CRI based collection mechanism.

<!-- body -->

## CRI Pod & Container Metrics

With `PodAndContainerStatsFromCRI` enabled, the kubelet polls the underlying container
runtime for pod and container stats instead of inspecting the host system directly using cAdvisor.
The benefits of relying on the container runtime for this information as opposed to direct
collection with cAdvisor include:

- Potential improved performance if the container runtime already collects this information
  during normal operations. In this case, the data can be re-used instead of being aggregated
  again by the kubelet.

- It further decouples the kubelet and the container runtime allowing collection of metrics for
  container runtimes that don't run processes directly on the host with kubelet where they are
  observable by cAdvisor (for example: container runtimes that use virtualization).
