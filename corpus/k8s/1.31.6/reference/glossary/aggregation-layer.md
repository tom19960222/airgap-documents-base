---
collection: k8s
version: "1.31.6"
title: "Aggregation Layer"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/aggregation-layer.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The aggregation layer lets you install additional Kubernetes-style APIs in your cluster.

<!--more-->

When you've configured the Kubernetes API Server to [support additional APIs](/docs/tasks/extend-kubernetes/configure-aggregation-layer/), you can add `APIService` objects to "claim" a URL path in the Kubernetes API.
