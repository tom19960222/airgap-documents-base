---
collection: k8s
version: "1.31.6"
title: "Scheduling Policies"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/scheduling/policies.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

In Kubernetes versions before v1.23, a scheduling policy can be used to specify the *predicates* and *priorities* process. For example, you can set a scheduling policy by
running `kube-scheduler --policy-config-file <filename>` or `kube-scheduler --policy-configmap <ConfigMap>`.

This scheduling policy is not supported since Kubernetes v1.23. Associated flags `policy-config-file`, `policy-configmap`, `policy-configmap-namespace` and `use-legacy-policy-config` are also not supported. Instead, use the [Scheduler Configuration](/docs/reference/scheduling/config/) to achieve similar behavior.

## What's next

* Learn about [scheduling](/docs/concepts/scheduling-eviction/kube-scheduler/)
* Learn about [kube-scheduler Configuration](/docs/reference/scheduling/config/)
* Read the [kube-scheduler configuration reference (v1)](/docs/reference/config-api/kube-scheduler-config.v1/)
