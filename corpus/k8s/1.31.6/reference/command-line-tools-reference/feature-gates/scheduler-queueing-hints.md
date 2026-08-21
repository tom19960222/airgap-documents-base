---
collection: k8s
version: "1.31.6"
title: "SchedulerQueueingHints"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/scheduler-queueing-hints.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables [the scheduler's _queueing hints_ enhancement](https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/4247-queueinghint/README.md),
which benefits to reduce the useless requeueing.
The scheduler retries scheduling pods if something changes in the cluster that could make the pod scheduled.
Queueing hints are internal signals that allow the scheduler to filter the changes in the cluster
that are relevant to the unscheduled pod, based on previous scheduling attempts.
