---
collection: kube-state-metrics
version: "2.12.0"
title: "StorageClass Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/storageclass-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# StorageClass Metrics

| Metric name                   | Metric type | Description                                                                                                               | Labels/tags                                                                                                                                                                                                             | Status       |
| ----------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_storageclass_annotations | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `storageclass`=&lt;storageclass-name&gt; <br> `annotation_STORAGECLASS_ANNOTATION`=&lt;STORAGECLASS_ANNOTATION&gt;                                                                                                      | EXPERIMENTAL |
| kube_storageclass_info        | Gauge       |                                                                                                                           | `storageclass`=&lt;storageclass-name&gt; <br> `provisioner`=&lt;storageclass-provisioner&gt; <br> `reclaim_policy`=&lt;storageclass-reclaimPolicy&gt; <br> `volume_binding_mode`=&lt;storageclass-volumeBindingMode&gt; | STABLE       |
| kube_storageclass_labels      | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `storageclass`=&lt;storageclass-name&gt; <br> `label_STORAGECLASS_LABEL`=&lt;STORAGECLASS_LABEL&gt;                                                                                                                     | STABLE       |
| kube_storageclass_created     | Gauge       |                                                                                                                           | `storageclass`=&lt;storageclass-name&gt;                                                                                                                                                                                | STABLE       |
