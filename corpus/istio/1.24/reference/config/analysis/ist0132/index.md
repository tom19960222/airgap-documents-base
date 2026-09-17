---
collection: istio
version: "1.24"
title: "VirtualServiceHostNotFoundInGateway"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0132/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when a `host` defined in a virtual service is not found in the corresponding gateway.

## Example

You will receive this message:

```plain
Warning [IST0132] (VirtualService testing-service.default testing.yaml:8) one or more host [wrong.com] defined in VirtualService default/testing-service not found in Gateway istio-system/testing-gateway.
```

when your cluster has the following virtual service:

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: testing-service
  namespace: default
spec:
  gateways:
  - istio-system/testing-gateway
  hosts:
  - wrong.com
  http:
  - match:
    - uri:
        prefix: /
    route:
    - destination:
        host: ratings
```

and the following Gateway:

```yaml
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: testing-gateway
  namespace: istio-system
spec:
  selector:
    istio: ingressgateway
  servers:
  - hosts:
    - testing.com
    port:
      name: http
      number: 80
      protocol: HTTP
```

In this example, virtual service `testing-service` has host `wrong.com` which is not included in the gateway `testing-gateway`.

## How to resolve

Make sure all `hosts` in a virtual service are included in the `hosts` of gateways that are bound to the virtual service.
