---
collection: k8s
version: "1.31.6"
title: "Init Container"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/init-container.md
fetched_at: 2026-01-16T10:18:07+05:30
---
One or more initialization containers that must run to completion before any app containers run.

<!--more--> 

Initialization (init) containers are like regular app containers, with one difference: init containers must run to completion before any app containers can start. Init containers run in series: each init container must run to completion before the next init container begins.

Unlike sidecar containers, init containers do not remain running after Pod startup.

For more information, read [init containers](/docs/concepts/workloads/pods/init-containers/).
