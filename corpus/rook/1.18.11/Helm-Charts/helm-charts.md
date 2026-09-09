---
collection: rook
version: "1.18.11"
title: "Helm Charts Overview"
source_url: https://github.com/rook/rook/blob/8059413c805f8ed3a0992af0113c002b0250805e/Documentation/Helm-Charts/helm-charts.md
fetched_at: 2026-05-27T11:20:14-06:00
---
Rook has published the following Helm charts for the Ceph storage provider:

* [Rook Ceph Operator](operator-chart.md): Starts the Ceph Operator, which will watch for Ceph CRs (custom resources)
* [Rook Ceph Cluster](ceph-cluster-chart.md): Creates Ceph CRs that the operator will use to configure the cluster

The Helm charts are intended to simplify deployment and upgrades.
Configuring the Rook resources without Helm is also fully supported by creating the
[manifests](https://github.com/rook/rook/tree/8059413c805f8ed3a0992af0113c002b0250805e/deploy/examples)
directly.
