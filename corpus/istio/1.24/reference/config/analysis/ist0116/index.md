---
collection: istio
version: "1.24"
title: "DeploymentAssociatedToMultipleServices"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0116/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when pods of a deployment are associated with multiple services using the same port but different protocols.

## An example

Consider an Istio mesh with the following services:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: productpage-tcp-v1
spec:
  ports:
    - port: 9080
      name: tcp
      protocol: TCP
  selector:
    app: productpage
---
apiVersion: v1
kind: Service
metadata:
  name: productpage-http-v1
spec:
  ports:
    - port: 9080
      name: http
      protocol: HTTP
  selector:
    app: productpage
```

This example shows both HTTP and TCP protocols associated with port 9080.

No two services should select the same pod port with different protocols.
