---
collection: kube-state-metrics
version: "2.12.0"
title: "Network Policy Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/networkpolicy-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# Network Policy Metrics

| Metric name                           | Metric type | Description                                                                                                               | Labels/tags                                                                   | Status       |
| ------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| kube_networkpolicy_annotations        | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `namespace`=&lt;namespace name&gt; `networkpolicy`=&lt;networkpolicy name&gt; | EXPERIMENTAL |
| kube_networkpolicy_created            | Gauge       |                                                                                                                           | `namespace`=&lt;namespace name&gt; `networkpolicy`=&lt;networkpolicy name&gt; | EXPERIMENTAL |
| kube_networkpolicy_labels             | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `namespace`=&lt;namespace name&gt; `networkpolicy`=&lt;networkpolicy name&gt; | EXPERIMENTAL |
| kube_networkpolicy_spec_egress_rules  | Gauge       |                                                                                                                           | `namespace`=&lt;namespace name&gt; `networkpolicy`=&lt;networkpolicy name&gt; | EXPERIMENTAL |
| kube_networkpolicy_spec_ingress_rules | Gauge       |                                                                                                                           | `namespace`=&lt;namespace name&gt; `networkpolicy`=&lt;networkpolicy name&gt; | EXPERIMENTAL |
