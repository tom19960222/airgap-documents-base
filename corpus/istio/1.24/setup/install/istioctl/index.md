---
collection: istio
version: "1.24"
title: "Install with Istioctl"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/istioctl/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Install and customize any Istio configuration profile for in-depth evaluation or production use."
---
Follow this guide to install and configure an Istio mesh for in-depth evaluation or production use.
If you are new to Istio, and just want to try it out, follow the
[quick start instructions](../../getting-started/index.md) instead.

This installation guide uses the [istioctl](https://istio.io/v1.24/docs/reference/commands/istioctl/) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> command line
tool to provide rich customization of the Istio control plane and of the sidecars for the Istio data plane.
It has user input validation to help prevent installation errors and customization options to
override any aspect of the configuration.

Using these instructions, you can select any one of Istio's built-in
[configuration profiles](../../additional-setup/config-profiles/index.md)
and then further customize the configuration for your specific needs.

The `istioctl` command supports the full [`IstioOperator` API](https://istio.io/v1.24/docs/reference/config/istio.operator.v1alpha1/) <!-- unresolved-site-link: route=/docs/reference/config/istio.operator.v1alpha1 -->
via command-line options for individual settings or for passing a yaml file containing an `IstioOperator`
custom resource (CR).

## Prerequisites

Before you begin, check the following prerequisites:

1. [Download the Istio release](../../additional-setup/download-istio-release/index.md).
1. Perform any necessary [platform-specific setup](../../platform-setup/_index.md).
1. Check the [Requirements for Pods and Services](../../../ops/deployment/application-requirements/index.md).

## Install Istio using the default profile

The simplest option is to install the `default` Istio
[configuration profile](../../additional-setup/config-profiles/index.md)
using the following command:

```bash
$ istioctl install
```

This command installs the `default` profile on the cluster defined by your
Kubernetes configuration. The `default` profile is a good starting point
for establishing a production environment, unlike the larger `demo` profile that
is intended for evaluating a broad set of Istio features.

Various settings can be configured to modify the installations. For example, to enable access logs:

```bash
$ istioctl install --set meshConfig.accessLogFile=/dev/stdout
```

> **Tip:**
>
> Many of the examples on this page and elsewhere in the documentation are written using `--set` to modify installation
> parameters, rather than passing a configuration file with `-f`. This is done to make the examples more compact.
> The two methods are equivalent, but `-f` is strongly recommended for production. The above command would be written as
> follows using `-f`:
>
>
>
> ```bash
> $ cat <<EOF > ./my-config.yaml
> apiVersion: install.istio.io/v1alpha1
> kind: IstioOperator
> spec:
>   meshConfig:
>     accessLogFile: /dev/stdout
> EOF
> $ istioctl install -f my-config.yaml
> ```

> **Tip:**
>
> The full API is documented in the [`IstioOperator` API reference](https://istio.io/v1.24/docs/reference/config/istio.operator.v1alpha1/) <!-- unresolved-site-link: route=/docs/reference/config/istio.operator.v1alpha1 -->.
> In general, you can use the `--set` flag in `istioctl` as you would with
> Helm, and the Helm `values.yaml` API is currently supported for backwards compatibility. The only difference is you must
> prefix the legacy `values.yaml` paths with `values.` because this is the prefix for the Helm pass-through API.

## Install from external charts

By default, `istioctl` uses compiled-in charts to generate the install manifest. These charts are released together with
`istioctl` for auditing and customization purposes and can be found in the release tar in the
`manifests` directory.
`istioctl` can also use external charts rather than the compiled-in ones. To select external charts, set
the `manifests` flag to a local file system path:

```bash
$ istioctl install --manifests=manifests/
```

If using the `istioctl` [istio_full_version] binary, this command will result in the same installation as `istioctl install` alone, because it points to the
same charts as the compiled-in ones.
Other than for experimenting with or testing new features, we recommend using the compiled-in charts rather than external ones to ensure compatibility of the
`istioctl` binary with the charts.

## Install a different profile

Other Istio configuration profiles can be installed in a cluster by passing the
profile name on the command line. For example, the following command can be used
to install the `demo` profile:

```bash
$ istioctl install --set profile=demo
```

## Generate a manifest before installation

You can generate the manifest before installing Istio using the `manifest generate`
sub-command.
For example, use the following command to generate a manifest for the `default` profile that can be installed with `kubectl`:

```bash
$ istioctl manifest generate > $HOME/generated-manifest.yaml
```

The generated manifest can be used to inspect what exactly is installed as well as to track changes to the manifest over time. While the `IstioOperator` CR represents the full user configuration and is sufficient for tracking it, the output from `manifest generate` also captures possible changes in the underlying charts and therefore can be used to track the actual installed resources.

> **Tip:**
>
> Any additional flags or custom values overrides you would normally use for installation should also be supplied to the `istioctl manifest generate` command.

> **Warning:**
>
> If attempting to install and manage Istio using `istioctl manifest generate`, please note the following caveats:
>
> 1. The Istio namespace (`istio-system` by default) must be created manually.
>
> 1. Istio validation will not be enabled by default. Unlike `istioctl install`, the `manifest generate` command will
> not create the `istiod-default-validator` validating webhook configuration unless `values.defaultRevision` is set:
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
> `istioctl install`.
>
> 1. This method is not tested as part of Istio releases.
>
> 1. While `istioctl install` will automatically detect environment specific settings from your Kubernetes context,
> `manifest generate` cannot as it runs offline, which may lead to unexpected results. In particular, you must ensure
> that you follow [these steps](../../../ops/best-practices/security/index.md#configure-third-party-service-account-tokens) if your
> Kubernetes environment does not support third party service account tokens. It is recommended to append `--cluster-specific` to your `istio manifest generate` command to detect the target cluster's environment, which will embed those cluster-specific environment settings into the generated manifests. This requires network access to your running cluster.
>
> 1. `kubectl apply` of the generated manifest may show transient errors due to resources not being available in the
> cluster in the correct order.
>
> 1. `istioctl install` automatically prunes any resources that should be removed when the configuration changes (e.g.
> if you remove a gateway). This does not happen when you use `istio manifest generate` with `kubectl` and these
> resources must be removed manually.

See [Customizing the installation configuration](../../additional-setup/customize-installation/index.md) for additional information on customizing the install.

## Uninstall Istio

To completely uninstall Istio from a cluster, run the following command:

```bash
$ istioctl uninstall --purge
```

> **Warning:**
>
> The optional `--purge` flag will remove all Istio resources, including cluster-scoped resources that may be shared with other Istio control planes.

Alternatively, to remove only a specific Istio control plane, run the following command:

```bash
$ istioctl uninstall <your original installation options>
```

or

```bash
$ istioctl manifest generate <your original installation options> | kubectl delete --ignore-not-found=true -f -
```

The control plane namespace (e.g., `istio-system`) is not removed by default.
If no longer needed, use the following command to remove it:

```bash
$ kubectl delete namespace istio-system
```
