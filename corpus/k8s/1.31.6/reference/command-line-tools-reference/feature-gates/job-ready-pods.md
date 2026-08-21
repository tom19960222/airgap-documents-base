---
collection: k8s
version: "1.31.6"
title: "JobReadyPods"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/job-ready-pods.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables tracking the number of Pods that have a `Ready`
[condition](/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions).
The count of `Ready` pods is recorded in the
[status](/docs/reference/kubernetes-api/workload-resources/job-v1/#JobStatus)
of a [Job](/docs/concepts/workloads/controllers/job) status.
