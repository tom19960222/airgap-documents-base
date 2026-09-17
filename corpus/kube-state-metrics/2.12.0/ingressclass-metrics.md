---
collection: kube-state-metrics
version: "2.12.0"
title: "IngressClass Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/ingressclass-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# IngressClass Metrics

| Metric name                   | Metric type | Description                                                                                                               | Labels/tags                                                                                                        | Status       |
| ----------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------ |
| kube_ingressclass_annotations | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `ingressclass`=&lt;ingressclass-name&gt; <br> `annotation_INGRESSCLASS_ANNOTATION`=&lt;INGRESSCLASS_ANNOTATION&gt; | EXPERIMENTAL |
| kube_ingressclass_info        | Gauge       |                                                                                                                           | `ingressclass`=&lt;ingressclass-name&gt; <br> `controller`=&lt;ingress-controller-name&gt; <br>                    | EXPERIMENTAL |
| kube_ingressclass_labels      | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `ingressclass`=&lt;ingressclass-name&gt; <br> `label_INGRESSCLASS_LABEL`=&lt;INGRESSCLASS_LABEL&gt;                | EXPERIMENTAL |
| kube_ingressclass_created     | Gauge       |                                                                                                                           | `ingressclass`=&lt;ingressclass-name&gt;                                                                           | EXPERIMENTAL |
