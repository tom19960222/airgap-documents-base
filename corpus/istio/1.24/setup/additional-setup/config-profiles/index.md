---
collection: istio
version: "1.24"
title: "Installation Configuration Profiles"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/config-profiles/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes the built-in Istio installation configuration profiles."
---
This page describes the built-in configuration profiles that can be used when
[installing Istio](../../install/istioctl/index.md).
The profiles provide customization of the Istio control plane and of the sidecars for the Istio data plane.

You can start with one of [Istio’s built-in configuration profiles](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/manifests/profiles) and then further
[customize the configuration](../customize-installation/index.md)
for your specific needs. The following built-in configuration profiles are currently available:

1. **default**: enables components according to the default settings of the
    [`IstioOperator` API](https://istio.io/v1.24/docs/reference/config/istio.operator.v1alpha1/) <!-- unresolved-site-link: route=/docs/reference/config/istio.operator.v1alpha1 -->.
    This profile is recommended for production deployments and for
    primary clusters in a
    [multicluster mesh](../../../ops/deployment/deployment-models/index.md#multiple-clusters).

1. **demo**: configuration designed to showcase Istio functionality with modest resource requirements.
    It is suitable to run the [Bookinfo](../../../examples/bookinfo/index.md) application and associated tasks.
    This is the configuration that is installed with the [quick start](../../getting-started/index.md) instructions.

> **Warning:**
>
> This profile enables high levels of tracing and access logging so it is not suitable for performance tests.

1. **minimal**: same as the default profile, but only the control plane components are installed.
    This allows you to configure the control plane and data plane components (e.g., gateways) using [separate profiles](../gateway/index.md#deploying-a-gateway).

1. **remote**: used for configuring a remote cluster that is managed by an
    external control plane or by a control plane in a primary cluster
    of a [multicluster mesh](../../../ops/deployment/deployment-models/index.md#multiple-clusters).

1. **empty**: deploys nothing. This can be useful as a base profile for custom configuration.

1. **preview**: the preview profile contains features that are experimental. This is intended to explore new features
                coming to Istio. Stability, security, and performance are not guaranteed - use at your own risk.

1. **ambient**: the ambient profile is designed to help you get started with [ambient mode](../../../ambient/_index.md).

> **Tip:**
>
> Some additional vendor-specific configuration profiles are also available.
> For more information, refer to the [setup instructions](../../platform-setup/_index.md) for your platform.

The components marked as &#x2714; are installed within each profile:

|     | default | demo | minimal | remote | empty | preview | ambient |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Core components | | | | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`istio-egressgateway` | | &#x2714; | | | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`istio-ingressgateway` | &#x2714; | &#x2714; | | | | &#x2714; | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`istiod` | &#x2714; | &#x2714; | &#x2714; | | | &#x2714; | &#x2714; |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`CNI` | | | | | | | &#x2714; |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Ztunnel` | | | | | | | &#x2714; |

To further customize Istio, a number of addon components can also be installed.
Refer to [integrations](../../../ops/integrations/_index.md) for more details.
