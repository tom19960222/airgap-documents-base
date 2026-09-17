---
collection: istio
version: "1.24"
title: "OpenTelemetry"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/distributed-tracing/opentelemetry/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Learn how to configure the proxies to send traces in OpenTelemetry format."
---
[OpenTelemetry](https://opentelemetry.io/) (OTel) is a vendor-neutral, open source observability framework for instrumenting, generating, collecting, and exporting telemetry data. [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp/) (OTLP) traces can be sent to [Jaeger](../jaeger/index.md), as well as many commercial services.

To learn how Istio handles tracing, visit this task's [overview](../overview/index.md).

After completing this task, you will understand how to have your application participate in tracing with [OpenTelemetry](https://www.opentelemetry.io/), regardless of the language, framework, or platform you use to build your application.

This task uses the [Bookinfo](../../../../examples/bookinfo/index.md) sample as the example application and the
[OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) as the receiver of traces. To see an example of how to send traces directly to an OTLP compatible backend, see the [Jaeger task](../jaeger/index.md).

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

## Installation

All tracing options can be configured globally via `MeshConfig`.
To simplify configuration, it is recommended to create a single YAML file
which you can pass to the `istioctl install -f` command.

## Choosing the exporter

Istio can be configured to export [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otel/protocol/)
traces via gRPC or HTTP. Only one exporter can be configured at a time (either gRPC or HTTP).

### Exporting via gRPC

In this example, traces will be exported via OTLP/gRPC to the OpenTelemetry Collector.
The example also enables the [environment resource detector](https://opentelemetry.io/docs/languages/js/resources/#adding-resources-with-environment-variables). The environment detector adds attributes from the environment variable
`OTEL_RESOURCE_ATTRIBUTES` to the exported OpenTelemetry resource.

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

### Exporting via HTTP

In this example, traces will be exported via OTLP/HTTP to the OpenTelemetry Collector.
The example also enables the [environment resource detector](https://opentelemetry.io/docs/languages/js/resources/#adding-resources-with-environment-variables). The environment detector adds attributes from the environment variable
`OTEL_RESOURCE_ATTRIBUTES` to the exported OpenTelemetry resource.

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
        port: 4318
        service: opentelemetry-collector.observability.svc.cluster.local
        http:
          path: "/v1/traces"
          timeout: 5s
          headers:
            - name: "custom-header"
              value: "custom value"
        resource_detectors:
          environment: {}
EOF
```

## Enable tracing for mesh via Telemetry API

Enable tracing by applying the following configuration:

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
    randomSamplingPercentage: 100
    customTags:
      "my-attribute":
        literal:
          value: "default-value"
EOF
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

1.  The OpenTelemetry Collector used in the example is configured to export traces to the console.
    If you used the example Collector config, you can verify traces are arriving by looking
    at the Collector logs. It should contain something like:

```yaml
Resource SchemaURL:
Resource labels:
      -> service.name: STRING(productpage.default)
ScopeSpans #0
ScopeSpans SchemaURL:
InstrumentationScope
Span #0
    Trace ID       : 79fb7b59c1c3a518750a5d6dad7cd2d1
    Parent ID      : 0cf792b061f0ad51
    ID             : 2dff26f3b4d6d20f
    Name           : egress reviews:9080
    Kind           : SPAN_KIND_CLIENT
    Start time     : 2024-01-30 15:57:58.588041 +0000 UTC
    End time       : 2024-01-30 15:57:59.451116 +0000 UTC
    Status code    : STATUS_CODE_UNSET
    Status message :
Attributes:
      -> node_id: STRING(sidecar~10.244.0.8~productpage-v1-564d4686f-t6s4m.default~default.svc.cluster.local)
      -> zone: STRING()
      -> guid:x-request-id: STRING(da543297-0dd6-998b-bd29-fdb184134c8c)
      -> http.url: STRING(http://reviews:9080/reviews/0)
      -> http.method: STRING(GET)
      -> downstream_cluster: STRING(-)
      -> user_agent: STRING(curl/7.74.0)
      -> http.protocol: STRING(HTTP/1.1)
      -> peer.address: STRING(10.244.0.8)
      -> request_size: STRING(0)
      -> response_size: STRING(441)
      -> component: STRING(proxy)
      -> upstream_cluster: STRING(outbound|9080||reviews.default.svc.cluster.local)
      -> upstream_cluster.name: STRING(outbound|9080||reviews.default.svc.cluster.local)
      -> http.status_code: STRING(200)
      -> response_flags: STRING(-)
      -> istio.namespace: STRING(default)
      -> istio.canonical_service: STRING(productpage)
      -> istio.mesh_id: STRING(cluster.local)
      -> istio.canonical_revision: STRING(v1)
      -> istio.cluster_id: STRING(Kubernetes)
      -> my-attribute: STRING(default-value)
```

## Cleanup

1.  Remove the Telemetry resource:

```bash
$ kubectl delete telemetry otel-demo
```

1.  Remove any `istioctl` processes that may still be running using control-C or:

```bash
$ killall istioctl
```

1.  Uninstall the OpenTelemetry Collector:

```bash
$ kubectl delete -f @samples/open-telemetry/otel.yaml@ -n observability
$ kubectl delete namespace observability
```

1.  If you are not planning to explore any follow-on tasks, refer to the
    [Bookinfo cleanup](../../../../examples/bookinfo/index.md#cleanup) instructions
    to shutdown the application.
