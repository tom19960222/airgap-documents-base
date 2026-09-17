---
collection: istio
version: "1.24"
title: "EnvoyFilterUsesRemoveOperationIncorrectly"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0154/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when an `EnvoyFilter` uses the `REMOVE` operation and `ApplyTo` is set to `ROUTE_CONFIGURATION` or `HTTP_ROUTE`.  This will cause the `REMOVE` operation to be ignored.  At the moment only the `MERGE` operation can be used for `ROUTE_CONFIGURATION`.

## An example

Consider an `EnvoyFilter` with the patch operation of `REMOVE` where this `EnvoyFilter` will just be ignored:

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  name: test-remove-2
  namespace: bookinfo
spec:
  workloadSelector:
    labels:
      app: mysvc2
  configPatches:
  - applyTo: ROUTE_CONFIGURATION
    match:
      context: GATEWAY
      listener:
        filterChain:
          sni: app.example.com
          filter:
            name: "envoy.filters.network.http_connection_manager.InternalAddressConfig"
    patch:
      operation: REMOVE
```
