---
collection: istio
version: "1.24"
title: "Managing In-Mesh Certificates"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/configuration/traffic-management/manage-mesh-certificates/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "How to configure certificates within your mesh."
---
---
---

> **Warning:**
>
> This feature is actively in development and is considered
> [experimental](https://github.com/istio/community/blob/master/FEATURE-LIFECYCLE.md).

Many users need to manage the types of the certificates used within their environment. For example,
some users require the use of Elliptical Curve Cryptography (ECC) while others may need to use a
stronger bit length for RSA certificates. Configuring certificates within your environment can be
a daunting task for most users.

This document is only intended to be used for in-mesh communication. For managing certificates at
your Gateway, see the [Secure Gateways](../../../../tasks/traffic-management/ingress/secure-ingress/index.md) document.
For managing the CA used by istiod to generate workload certificates, see
the [Plugin CA Certificates](../../../../tasks/security/cert-management/plugin-ca-cert/index.md) document.

## istiod

When Istio is installed without a root CA certificate, istiod will generate a self-signed
CA certificate using RSA 2048.

To change the self-signed CA certificate's bit length, you will need to modify either the IstioOperator manifest provided to
`istioctl` or the values file used during the Helm installation of the [istio-discovery](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/manifests/charts/istio-control/istio-discovery) chart.

> **Tip:**
>
> While there are many environment variables that can be changed for
> [pilot-discovery](https://istio.io/v1.24/docs/reference/commands/pilot-discovery/) <!-- unresolved-site-link: route=/docs/reference/commands/pilot-discovery -->, this document will only
> outline some of them.

**Tabset (certificates):**

**Tab: IstioOperator**

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  values:
    pilot:
      env:
        CITADEL_SELF_SIGNED_CA_RSA_KEY_SIZE: 4096
```

**Tab: Helm**

```yaml
pilot:
  env:
    CITADEL_SELF_SIGNED_CA_RSA_KEY_SIZE: 4096
```

## Sidecars

Since sidecars manage their own certificates for in-mesh communication, the sidecars
are responsible for managing their private keys and generated Certificate Signing Request (CSRs). The sidecar
injector needs to be modified to inject the environment variables to be used for
this purpose.

> **Tip:**
>
> While there are many environment variables that can be changed for
> [pilot-agent](https://istio.io/v1.24/docs/reference/commands/pilot-agent/) <!-- unresolved-site-link: route=/docs/reference/commands/pilot-agent -->, this document will only
> outline some of them.

**Tabset (gateway-install-type):**

**Tab: IstioOperator**

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    defaultConfig:
      proxyMetadata:
        CITADEL_SELF_SIGNED_CA_RSA_KEY_SIZE: 4096
```

**Tab: Helm**

```yaml
meshConfig:
  defaultConfig:
    proxyMetadata:
      CITADEL_SELF_SIGNED_CA_RSA_KEY_SIZE: 4096
```

**Tab: Annotation**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: curl
spec:
  ...
  template:
    metadata:
      ...
      annotations:
        ...
        proxy.istio.io/config: |
          CITADEL_SELF_SIGNED_CA_RSA_KEY_SIZE: 4096
    spec:
      ...
```

### Signature Algorithm

By default, the sidecars will create RSA certificates. If you want to change it to
ECC, you need to set `ECC_SIGNATURE_ALGORITHM` to `ECDSA`.

**Tabset (gateway-install-type):**

**Tab: IstioOperator**

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    defaultConfig:
      proxyMetadata:
        ECC_SIGNATURE_ALGORITHM: "ECDSA"
```

**Tab: Helm**

```yaml
meshConfig:
  defaultConfig:
    proxyMetadata:
      ECC_SIGNATURE_ALGORITHM: "ECDSA"
```

Only P256 and P384 are supported via `ECC_CURVE`.

If you prefer to retain RSA signature algorithms and want to modify the RSA key size,
you can change the value of `WORKLOAD_RSA_KEY_SIZE`.
