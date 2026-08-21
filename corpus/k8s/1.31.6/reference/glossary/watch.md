---
collection: k8s
version: "1.31.6"
title: "Watch"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/watch.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A verb that is used to track changes to an object in Kubernetes as a stream.
It is used for the efficient detection of changes.

<!--more-->

A verb that is used to track changes to an object in Kubernetes as a stream. Watches allow
efficient detection of changes; for example, a
controller that needs to know whenever a
ConfigMap has changed can use a watch rather than polling.

See [Efficient Detection of Changes in API Concepts](/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) for more information.
