---
collection: k8s
version: "1.31.6"
title: "Object"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/object.md
fetched_at: 2026-01-16T10:18:07+05:30
---
An entity in the Kubernetes system. The Kubernetes API uses these entities to represent the state
of your cluster.
<!--more-->
A Kubernetes object is typically a “record of intent”—once you create the object, the Kubernetes
control plane works constantly to ensure
that the item it represents actually exists.
By creating an object, you're effectively telling the Kubernetes system what you want that part of
your cluster's workload to look like; this is your cluster's desired state.
