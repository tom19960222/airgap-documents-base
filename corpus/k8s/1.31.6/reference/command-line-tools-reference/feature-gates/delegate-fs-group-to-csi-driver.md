---
collection: k8s
version: "1.31.6"
title: "DelegateFSGroupToCSIDriver"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/delegate-fs-group-to-csi-driver.md
fetched_at: 2026-01-16T10:18:07+05:30
---
If supported by the CSI driver, delegates the
role of applying `fsGroup` from a Pod's `securityContext` to the driver by
passing `fsGroup` through the NodeStageVolume and NodePublishVolume CSI calls.
