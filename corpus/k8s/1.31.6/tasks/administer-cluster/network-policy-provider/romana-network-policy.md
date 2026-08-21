---
collection: k8s
version: "1.31.6"
title: "Romana for NetworkPolicy"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/administer-cluster/network-policy-provider/romana-network-policy.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

This page shows how to use Romana for NetworkPolicy.

## Before you begin

Complete steps 1, 2, and 3 of the [kubeadm getting started guide](/docs/reference/setup-tools/kubeadm/).

<!-- steps -->

## Installing Romana with kubeadm

Follow the [containerized installation guide](https://github.com/romana/romana/tree/master/containerize) for kubeadm.

## Applying network policies

To apply network policies use one of the following:

* [Romana network policies](https://github.com/romana/romana/wiki/Romana-policies).
    * [Example of Romana network policy](https://github.com/romana/core/blob/master/doc/policy.md).
* The NetworkPolicy API.

## What's next

Once you have installed Romana, you can follow the
[Declare Network Policy](/docs/tasks/administer-cluster/declare-network-policy/)
to try out Kubernetes NetworkPolicy.
