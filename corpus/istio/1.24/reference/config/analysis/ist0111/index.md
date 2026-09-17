---
collection: istio
version: "1.24"
title: "MultipleSidecarsWithoutWorkloadSelectors"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0111/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when more than one Sidecar resource in a namespace does not define any workload selector. This can lead to undefined behavior. See the reference for the [Sidecar](https://istio.io/v1.24/docs/reference/config/networking/sidecar/) <!-- unresolved-site-link: route=/docs/reference/config/networking/sidecar --> resource for more information.

To fix this, ensure that each namespace has only one Sidecar resource without a workload selector.
