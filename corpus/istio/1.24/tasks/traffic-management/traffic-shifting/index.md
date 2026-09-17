---
collection: istio
version: "1.24"
title: "Traffic Shifting"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/traffic-shifting/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows you how to migrate traffic from an old to new version of a service."
---
This task shows you how to shift traffic from one version of a microservice to another.

A common use case is to migrate traffic gradually from an older version of a microservice to a new one.
In Istio, you accomplish this goal by configuring a sequence of routing rules that redirect a percentage of traffic
from one destination to another.

In this task, you will use send 50% of traffic to `reviews:v1` and 50% to `reviews:v3`. Then, you will
complete the migration by sending 100% of traffic to `reviews:v3`.

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

## Apply weight-based routing

> **Warning:**
>
> If you haven't already, follow the instructions in [define the service versions](../../../examples/bookinfo/index.md#define-the-service-versions).

1.  To get started, run this command to route all traffic to the `v1` version:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f @samples/bookinfo/networking/virtual-service-all-v1.yaml@
```

**Tab: Gateway API**

```bash
$ kubectl apply -f @samples/bookinfo/gateway-api/route-reviews-v1.yaml@
```

2)  Open the Bookinfo site in your browser. The URL is `http://$GATEWAY_URL/productpage`, where `$GATEWAY_URL` is the External IP address of the ingress, as explained in
the [Bookinfo](../../../examples/bookinfo/index.md#determine-the-ingress-ip-and-port) doc.

    Notice that the reviews part of the page displays with no rating stars, no
    matter how many times you refresh. This is because you configured Istio to route
    all traffic for the reviews service to the version `reviews:v1` and this
    version of the service does not access the star ratings service.

3)  Transfer 50% of the traffic from `reviews:v1` to `reviews:v3` with the following command:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f @samples/bookinfo/networking/virtual-service-reviews-50-v3.yaml@
```

**Tab: Gateway API**

```bash
$ kubectl apply -f @samples/bookinfo/gateway-api/route-reviews-50-v3.yaml@
```

4) Wait a few seconds for the new rules to propagate and then
confirm the rule was replaced:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl get virtualservice reviews -o yaml
apiVersion: networking.istio.io/v1
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
      weight: 50
    - destination:
        host: reviews
        subset: v3
      weight: 50
```

**Tab: Gateway API**

```bash
$ kubectl get httproute reviews -o yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
...
spec:
  parentRefs:
  - group: ""
    kind: Service
    name: reviews
    port: 9080
  rules:
  - backendRefs:
    - group: ""
      kind: Service
      name: reviews-v1
      port: 9080
      weight: 50
    - group: ""
      kind: Service
      name: reviews-v3
      port: 9080
      weight: 50
    matches:
    - path:
        type: PathPrefix
        value: /
status:
  parents:
  - conditions:
    - lastTransitionTime: "2022-11-10T18:13:43Z"
      message: Route was valid
      observedGeneration: 14
      reason: Accepted
      status: "True"
      type: Accepted
...
```

5)  Refresh the `/productpage` in your browser and you now see *red* colored star ratings approximately 50% of the time. This is because the `v3` version of `reviews` accesses
the star ratings service, but the `v1` version does not.

> **Tip:**
>
> With the current Envoy sidecar implementation, you may need to refresh the
>     `/productpage` many times --perhaps 15 or more--to see the proper distribution.
>     You can modify the rules to route 90% of the traffic to `v3` to see red stars
>     more often.

6)  Assuming you decide that the `reviews:v3` microservice is stable, you can
route 100% of the traffic to `reviews:v3` by applying this virtual service:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f @samples/bookinfo/networking/virtual-service-reviews-v3.yaml@
```

**Tab: Gateway API**

```bash
$ kubectl apply -f @samples/bookinfo/gateway-api/route-reviews-v3.yaml@
```

7) Refresh the `/productpage` several times. Now you will always see book reviews
    with *red* colored star ratings for each review.

## Understanding what happened

In this task you migrated traffic from an old to new version of the `reviews` service using Istio's weighted routing feature. Note that this is very different than doing version migration using the deployment features of container orchestration platforms, which use instance scaling to manage the traffic.

With Istio, you can allow the two versions of the `reviews` service to scale up and down independently, without affecting the traffic distribution between them.

For more information about version routing with autoscaling, check out the blog
article [Canary Deployments using Istio](https://istio.io/v1.24/blog/2017/0.1-canary/) <!-- unresolved-site-link: route=/blog/2017/0.1-canary -->.

## Cleanup

1. Remove the application routing rules:

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
