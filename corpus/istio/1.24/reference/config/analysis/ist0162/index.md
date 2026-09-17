---
collection: istio
version: "1.24"
title: "GatewayPortNotDefinedOnService"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0162/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when a gateway (usually `istio-ingressgateway`) offers a
port that the Kubernetes service workload selected by the gateway does not.

For example, your Istio configuration contains these values:

```yaml
# Gateway with bogus ports

apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: istio-ingressgateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"
  - port:
      number: 8004
      name: http2
      protocol: HTTP
    hosts:
    - "*"
---

# Default Gateway Service

apiVersion: v1
kind: Service
metadata:
  name: istio-ingressgateway
spec:
  selector:
    istio: ingressgateway
  ports:
  - name: status-port
    port: 15021
    protocol: TCP
    targetPort: 15021
  - name: http2
    port: 80
    protocol: TCP
    targetPort: 8080
  - name: https
    port: 443
    protocol: TCP
    targetPort: 8443
```

In this example, the `GatewayPortNotDefinedOnService` message occurs because this
configuration uses port 8004, but a default `IngressGateway` (named `istio-ingressgateway`) is only open on target ports
15021, 8080 and 8443.

To resolve this problem, change your gateway configuration to use a valid port
on the workload and try again.

Here's a corrected example:

```yaml
# Gateway with correct ports

apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: istio-ingressgateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 8080
      name: http2
      protocol: HTTP
    hosts:
    - "*"
  - port:
      number: 8443
      name: https
      protocol: HTTP
    hosts:
    - "*"
```
