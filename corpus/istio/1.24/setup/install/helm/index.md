---
collection: istio
version: "1.24"
title: "Install with Helm"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/helm/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to install and configure Istio in a Kubernetes cluster using Helm."
---
Follow this guide to install and configure an Istio mesh using
[Helm](https://helm.sh/docs/).

---
---
The Helm charts used in this guide are the same as those used when
installing Istio via [Istioctl](../istioctl/index.md), with the exception of the `gateway` chart.

Istioctl uses a different [gateway chart](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/manifests/charts/gateways/istio-ingress) than the [gateway chart](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/manifests/charts/gateway) described in this guide

---
---
## Prerequisites

1. Perform any necessary [platform-specific setup](../../platform-setup/_index.md).

1. Check the [Requirements for Pods and Services](../../../ops/deployment/application-requirements/index.md).

1. [Install the latest Helm client](https://helm.sh/docs/intro/install/). Helm versions released before the [oldest currently-supported Istio release](../../../releases/supported-releases/index.md#support-status-of-istio-releases) are not tested, supported, or recommended.

1. Configure the Helm repository:

```bash
$ helm repo add istio https://istio-release.storage.googleapis.com/charts
$ helm repo update
```

## Installation steps

This section describes the procedure to install Istio using Helm. The general syntax for helm installation is:

```bash
$ helm install <release> <chart> --namespace <namespace> --create-namespace [--set <other_parameters>]
```

The variables specified in the command are as follows:
* `<chart>` A path to a packaged chart, a path to an unpacked chart directory or a URL.
* `<release>` A name to identify and manage the Helm chart once installed.
* `<namespace>` The namespace in which the chart is to be installed.

Default configuration values can be changed using one or more `--set <parameter>=<value>` arguments. Alternatively, you can specify several parameters in a custom values file using the `--values <file>` argument.

> **Tip:**
>
> You can display the default values of configuration parameters using the `helm show values <chart>` command or refer to `artifacthub` chart documentation at [Custom Resource Definition parameters](https://artifacthub.io/packages/helm/istio-official/base?modal=values), [Istiod chart configuration parameters](https://artifacthub.io/packages/helm/istio-official/istiod?modal=values) and [Gateway chart configuration parameters](https://artifacthub.io/packages/helm/istio-official/gateway?modal=values).

1. Install the Istio base chart which contains cluster-wide Custom Resource Definitions (CRDs) which must be installed prior to the deployment of the Istio control plane:

> **Warning:**
>
> When performing a revisioned installation, the base chart requires the `--set defaultRevision=<revision>` value to be set for resource
>     validation to function. Below we install the `default` revision, so `--set defaultRevision=default` is configured.

```bash
$ helm install istio-base istio/base -n istio-system --set defaultRevision=default --create-namespace
```

1. Validate the CRD installation with the `helm ls` command:

```bash
$ helm ls -n istio-system
NAME       NAMESPACE    REVISION UPDATED                                 STATUS   CHART        APP VERSION
istio-base istio-system 1        2024-04-17 22:14:45.964722028 +0000 UTC deployed base-[istio_full_version]  [istio_full_version]
```

    In the output locate the entry for `istio-base` and make sure the status is set to `deployed`.

1. If you intend to use Istio CNI chart you must do so now. See [Install Istio with the CNI plugin](../../additional-setup/cni/index.md#installing-with-helm) for more info.

1. Install the Istio discovery chart which deploys the `istiod` service:

```bash
$ helm install istiod istio/istiod -n istio-system --wait
```

1. Verify the Istio discovery chart installation:

```bash
$ helm ls -n istio-system
NAME       NAMESPACE    REVISION UPDATED                                 STATUS   CHART         APP VERSION
istio-base istio-system 1        2024-04-17 22:14:45.964722028 +0000 UTC deployed base-[istio_full_version]   [istio_full_version]
istiod     istio-system 1        2024-04-17 22:14:45.964722028 +0000 UTC deployed istiod-[istio_full_version] [istio_full_version]
```

1. Get the status of the installed helm chart to ensure it is deployed:

```bash
$ helm status istiod -n istio-system
NAME: istiod
LAST DEPLOYED: Fri Jan 20 22:00:44 2023
NAMESPACE: istio-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
"istiod" successfully installed!

To learn more about the release, try:
  $ helm status istiod
  $ helm get all istiod

Next steps:
  * Deploy a Gateway: https://istio.io/latest/docs/setup/additional-setup/gateway/
  * Try out our tasks to get started on common configurations:
    * https://istio.io/latest/docs/tasks/traffic-management
    * https://istio.io/latest/docs/tasks/security/
    * https://istio.io/latest/docs/tasks/policy-enforcement/
    * https://istio.io/latest/docs/tasks/policy-enforcement/
  * Review the list of actively supported releases, CVE publications and our hardening guide:
    * https://istio.io/latest/docs/releases/supported-releases/
    * https://istio.io/latest/news/security/
    * https://istio.io/latest/docs/ops/best-practices/security/

For further documentation see https://istio.io website

Tell us how your install/upgrade experience went at https://forms.gle/99uiMML96AmsXY5d6
```

1. Check `istiod` service is successfully installed and its pods are running:

```bash
$ kubectl get deployments -n istio-system --output wide
NAME     READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS   IMAGES                         SELECTOR
istiod   1/1     1            1           10m   discovery    docker.io/istio/pilot:[istio_full_version]   istio=pilot
```

1. (Optional) Install an ingress gateway:

```bash
$ kubectl create namespace istio-ingress
$ helm install istio-ingress istio/gateway -n istio-ingress --wait
```

    See [Installing Gateways](../../additional-setup/gateway/index.md) for in-depth documentation on gateway installation.

> **Warning:**
>
> The namespace the gateway is deployed in must not have a `istio-injection=disabled` label.
>     See [Controlling the injection policy](../../additional-setup/sidecar-injection/index.md#controlling-the-injection-policy) for more info.

> **Tip:**
>
> See [Advanced Helm Chart Customization](../../additional-setup/customize-installation-helm/index.md) for in-depth documentation on how to use
> Helm post-renderer to customize the Helm charts.

## Updating your Istio configuration

You can provide override settings specific to any Istio Helm chart used above
and follow the Helm upgrade workflow to customize your Istio mesh installation.
The available configurable options can be found by using `helm show values istio/<chart>`;
for example `helm show values istio/gateway`.

### Migrating from non-Helm installations

If you're migrating from a version of Istio installed using `istioctl` to Helm (Istio 1.5 or earlier), you need to delete your current Istio
control plane resources and re-install Istio using Helm as described above. When
deleting your current Istio installation, you must not remove the Istio Custom Resource
Definitions (CRDs) as that can lead to loss of your custom Istio resources.

> **Warning:**
>
> It is highly recommended to take a backup of your Istio resources using steps
> described above before deleting current Istio installation in your cluster.

You can follow steps mentioned in the [Istioctl uninstall guide](../istioctl/index.md#uninstall-istio).

## Uninstall

You can uninstall Istio and its components by uninstalling the charts
installed above.

1. List all the Istio charts installed in `istio-system` namespace:

```bash
$ helm ls -n istio-system
NAME       NAMESPACE    REVISION UPDATED                                 STATUS   CHART         APP VERSION
istio-base istio-system 1        2024-04-17 22:14:45.964722028 +0000 UTC deployed base-[istio_full_version]   [istio_full_version]
istiod     istio-system 1        2024-04-17 22:14:45.964722028 +0000 UTC deployed istiod-[istio_full_version] [istio_full_version]
```

1. (Optional) Delete any Istio gateway chart installations:

```bash
$ helm delete istio-ingress -n istio-ingress
$ kubectl delete namespace istio-ingress
```

1. Delete Istio discovery chart:

```bash
$ helm delete istiod -n istio-system
```

1. Delete Istio base chart:

> **Tip:**
>
> By design, deleting a chart via Helm doesn't delete the installed Custom
>     Resource Definitions (CRDs) installed via the chart.

```bash
$ helm delete istio-base -n istio-system
```

1. Delete the `istio-system` namespace:

```bash
$ kubectl delete namespace istio-system
```

## Uninstall stable revision label resources

If you decide to continue using the old control plane, instead of completing the update,
you can uninstall the newer revision and its tag by first issuing
`helm template istiod istio/istiod -s templates/revision-tags.yaml --set revisionTags={prod-canary} --set revision=canary -n istio-system | kubectl delete -f -`.
You must then uninstall the revision of Istio that it pointed to by following the uninstall procedure above.

If you installed the gateway(s) for this revision using in-place upgrades, you must also reinstall the gateway(s) for the previous revision manually.
Removing the previous revision and its tags will not automatically revert the previously upgraded gateway(s).

### (Optional) Deleting CRDs installed by Istio

Deleting CRDs permanently removes any Istio resources you have created in your cluster.
To delete Istio CRDs installed in your cluster:

```bash
$ kubectl get crd -oname | grep --color=never 'istio.io' | xargs kubectl delete
```

## Generate a manifest before installation

You can generate the manifests for each component before installing Istio using the `helm template`
sub-command.
For example, to generate a manifest that can be installed with `kubectl` for the `istiod` component:

```bash
$ helm template istiod istio/istiod -n istio-system --kube-version {Kubernetes version of target cluster} > istiod.yaml
```

The generated manifest can be used to inspect what exactly is installed as well as to track changes to the manifest over time.

> **Tip:**
>
> Any additional flags or custom values overrides you would normally use for installation should also be supplied to the `helm template` command.

To install the manifest generated above, which will create the `istiod` component in the target cluster:

```bash
$ kubectl apply -f istiod.yaml
```

> **Warning:**
>
> If attempting to install and manage Istio using `helm template`, please note the following caveats:
>
> 1. The Istio namespace (`istio-system` by default) must be created manually.
>
> 1. Resources may not be installed with the same sequencing of dependencies as
> `helm install`
>
> 1. This method is not tested as part of Istio releases.
>
> 1. While `helm install` will automatically detect environment specific settings from your Kubernetes context,
> `helm template` cannot as it runs offline, which may lead to unexpected results. In particular, you must ensure
> that you follow [these steps](../../../ops/best-practices/security/index.md#configure-third-party-service-account-tokens) if your
> Kubernetes environment does not support third party service account tokens.
>
> 1. `kubectl apply` of the generated manifest may show transient errors due to resources not being available in the
> cluster in the correct order.
>
> 1. `helm install` automatically prunes any resources that should be removed when the configuration changes (e.g.
> if you remove a gateway). This does not happen when you use `helm template` with `kubectl`, and these
> resources must be removed manually.
