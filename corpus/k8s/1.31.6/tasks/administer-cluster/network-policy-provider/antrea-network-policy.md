---
collection: k8s
version: "1.31.6"
title: "Use Antrea for NetworkPolicy"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/administer-cluster/network-policy-provider/antrea-network-policy.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->
This page shows how to install and use Antrea CNI plugin on Kubernetes.
For background on Project Antrea, read the [Introduction to Antrea](https://antrea.io/docs/).

## Before you begin

You need to have a Kubernetes cluster. Follow the
[kubeadm getting started guide](/docs/reference/setup-tools/kubeadm/) to bootstrap one.

<!-- steps -->

## Deploying Antrea with kubeadm

Follow [Getting Started](https://github.com/vmware-tanzu/antrea/blob/main/docs/getting-started.md) guide to deploy Antrea for kubeadm.

## What's next

Once your cluster is running, you can follow the [Declare Network Policy](/docs/tasks/administer-cluster/declare-network-policy/) to try out Kubernetes NetworkPolicy.
