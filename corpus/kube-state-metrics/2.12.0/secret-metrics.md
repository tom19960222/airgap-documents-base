---
collection: kube-state-metrics
version: "2.12.0"
title: "Secret Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/secret-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# Secret Metrics

| Metric name                           | Metric type | Description                                                                                                               | Labels/tags                                                                                                                           | Status       |
| ------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_secret_annotations               | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `secret`=&lt;secret-name&gt; <br> `namespace`=&lt;secret-namespace&gt; <br> `annotations_SECRET_ANNOTATION`=&lt;SECRET_ANNOTATION&gt; | EXPERIMENTAL |
| kube_secret_info                      | Gauge       |                                                                                                                           | `secret`=&lt;secret-name&gt; <br> `namespace`=&lt;secret-namespace&gt;                                                                | STABLE       |
| kube_secret_type                      | Gauge       |                                                                                                                           | `secret`=&lt;secret-name&gt; <br> `namespace`=&lt;secret-namespace&gt; <br> `type`=&lt;secret-type&gt;                                | STABLE       |
| kube_secret_labels                    | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `secret`=&lt;secret-name&gt; <br> `namespace`=&lt;secret-namespace&gt; <br> `label_SECRET_LABEL`=&lt;SECRET_LABEL&gt;                 | STABLE       |
| kube_secret_created                   | Gauge       |                                                                                                                           | `secret`=&lt;secret-name&gt; <br> `namespace`=&lt;secret-namespace&gt;                                                                | STABLE       |
| kube_secret_metadata_resource_version | Gauge       |                                                                                                                           | `secret`=&lt;secret-name&gt; <br> `namespace`=&lt;secret-namespace&gt;                                                                | EXPERIMENTAL |
| kube_secret_owner                         | Gauge       |                                                                                                                           | `secret`=&lt;secret-name&gt; <br> `namespace`=&lt;secret-namespace&gt; <br> `owner_kind`=&lt;owner kind&gt; <br> `owner_name`=&lt;owner name&gt; <br> `owner_is_controller`=&lt;whether owner is controller&gt; | EXPERIMENTAL |
