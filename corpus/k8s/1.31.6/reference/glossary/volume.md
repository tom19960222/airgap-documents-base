---
collection: k8s
version: "1.31.6"
title: "Volume"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/volume.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A directory containing data, accessible to the containers in a pod.

<!--more-->

A Kubernetes volume lives as long as the Pod that encloses it. Consequently, a volume outlives any containers that run within the Pod, and data in the volume is preserved across container restarts.

See [storage](/docs/concepts/storage/) for more information.
