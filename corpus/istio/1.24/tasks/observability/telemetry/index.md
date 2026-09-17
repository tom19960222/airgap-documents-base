---
collection: istio
version: "1.24"
title: "Telemetry API"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/telemetry/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "This task shows you how to configure the Telemetry API."
---
Istio provides a [Telemetry API](https://istio.io/v1.24/docs/reference/config/telemetry/) <!-- unresolved-site-link: route=/docs/reference/config/telemetry --> that enables flexible configuration of
[metrics](../metrics/_index.md), [access logs](../logs/_index.md), and [tracing](../distributed-tracing/_index.md).

## Using the API

### Scope, Inheritance, and Overrides

Telemetry API resources inherit configuration from parent resources in the Istio configuration hierarchy:

1.  root configuration namespace (example: `istio-system`)
1.  local namespace (namespace-scoped resource with **no** workload `selector`)
1.  workload (namespace-scoped resource with a workload `selector`)

A Telemetry API resource in the root configuration namespace, typically `istio-system`, provides mesh-wide defaults for behavior.
Any workload-specific selector in the root configuration namespace will be ignored/rejected. It is not valid to define multiple
mesh-wide Telemetry API resources in the root configuration namespace.

Namespace-specific overrides for the mesh-wide configuration can be achieved by applying a new `Telemetry` resource in the desired
namespace (without a workload selector). Any fields specified in the namespace configuration will completely override
the field from the parent configuration (in the root configuration namespace).

Workload-specific overrides can be achieved by applying a new Telemetry resource in the desired namespace *with a workload selector*.

### Workload Selection

Individual workloads within a namespace are selected via a [`selector`](https://istio.io/v1.24/docs/reference/config/type/workload-selector/#WorkloadSelector) <!-- unresolved-site-link: route=/docs/reference/config/type/workload-selector -->
which allows label-based selection of workloads.

It is not valid to have two different `Telemetry` resources select the same workload using `selector`. Likewise, it is not valid to have two
distinct `Telemetry` resources in a namespace with no `selector` specified.

### Provider Selection

The Telemetry API uses the concept of providers to indicate the protocol or type of integration to use. Providers can be configured in [`MeshConfig`](https://istio.io/v1.24/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider) <!-- unresolved-site-link: route=/docs/reference/config/istio.mesh.v1alpha1 -->.

An example set of provider configuration in `MeshConfig` is:

```yaml
data:
  mesh: |-
      extensionProviders: # The following content defines two example tracing providers.
      - name: "localtrace"
        zipkin:
          service: "zipkin.istio-system.svc.cluster.local"
          port: 9411
          maxTagLength: 56
      - name: "cloudtrace"
        stackdriver:
          maxTagLength: 256
```

For convenience, Istio comes with a few providers configured out of the box with default settings:

| Provider Name | Functionality                    |
| ------------- | -------------------------------- |
| `prometheus`  | Metrics                          |
| `stackdriver` | Metrics, Tracing, Access Logging |
| `envoy`       | Access Logging                   |

In additional, a [default provider](https://istio.io/v1.24/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-DefaultProviders) <!-- unresolved-site-link: route=/docs/reference/config/istio.mesh.v1alpha1 --> can be set which
will be used when the `Telemetry` resources do not specify a provider.

> **Tip:**
>
> If you're using [Sidecar](https://istio.io/v1.24/docs/reference/config/networking/sidecar/) <!-- unresolved-site-link: route=/docs/reference/config/networking/sidecar --> configuration, do not forget to add provider's service.

> **Tip:**
>
> Providers do not support `$(HOST_IP)`. If you're running collector in agent mode, you can use [service internal traffic policy](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/#using-service-internal-traffic-policy), and set `InternalTrafficPolicy` to `Local` for better performance.

## Examples

### Configuring mesh-wide behavior

Telemetry API resources inherit from the root configuration namespace for a mesh, typically `istio-system`. To configure
mesh-wide behavior, add a new (or edit the existing) `Telemetry` resource in the root configuration namespace.

Here is an example configuration that uses the provider configuration from the prior section:

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: mesh-default
  namespace: istio-system
spec:
  tracing:
  - providers:
    - name: localtrace
    customTags:
      foo:
        literal:
          value: bar
    randomSamplingPercentage: 100
```

This configuration overrides the default provider from `MeshConfig`, setting the mesh default to be the `localtrace`
provider. It also sets the mesh-wide sampling percentage to be `100`, and configures a tag to be added to all trace
spans with a name of `foo` and a value of `bar`.

### Configuring namespace-scoped tracing behavior

To tailor the behavior for individual namespaces, add a `Telemetry` resource to the desired namespace.
Any fields specified in the namespace resource will completely override the inherited field configuration from the configuration hierarchy.
For example:

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: namespace-override
  namespace: myapp
spec:
  tracing:
  - customTags:
      userId:
        header:
          name: userId
          defaultValue: unknown
```

When deployed into a mesh with the prior mesh-wide example configuration, this will result in
tracing behavior in the `myapp` namespace that sends trace spans to the `localtrace` provider and
randomly selects requests for tracing at a `100%` rate, but that sets custom tags for each span with
a name of `userId` and a value taken from the `userId` request header.
Importantly, the `foo: bar` tag from the parent configuration will not be used in the `myapp` namespace.
The custom tags behavior completely overrides the behavior configured in the `mesh-default.istio-system` resource.

> **Tip:**
>
> Any configuration in a `Telemetry` resource completely overrides configuration of its parent resource in the configuration hierarchy. This includes provider selection.

### Configuring workload-specific behavior

To tailor the behavior for individual workloads, add a `Telemetry` resource to the desired namespace and use a
`selector`. Any fields specified in the workload-specific resource will completely override the inherited
field configuration from the configuration hierarchy.

For example:

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: workload-override
  namespace: myapp
spec:
  selector:
    matchLabels:
      service.istio.io/canonical-name: frontend
  tracing:
  - disableSpanReporting: true
```

In this case, tracing will be disabled for the `frontend` workload in the `myapp` namespace.
Istio will still forward the tracing headers, but no spans will be reported to the configured tracing provider.

> **Tip:**
>
> It is not valid to have two `Telemetry` resources with workload selectors select the same workload. In those cases, behavior is undefined.
