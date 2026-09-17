---
collection: istio
version: "1.24"
title: "Multi-Mesh"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/multi-mesh.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Multi-mesh is a deployment model that consists of two or more [service meshes](index.md#service-mesh).
Each mesh has independent administration for naming and identities but you can
expose services between meshes through [mesh federation](index.md#mesh-federation).
The resulting deployment is a multi-mesh deployment.
