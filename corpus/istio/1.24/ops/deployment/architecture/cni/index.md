---
collection: istio
version: "1.24"
title: "CNI plugin"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/deployment/architecture/cni/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes how Istio's CNI plugin works."
---
Kubernetes has a unique and permissive networking model. In order to configure L2-L4 networking between Pods, [a Kubernetes cluster requires an _interface_ Container Network Interface (CNI) plugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/). This plugin runs whenever a new pod is created, and sets up the network environment for that pod.

If you are using a hosted Kubernetes provider, you usually have limited choice in what CNI plugin you get in your cluster: it is an implementation detail of the hosted implementation.

In order to configure mesh traffic redirection, regardless of what CNI you or your provider choose to use for L2-L4 networking, Istio includes a _chained_ CNI plugin, which runs after all configured CNI interface plugins. The API for defining chained and interface plugins, and for sharing data between them, is part of the [CNI specification](https://www.cni.dev/). Istio works with all CNI implementations that follow the CNI standard, in both sidecar and ambient mode.

The Istio CNI plugin is optional in sidecar mode, and required in ambient mode.

* [Learn how to install Istio with a CNI plugin](../../../../setup/additional-setup/cni/index.md)
