---
collection: istio
version: "1.24"
title: "SchemaValidationError"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0106/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when your Istio configuration does not successfully pass
schema validation.

For example, you receive this error:

```plain
Error [IST0106] (VirtualService ratings-bogus-weight-default.default) Schema validation error: percentage 888 is not in range 0..100
```

and your Istio configuration contains these values:

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: ratings-bogus-weight-default
  namespace: default
spec:
  hosts:
  - ratings
  http:
  - route:
    - destination:
        host: ratings
        subset: v1
      weight: 999
    - destination:
        host: ratings
        subset: v2
      weight: 888
```

In this example, the error message indicates that the `weight` element has an
invalid value when checked against the schema.

To resolve this problem, refer to the
[message details](../message-format/index.md) field to determine
which element or value does not adhere to the schema, correct the error and try
again.

For details about the expected schema for Istio resources, see the
[configuration reference](../../_index.md).
