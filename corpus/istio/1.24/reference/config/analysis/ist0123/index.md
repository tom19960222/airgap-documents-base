---
collection: istio
version: "1.24"
title: "NamespaceMultipleInjectionLabels"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0123/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when a namespace specifies Istio sidecar auto-injection
using **both** the new and legacy style labels.

## Example

You will receive this message:

```plain
Warning [IST0123] (Namespace busted) The namespace has both new and legacy injection labels. Run 'kubectl label namespace busted istio.io/rev-' or 'kubectl label namespace busted istio-injection-'
```

when your cluster has following namespace:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: busted
  labels:
    istio-injection: enabled
    istio.io/rev: canary
```

In this example, the namespace `busted` uses both old-style and new-style injection labels.

## How to resolve

- Remove the `istio-injection` label
- Remove the `istio.io/rev` label
