---
collection: k8s
version: "1.31.6"
title: "kube-scheduler"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/kube-scheduler.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Control plane component that watches for newly created
Pods with no assigned
node, and selects a node for them
to run on.

<!--more-->

Factors taken into account for scheduling decisions include:
individual and collective resource requirements, hardware/software/policy
constraints, affinity and anti-affinity specifications, data locality,
inter-workload interference, and deadlines.
