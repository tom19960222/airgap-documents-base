---
collection: istio
version: "1.24"
title: "Querying Metrics from Prometheus"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/querying-metrics/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "This task shows you how to query for Istio Metrics using Prometheus."
---
This task shows you how to query for Istio Metrics using Prometheus. As part of
this task, you will use the web-based interface for querying metric values.

The [Bookinfo](../../../../examples/bookinfo/index.md) sample application is used as
the example application throughout this task.

## Before you begin

* [Install Istio](../../../../setup/_index.md) in your cluster.
* Install the [Prometheus Addon](../../../../ops/integrations/prometheus/index.md#option-1-quick-start).
* Deploy the [Bookinfo](../../../../examples/bookinfo/index.md) application.

## Querying Istio metrics

1.  Verify that the `prometheus` service is running in your cluster.

    In Kubernetes environments, execute the following command:

```bash
$ kubectl -n istio-system get svc prometheus
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
prometheus   ClusterIP   10.109.160.254   <none>        9090/TCP   4m
```

1.  Send traffic to the mesh.

    For the Bookinfo sample, visit `http://$GATEWAY_URL/productpage` in your web
    browser or issue the following command:

```bash
$ curl "http://$GATEWAY_URL/productpage"
```

> **Tip:**
>
> `$GATEWAY_URL` is the value set in the [Bookinfo](../../../../examples/bookinfo/index.md) example.

1.  Open the Prometheus UI.

    In Kubernetes environments, execute the following command:

```bash
$ istioctl dashboard prometheus
```

    Click **Graph** to the right of Prometheus in the header.

1.  Execute a Prometheus query.

    In the "Expression" input box at the top of the web page, enter the text:

```plain
istio_requests_total
```

    Then, click the **Execute** button.

The results will be similar to:

![Prometheus Query Result](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/querying-metrics/prometheus_query_result.png)

You can also see the query results graphically by selecting the Graph tab underneath the **Execute** button.

![Prometheus Query Result - Graphical](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/querying-metrics/prometheus_query_result_graphical.png)

Other queries to try:

*   Total count of all requests to the `productpage` service:

```plain
istio_requests_total{destination_service="productpage.default.svc.cluster.local"}
```

*   Total count of all requests to `v3` of the `reviews` service:

```plain
istio_requests_total{destination_service="reviews.default.svc.cluster.local", destination_version="v3"}
```

    This query returns the current total count of all requests to the v3 of the `reviews` service.

*   Rate of requests over the past 5 minutes to all instances of the `productpage` service:

```plain
rate(istio_requests_total{destination_service=~"productpage.*", response_code="200"}[5m])
```

### About the Prometheus addon

The Prometheus addon is a Prometheus server that comes preconfigured to scrape
Istio endpoints to collect metrics. It provides a mechanism for persistent storage and querying
of Istio metrics.

For more on querying Prometheus, please read their [querying
docs](https://prometheus.io/docs/querying/basics/).

## Cleanup

*   Remove any `istioctl` processes that may still be running using control-C or:

```bash
$ killall istioctl
```

*   If you are not planning to explore any follow-on tasks, refer to the
    [Bookinfo cleanup](../../../../examples/bookinfo/index.md#cleanup) instructions
    to shutdown the application.
