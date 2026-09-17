---
collection: istio
version: "1.24"
title: "TLS Origination"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/tls-origination.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
TLS origination occurs when an Istio proxy (sidecar or egress gateway) is configured to accept unencrypted
internal HTTP connections, encrypt the requests, and then forward them to HTTPS servers that are secured
using simple or mutual TLS. This is the opposite of [TLS termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
where an ingress proxy accepts incoming TLS connections, decrypts the TLS, and passes unencrypted
requests on to internal mesh services.
