---
collection: kube-state-metrics
version: "2.12.0"
title: "VolumeAttachment Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/volumeattachment-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# VolumeAttachment Metrics

| Metric name                                        | Metric type | Description                                                                                                     | Labels/tags                                                                                                          | Status       |
| -------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_volumeattachment_info                         | Gauge       |                                                                                                                 | `volumeattachment`=&lt;volumeattachment-name&gt; <br> `attacher`=&lt;attacher-name&gt; <br> `node`=&lt;node-name&gt; | EXPERIMENTAL |
| kube_volumeattachment_created                      | Gauge       |                                                                                                                 | `volumeattachment`=&lt;volumeattachment-name&gt;                                                                     | EXPERIMENTAL |
| kube_volumeattachment_labels                       | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md) | `volumeattachment`=&lt;volumeattachment-name&gt; <br> `label_VOLUMEATTACHMENT_LABEL`=&lt;VOLUMEATTACHMENT_LABEL&gt;  | EXPERIMENTAL |
| kube_volumeattachment_spec_source_persistentvolume | Gauge       |                                                                                                                 | `volumeattachment`=&lt;volumeattachment-name&gt; <br> `volumename`=&lt;persistentvolume-name&gt;                     | EXPERIMENTAL |
| kube_volumeattachment_status_attached              | Gauge       |                                                                                                                 | `volumeattachment`=&lt;volumeattachment-name&gt;                                                                     | EXPERIMENTAL |
| kube_volumeattachment_status_attachment_metadata   | Gauge       |                                                                                                                 | `volumeattachment`=&lt;volumeattachment-name&gt; <br> `metadata_METADATA_KEY`=&lt;METADATA_VALUE&gt;                 | EXPERIMENTAL |
