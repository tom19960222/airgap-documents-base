---
collection: k8s
version: "1.31.6"
title: "Kubelet"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/kubelet.md
fetched_at: 2026-01-16T10:18:07+05:30
---
An agent that runs on each node in the cluster. It makes sure that containers are running in a Pod.

<!--more-->

The [kubelet](/docs/reference/command-line-tools-reference/kubelet/) takes a set of PodSpecs that 
are provided through various mechanisms and ensures that the containers described in those 
PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by 
Kubernetes.
