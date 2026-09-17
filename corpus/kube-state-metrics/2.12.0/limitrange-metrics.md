---
collection: kube-state-metrics
version: "2.12.0"
title: "LimitRange Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/limitrange-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# LimitRange Metrics

| Metric name             | Metric type | Description | Labels/tags                                                                                                                                                                                                 | Status |
| ----------------------- | ----------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| kube_limitrange         | Gauge       |             | `limitrange`=&lt;limitrange-name&gt; <br> `namespace`=&lt;namespace&gt; <br> `resource`=&lt;ResourceName&gt; <br> `type`=&lt;Pod\|Container\|PersistentVolumeClaim&gt; <br> `constraint`=&lt;constraint&gt; | STABLE |
| kube_limitrange_created | Gauge       |             | `limitrange`=&lt;limitrange-name&gt; <br> `namespace`=&lt;namespace&gt;                                                                                                                                     | STABLE |
