---
collection: istio
version: "1.24"
title: "UnknownAnnotation"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0108/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when you attach an unrecognized annotation in the format `*.istio.io` to a namespace.

Istio only recognizes certain [annotation names](https://istio.io/v1.24/docs/reference/config/annotations/) <!-- unresolved-site-link: route=/docs/reference/config/annotations -->.

To resolve this problem, check the name of your annotation and try again.
