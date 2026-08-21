---
collection: k8s
version: "1.31.6"
title: "Preemption"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/preemption.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Preemption logic in Kubernetes helps a pending pod to find a suitable node by evicting low priority Pods existing on that Node.

<!--more-->

If a Pod cannot be scheduled, the scheduler tries to [preempt](/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption) lower priority Pods to make scheduling of the pending Pod possible.
