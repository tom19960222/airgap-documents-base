---
collection: istio
version: "1.24"
title: "InvalidAnnotation"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0125/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when an `annotation` mentions `istio.io` but the annotation

- isn't an annotation known to this version of Istio
- is known, but has a disallowed value, such as a string where a number is needed
- is applied to the wrong kind of resource, such as a pod-specific resource applied to a service

Consult [Istio's list of resource annotations](https://istio.io/v1.24/docs/reference/config/annotations/) <!-- unresolved-site-link: route=/docs/reference/config/annotations -->.

## Example

You will receive this message:

```plain
Warning [IST0108] (Service httpbin.default) Unknown annotation: networking.istio.io/exportTwo
```

when your cluster has following namespace:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: httpbin
  labels:
    app: httpbin
  annotations:
    # no such Istio annotation
    networking.istio.io/exportTwo: bar
spec:
  ports:
  - name: http
    port: 8000
    targetPort: 80
  selector:
    app: httpbin
```

In this example, the service `httpbin` is using `networking.istio.io/exportTwo` instead of `networking.istio.io/exportTo`.

## How to resolve

- Delete or rename unknown annotations
- Change annotations with disallowed values
