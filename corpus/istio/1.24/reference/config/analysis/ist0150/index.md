---
collection: istio
version: "1.24"
title: "ExternalNameServiceTypeInvalidPortName"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0150/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs for services of type ExternalName when the port doesn't follow Istio service port naming convention, the port is unnamed or the port is named tcp.

## Example

You will receive this message:

```plain
Warning [IST0150] (Service nginx.default) Port name for ExternalName service is invalid. Proxy may prevent tcp named ports and unmatched traffic for ports serving TCP protocol from being forwarded correctly.
```

when your cluster has the following service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  externalName: nginx.example.com
  ports:
  - name: tcp
    port: 443
    protocol: TCP
    targetPort: 443
  type: ExternalName
```

In this example, the port name `tcp` follows the syntax: `name: <protocol>`. However, for ExternalName services, there is no service IP defined, so the SNI field is needed for routing.

## How to resolve

- If you have an ExternalName service type, and the protocol is TCP, rename the port to `<protocol>[-<suffix>]` or `<protocol>` where protocol is `https` or `tls`. To learn more, review
docs on [explicit protocol selection](../../../../ops/configuration/traffic-management/protocol-selection/index.md#explicit-protocol-selection).
