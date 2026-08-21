---
collection: k8s
version: "1.31.6"
title: "JobTrackingWithFinalizers"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/job-tracking-with-finalizers.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables tracking [Job](/docs/concepts/workloads/controllers/job)
completions without relying on Pods remaining in the cluster indefinitely.
The Job controller uses Pod finalizers and a field in the Job status to keep
track of the finished Pods to count towards completion.
