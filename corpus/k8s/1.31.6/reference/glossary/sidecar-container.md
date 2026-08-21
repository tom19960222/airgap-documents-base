---
collection: k8s
version: "1.31.6"
title: "Sidecar Container"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/sidecar-container.md
fetched_at: 2026-01-16T10:18:07+05:30
---
One or more containers that are typically started before any app containers run.

<!--more--> 

Sidecar containers are like regular app containers, but with a different purpose: the sidecar provides a Pod-local service to the main app container.
Unlike init containers, sidecar containers
continue running after Pod startup.

Read [Sidecar containers](/docs/concepts/workloads/pods/sidecar-containers/) for more information.
