---
collection: k8s
version: "1.31.6"
title: "Container Runtime Interface (CRI)"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/cri.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The main protocol for the communication between the kubelet and Container Runtime.

<!--more-->

The Kubernetes Container Runtime Interface (CRI) defines the main
[gRPC](https://grpc.io) protocol for the communication between the
[node components](/docs/concepts/architecture/#node-components)
kubelet and
container runtime.
