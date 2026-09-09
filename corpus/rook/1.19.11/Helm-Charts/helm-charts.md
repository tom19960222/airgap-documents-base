---
collection: rook
version: "1.19.11"
title: "Helm Charts Overview"
source_url: https://github.com/rook/rook/blob/e6818be5fcdcc4e3752f1cb03a7c0fbcc12dbdf1/Documentation/Helm-Charts/helm-charts.md
fetched_at: 2026-09-02T10:46:10-06:00
---
Rook has published the following Helm charts for the Ceph storage provider:

* [Rook Ceph Operator](operator-chart.md): Starts the Ceph Operator, which will watch for Ceph CRs (custom resources)
* [Rook Ceph Cluster](ceph-cluster-chart.md): Creates Ceph CRs that the operator will use to configure the cluster

The Helm charts are intended to simplify deployment and upgrades.
Configuring the Rook resources without Helm is also fully supported by creating the
[manifests](https://github.com/rook/rook/tree/e6818be5fcdcc4e3752f1cb03a7c0fbcc12dbdf1/deploy/examples)
directly.
