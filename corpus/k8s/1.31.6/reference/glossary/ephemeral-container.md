---
collection: k8s
version: "1.31.6"
title: "Ephemeral Container"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/ephemeral-container.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A container type that you can temporarily run inside a pod.

<!--more-->

If you want to investigate a Pod that's running with problems, you can add an ephemeral container to that Pod and carry out diagnostics. Ephemeral containers have no resource or scheduling guarantees, and you should not use them to run any part of the workload itself.

Ephemeral containers are not supported by static pods.
