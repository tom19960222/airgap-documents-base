---
collection: istio
version: "1.24"
title: "ConflictingSidecarWorkloadSelectors"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0110/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when more than one Sidecar resource in a namespace selects the same workload instance. This can lead to undefined behavior. See the reference for the [Sidecar](https://istio.io/v1.24/docs/reference/config/networking/sidecar/) <!-- unresolved-site-link: route=/docs/reference/config/networking/sidecar --> resource for more information.

To fix, ensure that the set of workload instances (e.g. pods) selected by each Sidecar workload selector in a namespace do not overlap.
