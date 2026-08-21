---
collection: k8s
version: "1.31.6"
title: "Node Labels Populated By The Kubelet"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/node/node-labels.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Kubernetes nodes come pre-populated
with a standard set of labels.

You can also set your own labels on nodes, either through the kubelet configuration or
using the Kubernetes API.

## Preset labels

The preset labels that Kubernetes sets on nodes are:

* [`kubernetes.io/arch`](/docs/reference/labels-annotations-taints/#kubernetes-io-arch)
* [`kubernetes.io/hostname`](/docs/reference/labels-annotations-taints/#kubernetes-io-hostname)
* [`kubernetes.io/os`](/docs/reference/labels-annotations-taints/#kubernetes-io-os)
* [`node.kubernetes.io/instance-type`](/docs/reference/labels-annotations-taints/#nodekubernetesioinstance-type)
  (if known to the kubelet &ndash; Kubernetes may not have this information to set the label)
* [`topology.kubernetes.io/region`](/docs/reference/labels-annotations-taints/#topologykubernetesioregion)
  (if known to the kubelet &ndash; Kubernetes may not have this information to set the label)
* [`topology.kubernetes.io/zone`](/docs/reference/labels-annotations-taints/#topologykubernetesiozone)
  (if known to the kubelet &ndash; Kubernetes may not have this information to set the label)

> **Note:**
>
> The value of these labels is cloud provider specific and is not guaranteed to be reliable.
> For example, the value of `kubernetes.io/hostname` may be the same as the node name in some environments
> and a different value in other environments.

## What's next

- See [Well-Known Labels, Annotations and Taints](/docs/reference/labels-annotations-taints/) for a list of common labels.
- Learn how to [add a label to a node](/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node).
