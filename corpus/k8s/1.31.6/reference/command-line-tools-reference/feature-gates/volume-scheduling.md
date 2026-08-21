---
collection: k8s
version: "1.31.6"
title: "VolumeScheduling"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/volume-scheduling.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable volume topology aware scheduling and make the PersistentVolumeClaim
(PVC) binding aware of scheduling decisions. It also enables the usage of
[`local`](/docs/concepts/storage/volumes/#local) volume type when used together with the
`PersistentLocalVolumes` feature gate.
