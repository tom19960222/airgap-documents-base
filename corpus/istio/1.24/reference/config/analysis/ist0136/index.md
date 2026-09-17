---
collection: istio
version: "1.24"
title: "AlphaAnnotation"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0136/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when an Istio or Kubernetes resource has an Istio annotation that
is new, has been incompletely implemented, or lacks performance testing.

Consult Istio's [Feature Status documentation](../../../../releases/feature-stages/index.md) for information
on the relative maturity and support level of Istio features.

## How to resolve

Using an Istio annotation at an Alpha maturity level is not a problem.  It may be the best way
to gain experience with new Istio features.

The Istio team recommends using this analysis to be aware of your use of Alpha maturity features
before moving workloads to production clusters.
