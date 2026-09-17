---
collection: istio
version: "1.24"
title: "Upgrade with Helm"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/upgrade/helm/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to upgrade Istio using Helm."
---
Follow this guide to upgrade and configure an Istio mesh using
[Helm](https://helm.sh/docs/).  This guide assumes you have already performed an
[installation with Helm](../../install/helm/index.md) for a previous minor or patch version of Istio.

---
---
The Helm charts used in this guide are the same as those used when
installing Istio via [Istioctl](../../install/istioctl/index.md), with the exception of the `gateway` chart.

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

## Upgrade steps

Before upgrading Istio, it is recommended to run the `istioctl x precheck` command to make sure the upgrade is compatible with your environment.

```bash
$ istioctl x precheck
✔ No issues found when checking the cluster. Istio is safe to install or upgrade!
  To get started, check out <https://istio.io/latest/docs/setup/getting-started/>
```

### Canary upgrade (recommended)

You can install a canary version of Istio control plane to validate that the new
version is compatible with your existing configuration and data plane using
the steps below:

> **Warning:**
>
> Note that when you install a canary version of the `istiod` service, the underlying
> cluster-wide resources from the base chart are shared across your
> primary and canary installations.

---
---

> **Warning:**
>
> If upgrading CRDs via Helm from an Istio release 1.23 or older, you may encounter an error such as the following
>
> `Error: rendered manifests contain a resource that already exists. Unable to continue with update: CustomResourceDefinition "wasmplugins.extensions.istio.io" in namespace "" exists and cannot be imported into the current release: invalid ownership metadata`
>
> You can resolve this with a one-time migration using the following `kubectl` commands:
>
>
>
> ```bash
> $ for crd in $(kubectl get crds -l chart=istio -o name && kubectl get crds -l app.kubernetes.io/part-of=istio -o name)
> $ do
> $    kubectl label "$crd" "app.kubernetes.io/managed-by=Helm"
> $    kubectl annotate "$crd" "meta.helm.sh/release-name=istio-base" # replace with actual Helm release name, if different from the documentation default
> $    kubectl annotate "$crd" "meta.helm.sh/release-namespace=istio-system" # replace with actual istio namespace
> $ done
> ```

1. Upgrade the Istio base chart to ensure all cluster-wide resources are up-to-date

```bash
$ helm upgrade istio-base istio/base -n istio-system
```

1. Install a canary version of the Istio discovery chart by setting the revision
   value:

```bash
$ helm install istiod-canary istio/istiod \
    --set revision=canary \
    -n istio-system
```

1. Verify that you have two versions of `istiod` installed in your cluster:

```bash
$ kubectl get pods -l app=istiod -L istio.io/rev -n istio-system
  NAME                            READY   STATUS    RESTARTS   AGE   REV
  istiod-5649c48ddc-dlkh8         1/1     Running   0          71m   default
  istiod-canary-9cc9fd96f-jpc7n   1/1     Running   0          34m   canary
```

1. If you are using [Istio gateways](../../additional-setup/gateway/index.md#deploying-a-gateway), install a canary revision of the Gateway chart by setting the revision value:

```bash
$ helm install istio-ingress-canary istio/gateway \
    --set revision=canary \
    -n istio-ingress
```

1. Verify that you have two versions of `istio-ingress gateway` installed in your cluster:

```bash
$ kubectl get pods -L istio.io/rev -n istio-ingress
  NAME                                    READY   STATUS    RESTARTS   AGE     REV
  istio-ingress-754f55f7f6-6zg8n          1/1     Running   0          5m22s   default
  istio-ingress-canary-5d649bd644-4m8lp   1/1     Running   0          3m24s   canary
```

    See [Upgrading Gateways](../../additional-setup/gateway/index.md#canary-upgrade-advanced) for in-depth documentation on gateway canary upgrade.

1. Follow the steps [here](../canary/index.md#data-plane) to test or migrate
   existing workloads to use the canary control plane.

1. Once you have verified and migrated your workloads to use the canary control
   plane, you can uninstall your old control plane:

```bash
$ helm delete istiod -n istio-system
```

1. Upgrade the Istio base chart again, this time making the new `canary` revision the cluster-wide default.

```bash
$ helm upgrade istio-base istio/base --set defaultRevision=canary -n istio-system
```

### Stable revision labels

---
---
Manually relabeling namespaces when moving them to a new revision can be tedious and error-prone.
[Revision tags](https://istio.io/v1.24/docs/reference/commands/istioctl/#istioctl-tag) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> solve this problem.
[Revision tags](https://istio.io/v1.24/docs/reference/commands/istioctl/#istioctl-tag) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> are stable identifiers that point to revisions and can be used to avoid relabeling namespaces. Rather than relabeling the namespace, a mesh operator can simply change the tag to point to a new revision. All namespaces labeled with that tag will be updated at the same time.

#### Usage

---
---
Consider a cluster with two revisions installed, `{{< istio_previous_version_revision >}}-1` and `{{< istio_full_version_revision >}}`. The cluster operator creates a revision tag `prod-stable`,
pointed at the older, stable `{{< istio_previous_version_revision >}}-1` version, and a revision tag `prod-canary` pointed at the newer `{{< istio_full_version_revision >}}` revision. That
state could be reached via the following commands:

```bash
$ helm template istiod istio/istiod -s templates/revision-tags.yaml --set revisionTags="{prod-stable}" --set revision=[istio_previous_version_revision]-1 -n istio-system | kubectl apply -f -
$ helm template istiod istio/istiod -s templates/revision-tags.yaml --set revisionTags="{prod-canary}" --set revision=[istio_full_version_revision] -n istio-system | kubectl apply -f -
```

> **Warning:**
>
> These commands create new `MutatingWebhookConfiguration` resources in your cluster, however, they are not owned by any Helm chart due to `kubectl` manually applying the templates. See the instructions
> below to uninstall revision tags.

---
---
The resulting mapping between revisions, tags, and namespaces is as shown below:

![Two namespaces pointed to prod-stable and one pointed to prod-canary](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/upgrade/canary/revision-tags-before.svg)

The cluster operator can view this mapping in addition to tagged namespaces through the `istioctl tag list` command:

```bash
$ istioctl tag list
TAG         REVISION NAMESPACES
default     [istio_previous_version_revision]-1   ...
prod-canary [istio_full_version_revision]   ...
prod-stable [istio_previous_version_revision]-1   ...
```

After the cluster operator is satisfied with the stability of the control plane tagged with `prod-canary`, namespaces labeled
`istio.io/rev=prod-stable` can be updated with one action by modifying the `prod-stable` revision tag to point to the newer
`{{< istio_full_version_revision >}}` revision.

```bash
$ helm template istiod istio/istiod -s templates/revision-tags.yaml --set revisionTags="{prod-stable}" --set revision=[istio_full_version_revision] -n istio-system | kubectl apply -f -
```

---
---
Now, the updated mapping between revisions, tags, and namespaces is as shown below:

![Namespace labels unchanged but now all namespaces pointed to [istio_full_version_revision]](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/upgrade/canary/revision-tags-after.svg)

Restarting injected workloads in the namespaces marked `prod-stable` will now result in those workloads using the `{{< istio_full_version_revision >}}`
control plane. Notice that no namespace relabeling was required to migrate workloads to the new revision.

#### Default tag

---
---
The revision pointed to by the tag `default` is considered the ***default revision*** and has additional semantic meaning. The default
revision performs the following functions:

- Injects sidecars for the `istio-injection=enabled` namespace selector, the `sidecar.istio.io/inject=true` object
  selector, and the `istio.io/rev=default` selectors
- Validates Istio resources
- Steals the leader lock from non-default revisions and performs singleton mesh responsibilities (such as updating resource statuses)

To make a revision `{{< istio_full_version_revision >}}` the default, run:

```bash
$ helm template istiod istio/istiod -s templates/revision-tags.yaml --set revisionTags="{default}" --set revision=[istio_full_version_revision] -n istio-system | kubectl apply -f -
```

---
---
When using the `default` tag alongside an existing non-revisioned Istio installation it is recommended to remove the old
`MutatingWebhookConfiguration` (typically called `istio-sidecar-injector`) to avoid having both the older and newer control
planes attempt injection.

### In place upgrade

You can perform an in place upgrade of Istio in your cluster using the Helm
upgrade workflow.

> **Warning:**
>
> Add your override values file or custom options to the commands below to
> preserve your custom configuration during Helm upgrades.

---
---

> **Warning:**
>
> If upgrading CRDs via Helm from an Istio release 1.23 or older, you may encounter an error such as the following
>
> `Error: rendered manifests contain a resource that already exists. Unable to continue with update: CustomResourceDefinition "wasmplugins.extensions.istio.io" in namespace "" exists and cannot be imported into the current release: invalid ownership metadata`
>
> You can resolve this with a one-time migration using the following `kubectl` commands:
>
>
>
> ```bash
> $ for crd in $(kubectl get crds -l chart=istio -o name && kubectl get crds -l app.kubernetes.io/part-of=istio -o name)
> $ do
> $    kubectl label "$crd" "app.kubernetes.io/managed-by=Helm"
> $    kubectl annotate "$crd" "meta.helm.sh/release-name=istio-base" # replace with actual Helm release name, if different from the documentation default
> $    kubectl annotate "$crd" "meta.helm.sh/release-namespace=istio-system" # replace with actual istio namespace
> $ done
> ```

1. Upgrade the Istio base chart:

```bash
$ helm upgrade istio-base istio/base -n istio-system
```

1. Upgrade the Istio discovery chart:

```bash
$ helm upgrade istiod istio/istiod -n istio-system
```

1. (Optional) Upgrade and gateway charts  installed in your cluster:

```bash
$ helm upgrade istio-ingress istio/gateway -n istio-ingress
```

## Uninstall

Please refer to the uninstall section in our [Helm install guide](../../install/helm/index.md#uninstall).
