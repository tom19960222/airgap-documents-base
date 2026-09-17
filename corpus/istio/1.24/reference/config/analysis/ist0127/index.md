---
collection: istio
version: "1.24"
title: "NoMatchingWorkloadsFound"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0127/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when an authorization policy's selector does not match any pods.

## Example

You will receive this message:

```plain
Warning [IST0127] (AuthorizationPolicy httpbin-nopods.httpbin) No matching workloads for this resource with the following labels: app=bogus-label,version=v1
```

when your cluster has the following authorization policy:

```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: httpbin-nopods
  namespace: httpbin
spec:
  selector:
    matchLabels:
      app: bogus-label # Bogus label. No matching workloads
      version: v1
  rules:
    - from:
        - source:
            principals: ["cluster.local/ns/default/sa/curl"]
        - source:
            namespaces: ["httpbin"]
      to:
        - operation:
            methods: ["GET"]
            paths: ["/info*"]
        - operation:
            methods: ["POST"]
            paths: ["/data"]
      when:
        - key: request.auth.claims[iss]
          values: ["https://accounts.google.com"]
```

In this example, the authorization policy `httpbin-nopods` selects
pods with the label `app=bogus-label`, and none exist.

## How to resolve

- Change the selector to match the pods you have
- Label pods to match the selector
