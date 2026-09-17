---
collection: csi-addons
version: "0.14.0"
title: "CSI-Addons Operator Configuration"
source_url: https://github.com/csi-addons/kubernetes-csi-addons/blob/621cfdc3b7d36922a8d328324643540eeac2671d/docs/csi-addons-config.md
fetched_at: 2026-01-12T14:50:51Z
---
# CSI-Addons Operator Configuration

CSI-Addons Operator can consume configuration from a ConfigMap named `csi-addons-config`
in the same namespace as the operator. This enables configuration of the operator to persist across
upgrades. The ConfigMap can support the following configuration options:

| Option                      | Default value | Description                                               |
| --------------------------- | ------------- | --------------------------------------------------------- |
| `reclaim-space-timeout`     | `"3m"`        | Timeout for reclaimspace operation                        |
| `max-concurrent-reconciles` | `"100"`       | Maximum number of concurrent reconciles                   |
| `max-group-pvcs`            | `"100"`       | Maximum number of PVCs allowed in a volume group          |
| `schedule-precedence`       | `"pvc"`       | The order in which the schedule annotation should be read |

[`csi-addons-config` ConfigMap](../deploy/controller/csi-addons-config.yaml) <!-- unresolved-source-link: target=../deploy/controller/csi-addons-config.yaml --> is provided as an example.

> Note: The operator pod needs to be restarted for any change in configuration to take effect.
>
> Note: `max-group-pvcs` default value is set based on ceph's support/testing. User can tweak this value based on the supported count for their storage vendor.
>
> Note: The valid values for `schedule-precedence` are `storageclass` and `pvc`. If set to `storageclass` only the annotations from StorageClasses are considered for schedule of reclaim space and key rotation. `pvc` reads annotations in the order of: PVC > NS > StorageClasses.
