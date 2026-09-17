---
collection: istio
version: "1.24"
title: "Configure trace sampling"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/distributed-tracing/sampling/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Learn the different approaches on how to configure trace sampling on the proxies."
---
Istio provides multiple ways to configure trace sampling. In this page you will learn and understand
all the different ways sampling can be configured.

## Before you begin

1.  Ensure that your applications propagate tracing headers as described [here](../overview/index.md).

## Available trace sampling configurations

1.  Percentage Sampler: A random sampling rate for percentage of requests that will be selected for trace
    generation.

1.  Custom OpenTelemetry Sampler: A custom sampler implementation, that must be paired with the `OpenTelemetryTracingProvider`.

### Percentage Sampler

---
---

> **Tip:**
>
> Users are encouraged to transition to the [Telemetry API](../../telemetry/index.md) for tracing configuration.

The random sampling rate percentage uses the specified percentage value to pick which requests to sample.

The sampling rate should be in the range of 0.0 to 100.0 with a precision of 0.01.
For example, to trace 5 requests out of every 10000, use 0.05 as the value here.

There are three ways you can configure the random sampling rate:

#### Telemetry API

Sampling can be configured on various scopes: mesh-wide, namespace or workload, offering great flexibility.
To learn more, please see the [Telemetry API](../../telemetry/index.md) documentation.

Install Istio without setting `sampling` inside `defaultConfig`:

```bash
$ cat <<EOF | istioctl install -y -f -
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    enableTracing: true
    extensionProviders:
    - name: otel-tracing
      opentelemetry:
        port: 4317
        service: opentelemetry-collector.observability.svc.cluster.local
        resource_detectors:
          environment: {}
EOF
```

Enable the tracing provider via the Telemetry API and set the `randomSamplingPercentage`:

```bash
$ kubectl apply -f - <<EOF
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
   name: otel-demo
spec:
  tracing:
  - providers:
    - name: otel-tracing
    randomSamplingPercentage: 10
EOF
```

#### Using `MeshConfig`

Random percentage sampling can be configured globally via `MeshConfig`.

```bash
$ cat <<EOF | istioctl install -y -f -
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    enableTracing: true
    defaultConfig:
      tracing:
        sampling: 10
    extensionProviders:
    - name: otel-tracing
      opentelemetry:
        port: 4317
        service: opentelemetry-collector.observability.svc.cluster.local
        resource_detectors:
          environment: {}
EOF
```

Then, enable the tracing provider via Telemetry API. Note that we don't set `randomSamplingPercentage` here.

```bash
$ kubectl apply -f - <<EOF
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: mesh-default
  namespace: istio-system
spec:
  tracing:
  - providers:
    - name: otel-tracing
EOF
```

#### Using the `proxy.istio.io/config` annotation

You can add the `proxy.istio.io/config` annotation to your Pod metadata
specification to override any mesh-wide sampling settings.

For instance, to override the mesh-wide sampling above, you would add the following to your pod manifest:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: curl
spec:
  ...
  template:
    metadata:
      ...
      annotations:
        ...
        proxy.istio.io/config: |
          tracing:
            sampling: 20
    spec:
      ...
```

### Custom OpenTelemetry Sampler

The OpenTelemetry specification defines the [Sampler API](https://opentelemetry.io/docs/specs/otel/trace/sdk/#sampler).
The Sampler API enables building a custom sampler that can perform more intelligent and efficient sampling decisions,
such as [probability sampling](https://opentelemetry.io/docs/specs/otel/trace/tracestate-probability-sampling-experimental/).

Such samplers can then be paired with the [`OpenTelemetryTracingProvider`](https://istio.io/v1.24/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider-OpenTelemetryTracingProvider) <!-- unresolved-site-link: route=/docs/reference/config/istio.mesh.v1alpha1 -->.

> **Quote:**
>
> The sampler implementation resides in the proxy, and can be found in
> [Envoy OpenTelemetry Samplers](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/trace/opentelemetry/samplers#opentelemetry-samplers).

Current custom sampler configurations in Istio:

- [Dynatrace Sampler](https://istio.io/v1.24/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider-OpenTelemetryTracingProvider-DynatraceSampler) <!-- unresolved-site-link: route=/docs/reference/config/istio.mesh.v1alpha1 -->

Custom samplers are configured via `MeshConfig`. Here is an example of configuring the Dynatrace sampler:

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    extensionProviders:
    - name: otel-tracing
      opentelemetry:
        port: 443
        service: abc.live.dynatrace.com/api/v2/otlp
        http:
          path: "/api/v2/otlp/v1/traces"
          timeout: 10s
          headers:
            - name: "Authorization"
              value: "Api-Token dt0c01."
        dynatrace_sampler:
          tenant: "abc"
          cluster_id: 123
```

### Order of precedence

With multiple ways of configuring sampling, it is important to understand
the order of precedence of each method.

When using the random percentage sampler, the order of precedence is:

<table><tr><td>Telemetry API > Pod Annotation > <code>MeshConfig</code> </td></tr></table>

That means, if a value is defined in all of the above, the value on the Telemetry API is the one selected.

When a custom OpenTelemetry sampler is configured, the order of precedence is:

<table><tr><td>Custom OTel Sampler > (Telemetry API | Pod Annotation | <code>MeshConfig</code>)</td></tr></table>

That means, if a custom OpenTelemetry sampler is configured, it overrides all the others' methods.
Additionally, the random percentage value is set to `100` and cannot be changed. This is important,
because the custom sampler needs to receive 100% of spans to be able to properly perform its decision.

## Deploy the OpenTelemetry Collector

---
---
Create a namespace for the OpenTelemetry Collector:

```bash
$ kubectl create namespace observability
```

Deploy the OpenTelemetry Collector. You can use [this example configuration](https://github.com/istio/istio/blob/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/open-telemetry/otel.yaml) as a starting point.

```bash
$ kubectl apply -f @samples/open-telemetry/otel.yaml@ -n observability
```

## Deploy the Bookinfo Application

Deploy the [Bookinfo](../../../../examples/bookinfo/index.md#deploying-the-application) sample application.

## Generating traces using the Bookinfo sample

1.  When the Bookinfo application is up and running, access `http://$GATEWAY_URL/productpage`
    one or more times to generate trace information.

---
---
To see trace data, you must send requests to your service. The number of requests depends on Istio's sampling rate and can be configured using the [Telemetry API](../../telemetry/index.md). With the default sampling rate of 1%, you need to send at least 100 requests before the first trace is visible.
To send 100 requests to the `productpage` service, use the following command:

```bash
$ for i in $(seq 1 100); do curl -s -o /dev/null "http://$GATEWAY_URL/productpage"; done
```

## Cleanup

1.  Remove the Telemetry resource:

```bash
$ kubectl delete telemetry otel-demo
```

1.  Remove any `istioctl` processes that may still be running using control-C or:

```bash
$ istioctl uninstall --purge -y
```

1.  Uninstall the OpenTelemetry Collector:

```bash
$ kubectl delete -f @samples/open-telemetry/otel.yaml@ -n observability
$ kubectl delete namespace observability
```
