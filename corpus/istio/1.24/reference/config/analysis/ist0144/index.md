---
collection: istio
version: "1.24"
title: "InvalidApplicationUID"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0144/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when a workload is running as User ID (UID) `1337`. Application pods should not run as user ID (UID) `1337` because the istio-proxy container runs as UID `1337`. Running your application containers using the same UID would result in conflicts with its `iptables` configurations.

> **Warning:**
>
> User ID (UID) `1337` is reserved for the sidecar proxy.

## An example

Consider a `Deployment` with `securityContext.runAsUser` running either at Pod level or at container level using UID `1337`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-con-sec-uid
  labels:
    app: helloworld
    version: v1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: helloworld
      version: v1
  template:
    metadata:
      labels:
        app: helloworld
        version: v1
    spec:
      securityContext:
        runAsUser: 1337
      containers:
      - name: helloworld
        image: docker.io/istio/examples-helloworld-v1
        securityContext:
          runAsUser: 1337
        resources:
          requests:
            cpu: "100m"
        imagePullPolicy: IfNotPresent #Always
        ports:
        - containerPort: 5000
```

## How to resolve

Because the User ID (UID) `1337` is reserved for the sidecar proxy, you can use a different User ID (UID) such as `1338` for your workload.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-con-sec-uid
  labels:
    app: helloworld
    version: v1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: helloworld
      version: v1
  template:
    metadata:
      labels:
        app: helloworld
        version: v1
    spec:
      securityContext:
        runAsUser: 1338
      containers:
      - name: helloworld
        image: docker.io/istio/examples-helloworld-v1
        securityContext:
          runAsUser: 1338
        resources:
          requests:
            cpu: "100m"
        imagePullPolicy: IfNotPresent #Always
        ports:
        - containerPort: 5000
```
