---
collection: istio
version: "1.24"
title: "Workload Instance Principal"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/workload-instance-principal.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
The verifiable authority under which a [workload instance](index.md#workload-instance) runs.
Istio's service-to-service authentication is used to produce the workload principal.
By default workload principals are compliant with the SPIFFE ID format.

Workload instance principals are available in policy and telemetry configuration
using the `source.principal` and `destination.principal` [attributes](index.md#attribute).
