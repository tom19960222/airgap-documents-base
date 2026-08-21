---
collection: k8s
version: "1.31.6"
title: "Deployment"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/deployment.md
fetched_at: 2026-01-16T10:18:07+05:30
---
An API object that manages a replicated application, typically by running Pods with no local state.

<!--more--> 

Each replica is represented by a pod, and the Pods are distributed among the 
nodes of a cluster.
For workloads that do require local state, consider using a StatefulSet.
