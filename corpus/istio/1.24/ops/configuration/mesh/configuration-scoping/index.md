---
collection: istio
version: "1.24"
title: "Configuration Scoping"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/configuration/mesh/configuration-scoping/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows how to scope configuration in Istio, for operational and performance benefits."
---
In order to program the service mesh, the Istio control plane (Istiod) reads a variety of configurations, including core Kubernetes types like `Service` and `Node`,
and Istio's own types like `Gateway`.
These are then sent to the data plane (see [Architecture](../../../deployment/architecture/index.md) for more information).

By default, the control plane will read all configuration in all namespaces.
Each proxy instance will receive configuration for all namespaces as well.
This includes information about workloads that are not enrolled in the mesh.

This default ensures correct behavior out of the box, but comes with a scalability cost.
Each configuration has a cost (in CPU and memory, primarily) to maintain and keep up to date.
At large scales, it is critical to limit the configuration scope to avoid excessive resource consumption.

## Scoping mechanisms

Istio offers a few tools to help control the scope of a configuration to meet different use cases.
Depending on your requirements, these can be used alone or together.

* `Sidecar` provides a mechanism for specific workloads to _import_ a set of configurations
* `exportTo` provides a mechanism to _export_ a configuration to a set of workloads
* `discoverySelectors` provides a mechanism to let Istio completely ignore a set of configurations

### `Sidecar` import

The [`egress.hosts`](https://istio.io/v1.24/docs/reference/config/networking/sidecar/#IstioEgressListener) <!-- unresolved-site-link: route=/docs/reference/config/networking/sidecar --> field in `Sidecar`
allows specifying a list of configurations to import.
Only configurations matching the specified criteria will be seen by sidecars impacted by the `Sidecar` resource.

For example:

```yaml
apiVersion: networking.istio.io/v1
kind: Sidecar
metadata:
  name: default
spec:
  egress:
  - hosts:
    - "./*" # Import all configuration from our own namespace
    - "bookinfo/*" # Import all configuration from the bookinfo namespace
    - "external-services/example.com" # Import only 'example.com' from the external-services namespace
```

### `exportTo`

Istio's `VirtualService`, `DestinationRule`, and `ServiceEntry` provide a `spec.exportTo` field.
Similarly, `Service` can be configured with the `networking.istio.io/exportTo` annotation.

Unlike `Sidecar` which allows a workload owner to control what dependencies it has, `exportTo` works in the opposite way, and allows the service owners to control
their own service's visibility.

For example, this configuration makes the `details` `Service` only visible to its own namespace, and the `client` namespace:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: details
  annotations:
    networking.istio.io/exportTo: ".,client"
spec: ...
```

### `DiscoverySelectors`

While the previous controls operate on a workload or service owner level, [`DiscoverySelectors`](https://istio.io/v1.24/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig) <!-- unresolved-site-link: route=/docs/reference/config/istio.mesh.v1alpha1 --> provides mesh wide control over configuration visibility.
Discovery selectors allows specifying criteria for which namespaces should be visible to the control plane.
Any namespaces not matching are ignored by the control plane entirely.

This can be configured as part of `meshConfig` during installation. For example:

```yaml
meshConfig:
  discoverySelectors:
    - matchLabels:
        # Allow any namespaces with `istio-discovery=enabled`
        istio-discovery: enabled
    - matchLabels:
        # Allow "kube-system"; Kubernetes automatically adds this label to each namespace
        kubernetes.io/metadata.name: kube-system
```

> **Warning:**
>
> Istiod will always open a watch to Kubernetes for all namespaces.
> However, discovery selectors will ignore objects that are not selected very early in its processing, minimizing costs.

## Frequently asked questions

### How can I understand the cost of a certain configuration?

In order to get the best return-on-investment for scoping down configuration, it can be helpful to understand the cost of each object.
Unfortunately, there is not a straightforward answer; scalability depends on a large number of factors.
However, there are a few general guidelines:

Configuration *changes* are expensive in Istio, as they require recomputation.
While `Endpoints` changes (generally from a Pod scaling up or down) are heavily optimized, most other configurations are fairly expensive.
This can be especially harmful when controllers are constantly making changes to an object (sometimes this happens accidentally!).
Some tools to detect which configurations are changing:
* Istiod will log each change like: `Push debounce stable 1 for config Gateway/default/gateway: ..., full=true`.
  This shows a `Gateway` object in the `default` namespace changed. `full=false` would represent and optimized update such as `Endpoint`.
  Note: changes to `Service` and `Endpoints` will all show as `ServiceEntry`.
* Istiod exposes metrics `pilot_k8s_cfg_events` and `pilot_k8s_reg_events` for each change.
* `kubectl get <resource> --watch -oyaml --show-managed-fields` can show changes to an object (or objects) to help understand what is changing, and by whom.

[Headless services](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) (besides ones declared as [HTTP](../../traffic-management/protocol-selection/index.md#explicit-protocol-selection))
scale with the number of instances. This makes large headless services expensive, and a good candidate for exclusion with `exportTo` or equivalent.

### What happens if I connect to a service outside of my scope?

When connecting to a service that has been excluded through one of the scoping mechanisms, the data plane will not know anything about the destination,
so it will be treated as [Unmatched traffic](../../traffic-management/traffic-routing/index.md#unmatched-traffic).

### What about Gateways?

While [Gateways](../../../../setup/additional-setup/gateway/index.md) will respect `exportTo` and `DiscoverySelectors`, `Sidecar` objects do not impact Gateways.
However, unlike sidecars, gateways do not have configuration for the entire cluster by default.
Instead, each configuration is explicitly attached to the gateway, which mostly avoids this problem.

However, [currently](https://github.com/istio/istio/issues/29131) part of the data plane configuration (a "cluster", in Envoy terms), is always sent for
the entire cluster, even if it is not referenced explicitly.
