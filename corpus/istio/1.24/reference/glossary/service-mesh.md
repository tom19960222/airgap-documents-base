---
collection: istio
version: "1.24"
title: "Service Mesh"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/service-mesh.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
A *service mesh* or simply *mesh* is an infrastructure layer that enables
managed, observable and secure communication between
[workload instances](index.md#workload-instance).

Service names combined with a namespace are unique within a mesh.
In a [multicluster](index.md#multicluster) mesh, for example,
the `bar` service in the `foo` namespace in `cluster-1` is considered the same
service as the `bar` service in the `foo` namespace in `cluster-2`.

Since [identities](index.md#identity) are shared within the service
mesh, [workload instances](index.md#workload-instance) can authenticate communication with any other [workload
instance](index.md#workload-instance) within the same service mesh.
