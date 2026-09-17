---
collection: istio
version: "1.24"
title: "Compatibility Versions"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/compatibility-versions/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "How to configure \"compatibility versions\", to decouple behavioral changes from releases."
---
With each new version of Istio, there may be some intentional behavioral changes.
These can be to improve security, fix incorrect behavior, or otherwise improve Istio for users.
Generally, these types of changes impact only edge cases.

While beneficial on the long term, each behavioral change introduces risk during upgrades.
Historically, when upgrading users should read the release notes for any behavioral changes and determine if they are impacted; this can be tedious and error prone.

Compatibility versions give users an additional option, allowing release versions to be decoupled from behavioral changes.
For instance, you can install Istio [istio_version], but configure it to behave like [istio_previous_version].

## Using compatibility versions

To use a compatibility version, simply set the `compatibilityVersion` field.

**Tabset (install):**

**Tab: IstioOperator**

```shell
$ istioctl install --set values.compatibilityVersion=[istio_previous_version]
```

**Tab: Helm**

```shell
$ helm install ... --set compatibilityVersion=[istio_previous_version]
```

## When should I use compatibility versions?

Compatibility versions should be used only when an incompatibility between releases exists, as a temporary measure. You should plan to migrate to the new behavior as soon as practical.

Compatibility versions for a release will be removed, and will no longer be supported, when the release they refer to reaches end-of-life. Refer to the [current Istio release support status chart](../../../releases/supported-releases/index.md#support-status-of-istio-releases) for the status of specific releases.

To help detect if a compatibility version should be used, `istioctl x precheck` can be used with the `--from-version` flag.
For instance, if you are upgrading from version [istio_previous_version]:

```shell
$ istioctl x precheck --from-version [istio_previous_version]
Warning [IST0168] (DestinationRule default/tls) The configuration "ENABLE_AUTO_SNI" changed in release 1.20: previously, no SNI would be set; now it will be automatically set. Or, install with `--set compatibilityVersion=1.20` to retain the old default.
Error: Issues found when checking the cluster. Istio may not be safe to install or upgrade.
See https://istio.io/v1.21/docs/reference/config/analysis for more information about causes and resolutions.
```
