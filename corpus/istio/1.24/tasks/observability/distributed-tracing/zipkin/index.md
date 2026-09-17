---
collection: istio
version: "1.24"
title: "Zipkin"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/distributed-tracing/zipkin/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Learn how to configure the proxies to send tracing requests to Zipkin."
---
After completing this task, you understand how to have your application participate in tracing with [Zipkin](https://zipkin.io/),
regardless of the language, framework, or platform you use to build your application.

This task uses the [Bookinfo](../../../../examples/bookinfo/index.md) sample as the example application.

To learn how Istio handles tracing, visit this task's [overview](../overview/index.md).

## Before you begin

1.  Follow the [Zipkin installation](../../../../ops/integrations/zipkin/index.md#installation) documentation to deploy Zipkin into your cluster.

1.  Deploy the [Bookinfo](../../../../examples/bookinfo/index.md#deploying-the-application) sample application.

## Configure Istio for distributed tracing

### Configure an extension provider

Install Istio with an [extension provider](https://istio.io/v1.24/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider) <!-- unresolved-site-link: route=/docs/reference/config/istio.mesh.v1alpha1 --> referring to the Zipkin service:

```bash
$ cat <<EOF > ./tracing.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    enableTracing: true
    defaultConfig:
      tracing: {} # disable legacy MeshConfig tracing options
    extensionProviders:
    - name: zipkin
      zipkin:
        service: zipkin.istio-system.svc.cluster.local
        port: 9411
EOF
$ istioctl install -f ./tracing.yaml --skip-confirmation
```

### Enable tracing

Enable tracing by applying the following configuration:

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
    - name: zipkin
EOF
```

## Accessing the dashboard

The [Remotely Accessing Telemetry Addons task](../../gateways/index.md) details how to configure access to the Istio addons through a gateway.

For testing (and temporary access), you may also use port-forwarding. Use the following, assuming you've deployed Zipkin to the `istio-system` namespace:

```bash
$ istioctl dashboard zipkin
```

## Generating traces using the Bookinfo sample

1.  When the Bookinfo application is up and running, access `http://$GATEWAY_URL/productpage` one or more times
    to generate trace information.

---
---
To see trace data, you must send requests to your service. The number of requests depends on Istio's sampling rate and can be configured using the [Telemetry API](../../telemetry/index.md). With the default sampling rate of 1%, you need to send at least 100 requests before the first trace is visible.
To send 100 requests to the `productpage` service, use the following command:

```bash
$ for i in $(seq 1 100); do curl -s -o /dev/null "http://$GATEWAY_URL/productpage"; done
```

1.  From the search panel, click on the plus sign. Select `serviceName` from the first drop-down list, `productpage.default` from second drop-down, and then click the search icon:

![Tracing Dashboard](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/distributed-tracing/zipkin/istio-tracing-list-zipkin.png)

1.  Click on the `ISTIO-INGRESSGATEWAY` search result to see the details corresponding to the
    latest request to `/productpage`:

![Detailed Trace View](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/observability/distributed-tracing/zipkin/istio-tracing-details-zipkin.png)

1.  The trace is comprised of a set of spans,
    where each span corresponds to a Bookinfo service, invoked during the execution of a `/productpage` request, or
    internal Istio component, for example: `istio-ingressgateway`.

## Cleanup

1.  Remove any `istioctl` processes that may still be running using control-C or:

```bash
$ killall istioctl
```

1.  If you are not planning to explore any follow-on tasks, refer to the
    [Bookinfo cleanup](../../../../examples/bookinfo/index.md#cleanup) instructions
    to shutdown the application.
