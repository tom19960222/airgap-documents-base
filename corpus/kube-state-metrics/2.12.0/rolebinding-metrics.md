---
collection: kube-state-metrics
version: "2.12.0"
title: "RoleBinding Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/rolebinding-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# RoleBinding Metrics

| Metric name                                | Metric type | Description                                                                                                               | Labels/tags                                                                                                                                                       | Status       |
| ------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_rolebinding_annotations               | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `rolebinding`=&lt;rolebinding-name&gt; <br> `namespace`=&lt;rolebinding-namespace&gt;                                                                             | EXPERIMENTAL |
| kube_rolebinding_labels                    | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `rolebinding`=&lt;rolebinding-name&gt; <br> `namespace`=&lt;rolebinding-namespace&gt;                                                                             | EXPERIMENTAL |
| kube_rolebinding_info                      | Gauge       |                                                                                                                           | `rolebinding`=&lt;rolebinding-name&gt; <br> `namespace`=&lt;rolebinding-namespace&gt; <br> `roleref_kind`=&lt;role-kind&gt; <br> `roleref_name`=&lt;role-name&gt; | EXPERIMENTAL |
| kube_rolebinding_created                   | Gauge       |                                                                                                                           | `rolebinding`=&lt;rolebinding-name&gt; <br> `namespace`=&lt;rolebinding-namespace&gt;                                                                             | EXPERIMENTAL |
| kube_rolebinding_metadata_resource_version | Gauge       |                                                                                                                           | `rolebinding`=&lt;rolebinding-name&gt; <br> `namespace`=&lt;rolebinding-namespace&gt;                                                                             | EXPERIMENTAL |
