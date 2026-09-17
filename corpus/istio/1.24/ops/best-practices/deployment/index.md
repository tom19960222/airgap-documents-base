---
collection: istio
version: "1.24"
title: "Deployment Best Practices"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/best-practices/deployment/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "General best practices when setting up an Istio service mesh."
---
We have identified the following general principles to help you get the most
out of your Istio deployments. These best practices aim to limit the impact of
bad configuration changes and make managing your deployments easier.

## Deploy fewer clusters

Deploy Istio across a small number of large clusters, rather than a large number
of small clusters. Instead of adding clusters to your deployment, the best
practice is to use [namespace tenancy](../../deployment/deployment-models/index.md#namespace-tenancy)
to manage large clusters. Following this approach, you can deploy Istio across
one or two clusters per zone or region. You can then deploy a control plane on
one cluster per region or zone for added reliability.

## Deploy clusters near your users

Include clusters in your deployment across the globe for **geographic
proximity to end-users**. Proximity helps your deployment have low latency.

## Deploy across multiple availability zones

Include clusters in your deployment **across multiple availability regions
and zones** within each geographic region. This approach limits the size of the
failure domains of your deployment,
and helps you avoid global failures.
