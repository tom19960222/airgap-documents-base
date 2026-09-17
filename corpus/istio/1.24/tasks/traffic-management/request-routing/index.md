---
collection: istio
version: "1.24"
title: "Request Routing"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/request-routing/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "This task shows you how to configure dynamic request routing to multiple versions of a microservice."
---
This task shows you how to route requests dynamically to multiple versions of a
microservice.

---
---

> **Tip:**
>
> ---
> ---
> Istio supports the Kubernetes [Gateway API](https://istio.io/v1.24/blog/2024/gateway-mesh-ga/) <!-- unresolved-site-link: route=/blog/2024/gateway-mesh-ga --> and intends to make it the default API for traffic management in the future.
>
>
>
>
> ---
> ---
> The following instructions allow you to choose to use either the Gateway API or the Istio configuration API when configuring
> traffic management in the mesh. Follow instructions under either the `Gateway API` or `Istio APIs` tab,
> according to your preference.
>
>
>
>
>
> ---
> ---
> Note that the Kubernetes Gateway API CRDs do not come installed by default on most Kubernetes clusters, so make sure they are
> installed before using the Gateway API:
>
>
>
> ```bash
> $ kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
>   { kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/[k8s_gateway_api_version]/standard-install.yaml; }
> ```

## Before you begin

* Setup Istio by following the instructions in the
  [Installation guide](../../../setup/_index.md).

* Deploy the [Bookinfo](../../../examples/bookinfo/index.md) sample application.

* Review the [Traffic Management](../../../concepts/traffic-management/index.md) concepts doc.

## About this task

The Istio [Bookinfo](../../../examples/bookinfo/index.md) sample consists of four separate microservices, each with multiple versions.
Three different versions of one of the microservices, `reviews`, have been deployed and are running concurrently.
To illustrate the problem this causes, access the Bookinfo app's `/productpage` in a browser and refresh several times.
The URL is `http://$GATEWAY_URL/productpage`, where `$GATEWAY_URL` is the External IP address of the ingress, as explained in
the [Bookinfo](../../../examples/bookinfo/index.md#determine-the-ingress-ip-and-port) doc.

You’ll notice that sometimes the book review output contains star ratings and other times it does not.
This is because without an explicit default service version to route to, Istio routes requests to all available versions
in a round robin fashion.

The initial goal of this task is to apply rules that route all traffic to `v1` (version 1) of the microservices. Later, you
will apply a rule to route traffic based on the value of an HTTP request header.

## Route to version 1

To route to one version only, you configure route rules that send traffic to default versions for the microservices.

> **Warning:**
>
> If you haven't already, follow the instructions in [define the service versions](../../../examples/bookinfo/index.md#define-the-service-versions).

1. Run the following command to create the route rules:

**Tabset (config-api):**

**Tab: Istio APIs**

Istio uses virtual services to define route rules.
Run the following command to apply virtual services that will route all traffic to `v1` of each microservice:

```bash
$ kubectl apply -f @samples/bookinfo/networking/virtual-service-all-v1.yaml@
```

Because configuration propagation is eventually consistent, wait a few seconds
for the virtual services to take effect.

**Tab: Gateway API**

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: reviews
spec:
  parentRefs:
  - group: ""
    kind: Service
    name: reviews
    port: 9080
  rules:
  - backendRefs:
    - name: reviews-v1
      port: 9080
EOF
```

2) Display the defined routes with the following command:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl get virtualservices -o yaml
- apiVersion: networking.istio.io/v1
  kind: VirtualService
  ...
  spec:
    hosts:
    - details
    http:
    - route:
      - destination:
          host: details
          subset: v1
- apiVersion: networking.istio.io/v1
  kind: VirtualService
  ...
  spec:
    hosts:
    - productpage
    http:
    - route:
      - destination:
          host: productpage
          subset: v1
- apiVersion: networking.istio.io/v1
  kind: VirtualService
  ...
  spec:
    hosts:
    - ratings
    http:
    - route:
      - destination:
          host: ratings
          subset: v1
- apiVersion: networking.istio.io/v1
  kind: VirtualService
  ...
  spec:
    hosts:
    - reviews
    http:
    - route:
      - destination:
          host: reviews
          subset: v1
```

You can also display the corresponding `subset` definitions with the following command:

```bash
$ kubectl get destinationrules -o yaml
```

**Tab: Gateway API**

```bash
$ kubectl get httproute reviews -o yaml
...
spec:
  parentRefs:
  - group: gateway.networking.k8s.io
    kind: Service
    name: reviews
    port: 9080
  rules:
  - backendRefs:
    - group: ""
      kind: Service
      name: reviews-v1
      port: 9080
      weight: 1
    matches:
    - path:
        type: PathPrefix
        value: /
status:
  parents:
  - conditions:
    - lastTransitionTime: "2022-11-08T19:56:19Z"
      message: Route was valid
      observedGeneration: 8
      reason: Accepted
      status: "True"
      type: Accepted
    - lastTransitionTime: "2022-11-08T19:56:19Z"
      message: All references resolved
      observedGeneration: 8
      reason: ResolvedRefs
      status: "True"
      type: ResolvedRefs
    controllerName: istio.io/gateway-controller
    parentRef:
      group: gateway.networking.k8s.io
      kind: Service
      name: reviews
      port: 9080
```

In the resource status, make sure that the `Accepted` condition is `True` for the `reviews` parent.

You have configured Istio to route to the `v1` version of the Bookinfo microservices,
most importantly the `reviews` service version 1.

## Test the new routing configuration

You can easily test the new configuration by once again refreshing the `/productpage`
of the Bookinfo app in your browser.
Notice that the reviews part of the page displays with no rating stars, no
matter how many times you refresh. This is because you configured Istio to route
all traffic for the reviews service to the version `reviews:v1` and this
version of the service does not access the star ratings service.

You have successfully accomplished the first part of this task: route traffic to one
version of a service.

## Route based on user identity

Next, you will change the route configuration so that all traffic from a specific user
is routed to a specific service version. In this case, all traffic from a user
named Jason will be routed to the service `reviews:v2`.

This example is enabled by the fact that the `productpage` service
adds a custom `end-user` header to all outbound HTTP requests to the reviews
service.

Istio also supports routing based on strongly authenticated JWT on ingress gateway, refer to the
[JWT claim based routing](../../security/authentication/jwt-route/index.md) for more details.

Remember, `reviews:v2` is the version that includes the star ratings feature.

1. Run the following command to enable user-based routing:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f @samples/bookinfo/networking/virtual-service-reviews-test-v2.yaml@
```

You can confirm the rule is created using the following command:

```bash
$ kubectl get virtualservice reviews -o yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
...
spec:
  hosts:
  - reviews
  http:
  - match:
    - headers:
        end-user:
          exact: jason
    route:
    - destination:
        host: reviews
        subset: v2
  - route:
    - destination:
        host: reviews
        subset: v1
```

**Tab: Gateway API**

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: reviews
spec:
  parentRefs:
  - group: ""
    kind: Service
    name: reviews
    port: 9080
  rules:
  - matches:
    - headers:
      - name: end-user
        value: jason
    backendRefs:
    - name: reviews-v2
      port: 9080
  - backendRefs:
    - name: reviews-v1
      port: 9080
EOF
```

2) On the `/productpage` of the Bookinfo app, log in as user `jason`.

    Refresh the browser. What do you see? The star ratings appear next to each
    review.

3) Log in as another user (pick any name you wish).

    Refresh the browser. Now the stars are gone. This is because traffic is routed
    to `reviews:v1` for all users except Jason.

You have successfully configured Istio to route traffic based on user identity.

## Understanding what happened

In this task, you used Istio to send 100% of the traffic to the `v1` version
of each of the Bookinfo services. You then set a rule to selectively send traffic
to version `v2` of the `reviews` service based on a custom `end-user` header added
to the request by the `productpage` service.

Note that Kubernetes services, like the Bookinfo ones used in this task, must
adhere to certain restrictions to take advantage of Istio's L7 routing features.
Refer to the [Requirements for Pods and Services](../../../ops/deployment/application-requirements/index.md) for details.

In the [traffic shifting](../traffic-shifting/index.md) task, you
will follow the same basic pattern you learned here to configure route rules to
gradually send traffic from one version of a service to another.

## Cleanup

1. Remove the application route rules:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl delete -f @samples/bookinfo/networking/virtual-service-all-v1.yaml@
```

**Tab: Gateway API**

```bash
$ kubectl delete httproute reviews
```

2) If you are not planning to explore any follow-on tasks, refer to the
  [Bookinfo cleanup](../../../examples/bookinfo/index.md#cleanup) instructions
  to shutdown the application.
