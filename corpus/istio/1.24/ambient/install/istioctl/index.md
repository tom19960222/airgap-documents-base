---
collection: istio
version: "1.24"
title: "Install with istioctl"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/install/istioctl/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Install Istio with support for ambient mode using the istioctl command line tool."
---
> **Tip:**
>
> Follow this guide to install and configure an Istio mesh with support for ambient mode.
> If you are new to Istio and just want to try it out, follow the
> [quick start instructions](../../getting-started/_index.md) instead.

This installation guide uses the [istioctl](https://istio.io/v1.24/docs/reference/commands/istioctl/) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> command-line
tool. `istioctl`, like other installation methods, exposes many customization options. Additionally,
it offers user input validation to help prevent installation errors, and includes many
post-installation analysis and configuration tools.

Using these instructions, you can select any one of Istio's built-in
[configuration profiles](../../../setup/additional-setup/config-profiles/index.md)
and then further customize the configuration for your specific needs.

The `istioctl` command supports the full [`IstioOperator` API](https://istio.io/v1.24/docs/reference/config/istio.operator.v1alpha1/) <!-- unresolved-site-link: route=/docs/reference/config/istio.operator.v1alpha1 -->
via command-line options for individual settings, or passing a YAML file containing an `IstioOperator`
custom resource.

## Prerequisites

Before you begin, check the following prerequisites:

1. [Download the Istio release](../../../setup/additional-setup/download-istio-release/index.md).
1. Perform any necessary [platform-specific setup](../platform-prerequisites/index.md).

## Install or upgrade the Kubernetes Gateway API CRDs

---
---
Note that the Kubernetes Gateway API CRDs do not come installed by default on most Kubernetes clusters, so make sure they are
installed before using the Gateway API:

```bash
$ kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/[k8s_gateway_api_version]/standard-install.yaml; }
```

## Install Istio using the ambient profile

`istioctl` supports a number of [configuration profiles](../../../setup/additional-setup/config-profiles/index.md) that include different default options,
and can be customized for your production needs. Support for ambient mode is included in the `ambient` profile. Install Istio with the
following command:

```bash
$ istioctl install --set profile=ambient --skip-confirmation
```

This command installs the `ambient` profile on the cluster defined by your
Kubernetes configuration.

## Configure and modify profiles

Istio's installation API is documented in the [`IstioOperator` API reference](https://istio.io/v1.24/docs/reference/config/istio.operator.v1alpha1/) <!-- unresolved-site-link: route=/docs/reference/config/istio.operator.v1alpha1 -->. You
can use the `--set` option to `istioctl install` to modify individual installation parameters, or specify your own configuration file with `-f`.

Full details on how to use and customize `istioctl` installations are available in [the sidecar installation documentation](../../../setup/install/istioctl/index.md).

## Uninstall Istio

To completely uninstall Istio from a cluster, run the following command:

```bash
$ istioctl uninstall --purge -y
```

> **Warning:**
>
> The optional `--purge` flag will remove all Istio resources, including cluster-scoped resources that may be shared with other Istio control planes.

Alternatively, to remove only a specific Istio control plane, run the following command:

```bash
$ istioctl uninstall <your original installation options>
```

The control plane namespace (e.g., `istio-system`) is not removed by default.
If no longer needed, use the following command to remove it:

```bash
$ kubectl delete namespace istio-system
```

## Generate a manifest before installation

You can generate the manifest before installing Istio using the `manifest generate`
sub-command.
For example, use the following command to generate a manifest for the `default` profile that can be installed with `kubectl`:

```bash
$ istioctl manifest generate > $HOME/generated-manifest.yaml
```

The generated manifest can be used to inspect what exactly is installed as well as to track changes
to the manifest over time. While the `IstioOperator` CR represents the full user configuration and
is sufficient for tracking it, the output from `manifest generate` also captures possible changes
in the underlying charts and therefore can be used to track the actual installed resources.

> **Tip:**
>
> Any additional flags or custom values overrides you would normally use for installation should
> also be supplied to the `istioctl manifest generate` command.

> **Warning:**
>
> If attempting to install and manage Istio using `istioctl manifest generate`, please note the following caveats:
>
> 1. Manually create the Istio namespace (`istio-system` by default).
>
> 1. Istio validation will not be enabled by default. Unlike `istioctl install`, the `manifest generate` command will
>    not create the `istiod-default-validator` validating webhook configuration unless `values.defaultRevision` is set:
>
>
>
> ```bash
> $ istioctl manifest generate --set values.defaultRevision=default
> ```
>
>
>
> 1. Resources may not be installed with the same sequencing of dependencies as
>    `istioctl install`.
>
> 1. This method is not tested as part of Istio releases.
>
> 1. While `istioctl install` will automatically detect environment-specific settings from your Kubernetes context,
>    `manifest generate` cannot do so as it runs offline, which may lead to unexpected results. In particular, you must ensure
>    that you follow [these steps](../../../ops/best-practices/security/index.md#configure-third-party-service-account-tokens) if your
>    Kubernetes environment does not support third party service account tokens. It is recommended to append
>    `--cluster-specific` to your `istio manifest generate` command to detect the target cluster's environment,
>    which will embed those cluster-specific environment settings into the generated manifests.
>    This requires network access to your running cluster.
>
> 1. `kubectl apply` of the generated manifest may show transient errors due to resources not being available in the
>    cluster in the correct order.
>
> 1. `istioctl install` automatically prunes any resources that should be removed when the configuration changes (e.g.
>    if you remove a gateway). This does not happen when you use `istio manifest generate` with `kubectl` and these
>    resources must be removed manually.
