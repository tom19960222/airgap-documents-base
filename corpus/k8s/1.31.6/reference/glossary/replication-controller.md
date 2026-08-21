---
collection: k8s
version: "1.31.6"
title: "ReplicationController"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/replication-controller.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A workload resource that manages a replicated application, ensuring that
a specific number of instances of a Pod are running.

<!--more-->

The control plane ensures that the defined number of Pods are running, even if some
Pods fail, if you delete Pods manually, or if too many are started by mistake.

> **Note:**
>
> ReplicationController is deprecated. See
> Deployment, which is similar.
