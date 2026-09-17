---
collection: istio
version: "1.24"
title: "Tencent Cloud"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/tencent-cloud-mesh/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up Istio quickly in Tencent Cloud."
---
## Prerequisites

Follow these instructions to prepare a [Tencent Kubernetes Engine](https://intl.cloud.tencent.com/products/tke) or [Elastic Kubernetes Service](https://intl.cloud.tencent.com/product/eks) cluster for Istio.

You can deploy a Kubernetes cluster to Tencent Cloud via [Tencent Kubernetes Engine](https://intl.cloud.tencent.com/document/product/457/40029) or [Elastic Kubernetes Service](https://intl.cloud.tencent.com/document/product/457/34048) which fully supports Istio.

![Create Cluster](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/tencent-cloud-mesh/tke.png)

## Procedure

After creating a Tencent Kubernetes Engine or Elastic Kubernetes Service cluster, you can quickly start to deploy and use Istio by [Tencent Cloud Mesh](https://cloud.tencent.com/product/tcm):

![Create Tencent Cloud Mesh](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/tencent-cloud-mesh/tcm.png)

1. Log on to the `Container Service console`, and click **Service Mesh** in the left-side navigation pane to enter the **Service Mesh** page.

1. Click the **Create** button in the upper-left corner.

1. Enter the mesh name.

> **Tip:**
>
> The mesh name can be 1–60 characters long and it can contain numbers, Chinese characters, English letters, and hyphens (-).

1. Select the **Region** and **Zone** in which the cluster resides.

1. Choose the Istio version.

1. Choose the service mesh mode: `Managed Mesh` or `Stand-Alone Mesh`.

> **Tip:**
>
> Tencent Cloud Mesh supports **Stand-Alone Mesh** (Istiod is running in the user cluster and managed by users) and **Managed Mesh** (Istiod is managed by Tencent Cloud Mesh Team).

1. Configure the Egress traffic policy:  `Register Only` or `Allow Any` .

1. Choose the related **Tencent Kubernetes Engine** or **Elastic Kubernetes Service** cluster.

1. Choose to open sidecar injection in the selected namespaces.

1. Configure external requests to bypass the IP address block directly accessed by the sidecar, and external request traffic will not be able to use Istio traffic management, observability and other features.

1. Choose to open **SideCar Readiness Guarantee** or not. If it is open, app containers will be created after sidecar is running.

1. Configure the Ingress Gateway and Egress Gateway.

![Configure Observability](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/tencent-cloud-mesh/tps.png)

1. Configure the Observability of Metrics, Tracing and Logging.

> **Tip:**
>
> Besides the default Cloud Monitor services, You can choose to open the advanced external services like [Managed Service for Prometheus](https://intl.cloud.tencent.com/document/product/457/38824?has_map=1) and the [Cloud Log Service](https://intl.cloud.tencent.com/product/cls).

After finishing these steps, you can confirm to create Istio and start to use Istio in Tencent Cloud Mesh.
