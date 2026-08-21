---
collection: rook
version: "1.17.2"
title: "Helm Charts Overview"
source_url: https://rook.io/docs/rook/v1.17/Helm-Charts/helm-charts/
fetched_at: 2026-08-21T02:33:51+00:00
---
# Helm Charts Overview

Rook has published the following Helm charts for the Ceph storage provider:

- [Rook Ceph Operator](../operator-chart/index.md): Starts the Ceph Operator, which will watch for Ceph CRs (custom resources)
- [Rook Ceph Cluster](../ceph-cluster-chart/index.md): Creates Ceph CRs that the operator will use to configure the cluster

The Helm charts are intended to simplify deployment and upgrades. Configuring the Rook resources without Helm is also fully supported by creating the [manifests](https://github.com/rook/rook/tree/release-1.17/deploy/examples) directly.
