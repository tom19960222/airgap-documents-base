---
collection: istio
version: "1.24"
title: "Monitoring with Istio"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/logs-istio/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Monitoring is crucial to support transitioning to the microservices architecture style.

With Istio, you gain monitoring of the traffic between microservices by default.
You can use the Istio Dashboard for monitoring your microservices in real time.

Istio is integrated out-of-the-box with
[Prometheus time series database and monitoring system](https://prometheus.io). Prometheus collects various
traffic-related metrics and provides
[a rich query language](https://prometheus.io/docs/prometheus/latest/querying/basics/) for them.

See below several examples of Prometheus Istio-related queries.

1.  Access the Prometheus UI at [http://my-istio-logs-database.io](http://my-istio-logs-database.io).
(The `my-istio-logs-database.io` URL should be in your /etc/hosts file, you set it
[previously](../bookinfo-kubernetes/index.md#update-your-etc-hosts-configuration-file)).

![Prometheus Query UI](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/logs-istio/prometheus.png)

1.  Run the following example queries in the _Expression_ input box. Push the _Execute_ button to see query results in
the _Console_ tab. The queries use `tutorial` as the name of the application's namespace, substitute it with the name of
your namespace. For best results, run the real-time traffic simulator described in the previous steps when querying data.

    1. Get all the requests in your namespace:

```plain
istio_requests_total{destination_service_namespace="tutorial", reporter="destination"}
```

    1.  Get the sum of all the requests in your namespace:

```plain
sum(istio_requests_total{destination_service_namespace="tutorial", reporter="destination"})
```

    1.  Get the requests to `reviews` microservice:

```plain
istio_requests_total{destination_service_namespace="tutorial", reporter="destination",destination_service_name="reviews"}
```

    1.  [Rate](https://prometheus.io/docs/prometheus/latest/querying/functions/#rate) of requests over the past 5 minutes to all instances of the `reviews` microservice:

```plain
rate(istio_requests_total{destination_service_namespace="tutorial", reporter="destination",destination_service_name="reviews"}[5m])
```

The queries above use the `istio_requests_total` metric, which is a standard Istio metric. You can observe
other metrics, in particular, the ones of Envoy ([Envoy](https://www.envoyproxy.io) is the sidecar proxy of Istio). You
can see the collected metrics in the _insert metric at cursor_ drop-down menu.

## Next steps

Congratulations on completing the tutorial!

These tasks are a great place for beginners to further evaluate Istio's
features using this `demo` installation:

- [Request routing](../../../tasks/traffic-management/request-routing/index.md)
- [Fault injection](../../../tasks/traffic-management/fault-injection/index.md)
- [Traffic shifting](../../../tasks/traffic-management/traffic-shifting/index.md)
- [Querying metrics](../../../tasks/observability/metrics/querying-metrics/index.md)
- [Visualizing metrics](../../../tasks/observability/metrics/using-istio-dashboard/index.md)
- [Accessing external services](../../../tasks/traffic-management/egress/egress-control/index.md)
- [Visualizing your mesh](../../../tasks/observability/kiali/index.md)

Before you customize Istio for production use, see these resources:

- [Deployment models](../../../ops/deployment/deployment-models/index.md)
- [Deployment best practices](../../../ops/best-practices/deployment/index.md)
- [Pod requirements](../../../ops/deployment/application-requirements/index.md)
- [General installation instructions](../../../setup/_index.md)

## Join the Istio community

We welcome you to ask questions and give us feedback by joining the
[Istio community](https://istio.io/v1.24/get-involved/) <!-- unresolved-site-link: route=/get-involved -->.
