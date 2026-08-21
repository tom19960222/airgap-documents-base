---
collection: k8s
version: "1.31.6"
title: "Garbage Collection"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/garbage-collection.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Garbage collection is a collective term for the various mechanisms Kubernetes uses to clean up
cluster resources. 

<!--more-->

Kubernetes uses garbage collection to clean up resources like
[unused containers and images](/docs/concepts/architecture/garbage-collection/#containers-images),
[failed Pods](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection),
[objects owned by the targeted resource](/docs/concepts/overview/working-with-objects/owners-dependents/),
[completed Jobs](/docs/concepts/workloads/controllers/ttlafterfinished/), and resources
that have expired or failed.
