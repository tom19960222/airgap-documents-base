---
collection: k8s
version: "1.31.6"
title: "ResourceLimitsPriorityFunction"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/resource-limits-priority-function.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable a scheduler priority function that
assigns a lowest possible score of 1 to a node that satisfies at least one of
the input Pod's cpu and memory limits. The intent is to break ties between
nodes with same scores.
