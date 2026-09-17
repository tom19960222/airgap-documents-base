---
collection: istio
version: "1.24"
title: "ReferencedResourceNotFound"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0101/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when an Istio resource references another resource that does
not exist. This will lead to errors when Istio tries to look up the referenced
resource but cannot find it.

For example, you receive this error:

```plain
Error [IST0101] (VirtualService httpbin.default) Referenced gateway not found: "httpbin-gateway-bogus"
```

In this example, the `VirtualService` refers to a gateway that does not exist:

```yaml
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: httpbin-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http2
      protocol: HTTP2
    hosts:
    - "*"
---
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: httpbin
spec:
  hosts:
  - "*"
  gateways:
  - httpbin-gateway-bogus #  Should have been "httpbin-gateway"
  http:
  - route:
    - destination:
        host: httpbin-gateway
```

To resolve this problem, look for the resource type in the detailed error
message, correct your Istio configuration and try again.
