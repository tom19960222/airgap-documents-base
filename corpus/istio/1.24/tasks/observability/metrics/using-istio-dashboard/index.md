---
collection: istio
version: "1.24"
title: "Visualizing Metrics with Grafana"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/using-istio-dashboard/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "This task shows you how to set up and use the Istio Dashboard to monitor mesh traffic."
---
This task shows you how to set up and use the Istio Dashboard to monitor mesh
traffic. As part of this task, you will use the Grafana Istio addon and
the web-based interface for viewing service mesh traffic data.

The [Bookinfo](../../../../examples/bookinfo/index.md) sample application is used as
the example application throughout this task.

## Before you begin

* [Install Istio](../../../../setup/_index.md) in your cluster.
* Install the [Grafana Addon](../../../../ops/integrations/grafana/index.md#option-1-quick-start).
* Install the [Prometheus Addon](../../../../ops/integrations/prometheus/index.md#option-1-quick-start).
* Deploy the [Bookinfo](../../../../examples/bookinfo/index.md) application.

## Viewing the Istio dashboard

1.  Verify that the `prometheus` service is running in your cluster.

    In Kubernetes environments, execute the following command:

```bash
$ kubectl -n istio-system get svc prometheus
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
prometheus   ClusterIP   10.100.250.202   <none>        9090/TCP   103s
```

1.  Verify that the Grafana service is running in your cluster.

    In Kubernetes environments, execute the following command:

```bash
$ kubectl -n istio-system get svc grafana
NAME      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
grafana   ClusterIP   10.103.244.103   <none>        3000/TCP   2m25s
```

1.  Open the Istio Dashboard via the Grafana UI.

    In Kubernetes environments, execute the following command:

```bash
$ istioctl dashboard grafana
```

    Visit [http://localhost:3000/d/G8wLrJIZk/istio-mesh-dashboard](http://localhost:3000/d/G8wLrJIZk/istio-mesh-dashboard) in your web browser.

    The Istio Dashboard will look similar to:

![Istio Dashboard](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/using-istio-dashboard/grafana-istio-dashboard.png)

1.  Send traffic to the mesh.

    For the Bookinfo sample, visit `http://$GATEWAY_URL/productpage` in your web
    browser or issue the following command:

---
---
To see trace data, you must send requests to your service. The number of requests depends on Istio's sampling rate and can be configured using the [Telemetry API](../../telemetry/index.md). With the default sampling rate of 1%, you need to send at least 100 requests before the first trace is visible.
To send 100 requests to the `productpage` service, use the following command:

```bash
$ for i in $(seq 1 100); do curl -s -o /dev/null "http://$GATEWAY_URL/productpage"; done
```

> **Tip:**
>
> `$GATEWAY_URL` is the value set in the [Bookinfo](../../../../examples/bookinfo/index.md) example.

    Refresh the page a few times (or send the command a few times) to generate a
    small amount of traffic.

    Look at the Istio Dashboard again. It should reflect the traffic that was
    generated. It will look similar to:

![Istio Dashboard With Traffic](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/using-istio-dashboard/dashboard-with-traffic.png)

    This gives the global view of the Mesh along with services and workloads in the mesh.
    You can get more details about services and workloads by navigating to their specific dashboards as explained below.

1.  Visualize Service Dashboards.

    From the Grafana dashboard's left hand corner navigation menu, you can navigate to Istio Service Dashboard or visit
    [http://localhost:3000/d/LJ_uJAvmk/istio-service-dashboard](http://localhost:3000/d/LJ_uJAvmk/istio-service-dashboard) in your web browser.

> **Tip:**
>
> You may need to select a service in the Service dropdown.

    The Istio Service Dashboard will look similar to:

![Istio Service Dashboard](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/using-istio-dashboard/istio-service-dashboard.png)

    This gives details about metrics for the service and then client workloads (workloads that are calling this service)
    and service workloads (workloads that are providing this service) for that service.

1.  Visualize Workload Dashboards.

    From the Grafana dashboard's left hand corner navigation menu, you can navigate to Istio Workload Dashboard or visit
    [http://localhost:3000/d/UbsSZTDik/istio-workload-dashboard](http://localhost:3000/d/UbsSZTDik/istio-workload-dashboard) in your web browser.

    The Istio Workload Dashboard will look similar to:

![Istio Workload Dashboard](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/metrics/using-istio-dashboard/istio-workload-dashboard.png)

    This gives details about metrics for each workload and then inbound workloads (workloads that are sending request to
    this workload) and outbound services (services to which this workload send requests) for that workload.

### About the Grafana dashboards

The Istio Dashboard consists of three main sections:

1. A Mesh Summary View. This section provides Global Summary view of the Mesh and shows HTTP/gRPC and TCP
   workloads in the Mesh.

1. Individual Services View. This section provides metrics about requests and
   responses for each individual service within the mesh (HTTP/gRPC and TCP).
   This also provides metrics about client and service workloads for this service.

1. Individual Workloads View: This section provides metrics about requests and
   responses for each individual workload within the mesh (HTTP/gRPC and TCP).
   This also provides metrics about inbound workloads and outbound services for this workload.

For more on how to create, configure, and edit dashboards, please see the
[Grafana documentation](https://docs.grafana.org/).

## Cleanup

*   Remove any `kubectl port-forward` processes that may be running:

```bash
$ killall kubectl
```

* If you are not planning to explore any follow-on tasks, refer to the
[Bookinfo cleanup](../../../../examples/bookinfo/index.md#cleanup) instructions
to shutdown the application.
