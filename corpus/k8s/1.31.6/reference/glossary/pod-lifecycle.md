---
collection: k8s
version: "1.31.6"
title: "Pod Lifecycle"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/pod-lifecycle.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The sequence of states through which a Pod passes during its lifetime.

<!--more--> 

The [Pod Lifecycle](/docs/concepts/workloads/pods/pod-lifecycle/) is defined by the states or phases of a Pod. There are five possible Pod phases: Pending, Running, Succeeded, Failed, and Unknown. A high-level description of the Pod state is summarized in the [PodStatus](/docs/reference/generated/kubernetes-api/version/#podstatus-v1-core) `phase` field.
