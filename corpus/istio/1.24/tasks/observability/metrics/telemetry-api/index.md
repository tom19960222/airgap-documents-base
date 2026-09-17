---
collection: istio
version: "1.24"
title: "Customizing Istio Metrics with Telemetry API"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/telemetry-api/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "This task shows you how to customize the Istio metrics with Telemetry API."
---
Telemetry API has been in Istio as a first-class API for quite sometime now.
Previously, users had to configure metrics in the `telemetry` section of the Istio configuration.

This task shows you how to customize the metrics that Istio generates with Telemetry API.

## Before you begin

[Install Istio](../../../../setup/_index.md) in your cluster and deploy an application.

Telemetry API can not work together with `EnvoyFilter`. For more details please checkout this [issue](https://github.com/istio/istio/issues/39772).

* Starting with Istio version `1.18`, the Prometheus `EnvoyFilter` will not be
  installed by default, and instead `meshConfig.defaultProviders` is used to
  enable it. Telemetry API should be used to further customize the telemetry
  pipeline.

* For versions of Istio before `1.18`, you should install with the following `IstioOperator` configuration:

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  values:
    telemetry:
      enabled: true
      v2:
        enabled: false
```

## Override metrics

The `metrics` section provides values for the metric dimensions as expressions,
and allows you to remove or override the existing metric dimensions.
You can modify the standard metric definitions using `tags_to_remove` or by re-defining a dimension.

1. Remove `grpc_response_status` tags from `REQUEST_COUNT` metric

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: remove-tags
  namespace: istio-system
spec:
  metrics:
    - providers:
        - name: prometheus
      overrides:
        - match:
            mode: CLIENT_AND_SERVER
            metric: REQUEST_COUNT
          tagOverrides:
            grpc_response_status:
              operation: REMOVE
```

1. Add custom tags for `REQUEST_COUNT` metric

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: custom-tags
  namespace: istio-system
spec:
  metrics:
    - overrides:
        - match:
            metric: REQUEST_COUNT
            mode: CLIENT
          tagOverrides:
            destination_x:
              value: upstream_peer.labels['app'].value
        - match:
            metric: REQUEST_COUNT
            mode: SERVER
          tagOverrides:
            source_x:
              value: downstream_peer.labels['app'].value
      providers:
        - name: prometheus
```

## Disable metrics

1. Disable all metrics by following configuration:

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: remove-all-metrics
  namespace: istio-system
spec:
  metrics:
    - providers:
        - name: prometheus
      overrides:
        - disabled: true
          match:
            mode: CLIENT_AND_SERVER
            metric: ALL_METRICS
```

1. Disable `REQUEST_COUNT` metrics by following configuration:

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: remove-request-count
  namespace: istio-system
spec:
  metrics:
    - providers:
        - name: prometheus
      overrides:
        - disabled: true
          match:
            mode: CLIENT_AND_SERVER
            metric: REQUEST_COUNT
```

1. Disable `REQUEST_COUNT` metrics for client by following configuration:

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: remove-client
  namespace: istio-system
spec:
  metrics:
    - providers:
        - name: prometheus
      overrides:
        - disabled: true
          match:
            mode: CLIENT
            metric: REQUEST_COUNT
```

1. Disable `REQUEST_COUNT` metrics for server by following configuration:

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: remove-server
  namespace: istio-system
spec:
  metrics:
    - providers:
        - name: prometheus
      overrides:
        - disabled: true
          match:
            mode: SERVER
            metric: REQUEST_COUNT
```

## Verify the results

Send traffic to the mesh. For the Bookinfo sample, visit `http://$GATEWAY_URL/productpage` in your web
browser or issue the following command:

```bash
$ curl "http://$GATEWAY_URL/productpage"
```

> **Tip:**
>
> `$GATEWAY_URL` is the value set in the [Bookinfo](../../../../examples/bookinfo/index.md) example.

Use the following command to verify that Istio generates the data for your new
or modified dimensions:

```bash
$ istioctl x es "$(kubectl get pod -l app=productpage -o jsonpath='{.items[0].metadata.name}')" -oprom | grep istio_requests_total | grep -v TYPE |grep -v 'reporter="destination"'
```

```bash
$ istioctl x es "$(kubectl get pod -l app=details -o jsonpath='{.items[0].metadata.name}')" -oprom | grep istio_requests_total
```

For example, in the output, locate the metric `istio_requests_total` and
verify it contains your new dimension.

> **Tip:**
>
> It might take a short period of time for the proxies to start applying the config. If the metric is not received,
> you may retry sending requests after a short wait, and look for the metric again.
