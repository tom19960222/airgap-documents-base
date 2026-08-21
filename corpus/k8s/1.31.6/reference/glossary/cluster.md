---
collection: k8s
version: "1.31.6"
title: "Cluster"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/cluster.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A set of worker machines, called nodes,
that run containerized applications. Every cluster has at least one worker node.

<!--more-->
The worker node(s) host the Pods that are
the components of the application workload. The
control plane manages the worker
nodes and the Pods in the cluster. In production environments, the control plane usually
runs across multiple computers and a cluster usually runs multiple nodes, providing
fault-tolerance and high availability.
