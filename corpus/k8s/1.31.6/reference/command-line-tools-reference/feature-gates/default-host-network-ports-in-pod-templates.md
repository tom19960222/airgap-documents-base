---
collection: k8s
version: "1.31.6"
title: "DefaultHostNetworkHostPortsInPodTemplates"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/default-host-network-ports-in-pod-templates.md
fetched_at: 2026-01-16T10:18:07+05:30
---
This feature gate controls the point at which a default value for
`.spec.containers[*].ports[*].hostPort`
is assigned, for Pods using `hostNetwork: true`. The default since Kubernetes v1.28 is to only set a default
value in Pods.

Enabling this means a default will be assigned even to the `.spec` of an embedded
[PodTemplate](/docs/concepts/workloads/pods/#pod-templates) (for example, in a Deployment),
which is the way that older releases of Kubernetes worked.
You should migrate your code so that it does not rely on the legacy behavior.
