---
collection: istio
version: "1.24"
title: "Monitoring Multicluster Istio with Prometheus"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/configuration/telemetry/monitoring-multicluster-prometheus/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Configure Prometheus to monitor multicluster Istio."
---
## Overview

This guide is meant to provide operational guidance on how to configure monitoring of Istio meshes comprised of two
or more individual Kubernetes clusters. It is not meant to establish the *only* possible path forward, but rather
to demonstrate a workable approach to multicluster telemetry with Prometheus.

Our recommendation for multicluster monitoring of Istio with Prometheus is built upon the foundation of Prometheus
[hierarchical federation](https://prometheus.io/docs/prometheus/latest/federation/#hierarchical-federation).
Prometheus instances that are deployed locally to each cluster by Istio act as initial collectors that then federate up
to a production mesh-wide Prometheus instance. That mesh-wide Prometheus can either live outside of the mesh (external), or in one
of the clusters within the mesh.

## Multicluster Istio setup

Follow the [multicluster installation](../../../../setup/install/multicluster/_index.md) section to set up your Istio clusters in one of the
supported [multicluster deployment models](../../../deployment/deployment-models/index.md#multiple-clusters). For the purpose of
this guide, any of those approaches will work, with the following caveat:

**Ensure that a cluster-local Istio Prometheus instance is installed in each cluster.**

Individual Istio deployment of Prometheus in each cluster is required to form the basis of cross-cluster monitoring by
way of federation to a production-ready instance of Prometheus that runs externally or in one of the clusters.

Validate that you have an instance of Prometheus running in each cluster:

```bash
$ kubectl -n istio-system get services prometheus
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
prometheus   ClusterIP   10.8.4.109   <none>        9090/TCP   20h
```

## Configure Prometheus federation

### External production Prometheus

There are several reasons why you may want to have a Prometheus instance running outside of your Istio deployment.
Perhaps you want long-term monitoring disjoint from the cluster being monitored. Perhaps you want to monitor multiple
separate meshes in a single place. Or maybe you have other motivations. Whatever your reason is, you’ll need some special
configurations to make it all work.

![External Production Prometheus for monitoring multicluster Istio](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/configuration/telemetry/monitoring-multicluster-prometheus/external-production-prometheus.svg)

> **Warning:**
>
> This guide demonstrates connectivity to cluster-local Prometheus instances, but does not address security considerations.
> For production use, secure access to each Prometheus endpoint with HTTPS. In addition, take precautions, such as using an
> internal load-balancer instead of a public endpoint and the appropriate configuration of firewall rules.

Istio provides a way to expose cluster services externally via [Gateways](https://istio.io/v1.24/docs/reference/config/networking/gateway/) <!-- unresolved-site-link: route=/docs/reference/config/networking/gateway -->.
You can configure an ingress gateway for the cluster-local Prometheus, providing external connectivity to the in-cluster
Prometheus endpoint.

For each cluster, follow the appropriate instructions from the [Remotely Accessing Telemetry Addons](../../../../tasks/observability/gateways/index.md#option-1-secure-access-https) task.
Also note that you **SHOULD** establish secure (HTTPS) access.

Next, configure your external Prometheus instance to access the cluster-local Prometheus instances using a configuration
like the following (replacing the ingress domain and cluster name):

```yaml
scrape_configs:
- job_name: 'federate-{{CLUSTER_NAME}}'
  scrape_interval: 15s

  honor_labels: true
  metrics_path: '/federate'

  params:
    'match[]':
      - '{job="kubernetes-pods"}'

  static_configs:
    - targets:
      - 'prometheus.{{INGRESS_DOMAIN}}'
      labels:
        cluster: '{{CLUSTER_NAME}}'
```

Notes:

* `CLUSTER_NAME` should be set to the same value that you used to create the cluster (set via `values.global.multiCluster.clusterName`).

* No authentication to the Prometheus endpoint(s) is provided. This means that anyone can query your
cluster-local Prometheus instances. This may not be desirable.

* Without proper HTTPS configuration of the gateway, everything is being transported via plaintext. This may not be
desirable.

### Production Prometheus on an in-mesh cluster

If you prefer to run the production Prometheus in one of the clusters, you need to establish connectivity from it to
the other cluster-local Prometheus instances in the mesh.

This is really just a variation of the configuration for external federation. In this case the configuration on the
cluster running the production Prometheus is different from the configuration for remote cluster Prometheus scraping.

![In-mesh Production Prometheus for monitoring multicluster Istio](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/configuration/telemetry/monitoring-multicluster-prometheus/in-mesh-production-prometheus.svg)

Configure your production Prometheus to access both of the *local* and *remote* Prometheus instances.

First execute the following command:

```bash
$ kubectl -n istio-system edit cm prometheus -o yaml
```

Then add configurations for the *remote* clusters (replacing the ingress domain and cluster name for each cluster) and
add one configuration for the *local* cluster:

```yaml
scrape_configs:
- job_name: 'federate-{{REMOTE_CLUSTER_NAME}}'
  scrape_interval: 15s

  honor_labels: true
  metrics_path: '/federate'

  params:
    'match[]':
      - '{job="kubernetes-pods"}'

  static_configs:
    - targets:
      - 'prometheus.{{REMOTE_INGRESS_DOMAIN}}'
      labels:
        cluster: '{{REMOTE_CLUSTER_NAME}}'

- job_name: 'federate-local'

  honor_labels: true
  metrics_path: '/federate'

  metric_relabel_configs:
  - replacement: '{{CLUSTER_NAME}}'
    target_label: cluster

  kubernetes_sd_configs:
  - role: pod
    namespaces:
      names: ['istio-system']
  params:
    'match[]':
    - '{__name__=~"istio_(.*)"}'
    - '{__name__=~"pilot(.*)"}'
```
