---
collection: istio
version: "1.24"
title: "Customizing Istio Metrics"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/customize-metrics/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "This task shows you how to customize the Istio metrics."
---
This task shows you how to customize the metrics that Istio generates.

Istio generates telemetry that various dashboards consume to help you visualize
your mesh. For example, dashboards that support Istio include:

* [Grafana](../using-istio-dashboard/index.md)
* [Kiali](../../kiali/index.md)
* [Prometheus](../querying-metrics/index.md)

By default, Istio defines and generates a set of standard metrics (e.g.
`requests_total`), but you can also customize them and create new metrics
using the [Telemetry API](../../telemetry/index.md).

## Before you begin

[Install Istio](../../../../setup/_index.md) in your cluster and deploy an application.
Alternatively, you can set up custom statistics as part of the Istio
installation.

The [Bookinfo](../../../../examples/bookinfo/index.md) sample application is used as
the example application throughout this task. For installation instructions, see [deploying the Bookinfo application](../../../../examples/bookinfo/index.md#deploying-the-application).

## Enable custom metrics

To customize telemetry metrics, for example, to add `request_host`
and `destination_port` dimensions to the `requests_total` metric emitted by both
gateways and sidecars in the inbound and outbound direction, use the following:

```bash
$ cat <<EOF > ./custom_metrics.yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: namespace-metrics
spec:
  metrics:
  - providers:
    - name: prometheus
    overrides:
    - match:
        metric: REQUEST_COUNT
      tagOverrides:
        destination_port:
          value: "string(destination.port)"
        request_host:
          value: "request.host"
EOF
$ kubectl apply -f custom_metrics.yaml
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
$ kubectl exec "$(kubectl get pod -l app=productpage -o jsonpath='{.items[0].metadata.name}')" -c istio-proxy -- curl -sS 'localhost:15000/stats/prometheus' | grep istio_requests_total
```

For example, in the output, locate the metric `istio_requests_total` and
verify it contains your new dimension.

> **Tip:**
>
> It might take a short period of time for the proxies to start applying the config. If the metric is not received,
> you may retry sending requests after a short wait, and look for the metric again.

## Use expressions for values

The values in the metric configuration are common expressions, which means you
must double-quote strings in JSON, e.g. "'string value'". Unlike Mixer
expression language, there is no support for the pipe (`|`) operator, but you
can emulate it with the `has` or `in` operator, for example:

```plain
has(request.host) ? request.host : "unknown"
```

For more information, see [Common Expression Language](https://opensource.google/projects/cel).

Istio exposes all standard [Envoy attributes](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/advanced/attributes).
Peer metadata is available as attributes `upstream_peer` for outbound and `downstream_peer` for inbound with the following fields:

| Field       | Type     | Value                                                      |
|-------------|----------|------------------------------------------------------------|
| `app`       | `string` | Application name.                                          |
| `version`   | `string` | Application version.                                       |
| `service`   | `string` | Service instance.                                          |
| `revision`  | `string` | Service version.                                           |
| `name`      | `string` | Name of the pod.                                           |
| `namespace` | `string` | Namespace that the pod runs in.                            |
| `type`      | `string` | Workload type.                                             |
| `workload`  | `string` | Workload name.                                             |
| `cluster`   | `string` | Identifier for the cluster to which this workload belongs. |

For example, the expression for the peer `app` label to be used in an outbound configuration is
`filter_state.downstream_peer.app` or `filter_state.upstream_peer.app`.

## Cleanup

To delete the `Bookinfo` sample application and its configuration, see
[`Bookinfo` cleanup](../../../../examples/bookinfo/index.md#cleanup).
