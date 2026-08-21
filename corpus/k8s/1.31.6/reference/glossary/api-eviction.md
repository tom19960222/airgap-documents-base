---
collection: k8s
version: "1.31.6"
title: "API-initiated eviction"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/api-eviction.md
fetched_at: 2026-01-16T10:18:07+05:30
---
API-initiated eviction is the process by which you use the [Eviction API](/docs/reference/generated/kubernetes-api/version/#create-eviction-pod-v1-core)
to create an `Eviction` object that triggers graceful pod termination.

<!--more-->

You can request eviction either by directly calling the Eviction API 
using a client of the kube-apiserver, like the `kubectl drain` command. 
When an `Eviction` object is created, the API server terminates the Pod. 

API-initiated evictions respect your configured [`PodDisruptionBudgets`](/docs/tasks/run-application/configure-pdb/)
and [`terminationGracePeriodSeconds`](/docs/concepts/workloads/pods/pod-lifecycle#pod-termination).

API-initiated eviction is not the same as [node-pressure eviction](/docs/concepts/scheduling-eviction/node-pressure-eviction/).

* See [API-initiated eviction](/docs/concepts/scheduling-eviction/api-eviction/) for more information.
