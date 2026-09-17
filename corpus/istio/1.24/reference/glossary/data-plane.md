---
collection: istio
version: "1.24"
title: "Data Plane"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/data-plane.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
The data plane is the part of the mesh that directly handles and routes traffic between workload instances.

In sidecar mode, Istio's data plane uses [Envoy](index.md#envoy) proxies deployed as sidecars to mediate and control all traffic that your mesh services send and receive.

In ambient mode, Istio's data plane uses node-level ztunnel proxies deployed as a DaemonSet to mediate and control all traffic that your mesh services send and receive.
