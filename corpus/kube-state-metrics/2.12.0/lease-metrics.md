---
collection: kube-state-metrics
version: "2.12.0"
title: "Lease Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/lease-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# Lease Metrics

| Metric name           | Metric type | Description | Labels/tags                                                                                                                                                                             | Status       |
| --------------------- | ----------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| kube_lease_owner      | Gauge       |             | `lease`=&lt;lease-name&gt; <br> `owner_kind`=&lt;onwer kind&gt; <br> `owner_name`=&lt;owner name&gt; <br> `namespace` = &lt;namespace&gt; <br> `lease_holder`=&lt;lease holder name&gt; | EXPERIMENTAL |
| kube_lease_renew_time | Gauge       |             | `lease`=&lt;lease-name&gt;  <br> `namespace` = &lt;namespace&gt;                                                                                                                        | EXPERIMENTAL |
