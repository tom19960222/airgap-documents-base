---
collection: k8s
version: "1.31.6"
title: "kubeadm join phase"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/setup-tools/kubeadm/kubeadm-join-phase.md
fetched_at: 2026-01-16T10:18:07+05:30
---
`kubeadm join phase` enables you to invoke atomic steps of the join process.
Hence, you can let kubeadm do some of the work and you can fill in the gaps
if you wish to apply customization.

`kubeadm join phase` is consistent with the [kubeadm join workflow](/docs/reference/setup-tools/kubeadm/kubeadm-join/#join-workflow),
and behind the scene both use the same code.

## kubeadm join phase {#cmd-join-phase}

**Tab: phase**

## kubeadm join phase preflight {#cmd-join-phase-preflight}

Using this phase you can execute preflight checks on a joining node.

**Tab: preflight**

## kubeadm join phase control-plane-prepare {#cmd-join-phase-control-plane-prepare}

Using this phase you can prepare a node for serving a control-plane.

**Tab: control-plane-prepare**

**Tab: all**

**Tab: download-certs**

**Tab: certs**

**Tab: kubeconfig**

**Tab: control-plane**

## kubeadm join phase kubelet-start {#cmd-join-phase-kubelet-start}

Using this phase you can write the kubelet settings, certificates and (re)start the kubelet.

**Tab: kubelet-start**

## kubeadm join phase control-plane-join {#cmd-join-phase-control-plane-join}

Using this phase you can join a node as a control-plane instance.

**Tab: control-plane-join**

**Tab: all**

**Tab: etcd**

**Tab: mark-control-plane**

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to connect a node to the cluster
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`
* [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) to try experimental functionality
