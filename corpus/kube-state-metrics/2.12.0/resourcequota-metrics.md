---
collection: kube-state-metrics
version: "2.12.0"
title: "ResourceQuota Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/resourcequota-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# ResourceQuota Metrics

| Metric name                    | Metric type | Description                                                                                                               | Labels/tags                                                                                                                                         | Status       |
| ------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_resourcequota             | Gauge       |                                                                                                                           | `resourcequota`=&lt;quota-name&gt; <br> `namespace`=&lt;namespace&gt; <br> `resource`=&lt;ResourceName&gt; <br> `type`=&lt;quota-type&gt;           | STABLE       |
| kube_resourcequota_created     | Gauge       |                                                                                                                           | `resourcequota`=&lt;quota-name&gt; <br> `namespace`=&lt;namespace&gt;                                                                               | STABLE       |
| kube_resourcequota_annotations | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `resourcequota`=&lt;quota-name&gt; <br> `namespace`=&lt;namespace&gt; <br> `annotation_RESOURCE_QUOTA_ANNOTATION`=&lt;RESOURCE_QUOTA_ANNOTATION&gt; | EXPERIMENTAL |
| kube_resourcequota_labels      | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `resourcequota`=&lt;quota-name&gt; <br> `namespace`=&lt;namespace&gt; <br> `label_RESOURCE_QUOTA_LABEL`=&lt;RESOURCE_QUOTA_LABEL&gt;                | EXPERIMENTAL |
