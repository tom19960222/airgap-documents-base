---
collection: k8s
version: "1.31.6"
title: "Replica"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/replica.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A copy or duplicate of a Pod or
a set of pods. Replicas ensure high availability, scalability, and fault tolerance
by maintaining multiple identical instances of a pod.

<!--more-->
Replicas are commonly used in Kubernetes to achieve the desired application state and reliability.
They enable workload scaling and distribution across multiple nodes in a cluster.

By defining the number of replicas in a Deployment or ReplicaSet, Kubernetes ensures that
the specified number of instances are running, automatically adjusting the count as needed.

Replica management allows for efficient load balancing, rolling updates, and
self-healing capabilities in a Kubernetes cluster.
