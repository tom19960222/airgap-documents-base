---
collection: istio
version: "1.24"
title: "Workload Instance"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/workload-instance.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
A single instantiation of a [workload's](index.md#workload) binary.
A workload instance can expose zero or more [service endpoints](index.md#service-endpoint),
and can consume zero or more [services](index.md#service).

Workload instances have a number of properties:

- Name and namespace
- Unique ID
- IP Address
- Labels
- Principal

These properties are available in policy and telemetry configuration
using the many [`source.*` and `destination.*` attributes](https://istio.io/v1.24/docs/reference/config/policy-and-telemetry/attribute-vocabulary/) <!-- unresolved-site-link: route=/docs/reference/config/policy-and-telemetry/attribute-vocabulary -->.
