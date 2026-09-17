---
collection: istio
version: "1.24"
title: "Mesh Federation"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/mesh-federation.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Mesh federation is the act of exposing services between meshes and enabling
communication across mesh boundaries. Each mesh may expose a subset of its
services to enable one or more other meshes to consume the exposed services. You
can use mesh federation to enable communication between meshes in a
[multi-mesh deployment](../../ops/deployment/deployment-models/index.md#multiple-meshes).
