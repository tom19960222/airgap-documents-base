---
collection: istio
version: "1.24"
title: "Configure access logs with Telemetry API"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/logs/telemetry-api/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "This task shows you how to configure Envoy proxies to send access logs with Telemetry API."
---
Telemetry API has been in Istio as a first-class API for quite sometime now.
Previously users had to configure telemetry in the `MeshConfig` section of Istio configuration.

---
---
## Before you begin

*   Setup Istio by following the instructions in the [Installation guide](../../../../setup/_index.md).

> **Tip:**
>
> The egress gateway and access logging will be enabled if you install the `demo`
>     [configuration profile](../../../../setup/additional-setup/config-profiles/index.md).

*   Deploy the [curl](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl) sample app to use as a test source for sending requests.
    If you have
    [automatic sidecar injection](../../../../setup/additional-setup/sidecar-injection/index.md#automatic-sidecar-injection)
    enabled, run the following command to deploy the sample app:

```bash
$ kubectl apply -f @samples/curl/curl.yaml@
```

    Otherwise, manually inject the sidecar before deploying the `curl` application with the following command:

```bash
$ kubectl apply -f <(istioctl kube-inject -f @samples/curl/curl.yaml@)
```

> **Tip:**
>
> You can use any pod with `curl` installed as a test source.

*   Set the `SOURCE_POD` environment variable to the name of your source pod:

```bash
$ export SOURCE_POD=$(kubectl get pod -l app=curl -o jsonpath={.items..metadata.name})
```

---
---
*   Start the [httpbin](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/httpbin) sample.

    If you have enabled [automatic sidecar injection](../../../../setup/additional-setup/sidecar-injection/index.md#automatic-sidecar-injection), deploy the `httpbin` service:

```bash
$ kubectl apply -f @samples/httpbin/httpbin.yaml@
```

    Otherwise, you have to manually inject the sidecar before deploying the `httpbin` application:

```bash
$ kubectl apply -f <(istioctl kube-inject -f @samples/httpbin/httpbin.yaml@)
```

## Installation

In this example, we will send logs to [Grafana Loki](https://grafana.com/oss/loki/) so make sure it is installed:

```bash
$ istioctl install -f @samples/open-telemetry/loki/iop.yaml@ --skip-confirmation
$ kubectl apply -f @samples/addons/loki.yaml@ -n istio-system
$ kubectl apply -f @samples/open-telemetry/loki/otel.yaml@ -n istio-system
```

## Get started with Telemetry API

1. Enable access logging

```bash
$ cat <<EOF | kubectl apply -n istio-system -f -
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: mesh-logging-default
spec:
  accessLogging:
  - providers:
    - name: otel
EOF
```

    The above example uses the built-in `envoy` access log provider, and we do not configure anything other than default settings.

1. Disable access log for specific workload

    You can disable access log for `curl` service with the following configuration:

```bash
$ cat <<EOF | kubectl apply -n default -f -
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: disable-curl-logging
  namespace: default
spec:
  selector:
    matchLabels:
      app: curl
  accessLogging:
  - providers:
    - name: otel
    disabled: true
EOF
```

1. Filter access log with workload mode

    You can disable inbound access log for `httpbin` service with the following configuration:

```bash
$ cat <<EOF | kubectl apply -n default -f -
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: disable-httpbin-logging
spec:
  selector:
    matchLabels:
      app: httpbin
  accessLogging:
  - providers:
    - name: otel
    match:
      mode: SERVER
    disabled: true
EOF
```

1. Filter access log with CEL expression

    The following configuration displays access log only when response code is greater or equal to 500:

```bash
$ cat <<EOF | kubectl apply -n default -f -
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: filter-curl-logging
spec:
  selector:
    matchLabels:
      app: curl
  accessLogging:
  - providers:
    - name: otel
    filter:
      expression: response.code >= 500
EOF
```

> **Tip:**
>
> There's no `response.code` attribute when connections fail. In that case, you should use the CEL expression `!has(response.code) || response.code >= 500`.

1. Set default filter access log with CEL expression

    The following configuration displays access logs only when the response code is greater or equal to 400 or the request went to the BlackHoleCluster or the PassthroughCluster:
    Note: The `xds.cluster_name` is only available with Istio release 1.16.2 and higher

```bash
$ cat <<EOF | kubectl apply -f -
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: default-exception-logging
  namespace: istio-system
spec:
  accessLogging:
  - providers:
    - name: otel
    filter:
      expression: "response.code >= 400 || xds.cluster_name == 'BlackHoleCluster' ||  xds.cluster_name == 'PassthroughCluster' "

EOF
```

1. Filter health check access logs with CEL expression

    The following configuration displays access logs only when the logs are not generated by the Amazon Route 53 Health Check Service.
    Note: The `request.useragent` is specific to HTTP traffic, therefore to avoid breaking TCP traffic, we need to check for the existence of the field.
    For more information, see [CEL Type Checking](https://kubernetes.io/docs/reference/using-api/cel/#type-checking)

```bash
$ cat <<EOF | kubectl apply -f -
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: filter-health-check-logging
spec:
  accessLogging:
  - providers:
    - name: otel
    filter:
      expression: "!has(request.useragent) || !(request.useragent.startsWith("Amazon-Route53-Health-Check-Service"))"
EOF
```

    For more information, see [Use expressions for values](../../metrics/customize-metrics/index.md#use-expressions-for-values)

## Work with OpenTelemetry provider

Istio supports sending access logs with [OpenTelemetry](https://opentelemetry.io/) protocol, as explained [here](../otel-provider/index.md).

## Cleanup

1.  Remove all Telemetry API:

```bash
$ kubectl delete telemetry --all -A
```

1.  Remove `loki`:

```bash
$ kubectl delete -f @samples/addons/loki.yaml@ -n istio-system
$ kubectl delete -f @samples/open-telemetry/loki/otel.yaml@ -n istio-system
```

1.  Uninstall Istio from the cluster:

```bash
$ istioctl uninstall --purge --skip-confirmation
```
