---
collection: istio
version: "1.24"
title: "External Control Plane"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/external-control-plane.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
An external control plane is a [control plane](index.md#control-plane)
that externally manages mesh workloads running in their own [clusters](index.md#cluster)
or other infrastructure. The control plane may, itself, be deployed in a cluster, although not
in one of the clusters that is part of the mesh it's controlling.
Its purpose is to cleanly separate the control plane from the data plane of a mesh.
