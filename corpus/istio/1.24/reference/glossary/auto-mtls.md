---
collection: istio
version: "1.24"
title: "Auto mTLS"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/auto-mtls.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Auto mTLS is a feature of Istio to automatically configure client side proxies to send
[mutual TLS traffic](../../tasks/security/authentication/authn-policy/index.md#auto-mutual-tls)
on connections where both the client and server are able to handle Mutual TLS traffic.
Istio downgrades to plaintext when either the client or server is not able to handle such traffic.
