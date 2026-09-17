---
collection: istio
version: "1.24"
title: "Install Multicluster"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/multicluster/_index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Install an Istio mesh across multiple Kubernetes clusters."
---
Follow this guide to install an Istio service mesh
that spans multiple clusters.

This guide covers some of the most common concerns when creating a
multicluster mesh:

- [Network topologies](../../../ops/deployment/deployment-models/index.md#network-models):
  one or two networks

- [Control plane topologies](../../../ops/deployment/deployment-models/index.md#control-plane-models):
  multiple primary clusters,
  a primary and remote cluster

> **Tip:**
>
> For meshes that span more than two clusters, you can extend the steps in this
> guide to configure more complex topologies.
>
> See [deployment models](../../../ops/deployment/deployment-models/index.md) for more
> information.
