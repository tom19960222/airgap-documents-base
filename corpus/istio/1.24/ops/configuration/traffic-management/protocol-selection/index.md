---
collection: istio
version: "1.24"
title: "Protocol Selection"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/configuration/traffic-management/protocol-selection/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Information on how to specify protocols."
---
Istio supports proxying any TCP traffic. This includes HTTP, HTTPS, gRPC, as well as raw TCP protocols.
In order to provide additional capabilities, such as routing and rich metrics, the protocol must be determined. This can be done automatically or explicitly specified.

Non-TCP based protocols, such as UDP, are not proxied. These protocols will continue to function as normal, without
any interception by the Istio proxy but cannot be used in proxy-only components such as ingress or egress gateways.

## Automatic protocol selection

Istio can automatically detect HTTP and HTTP/2 traffic. If the protocol cannot automatically be determined, traffic will be treated as plain TCP traffic.

> **Tip:**
>
> Server First protocols, such as MySQL, are incompatible with automatic protocol selection. See [Server first protocols](../../../deployment/application-requirements/index.md#server-first-protocols) for more information.

## Explicit protocol selection

Protocols can be specified manually in the Service definition.

This can be configured in two ways:

- By the name of the port: `name: <protocol>[-<suffix>]`.
- In Kubernetes 1.18+, by the `appProtocol` field: `appProtocol: <protocol>`.

If both are defined, `appProtocol` takes precedence over the port name.

Note that behavior at the Gateway differs in some cases as the gateway can terminate TLS and the protocol can be negotiated.

The following protocols are supported:

| Protocol                              | Sidecar Purpose                                                                                                                                                         | Gateway Purpose                                                                                                                                                         |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `http`                                | Plaintext HTTP/1.1 traffic                                                                                                                                              | Plaintext HTTP (1.1 or 2) traffic                                                                                                                                       |
| `http2`                               | Plaintext HTTP/2 traffic                                                                                                                                                | Plaintext HTTP (1.1 or 2) traffic                                                                                                                                       |
| `https`                               | TLS Encrypted data. Because the Sidecar does not decrypt TLS traffic, this is the same as `tls`                                                                         | TLS Encrypted HTTP (1.1 or 2) traffic                                                                                                                                   |
| `tcp`                                 | Opaque TCP data stream                                                                                                                                                  | Opaque TCP data stream                                                                                                                                                  |
| `tls`                                 | TLS Encrypted data                                                                                                                                                      | TLS Encrypted data                                                                                                                                                      |
| `grpc`, `grpc-web`                                | Same as `http2`                                                                                                                                                         | Same as `http2`                                                                                                                                                         |  |
| `mongo`, `mysql`, `redis` | Experimental application protocol support. To enable them, configure the corresponding [environment variables](https://istio.io/v1.24/docs/reference/commands/pilot-discovery/#envvars) <!-- unresolved-site-link: route=/docs/reference/commands/pilot-discovery -->. If not enabled, treated as opaque TCP data stream | Experimental application protocol support. To enable them, configure the corresponding [environment variables](https://istio.io/v1.24/docs/reference/commands/pilot-discovery/#envvars) <!-- unresolved-site-link: route=/docs/reference/commands/pilot-discovery -->. If not enabled, treated as opaque TCP data stream |

Below is an example of a Service that defines a `https` port by `appProtocol` and an `http` port by name:

```yaml
kind: Service
metadata:
  name: myservice
spec:
  ports:
  - port: 3306
    name: database
    appProtocol: https
  - port: 80
    name: http-web
```

## HTTP gateway protocol selection

Unlike sidecars, gateways are by default unable to automatically detect the specific HTTP protocol to use when forwarding requests to backend services. Therefore, unless explicit protocol selection is used to specify HTTP/1.1 (`http`) or HTTP/2 (`http2` or `grpc`), gateways will forward all incoming HTTP requests using HTTP/1.1.

Instead of using explicit protocol selection, you can instruct gateways to forward requests using the same protocol as the incoming request by setting the [`useClientProtocol`](https://istio.io/v1.24/docs/reference/config/networking/destination-rule/#ConnectionPoolSettings-HTTPSettings) <!-- unresolved-site-link: route=/docs/reference/config/networking/destination-rule --> option for a Service. Note, however, that using this option with services that do not support HTTP/2 can be risky because HTTPS gateways always [advertise](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation) support for HTTP/1.1 and HTTP/2. So even when a backend service doesn't support HTTP/2, modern clients will think it does and often choose to use it.
