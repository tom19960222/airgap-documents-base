---
collection: istio
version: "1.24"
title: "NoServerCertificateVerificationDestinationLevel"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0128/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when no `caCertificates` are set in a destination rule, but they
are needed for the traffic policy.

## Example

You will receive this message:

```plain
Error [IST0128] (DestinationRule db-tls.default) DestinationRule default/db-tls in namespace default has TLS mode set to SIMPLE but no caCertificates are set to validate server identity for host: mydbserver.prod.svc.cluster.local
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
    tls:
      mode: SIMPLE
      clientCertificate: /etc/certs/myclientcert.pem
      privateKey: /etc/certs/client_private_key.pem
      # caCertificates not set
```

In this example, the destination rule `db-tls` specifies
TLS, but does not set the CA certificate file.

## How to resolve

- Supply the filename of a CA certificate
- Change the traffic policy so that a certificate is not needed
