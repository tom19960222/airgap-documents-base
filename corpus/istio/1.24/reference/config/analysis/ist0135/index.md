---
collection: istio
version: "1.24"
title: "DeprecatedAnnotation"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0135/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when an Istio or Kubernetes resource has an Istio annotation that
has been deprecated by the Istio team.

## How to resolve

It is likely the annotation will stop taking affect when the Istio control plane is upgraded.
Before upgrading, remove or replace this annotation with a supported replacement.

Consult the [Istio annotation documentation](https://istio.io/v1.24/docs/reference/config/annotations/) <!-- unresolved-site-link: route=/docs/reference/config/annotations --> for a list of Istio annotations.

The Istio release announcements may include advice or suggested replacements for deprecated
Istio annotations.
