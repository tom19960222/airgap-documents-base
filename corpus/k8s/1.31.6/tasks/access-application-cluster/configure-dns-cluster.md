---
collection: k8s
version: "1.31.6"
title: "Configure DNS for a Cluster"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/access-application-cluster/configure-dns-cluster.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->
Kubernetes offers a DNS cluster addon, which most of the supported environments enable by default. In Kubernetes version 1.11 and later, CoreDNS is recommended and is installed by default with kubeadm.

<!-- body -->
For more information on how to configure CoreDNS for a Kubernetes cluster, see the [Customizing DNS Service](/docs/tasks/administer-cluster/dns-custom-nameservers/). An example demonstrating how to use Kubernetes DNS with kube-dns, see the [Kubernetes DNS sample plugin](https://github.com/kubernetes/examples/tree/master/staging/cluster-dns).
