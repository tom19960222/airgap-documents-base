---
collection: istio
version: "1.24"
title: "ServiceEntryAddressesRequired"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0134/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when a `ServiceEntry` with the `protocol` field not set, or set to `TCP`, doesn't have `addresses` defined.

## Example

You will receive this message:

```plain
Warning [IST0134] (ServiceEntry service-entry.default serviceentry.yaml:13) ServiceEntry addresses are required for this protocol.
```

When your cluster has the following `ServiceEntry` with unset `protocol` and missing `addresses`:

```yaml
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: service-entry
  namespace: default
spec:
  hosts:
    - 'istio.io'
  exportTo:
    - "."
  ports:
    - number: 443
      name: https
  location: MESH_EXTERNAL
  resolution: DNS
```

Another example of this analyzer is when you have a `ServiceEntry` with `protocol: TCP` and missing `addresses`:

```yaml
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: service-entry
  namespace: default
spec:
  hosts:
    - 'istio.io'
  exportTo:
    - "."
  ports:
    - number: 443
      name: https
      protocol: TCP
  location: MESH_EXTERNAL
  resolution: DNS
```

## How to resolve

Make sure to set `addresses` in your `ServiceEntry` when `protocol` is not set, or set to TCP. If `addresses` is not set, all traffic on the port defined in the `ServiceEntry` is matched, regardless of the host.
