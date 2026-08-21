---
collection: k8s
version: "1.31.6"
title: "Using CoreDNS for Service Discovery"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/administer-cluster/coredns.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->
This page describes the CoreDNS upgrade process and how to install CoreDNS instead of kube-dns.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)
 

<!-- steps -->

## About CoreDNS

[CoreDNS](https://coredns.io) is a flexible, extensible DNS server
that can serve as the Kubernetes cluster DNS.
Like Kubernetes, the CoreDNS project is hosted by the
CNCF.

You can use CoreDNS instead of kube-dns in your cluster by replacing
kube-dns in an existing deployment, or by using tools like kubeadm
that will deploy and upgrade the cluster for you.

## Installing CoreDNS

For manual deployment or replacement of kube-dns, see the documentation at the
[CoreDNS website](https://coredns.io/manual/installation/).

## Migrating to CoreDNS

### Upgrading an existing cluster with kubeadm

In Kubernetes version 1.21, kubeadm removed its support for `kube-dns` as a DNS application.
For `kubeadm` v1.31, the only supported cluster DNS application
is CoreDNS.

You can move to CoreDNS when you use `kubeadm` to upgrade a cluster that is
using `kube-dns`. In this case, `kubeadm` generates the CoreDNS configuration
("Corefile") based upon the `kube-dns` ConfigMap, preserving configurations for
stub domains, and upstream name server.

## Upgrading CoreDNS

You can check the version of CoreDNS that kubeadm installs for each version of
Kubernetes in the page
[CoreDNS version in Kubernetes](https://github.com/coredns/deployment/blob/master/kubernetes/CoreDNS-k8s_version.md).

CoreDNS can be upgraded manually in case you want to only upgrade CoreDNS
or use your own custom image.
There is a helpful [guideline and walkthrough](https://github.com/coredns/deployment/blob/master/kubernetes/Upgrading_CoreDNS.md)
available to ensure a smooth upgrade.
Make sure the existing CoreDNS configuration ("Corefile") is retained when
upgrading your cluster.

If you are upgrading your cluster using the `kubeadm` tool, `kubeadm`
can take care of retaining the existing CoreDNS configuration automatically.

## Tuning CoreDNS

When resource utilisation is a concern, it may be useful to tune the
configuration of CoreDNS. For more details, check out the
[documentation on scaling CoreDNS](https://github.com/coredns/deployment/blob/master/kubernetes/Scaling_CoreDNS.md).

## What's next

You can configure [CoreDNS](https://coredns.io) to support many more use cases than
kube-dns does by modifying the CoreDNS configuration ("Corefile").
For more information, see the [documentation](https://coredns.io/plugins/kubernetes/)
for the `kubernetes` CoreDNS plugin, or read the 
[Custom DNS Entries for Kubernetes](https://coredns.io/2017/05/08/custom-dns-entries-for-kubernetes/).
in the CoreDNS blog.
