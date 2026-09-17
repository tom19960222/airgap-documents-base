---
collection: istio
version: "1.24"
title: "IneffectiveSelector"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0166/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when a workload selector in policies
like `AuthorizationPolicy`, `RequestAuthentication`, `Telemetry`, or
`WasmPlugin` does not effectively target any pods within the Kubernetes Gateway.

## Example

You will receive similar messages like:

```plain
Warning [IST0166] (AuthorizationPolicy default/ap-ineffective testdata/k8sgateway-selector.yaml:47) Ineffective selector on
Kubernetes Gateway bookinfo-gateway. Use the TargetRef field instead.
```

when your policy's selector matches a Kubernetes Gateway.

For example, when you have a Kubernetes Gateway pod like:

```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    istio.io/rev: default
  labels:
    gateway.networking.k8s.io/gateway-name: bookinfo-gateway
  name: bookinfo-gateway-istio-6ff4cf9645-xbqmc
  namespace: default
spec:
  containers:
  - image: proxyv2:1.21.0
    name: istio-proxy
```

And there is an `AuthorizationPolicy` with a `selector` like:

```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  namespace: default
  name: ap-ineffective
spec:
  selector:
    matchLabels:
      gateway.networking.k8s.io/gateway-name: bookinfo-gateway
  action: DENY
  rules:
  - from:
    - source:
      namespaces: ["dev"]
    to:
    - operation:
      methods: ["POST"]
```

If you have both `targetRef` and `selector` in the policy, this message will not occur. For example:

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: telemetry-example
  namespace: default
spec:
  tracing:
  - randomSamplingPercentage: 10.00
  selector:
    matchLabels:
      gateway.networking.k8s.io/gateway-name: bookinfo-gateway
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: bookinfo-gateway
```

## How to resolve

Make sure you are using the `selector` field for sidecars or Istio Gateway pods, and use the `targetRef` field for
Kubernetes Gateway pods. Otherwise, the policy will not be applied.

Here is an example:

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: telemetry-example
  namespace: default
spec:
  tracing:
  - randomSamplingPercentage: 10.00
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: bookinfo-gateway
```
