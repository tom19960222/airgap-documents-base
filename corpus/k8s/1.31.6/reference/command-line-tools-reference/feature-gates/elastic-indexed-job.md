---
collection: k8s
version: "1.31.6"
title: "ElasticIndexedJob"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/elastic-indexed-job.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables Indexed Jobs to be scaled up or down by mutating both
`spec.completions` and `spec.parallelism` together such that `spec.completions == spec.parallelism`.
See docs on [elastic Indexed Jobs](/docs/concepts/workloads/controllers/job#elastic-indexed-jobs)
for more details.
