---
collection: istio
version: "1.24"
title: "Attribute"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/attribute.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Attributes control the runtime behavior of services running in the mesh.
Attributes are named and typed pieces of metadata describing ingress and egress traffic and the
environment this traffic occurs in. An Istio attribute carries a specific piece
of information such as the error code of an API request, the latency of an API request, or the
original IP address of a TCP connection. For example:

```yaml
request.path: xyz/abc
request.size: 234
request.time: 12:34:56.789 04/17/2017
source.ip: 192.168.0.1
destination.workload.name: example
```

Attributes are used by Istio's [policy and telemetry](https://istio.io/v1.24/docs/reference/config/policy-and-telemetry/) <!-- unresolved-site-link: route=/docs/reference/config/policy-and-telemetry --> features.
