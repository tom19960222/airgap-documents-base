---
collection: k8s
version: "1.31.6"
title: "PriorityClass"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/priority-class.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A PriorityClass is a named class for the scheduling priority that should be assigned to a Pod
in that class.

<!--more-->

A [PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption)
is a non-namespaced object mapping a name to an integer priority, used for a Pod. The name is
specified in the `metadata.name` field, and the priority value in the `value` field. Priorities range from
-2147483648 to 1000000000 inclusive. Higher values indicate higher priority.
