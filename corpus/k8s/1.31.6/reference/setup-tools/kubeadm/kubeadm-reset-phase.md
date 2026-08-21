---
collection: k8s
version: "1.31.6"
title: "kubeadm reset phase"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/setup-tools/kubeadm/kubeadm-reset-phase.md
fetched_at: 2026-01-16T10:18:07+05:30
---
`kubeadm reset phase` enables you to invoke atomic steps of the node reset process.
Hence, you can let kubeadm do some of the work and you can fill in the gaps
if you wish to apply customization.

`kubeadm reset phase` is consistent with the [kubeadm reset workflow](/docs/reference/setup-tools/kubeadm/kubeadm-reset/#reset-workflow),
and behind the scene both use the same code.

## kubeadm reset phase {#cmd-reset-phase}

**Tab: phase**

## kubeadm reset phase preflight {#cmd-reset-phase-preflight}

Using this phase you can execute preflight checks on a node that is being reset.

**Tab: preflight**

## kubeadm reset phase remove-etcd-member {#cmd-reset-phase-remove-etcd-member}

Using this phase you can remove this control-plane node's etcd member from the etcd cluster.

**Tab: remove-etcd-member**

## kubeadm reset phase cleanup-node {#cmd-reset-phase-cleanup-node}

Using this phase you can perform cleanup on this node.

**Tab: cleanup-node**

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to connect a node to the cluster
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`
* [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) to try experimental functionality
