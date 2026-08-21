---
collection: k8s
version: "1.31.6"
title: "Horizontal Pod Autoscaler"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/horizontal-pod-autoscaler.md
fetched_at: 2026-01-16T10:18:07+05:30
---
An API resource that automatically scales the number of pod replicas based on targeted CPU utilization or custom metric targets.

<!--more--> 

HPA is typically used with ReplicationControllers, Deployments, or ReplicaSets. It cannot be applied to objects that cannot be scaled, for example DaemonSets.
