---
collection: kube-state-metrics
version: "2.12.0"
title: "ClusterRole Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/clusterrole-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# ClusterRole Metrics

| Metric name                                | Metric type | Description                                                                                                               | Labels/tags                            | Status       |
| ------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------ |
| kube_clusterrole_annotations               | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `clusterrole`=&lt;clusterrole-name&gt; | EXPERIMENTAL |
| kube_clusterrole_labels                    | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `clusterrole`=&lt;clusterrole-name&gt; | EXPERIMENTAL |
| kube_clusterrole_info                      | Gauge       |                                                                                                                           | `clusterrole`=&lt;clusterrole-name&gt; | EXPERIMENTAL |
| kube_clusterrole_created                   | Gauge       |                                                                                                                           | `clusterrole`=&lt;clusterrole-name&gt; | EXPERIMENTAL |
| kube_clusterrole_metadata_resource_version | Gauge       |                                                                                                                           | `clusterrole`=&lt;clusterrole-name&gt; | EXPERIMENTAL |
