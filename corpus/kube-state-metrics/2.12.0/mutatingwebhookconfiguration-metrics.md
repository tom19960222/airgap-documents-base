---
collection: kube-state-metrics
version: "2.12.0"
title: "MutatingWebhookConfiguration Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/mutatingwebhookconfiguration-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# MutatingWebhookConfiguration Metrics

| Metric name                                                    | Metric type | Description | Labels/tags                                                                                                                                                                                                                                                                                   | Status       |
| -------------------------------------------------------------- | ----------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_mutatingwebhookconfiguration_info                         | Gauge       |             | `mutatingwebhookconfiguration`=&lt;mutatingwebhookconfiguration-name&gt; <br> `namespace`=&lt;mutatingwebhookconfiguration-namespace&gt;                                                                                                                                                      | EXPERIMENTAL |
| kube_mutatingwebhookconfiguration_created                      | Gauge       |             | `mutatingwebhookconfiguration`=&lt;mutatingwebhookconfiguration-name&gt; <br> `namespace`=&lt;mutatingwebhookconfiguration-namespace&gt;                                                                                                                                                      | EXPERIMENTAL |
| kube_mutatingwebhookconfiguration_metadata_resource_version    | Gauge       |             | `mutatingwebhookconfiguration`=&lt;mutatingwebhookconfiguration-name&gt; <br> `namespace`=&lt;mutatingwebhookconfiguration-namespace&gt;                                                                                                                                                      | EXPERIMENTAL |
| kube_mutatingwebhookconfiguration_webhook_clientconfig_service | Gauge       |             | `mutatingwebhookconfiguration`=&lt;mutatingwebhookconfiguration-name&gt; <br> `namespace`=&lt;mutatingwebhookconfiguration-namespace&gt; <br> `webhook_name`=&lt;webhook-name&gt; <br> `service_name`=&lt;webhook-service-name&gt; <br> `service_namespace`=&lt;webhook-service-namespace&gt; | EXPERIMENTAL |
