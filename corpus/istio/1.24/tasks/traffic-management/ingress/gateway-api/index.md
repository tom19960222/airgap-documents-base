---
collection: istio
version: "1.24"
title: "Kubernetes Gateway API"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/ingress/gateway-api/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes how to configure the Kubernetes Gateway API with Istio."
---
In addition to its own traffic management API,

---
---
Istio supports the Kubernetes [Gateway API](https://istio.io/v1.24/blog/2024/gateway-mesh-ga/) <!-- unresolved-site-link: route=/blog/2024/gateway-mesh-ga --> and intends to make it the default API for traffic management in the future.

This document describes the differences between the Istio and Kubernetes APIs and provides a simple example
that shows you how to configure Istio to expose a service outside the service mesh cluster using the Gateway API.
Note that these APIs are an actively developed evolution of the Kubernetes [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
and [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) APIs.

> **Tip:**
>
> Many of the Istio traffic management documents include instructions for using either the Istio or Kubernetes API
> (see the [control ingress traffic task](../ingress-control/index.md), for example).
> You can use the Gateway API, right from the start, by following the [getting started instructions](../../../../setup/getting-started/index.md).

## Setup

1. The Gateway APIs do not come installed by default on most Kubernetes clusters. Install the Gateway API CRDs if they are not present:

```bash
$ kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=[k8s_gateway_api_version]" | kubectl apply -f -; }
```

1. Install Istio using the `minimal` profile:

```bash
$ istioctl install --set profile=minimal -y
```

## Differences from Istio APIs

The Gateway APIs share a lot of similarities to the Istio APIs such as Gateway and VirtualService.
The main resource shares the same name, `Gateway`, and the resources serve similar goals.

The new Gateway APIs aim to take the learnings from various Kubernetes ingress implementations, including Istio,
to build a standardized vendor neutral API. These APIs generally serve the same purposes as Istio Gateway and VirtualService,
with a few key differences:

* In Istio APIs, a `Gateway` *configures* an existing gateway Deployment/Service that has [been deployed](../../../../setup/additional-setup/gateway/index.md).
  In the Gateway APIs, the `Gateway` resource both *configures and deploys* a gateway.
  See [Deployment Methods](#deployment-methods) for more information.
* In the Istio `VirtualService`, all protocols are configured within a single resource.
  In the Gateway APIs, each protocol type has its own resource, such as `HTTPRoute` and `TCPRoute`.
* While the Gateway APIs offer a lot of rich routing functionality, it does not yet cover 100% of Istio's feature set.
  Work is ongoing to extend the API to cover these use cases, as well as utilizing the APIs [extensibility](https://gateway-api.sigs.k8s.io/#gateway-api-concepts)
  to better expose Istio functionality.

## Configuring a Gateway

See the [Gateway API](https://gateway-api.sigs.k8s.io/) documentation for information about the APIs.

In this example, we will deploy a simple application and expose it externally using a `Gateway`.

1. First, deploy the `httpbin` test application:

```bash
$ kubectl apply -f @samples/httpbin/httpbin.yaml@
```

1. Deploy the Gateway API configuration including a single exposed route (i.e., `/get`):

```bash
$ kubectl create namespace istio-ingress
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: gateway
  namespace: istio-ingress
spec:
  gatewayClassName: istio
  listeners:
  - name: default
    hostname: "*.example.com"
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: All
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http
  namespace: default
spec:
  parentRefs:
  - name: gateway
    namespace: istio-ingress
  hostnames: ["httpbin.example.com"]
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /get
    backendRefs:
    - name: httpbin
      port: 8000
EOF
```

1.  Set the Ingress Host environment variable:

```bash
$ kubectl wait -n istio-ingress --for=condition=programmed gateways.gateway.networking.k8s.io gateway
$ export INGRESS_HOST=$(kubectl get gateways.gateway.networking.k8s.io gateway -n istio-ingress -ojsonpath='{.status.addresses[0].value}')
```

1.  Access the `httpbin` service using _curl_:

```bash
$ curl -s -I -HHost:httpbin.example.com "http://$INGRESS_HOST/get"
...
HTTP/1.1 200 OK
...
server: istio-envoy
...
```

    Note the use of the `-H` flag to set the _Host_ HTTP header to
    "httpbin.example.com". This is needed because the `HTTPRoute` is configured to handle "httpbin.example.com",
    but in your test environment you have no DNS binding for that host and are simply sending your request to the ingress IP.

1.  Access any other URL that has not been explicitly exposed. You should see an HTTP 404 error:

```bash
$ curl -s -I -HHost:httpbin.example.com "http://$INGRESS_HOST/headers"
HTTP/1.1 404 Not Found
...
```

1.  Update the route rule to also expose `/headers` and to add a header to the request:

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http
  namespace: default
spec:
  parentRefs:
  - name: gateway
    namespace: istio-ingress
  hostnames: ["httpbin.example.com"]
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /get
    - path:
        type: PathPrefix
        value: /headers
    filters:
    - type: RequestHeaderModifier
      requestHeaderModifier:
        add:
        - name: my-added-header
          value: added-value
    backendRefs:
    - name: httpbin
      port: 8000
EOF
```

1.  Access `/headers` again and notice header `My-Added-Header` has been added to the request:

```bash
$ curl -s -HHost:httpbin.example.com "http://$INGRESS_HOST/headers" | jq '.headers["My-Added-Header"][0]'
...
"added-value"
...
```

## Deployment methods

In the example above, you did not need to install an ingress gateway `Deployment` prior to configuring a Gateway.
In the default configuration, a gateway `Deployment` and `Service` is automatically provisioned based on the `Gateway` configuration.
For advanced use cases, manual deployment is still allowed.

### Automated Deployment

By default, each `Gateway` will automatically provision a `Service` and `Deployment` of the same name.
These configurations will be updated automatically if the `Gateway` changes (for example, if a new port is added).

These resources can be customized in a few ways:

* Annotations and labels on the `Gateway` will be copied to the `Service` and `Deployment`.
  This allows configuring things such as [Internal load balancers](https://kubernetes.io/docs/concepts/services-networking/service/#internal-load-balancer) that read from these fields.
* Istio offers an additional annotation to configure the generated resources:

    |Annotation|Purpose|
    |----------|-------|
    |`networking.istio.io/service-type`|Controls the `Service.spec.type` field. For example, set to `ClusterIP` to not expose the service externally. The default is `LoadBalancer`.|

* The `Service.spec.loadBalancerIP` field can be explicit set by configuring the `addresses` field:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: gateway
spec:
  addresses:
  - value: 192.0.2.0
    type: IPAddress
...
```

Note: only one address may be specified.

* (Advanced) The generated Pod configuration can be configured by [Custom Injection Templates](../../../../setup/additional-setup/sidecar-injection/index.md#custom-templates-experimental).

#### Resource Attachment and Scaling

Resources can be *attached* to a `Gateway` to customize it.
However, most Kubernetes resources do not currently support attaching directly to a `Gateway`, but they can be attached to the corresponding generated `Deployment` and `Service` instead.
This is easily done because [the resources are generated with well-known labels](https://gateway-api.sigs.k8s.io/geps/gep-1762/#resource-attachment) (`gateway.networking.k8s.io/gateway-name: <gateway name>`) and names:

* Gateway: `<gateway name>-<gateway class name>`
* Waypoint: `<gateway name>`

For example, to deploy a `Gateway` with a `HorizontalPodAutoscaler` and `PodDisruptionBudget`:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: gateway
spec:
  gatewayClassName: istio
  listeners:
  - name: default
    hostname: "*.example.com"
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: All
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: gateway
spec:
  # Match the generated Deployment by reference
  # Note: Do not use `kind: Gateway`.
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: gateway-istio
  minReplicas: 2
  maxReplicas: 5
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: gateway
spec:
  minAvailable: 1
  selector:
    # Match the generated Deployment by label
    matchLabels:
      gateway.networking.k8s.io/gateway-name: gateway
```

### Manual Deployment

If you do not want to have an automated deployment, a `Deployment` and `Service` can be [configured manually](../../../../setup/additional-setup/gateway/index.md).

When this option is done, you will need to manually link the `Gateway` to the `Service`, as well as keep their port configuration in sync.

In order to support Policy Attachment, e.g. when you're using the [`targetRef`](https://istio.io/v1.24/docs/reference/config/type/workload-selector/#PolicyTargetReference) <!-- unresolved-site-link: route=/docs/reference/config/type/workload-selector --> field on an AuthorizationPolicy, you will also need to reference the name of your `Gateway` by adding the following label to your gateway pod: `gateway.networking.k8s.io/gateway-name: <gateway name>`.

To link a `Gateway` to a `Service`, configure the `addresses` field to point to a **single** `Hostname`.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: gateway
spec:
  addresses:
  - value: ingress.istio-gateways.svc.cluster.local
    type: Hostname
...
```

## Mesh Traffic

The Gateway API can also be used to configure mesh traffic.
This is done by configuring the `parentRef` to point to a service, instead of a gateway.

For example, to add a header on all calls to an in-cluster `Service` named `example`:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: mesh
spec:
  parentRefs:
  - group: ""
    kind: Service
    name: example
  rules:
  - filters:
    - type: RequestHeaderModifier
      requestHeaderModifier:
        add:
        - name: my-added-header
          value: added-value
    backendRefs:
    - name: example
      port: 80
```

More details and examples can be found in other [traffic management tasks](../../_index.md).

## Cleanup

1. Remove the `httpbin` sample and gateway:

```bash
$ kubectl delete -f @samples/httpbin/httpbin.yaml@
$ kubectl delete httproute http
$ kubectl delete gateways.gateway.networking.k8s.io gateway -n istio-ingress
$ kubectl delete ns istio-ingress
```

1. Uninstall Istio:

```bash
$ istioctl uninstall -y --purge
$ kubectl delete ns istio-system
```

1. Remove the Gateway API CRDs if they are no longer needed:

```bash
$ kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=[k8s_gateway_api_version]" | kubectl delete -f -
```
