---
collection: istio
version: "1.24"
title: "Before you begin"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/multicluster/before-you-begin/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Initial steps before installing Istio on multiple clusters."
---
Before you begin a multicluster installation, review the
[deployment models guide](../../../../ops/deployment/deployment-models/index.md)
which describes the foundational concepts used throughout this guide.

In addition, review the requirements and perform the initial steps below.

## Requirements

### Cluster

This guide requires that you have two Kubernetes clusters with any of the
[supported Kubernetes versions:](../../../../releases/supported-releases/index.md#support-status-of-istio-releases) [supported_kubernetes_versions].

### API Server Access

The API Server in each cluster must be accessible to the other clusters in the
mesh. Many cloud providers make API Servers publicly accessible via network
load balancers (NLB). If the API Server is not directly accessible, you will
have to modify the installation procedure to enable access. For example, the
[east-west](https://en.wikipedia.org/wiki/East-west_traffic) gateway used in
the multi-network and primary-remote configurations could also be used
to enable access to the API Server.

## Environment Variables

This guide will refer to two clusters: `cluster1` and `cluster2`. The following
environment variables will be used throughout to simplify the instructions:

Variable | Description
-------- | -----------
`CTX_CLUSTER1` | The context name in the default [Kubernetes configuration file](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) used for accessing the `cluster1` cluster.
`CTX_CLUSTER2` | The context name in the default [Kubernetes configuration file](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) used for accessing the `cluster2` cluster.

Set the two variables before proceeding:

```bash
$ export CTX_CLUSTER1=<your cluster1 context>
$ export CTX_CLUSTER2=<your cluster2 context>
```

## Configure Trust

A multicluster service mesh deployment requires that you establish trust
between all clusters in the mesh. Depending on the requirements for your
system, there may be multiple options available for establishing trust.
See [certificate management](../../../../tasks/security/cert-management/_index.md) for
detailed descriptions and instructions for all available options.
Depending on which option you choose, the installation instructions for
Istio may change slightly.

> **Tip:**
>
> If you are planning to deploy only one primary cluster (i.e., one of the
> Primary-Remote installations, below), you will only have a single CA
> (i.e., `istiod` on `cluster1`) issuing certificates for both clusters.
> In that case, you can skip the following CA certificate generation step
> and simply use the default self-signed CA for the installation.

This guide will assume that you use a common root to generate intermediate
certificates for each primary cluster.
Follow the [instructions](../../../../tasks/security/cert-management/plugin-ca-cert/index.md)
to generate and push a CA certificate secret to both the `cluster1` and `cluster2`
clusters.

> **Tip:**
>
> If you currently have a single cluster with a self-signed CA (as described
> in [Getting Started](../../../getting-started/index.md)), you need to
> change the CA using one of the methods described in
> [certificate management](../../../../tasks/security/cert-management/_index.md). Changing the
> CA typically requires reinstalling Istio. The installation instructions
> below may have to be altered based on your choice of CA.

## Next steps

You're now ready to install an Istio mesh across multiple clusters. The
particular steps will depend on your requirements for network and
control plane topology.

Choose the installation that best fits your needs:

- [Install Multi-Primary](../multi-primary/index.md)

- [Install Primary-Remote](../primary-remote/index.md)

- [Install Multi-Primary on Different Networks](../multi-primary_multi-network/index.md)

- [Install Primary-Remote on Different Networks](../primary-remote_multi-network/index.md)

> **Tip:**
>
> If you plan on installing Istio multi-cluster using Helm, follow the
> [Helm prerequisites](../../helm/index.md#prerequisites) in the Helm install guide first.

> **Tip:**
>
> For meshes that span more than two clusters, you may need to use more than
> one of these options. For example, you may have a primary cluster per region
> (i.e. multi-primary) where each zone has a remote cluster that uses the
> control plane in the regional primary (i.e. primary-remote).
>
> See [deployment models](../../../../ops/deployment/deployment-models/index.md) for more
> information.
