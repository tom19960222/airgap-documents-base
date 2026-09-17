---
collection: kube-state-metrics
version: "2.12.0"
title: "ClusterRoleBinding Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/clusterrolebinding-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# ClusterRoleBinding Metrics

| Metric name                                       | Metric type | Description                                                                                                               | Labels/tags                                                                                                                      | Status       |
| ------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_clusterrolebinding_annotations               | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `clusterrolebinding`=&lt;clusterrolebinding-name&gt;                                                                             | EXPERIMENTAL |
| kube_clusterrolebinding_labels                    | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `clusterrolebinding`=&lt;clusterrolebinding-name&gt;                                                                             | EXPERIMENTAL |
| kube_clusterrolebinding_info                      | Gauge       |                                                                                                                           | `clusterrolebinding`=&lt;clusterrolebinding-name&gt; <br> `roleref_kind`=&lt;role-kind&gt; <br> `roleref_name`=&lt;role-name&gt; | EXPERIMENTAL |
| kube_clusterrolebinding_created                   | Gauge       |                                                                                                                           | `clusterrolebinding`=&lt;clusterrolebinding-name&gt;                                                                             | EXPERIMENTAL |
| kube_clusterrolebinding_metadata_resource_version | Gauge       |                                                                                                                           | `clusterrolebinding`=&lt;clusterrolebinding-name&gt;                                                                             | EXPERIMENTAL |
