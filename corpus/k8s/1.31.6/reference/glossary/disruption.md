---
collection: k8s
version: "1.31.6"
title: "Disruption"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/disruption.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Disruptions are events that lead to one or more
Pods going out of service.
A disruption has consequences for workload resources, such as
deployment, that rely on the affected
Pods.

<!--more-->

If you, as cluster operator, destroy a Pod that belongs to an application,
Kubernetes terms that a _voluntary disruption_. If a Pod goes offline
because of a Node failure, or an outage affecting a wider failure zone,
Kubernetes terms that an _involuntary disruption_.

See [Disruptions](/docs/concepts/workloads/pods/disruptions/) for more information.
