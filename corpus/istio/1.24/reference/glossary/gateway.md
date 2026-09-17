---
collection: istio
version: "1.24"
title: "Gateway"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/gateway.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
A gateway is a standalone Istio proxy deployed at the edge of the mesh.
Gateways are used to route traffic [into](../../tasks/traffic-management/ingress/_index.md) or [out of](../../tasks/traffic-management/egress/_index.md) the mesh.

An Istio `Gateway` CR is used to configure the exposed ports of a gateway deployment.
