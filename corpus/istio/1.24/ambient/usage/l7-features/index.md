---
collection: istio
version: "1.24"
title: "Use Layer 7 features"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/usage/l7-features/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Supported features when using a L7 waypoint proxy."
---
By adding a waypoint proxy to your traffic flow you can enable more of [Istio's features](../../../concepts/_index.md). Waypoints are configured using the Kubernetes Gateway API.

> **Warning:**
>
> Usage of VirtualService with the ambient data plane mode is considered Alpha. Mixing with Gateway API configuration is not supported, and will lead to undefined behavior.

## Route and policy attachment

The Gateway API defines the relationship between objects (such as routes and gateways) in terms of *attachment*.

* Route objects (such as [HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/)) include a way to reference the **parent** resources it wants to attach to.
* Policy objects are considered [*metaresources*](https://gateway-api.sigs.k8s.io/geps/gep-713/): objects that augments the behavior of a **target** object in a standard way.

The tables below show the type of attachment that is configured for each object.

## Traffic routing

With a waypoint proxy deployed, you can use the following traffic route types:

|  Name  | Feature Status | Attachment |
| --- | --- | --- |
| [`HTTPRoute`](https://gateway-api.sigs.k8s.io/guides/http-routing/) | Beta | `parentRefs` |
| [`TLSRoute`](https://gateway-api.sigs.k8s.io/guides/tls) | Alpha | `parentRefs` |
| [`TCPRoute`](https://gateway-api.sigs.k8s.io/guides/tcp/) | Alpha | `parentRefs` |

Refer to the [traffic management](../../../tasks/traffic-management/_index.md) documentation to see the range of features that can be implemented using these routes.

## Security

Without a waypoint installed, you can only use [Layer 4 security policies](../l4-policy/index.md). By adding a waypoint, you gain access to the following policies:

|  Name  | Feature Status | Attachment |
| --- | --- | --- |
| [`AuthorizationPolicy`](https://istio.io/v1.24/docs/reference/config/security/authorization-policy/) <!-- unresolved-site-link: route=/docs/reference/config/security/authorization-policy --> (including L7 features) | Beta | `targetRefs` |
| [`RequestAuthentication`](https://istio.io/v1.24/docs/reference/config/security/request_authentication/) <!-- unresolved-site-link: route=/docs/reference/config/security/request_authentication --> | Beta | `targetRefs` |

### Considerations for authorization policies {#considerations}

In ambient mode, authorization policies can either be *targeted* (for ztunnel enforcement) or *attached* (for waypoint enforcement). For an authorization policy to be attached to a waypoint it must have a `targetRef` which refers to the waypoint, or a Service which uses that waypoint.

The ztunnel cannot enforce L7 policies. If a policy with rules matching L7 attributes is targeted with a workload selector (rather than attached with a `targetRef`), such that it is enforced by a ztunnel, it will fail safe by becoming a `DENY` policy.

See [the L4 policy guide](../l4-policy/index.md) for more information, including when to attach policies to waypoints for TCP-only use cases.

## Observability

The [full set of Istio traffic metrics](../../../reference/config/metrics/index.md) are exported by a waypoint proxy.

## Extension

As the waypoint proxy is a deployment of Envoy, the extension mechanisms that are available for Envoy in sidecar mode are also available to waypoint proxies.

|  Name  | Feature Status | Attachment |
| --- | --- | --- |
| `WasmPlugin` † | Alpha | `targetRefs` |
| `EnvoyFilter` | Alpha | `targetRefs` |

† [Read more on how to extend waypoints with WebAssembly plugins](../extend-waypoint-wasm/index.md).

Extension configurations are considered policy by the Gateway API definition.

## Scoping routes or policies

A route or policy can be scoped to apply to all traffic traversing a waypoint proxy, or only specific services.

### Attach to the entire waypoint proxy

To attach a route or a policy to the entire waypoint — so that it applies to all traffic enrolled to use it — set `Gateway` as the `parentRefs` or `targetRefs` value, depending on the type.

To scope an `AuthorizationPolicy` policy to apply to the waypoint named `default` for the `default` namespace:

```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: view-only
  namespace: default
spec:
  targetRefs:
  - kind: Gateway
    group: gateway.networking.k8s.io
    name: default
  action: ALLOW
  rules:
  - from:
    - source:
        namespaces: ["default", "istio-system"]
    to:
    - operation:
        methods: ["GET"]
```

### Attach to a specific service

You can also attach a route to one or more specific services within the waypoint. Set `Service` as the `parentRefs` or `targetRefs` value, as appropriate.

To apply the `reviews` HTTPRoute to the `reviews` service in the `default` namespace:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: reviews
  namespace: default
spec:
  parentRefs:
  - group: ""
    kind: Service
    name: reviews
    port: 9080
  rules:
  - backendRefs:
    - name: reviews-v1
      port: 9080
      weight: 90
    - name: reviews-v2
      port: 9080
      weight: 10
```
