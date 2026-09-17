---
collection: istio
version: "1.24"
title: "VirtualServiceDestinationPortSelectorRequired"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0112/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when a virtual service routes to a service with more than one port exposed, but does not specify which one to use. This ambiguity can lead to undefined behavior.

To fix, add a `port` to the virtual service [Destination](https://istio.io/v1.24/docs/reference/config/networking/virtual-service/#Destination) <!-- unresolved-site-link: route=/docs/reference/config/networking/virtual-service --> to disambiguate which service port should be routed to.
