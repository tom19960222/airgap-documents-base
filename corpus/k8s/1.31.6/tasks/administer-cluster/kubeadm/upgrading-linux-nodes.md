---
collection: k8s
version: "1.31.6"
title: "Upgrading Linux nodes"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

This page explains how to upgrade a Linux Worker Nodes created with kubeadm.

## Before you begin

You need to have shell access to all the nodes, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial 
on a cluster with at least two nodes that are not acting as control plane hosts.
 
* Familiarize yourself with [the process for upgrading the rest of your kubeadm
cluster](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade). You will want to
upgrade the control plane nodes before upgrading your Linux Worker nodes.

<!-- steps -->

## Changing the package repository

If you're using the community-owned package repositories (`pkgs.k8s.io`), you need to 
enable the package repository for the desired Kubernetes minor release. This is explained in
[Changing the Kubernetes package repository](/docs/tasks/administer-cluster/kubeadm/change-package-repository/)
document.

> **Warning:** The legacy package repositories (apt.kubernetes.io and yum.kubernetes.io) are deprecated and frozen.

## Upgrading worker nodes

### Upgrade kubeadm

Upgrade kubeadm:

**Tab: Ubuntu, Debian or HypriotOS**

```shell
# replace x in 1.31.x-* with the latest patch version
sudo apt-mark unhold kubeadm && \
sudo apt-get update && sudo apt-get install -y kubeadm='1.31.x-*' && \
sudo apt-mark hold kubeadm
```

**Tab: CentOS, RHEL or Fedora**

```shell
# replace x in 1.31.x-* with the latest patch version
sudo yum install -y kubeadm-'1.31.x-*' --disableexcludes=kubernetes
```

### Call "kubeadm upgrade"

For worker nodes this upgrades the local kubelet configuration:

```shell
sudo kubeadm upgrade node
```

### Drain the node

Prepare the node for maintenance by marking it unschedulable and evicting the workloads:

```shell
# execute this command on a control plane node
# replace <node-to-drain> with the name of your node you are draining
kubectl drain <node-to-drain> --ignore-daemonsets
```

### Upgrade kubelet and kubectl

1. Upgrade the kubelet and kubectl:

   
   

**Tab: Ubuntu, Debian or HypriotOS**

   ```shell
   # replace x in 1.31.x-* with the latest patch version
   sudo apt-mark unhold kubelet kubectl && \
   sudo apt-get update && sudo apt-get install -y kubelet='1.31.x-*' kubectl='1.31.x-*' && \
   sudo apt-mark hold kubelet kubectl
   ```
   
   

**Tab: CentOS, RHEL or Fedora**

   ```shell
   # replace x in 1.31.x-* with the latest patch version
   sudo yum install -y kubelet-'1.31.x-*' kubectl-'1.31.x-*' --disableexcludes=kubernetes
   ```
   
   

1. Restart the kubelet:

   ```shell
   sudo systemctl daemon-reload
   sudo systemctl restart kubelet
   ```

### Uncordon the node

Bring the node back online by marking it schedulable:

```shell
# execute this command on a control plane node
# replace <node-to-uncordon> with the name of your node
kubectl uncordon <node-to-uncordon>
```

## What's next

* See how to [Upgrade Windows nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/).
