---
collection: istio
version: "1.24"
title: "VirtualServiceIneffectiveMatch"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0131/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when a virtual service contains a match rule that will never be used because a previous rule specifies the same match.

## Example

You will receive this message:

```plain
Info [IST0131] (VirtualService tls-routing.default) VirtualService rule #1 match #0 is not used (duplicates a match in rule #0).
```

when your cluster has the following virtual service:

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: tls-routing
spec:
  hosts:
  - www1.googleapis.com
  - api1.facebook.com
  tls:
  - match:
    - port: 2443
      sniHosts:
      - www1.googleapis.com
    route:
    - destination:
        host: www1.googleapis.com
  - match:
    - port: 2443
      sniHosts:
      - www1.googleapis.com
    route:
    - destination:
        host: api1.facebook.com
```

In this example, the virtual service specifies two different destinations
for the same match.  Istio will use the first match, and never send traffic to
the second destination.

## How to resolve

If you need traffic to go to more than one place, use `mirror`.

Re-order your routes so that the most specific ones are first.  Place 'catch all'
routes at the end.
