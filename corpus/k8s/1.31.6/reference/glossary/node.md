---
collection: k8s
version: "1.31.6"
title: "Node"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/node.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A node is a worker machine in Kubernetes.

<!--more-->

A worker node may be a VM or physical machine, depending on the cluster. It has local daemons or services necessary to run Pods and is managed by the control plane. The daemons on a node include kubelet, kube-proxy, and a container runtime implementing the CRI such as docker.

In early Kubernetes versions, Nodes were called "Minions".
