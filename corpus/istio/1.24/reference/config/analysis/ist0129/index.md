---
collection: istio
version: "1.24"
title: "NoServerCertificateVerificationPortLevel"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0129/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when `caCertificates` is not set in a destination rule, but is
needed for the traffic policy.

## Example

You will receive this message:

```plain
Error [IST0129] (DestinationRule db-tls.default) DestinationRule default/db-tls in namespace default has TLS mode set to SIMPLE but no caCertificates are set to validate server identity for host: mydbserver.prod.svc.cluster.local at port number:443
```

when your cluster has the following destination rule:

```yaml
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: db-tls
spec:
  host: mydbserver.prod.svc.cluster.local
  trafficPolicy:
    portLevelSettings:
      - port:
          number: 443
        tls:
          mode: SIMPLE
          clientCertificate: /etc/certs/myclientcert.pem
          privateKey: /etc/certs/client_private_key.pem
          sni: my-nginx.mesh-external.svc.cluster.local
          # caCertificates not set
```

In this example, the destination rule `db-tls` specifies
TLS, but does not set the CA certificate file.

## How to resolve

- Supply the filename of a CA certificate
- Change the traffic policy so that a certificate is not needed
