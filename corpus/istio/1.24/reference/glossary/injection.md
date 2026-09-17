---
collection: istio
version: "1.24"
title: "Injection"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/injection.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Injection, or sidecar injection, refers to the use of [mutating webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) to modify pod specifications at creation time.

Injection can be used to add the Envoy sidecar configuration for mesh services or to configure the Envoy proxy of [gateways](index.md#gateway).

See [Installing the sidecar](../../setup/additional-setup/sidecar-injection/index.md) for more information.
