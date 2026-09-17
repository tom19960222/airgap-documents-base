---
collection: prometheus-operator
version: "0.73.2"
title: "basic-auth"
source_url: https://github.com/prometheus-operator/prometheus-operator/blob/20beb0b00b0bb61840ec2461ace4f22e4037b474/Documentation/user-guides/basic-auth.md
fetched_at: 2024-04-19T20:50:34+05:30
---
<br>
<div class="alert alert-info" role="alert">
    <i class="fa fa-exclamation-triangle"></i><b> Note:</b> Starting with v0.39.0, Prometheus Operator requires use of Kubernetes v1.16.x and up.
</div>

## Basic auth for targets

To authenticate a `ServiceMonitor`s over a metrics endpoint use [`basicAuth`](../api.md#monitoring.coreos.com/v1.BasicAuth)

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    k8s-apps: basic-auth-example
  name: basic-auth-example
spec:
  endpoints:
  - basicAuth:
      password:
        name: basic-auth
        key: password
      username:
        name: basic-auth
        key: user
    port: metrics
  namespaceSelector:
    matchNames:
    - logging
  selector:
    matchLabels:
      app: myapp
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: basic-auth
data:
  password: dG9vcg== # toor
  user: YWRtaW4= # admin
type: Opaque
```
