---
collection: kube-state-metrics
version: "2.12.0"
title: "CertificateSigningRequest Metrics"
source_url: https://github.com/kubernetes/kube-state-metrics/blob/1e8b837eb1fa1cb2dc3c37821637334e2dd47488/docs/certificatesigningrequest-metrics.md
fetched_at: 2024-04-02T08:08:11-07:00
---
# CertificateSigningRequest Metrics

| Metric name                                | Metric type | Description                                                                                                               | Labels/tags                                                                                                                                                                   | Status       |
| ------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| kube_certificatesigningrequest_annotations | Gauge       | Kubernetes annotations converted to Prometheus labels controlled via [--metric-annotations-allowlist](cli-arguments.md) | `certificatesigningrequest`=&lt;certificatesigningrequest-name&gt; <br> `signer_name`=&lt;certificatesigningrequest-signer-name&gt;                                           | EXPERIMENTAL |
| kube_certificatesigningrequest_created     | Gauge       |                                                                                                                           | `certificatesigningrequest`=&lt;certificatesigningrequest-name&gt; <br> `signer_name`=&lt;certificatesigningrequest-signer-name&gt;                                           | STABLE       |
| kube_certificatesigningrequest_condition   | Gauge       |                                                                                                                           | `certificatesigningrequest`=&lt;certificatesigningrequest-name&gt; <br> `signer_name`=&lt;certificatesigningrequest-signer-name&gt; <br> `condition`=&lt;approved\|denied&gt; | STABLE       |
| kube_certificatesigningrequest_labels      | Gauge       | Kubernetes labels converted to Prometheus labels controlled via [--metric-labels-allowlist](cli-arguments.md)           | `certificatesigningrequest`=&lt;certificatesigningrequest-name&gt; <br> `signer_name`=&lt;certificatesigningrequest-signer-name&gt;                                           | STABLE       |
| kube_certificatesigningrequest_cert_length | Gauge       |                                                                                                                           | `certificatesigningrequest`=&lt;certificatesigningrequest-name&gt; <br> `signer_name`=&lt;certificatesigningrequest-signer-name&gt;                                           | STABLE       |
