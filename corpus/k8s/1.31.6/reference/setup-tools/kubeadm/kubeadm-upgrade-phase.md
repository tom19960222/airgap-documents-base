---
collection: k8s
version: "1.31.6"
title: "kubeadm upgrade phase"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/setup-tools/kubeadm/kubeadm-upgrade-phase.md
fetched_at: 2026-01-16T10:18:07+05:30
---
In v1.15.0, kubeadm introduced preliminary support for `kubeadm upgrade node` phases.
Phases for other `kubeadm upgrade` sub-commands such as `apply`, could be added in the
following releases.

## kubeadm upgrade node phase {#cmd-node-phase}

Using this phase you can choose to execute the separate steps of the upgrade of
secondary control-plane or worker nodes. Please note that `kubeadm upgrade apply` still has to
be called on a primary control-plane node.

**Tab: phase**

**Tab: preflight**

**Tab: control-plane**

**Tab: kubelet-config**

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to connect a node to the cluster
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`
* [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/) to upgrade a kubeadm node
* [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) to try experimental functionality
