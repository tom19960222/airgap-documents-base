---
collection: k8s
version: "1.31.6"
title: "ReplicaSet"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/replica-set.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A ReplicaSet (aims to) maintain a set of replica Pods running at any given time.

<!--more-->

Workload objects such as deployment make use of ReplicaSets
to ensure that the configured number of Pods are
running in your cluster, based on the spec of that ReplicaSet.
