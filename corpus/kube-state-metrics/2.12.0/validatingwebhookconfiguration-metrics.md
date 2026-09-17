---
collection: kube-state-metrics
version: "2.12.0"
title: "ValidatingWebhookConfiguration Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/validatingwebhookconfiguration-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# ValidatingWebhookConfiguration Metrics

| Metric name                                                      | Metric type | Description | Labels/tags                                                                                                                                                                                                                                                                                         | Status       |
| ---------------------------------------------------------------- | ----------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_validatingwebhookconfiguration_info                         | Gauge       |             | `validatingwebhookconfiguration`=&lt;validatingwebhookconfiguration-name&gt; <br> `namespace`=&lt;validatingwebhookconfiguration-namespace&gt;                                                                                                                                                      | EXPERIMENTAL |
| kube_validatingwebhookconfiguration_created                      | Gauge       |             | `validatingwebhookconfiguration`=&lt;validatingwebhookconfiguration-name&gt; <br> `namespace`=&lt;validatingwebhookconfiguration-namespace&gt;                                                                                                                                                      | EXPERIMENTAL |
| kube_validatingwebhookconfiguration_metadata_resource_version    | Gauge       |             | `validatingwebhookconfiguration`=&lt;validatingwebhookconfiguration-name&gt; <br> `namespace`=&lt;validatingwebhookconfiguration-namespace&gt;                                                                                                                                                      | EXPERIMENTAL |
| kube_validatingwebhookconfiguration_webhook_clientconfig_service | Gauge       |             | `validatingwebhookconfiguration`=&lt;validatingwebhookconfiguration-name&gt; <br> `namespace`=&lt;validatingwebhookconfiguration-namespace&gt; <br> `webhook_name`=&lt;webhook-name&gt; <br> `service_name`=&lt;webhook-service-name&gt; <br> `service_namespace`=&lt;webhook-service-namespace&gt; | EXPERIMENTAL |
