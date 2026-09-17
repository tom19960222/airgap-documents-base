---
collection: ceph-csi-operator
version: "1.0.4"
title: "Helm Charts Overview"
source_url: https://github.com/ceph/ceph-csi-operator/blob/29a66b683aa8873001c729b7b120e18604cdb445/docs/helm-charts/helm-charts.md
fetched_at: 2026-07-07T13:06:31+05:30
---
Ceph-csi-operator has published the following Helm charts for the ceph-csi-operators:

* [ceph-csi Operator](operator-chart.md): Starts the ceph-csi Operator, which will watch for Ceph CRs (custom resources)
* [ceph-csi Drivers](drivers-chart.md): Creates `Drivers`,`Cephconnection`,`ClientProfile` and `ClientProfileMapping` CRs that the operator will use to configure the ceph-csi drivers

The Helm charts are intended to simplify deployment and upgrades.
