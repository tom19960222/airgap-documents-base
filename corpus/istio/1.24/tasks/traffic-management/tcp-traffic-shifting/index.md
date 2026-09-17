---
collection: istio
version: "1.24"
title: "TCP Traffic Shifting"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/tcp-traffic-shifting/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows you how to migrate TCP traffic from an old to new version of a TCP service."
---
This task shows you how to shift TCP traffic from one version of a microservice to another.

A common use case is to migrate TCP traffic gradually from an older version of a microservice to a new one.
In Istio, you accomplish this goal by configuring a sequence of routing rules that redirect a percentage of TCP traffic
from one destination to another.

In this task, you will send 100% of the TCP traffic to `tcp-echo:v1`.
Then, you will route 20% of the TCP traffic to `tcp-echo:v2` using Istio's
weighted routing feature.

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

> **Warning:**
>
> This document configures Istio using Gateway API features that are
> [experimental](https://gateway-api.sigs.k8s.io/geps/overview/#status)
> Before using the Gateway API instructions, make sure to:
>
> 1) Install the **experimental version** of the Gateway API CRDs:
>
>
>
> ```bash
> $ kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd/experimental?ref=[k8s_gateway_api_version]" | kubectl apply -f -
> ```
>
>
>
> 2) Configure Istio to read the alpha Gateway API resources by setting the `PILOT_ENABLE_ALPHA_GATEWAY_API` environment
>     variable to `true` when installing Istio:
>
>
>
> ```bash
> $ istioctl install --set values.pilot.env.PILOT_ENABLE_ALPHA_GATEWAY_API=true --set profile=minimal -y
> ```

## Before you begin

* Setup Istio by following the instructions in the [Installation guide](../../../setup/_index.md).

* Review the [Traffic Management](../../../concepts/traffic-management/index.md) concepts doc.

## Set up the test environment

1.  To get started, create a namespace for testing TCP traffic shifting.

```bash
$ kubectl create namespace istio-io-tcp-traffic-shifting
```

1.  Deploy the [curl](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl) sample app to use as a test source for sending requests.

```bash
$ kubectl apply -f @samples/curl/curl.yaml@ -n istio-io-tcp-traffic-shifting
```

1.  Deploy the `v1` and `v2` versions of the `tcp-echo` microservice.

```bash
$ kubectl apply -f @samples/tcp-echo/tcp-echo-services.yaml@ -n istio-io-tcp-traffic-shifting
```

## Apply weight-based TCP routing

1.  Route all TCP traffic to the `v1` version of the `tcp-echo` microservice.

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f @samples/tcp-echo/tcp-echo-all-v1.yaml@ -n istio-io-tcp-traffic-shifting
```

**Tab: Gateway API**

```bash
$ kubectl apply -f @samples/tcp-echo/gateway-api/tcp-echo-all-v1.yaml@ -n istio-io-tcp-traffic-shifting
```

2)  Determine the ingress IP and port:

**Tabset (config-api):**

**Tab: Istio APIs**

Follow the instructions in
[Determining the ingress IP and ports](../ingress/ingress-control/index.md#determining-the-ingress-ip-and-ports)
to set the `TCP_INGRESS_PORT` and `INGRESS_HOST` environment variables.

**Tab: Gateway API**

Use the following commands to set the `SECURE_INGRESS_PORT` and `INGRESS_HOST` environment variables:

```bash
$ kubectl wait --for=condition=programmed gtw tcp-echo-gateway -n istio-io-tcp-traffic-shifting
$ export INGRESS_HOST=$(kubectl get gtw tcp-echo-gateway -n istio-io-tcp-traffic-shifting -o jsonpath='{.status.addresses[0].value}')
$ export TCP_INGRESS_PORT=$(kubectl get gtw tcp-echo-gateway -n istio-io-tcp-traffic-shifting -o jsonpath='{.spec.listeners[?(@.name=="tcp-31400")].port}')
```

3)  Confirm that the `tcp-echo` service is up and running by sending some TCP traffic.

```bash
$ export CURL=$(kubectl get pod -l app=curl -n istio-io-tcp-traffic-shifting -o jsonpath={.items..metadata.name})
$ for i in {1..20}; do \
kubectl exec "$CURL" -c curl -n istio-io-tcp-traffic-shifting -- sh -c "(date; sleep 1) | nc $INGRESS_HOST $TCP_INGRESS_PORT"; \
done
one Mon Nov 12 23:24:57 UTC 2022
one Mon Nov 12 23:25:00 UTC 2022
one Mon Nov 12 23:25:02 UTC 2022
one Mon Nov 12 23:25:05 UTC 2022
one Mon Nov 12 23:25:07 UTC 2022
one Mon Nov 12 23:25:10 UTC 2022
one Mon Nov 12 23:25:12 UTC 2022
one Mon Nov 12 23:25:15 UTC 2022
one Mon Nov 12 23:25:17 UTC 2022
one Mon Nov 12 23:25:19 UTC 2022
...
```

    You should notice that all the timestamps have a prefix of _one_, which means that all traffic
    was routed to the `v1` version of the `tcp-echo` service.

4)  Transfer 20% of the traffic from `tcp-echo:v1` to `tcp-echo:v2` with the following command:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f @samples/tcp-echo/tcp-echo-20-v2.yaml@ -n istio-io-tcp-traffic-shifting
```

**Tab: Gateway API**

```bash
$ kubectl apply -f @samples/tcp-echo/gateway-api/tcp-echo-20-v2.yaml@ -n istio-io-tcp-traffic-shifting
```

5) Wait a few seconds for the new rules to propagate and then confirm that the rule was replaced:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl get virtualservice tcp-echo -o yaml -n istio-io-tcp-traffic-shifting
apiVersion: networking.istio.io/v1
kind: VirtualService
  ...
spec:
  ...
  tcp:
  - match:
    - port: 31400
    route:
    - destination:
        host: tcp-echo
        port:
          number: 9000
        subset: v1
      weight: 80
    - destination:
        host: tcp-echo
        port:
          number: 9000
        subset: v2
      weight: 20
```

**Tab: Gateway API**

```bash
$ kubectl get tcproute tcp-echo -o yaml -n istio-io-tcp-traffic-shifting
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: TCPRoute
  ...
spec:
  parentRefs:
  - group: gateway.networking.k8s.io
    kind: Gateway
    name: tcp-echo-gateway
    sectionName: tcp-31400
  rules:
  - backendRefs:
    - group: ""
      kind: Service
      name: tcp-echo-v1
      port: 9000
      weight: 80
    - group: ""
      kind: Service
      name: tcp-echo-v2
      port: 9000
      weight: 20
...
```

6)  Send some more TCP traffic to the `tcp-echo` microservice.

```bash
$ export CURL=$(kubectl get pod -l app=curl -n istio-io-tcp-traffic-shifting -o jsonpath={.items..metadata.name})
$ for i in {1..20}; do \
kubectl exec "$CURL" -c curl -n istio-io-tcp-traffic-shifting -- sh -c "(date; sleep 1) | nc $INGRESS_HOST $TCP_INGRESS_PORT"; \
done
one Mon Nov 12 23:38:45 UTC 2022
two Mon Nov 12 23:38:47 UTC 2022
one Mon Nov 12 23:38:50 UTC 2022
one Mon Nov 12 23:38:52 UTC 2022
one Mon Nov 12 23:38:55 UTC 2022
two Mon Nov 12 23:38:57 UTC 2022
one Mon Nov 12 23:39:00 UTC 2022
one Mon Nov 12 23:39:02 UTC 2022
one Mon Nov 12 23:39:05 UTC 2022
one Mon Nov 12 23:39:07 UTC 2022
...
```

    You should now notice that about 20% of the timestamps have a prefix of _two_, which means that
    80% of the TCP traffic was routed to the `v1` version of the `tcp-echo` service, while 20% was
    routed to `v2`.

## Understanding what happened

In this task you partially migrated TCP traffic from an old to new version of
the `tcp-echo` service using Istio's weighted routing feature. Note that this is
very different than doing version migration using the deployment features of
container orchestration platforms, which use instance scaling to manage the
traffic.

With Istio, you can allow the two versions of the `tcp-echo` service to scale up
and down independently, without affecting the traffic distribution between them.

For more information about version routing with autoscaling, check out the blog
article [Canary Deployments using Istio](https://istio.io/v1.24/blog/2017/0.1-canary/) <!-- unresolved-site-link: route=/blog/2017/0.1-canary -->.

## Cleanup

1. Remove the routing rules:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl delete -f @samples/tcp-echo/tcp-echo-all-v1.yaml@ -n istio-io-tcp-traffic-shifting
```

**Tab: Gateway API**

```bash
$ kubectl delete -f @samples/tcp-echo/gateway-api/tcp-echo-all-v1.yaml@ -n istio-io-tcp-traffic-shifting
```

2) Remove the `curl` sample, `tcp-echo` application and test namespace:

```bash
$ kubectl delete -f @samples/curl/curl.yaml@ -n istio-io-tcp-traffic-shifting
$ kubectl delete -f @samples/tcp-echo/tcp-echo-services.yaml@ -n istio-io-tcp-traffic-shifting
$ kubectl delete namespace istio-io-tcp-traffic-shifting
```
