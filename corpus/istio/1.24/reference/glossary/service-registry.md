---
collection: istio
version: "1.24"
title: "Service Registry"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/service-registry.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Istio maintains an internal service registry containing the set of [services](index.md#service),
and their corresponding [service endpoints](index.md#service-endpoint), running in a service mesh.
Istio uses the service registry to generate [Envoy](index.md#envoy) configuration.

Istio does not provide [service discovery](https://en.wikipedia.org/wiki/Service_discovery),
although most services are automatically added to the registry by [Pilot](index.md#pilot)
adapters that reflect the discovered services of the underlying platform (Kubernetes, Consul, plain DNS).
Additional services can also be registered manually using a
[`ServiceEntry`](../../concepts/traffic-management/index.md#service-entries) configuration.
