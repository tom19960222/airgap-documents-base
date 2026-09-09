---
collection: rook
version: "1.20.7"
title: "Helm Charts Overview"
source_url: https://github.com/rook/rook/blob/95a8e2a8b61cf7f8152213939f995c88a2e72ab6/Documentation/Helm-Charts/helm-charts.md
fetched_at: 2026-09-02T11:15:12-06:00
---
The following charts are available to configure Ceph storage:

1. [Rook Ceph Operator](operator-chart.md): Starts the Ceph Operator, which will watch for Ceph CRs (custom resources). Also installs the Ceph-CSI operator as a Helm dependency.
1. [Ceph-CSI drivers chart](csi-drivers-chart.md): Installs the Ceph-CSI drivers to provision and mount volumes.
1. [Rook Ceph Cluster](ceph-cluster-chart.md): Creates Ceph CRs that the operator will use to configure the cluster.

The Helm charts are intended to simplify deployment and upgrades.
Configuring the Rook resources without Helm is also fully supported by creating the
[manifests](https://github.com/rook/rook/tree/95a8e2a8b61cf7f8152213939f995c88a2e72ab6/deploy/examples)
directly.
