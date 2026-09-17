---
collection: kube-state-metrics
version: "2.12.0"
title: "Namespace Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/namespace-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# Namespace Metrics

| Metric name                     | Metric type | Description                                                                                                               | Labels/tags                                                                                                                                                                                                             | Status       |
| ------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_namespace_annotations      | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `namespace`=&lt;namespace-name&gt; <br> `label_NS_ANNOTATION`=&lt;NS_ANNOTATION&gt;                                                                                                                                     | EXPERIMENTAL |
| kube_namespace_created          | Gauge       |                                                                                                                           | `namespace`=&lt;namespace-name&gt;                                                                                                                                                                                      | STABLE       |
| kube_namespace_labels           | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `namespace`=&lt;namespace-name&gt; <br> `label_NS_LABEL`=&lt;NS_LABEL&gt;                                                                                                                                               | STABLE       |
| kube_namespace_status_condition | Gauge       |                                                                                                                           | `namespace`=&lt;namespace-name&gt; <br> `condition`=&lt;NamespaceDeletionDiscoveryFailure\|NamespaceDeletionContentFailure\|NamespaceDeletionGroupVersionParsingFailure&gt;  <br> `status`=&lt;true\|false\|unknown&gt; | EXPERIMENTAL |
| kube_namespace_status_phase     | Gauge       |                                                                                                                           | `namespace`=&lt;namespace-name&gt; <br> `phase`=&lt;Active\|Terminating&gt;                                                                                                                                             | STABLE       |
