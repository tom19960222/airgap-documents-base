---
collection: istio
version: "1.24"
title: "Install Istio in Dual-Stack mode"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/dual-stack/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Install and use Istio in Dual-Stack mode running on a Dual-Stack Kubernetes cluster."
---
---
---

> **Warning:**
>
> This feature is targeted at developers / expert users and is considered
> [Alpha](https://github.com/istio/community/blob/master/FEATURE-LIFECYCLE.md).

## Prerequisites

* Istio 1.17 or later.
* Kubernetes 1.23 or later [configured for dual-stack operations](https://kubernetes.io/docs/concepts/services-networking/dual-stack/).

## Installation steps

If you want to use `kind` for your test, you can set up a dual stack cluster with the following command:

```bash
$ kind create cluster --name istio-ds --config - <<EOF
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  ipFamily: dual
EOF
```

To enable dual-stack for Istio, you will need to modify your `IstioOperator` or Helm values with the following configuration.

**Tabset (dualstack):**

**Tab: IstioOperator**

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    defaultConfig:
      proxyMetadata:
        ISTIO_DUAL_STACK: "true"
  values:
    pilot:
      env:
        ISTIO_DUAL_STACK: "true"
    # The below values are optional and can be used based on your requirements
    gateways:
      istio-ingressgateway:
        ipFamilyPolicy: RequireDualStack
      istio-egressgateway:
        ipFamilyPolicy: RequireDualStack
```

**Tab: Helm**

```yaml
meshConfig:
  defaultConfig:
    proxyMetadata:
      ISTIO_DUAL_STACK: "true"
values:
  pilot:
    env:
      ISTIO_DUAL_STACK: "true"
  # The below values are optional and can be used based on your requirements
  gateways:
    istio-ingressgateway:
      ipFamilyPolicy: RequireDualStack
    istio-egressgateway:
      ipFamilyPolicy: RequireDualStack
```

## Verification

1. Create three namespaces:

    * `dual-stack`: `tcp-echo` will listen on both an IPv4 and IPv6 address.
    * `ipv4`: `tcp-echo` will listen on only an IPv4 address.
    * `ipv6`: `tcp-echo` will listen on only an IPv6 address.

```bash
$ kubectl create namespace dual-stack
$ kubectl create namespace ipv4
$ kubectl create namespace ipv6
```

1. Enable sidecar injection on all of those namespaces as well as the `default` namespace:

```bash
$ kubectl label --overwrite namespace default istio-injection=enabled
$ kubectl label --overwrite namespace dual-stack istio-injection=enabled
$ kubectl label --overwrite namespace ipv4 istio-injection=enabled
$ kubectl label --overwrite namespace ipv6 istio-injection=enabled
```

1. Create [tcp-echo](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/tcp-echo) deployments in the namespaces:

```bash
$ kubectl apply --namespace dual-stack -f @samples/tcp-echo/tcp-echo-dual-stack.yaml@
$ kubectl apply --namespace ipv4 -f @samples/tcp-echo/tcp-echo-ipv4.yaml@
$ kubectl apply --namespace ipv6 -f @samples/tcp-echo/tcp-echo-ipv6.yaml@
```

1. Deploy the [curl](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl) sample app to use as a test source for sending requests.

```bash
$ kubectl apply -f @samples/curl/curl.yaml@
```

1. Verify the traffic reaches the dual-stack pods:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -o jsonpath='{.items[0].metadata.name}')" -- sh -c "echo dualstack | nc tcp-echo.dual-stack 9000"
hello dualstack
```

1. Verify the traffic reaches the IPv4 pods:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -o jsonpath='{.items[0].metadata.name}')" -- sh -c "echo ipv4 | nc tcp-echo.ipv4 9000"
hello ipv4
```

1. Verify the traffic reaches the IPv6 pods:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -o jsonpath='{.items[0].metadata.name}')" -- sh -c "echo ipv6 | nc tcp-echo.ipv6 9000"
hello ipv6
```

1. Verify the envoy listeners:

```bash
$ istioctl proxy-config listeners "$(kubectl get pod -n dual-stack -l app=tcp-echo -o jsonpath='{.items[0].metadata.name}')" -n dual-stack --port 9000 -ojson | jq '.[] | {name: .name, address: .address, additionalAddresses: .additionalAddresses}'
```

    You will see listeners are now bound to multiple addresses, but only for dual stack services. Other services will only be listening on a single IP address.

```json
"name": "fd00:10:96::f9fc_9000",
"address": {
    "socketAddress": {
        "address": "fd00:10:96::f9fc",
        "portValue": 9000
    }
},
"additionalAddresses": [
    {
        "address": {
            "socketAddress": {
                "address": "10.96.106.11",
                "portValue": 9000
            }
        }
    }
],
```

1. Verify virtual inbound addresses are configured to listen on both `0.0.0.0` and `[::]`.

```bash
$ istioctl proxy-config listeners "$(kubectl get pod -n dual-stack -l app=tcp-echo -o jsonpath='{.items[0].metadata.name}')" -n dual-stack -o json | jq '.[] | select(.name=="virtualInbound") | {name: .name, address: .address, additionalAddresses: .additionalAddresses}'
```

```json
"name": "virtualInbound",
"address": {
    "socketAddress": {
        "address": "0.0.0.0",
        "portValue": 15006
    }
},
"additionalAddresses": [
    {
        "address": {
            "socketAddress": {
                "address": "::",
                "portValue": 15006
            }
        }
    }
],
```

1. Verify envoy endpoints are configured to route to both IPv4 and IPv6:

```bash
$ istioctl proxy-config endpoints "$(kubectl get pod -l app=curl -o jsonpath='{.items[0].metadata.name}')" --port 9000
ENDPOINT                 STATUS      OUTLIER CHECK     CLUSTER
10.244.0.19:9000         HEALTHY     OK                outbound|9000||tcp-echo.ipv4.svc.cluster.local
10.244.0.26:9000         HEALTHY     OK                outbound|9000||tcp-echo.dual-stack.svc.cluster.local
fd00:10:244::1a:9000     HEALTHY     OK                outbound|9000||tcp-echo.dual-stack.svc.cluster.local
fd00:10:244::18:9000     HEALTHY     OK                outbound|9000||tcp-echo.ipv6.svc.cluster.local
```

Now you can experiment with dual-stack services in your environment!

## Cleanup

1. Cleanup application namespaces and deployments

```bash
$ kubectl delete -f @samples/curl/curl.yaml@
$ kubectl delete ns dual-stack ipv4 ipv6
```
