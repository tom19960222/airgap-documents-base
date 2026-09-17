---
collection: istio
version: "1.24"
title: "Service"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/service.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
A delineated group of related behaviors within a [service mesh](index.md#service-mesh). Services are identified using a
[service name](index.md#service-name),
and Istio policies such as load balancing and routing are applied using these names.
A service is typically materialized by one or more [service endpoints](index.md#service-endpoint), and may consist of multiple
[service versions](index.md#service-version).
