---
collection: istio
version: "1.24"
title: "Upgrade with Helm"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/upgrade/helm/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Upgrading an ambient mode installation with Helm."
---
Follow this guide to upgrade and configure an ambient mode installation using
[Helm](https://helm.sh/docs/). This guide assumes you have already performed an [ambient mode installation with Helm](../../install/helm/index.md) with a previous version of Istio.

> **Warning:**
>
> In contrast to sidecar mode, ambient mode supports moving application pods to an upgraded ztunnel proxy without a mandatory restart or reschedule of running application pods. However, upgrading ztunnel **will** cause all long-lived TCP connections on the upgraded node to reset, and Istio does not currently support canary upgrades of ztunnel, **even with the use of revisions**.
>
> Node cordoning and blue/green node pools are recommended to limit the blast radius of resets on application traffic during production upgrades. See your Kubernetes provider documentation for details.

## Understanding ambient mode upgrades

All Istio upgrades involve upgrading the control plane, data plane, and Istio CRDs. Because the ambient data plane is split across [two components](../../architecture/data-plane/index.md), the ztunnel and gateways (which includes waypoints), upgrades involve separate steps for these components. Upgrading the control plane and CRDs is covered here in brief, but is essentially identical to [the process for upgrading these components in sidecar mode](../../../setup/upgrade/canary/index.md).

Like sidecar mode, gateways can make use of [revision tags](../../../setup/upgrade/canary/index.md#stable-revision-labels) to allow fine-grained control over (gateway) upgrades, including waypoints, with simple controls for rolling back to a previous version of the Istio control plane at any point. However, unlike sidecar mode, the ztunnel runs as a DaemonSet — a per-node proxy — meaning that ztunnel upgrades affect, at minimum, an entire node at a time. While this may be acceptable in many cases, applications with long-lived TCP connections may be disrupted.  In such cases, we recommend using node cordoning and draining before upgrading the ztunnel for a given node. For the sake of simplicity, this document will demonstrate in-place upgrades of the ztunnel, which may involve a short downtime.

## Prerequisites

### Prepare for the upgrade

Before upgrading Istio, we recommend downloading the new version of istioctl, and running `istioctl x precheck` to make sure the upgrade is compatible with your environment. The output should look something like this:

```bash
$ istioctl x precheck
✔ No issues found when checking the cluster. Istio is safe to install or upgrade!
  To get started, check out <https://istio.io/latest/docs/setup/getting-started/>
```

Now, update the Helm repository:

```bash
$ helm repo update istio
```

**Tabset (upgrade-prerequisites):**

**Tab: In-place upgrade**

No additional preparations for in-place upgrades, proceed to the next step.

**Tab: Revisioned upgrade**

### Organize your tags and revisions

In order to upgrade a mesh in ambient mode in a controlled manner, we recommend that your gateways and namespaces use the `istio.io/rev` label to specify a revision tag to control which gateway and control plane versions will be used to manage traffic for your workloads. We recommend dividing your production cluster into multiple tags to organize your upgrade. All members of a given tag will be upgraded simultaneously, so it is wise to begin your upgrade with your lowest risk applications. We do not recommend referencing revisions directly via labels for upgrades, as this process can easily result in the accidental upgrade of a large number of proxies, and is difficult to segment. To see what tags and revisions you are using in your cluster, see the section on upgrading tags.

### Choose a revision name

Revisions identify unique instances of the Istio control plane, allowing you to run multiple distinct versions of the control plane simultaneously in a single mesh.

It is recommended that revisions stay immutable, that is, once a control plane is installed with a particular revision name, the installation should not be modified, and the revision name should not be reused. Tags, on the other hand, are mutable pointers to revisions. This enables a cluster operator to effect data plane upgrades without the need to adjust any workload labels, simply by moving a tag from one revision to the next. All data planes will connect only to one control plane, specified by the `istio.io/rev` label (pointing to either a revision or tag), or by the default revision if no `istio.io/rev` label is present. Upgrading a data plane consists of simply changing the control plane it is pointed to via modifying labels or editing tags.

Because revisions are intended to be immutable, we recommend choosing a revision name that corresponds with the version of Istio you are installing, such as `1-22-1`. In addition to choosing a new revision name, you should note your current revision name. You can find this by running:

```bash
$ kubectl get mutatingwebhookconfigurations -l 'istio.io/rev,!istio.io/tag' -L istio\.io/rev
$ # Store your revision and new revision in variables:
$ export REVISION=istio-1-22-1
$ export OLD_REVISION=istio-1-21-2
```

## Upgrade the control plane

### Base components

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

The cluster-wide Custom Resource Definitions (CRDs) must be upgraded prior to the deployment of a new version of the control plane:

```bash
$ helm upgrade istio-base istio/base -n istio-system
```

### istiod control plane

The [Istiod](../../../ops/deployment/architecture/index.md#istiod) control plane manages and configures the proxies that route traffic within the mesh. The following command will install a new instance of the control plane alongside the current one, but will not introduce any new gateway proxies or waypoints, or take over control of existing ones.

If you have customized your istiod installation, you can reuse the `values.yaml` file from previous upgrades or installs to keep your control planes consistent.

**Tabset (upgrade-control-plane):**

**Tab: In-place upgrade**

```bash
$ helm upgrade istiod istio/istiod -n istio-system --wait
```

**Tab: Revisioned upgrade**

```bash
$ helm install istiod-"$REVISION" istio/istiod -n istio-system --set revision="$REVISION" --set profile=ambient --wait
```

### CNI node agent

The Istio CNI node agent is responsible for detecting pods added to the ambient mesh, informing ztunnel that proxy ports should be established within added pods, and configuring traffic redirection within the pod network namespace. It is not part of the data plane or control plane.

The CNI at version 1.x is compatible with the control plane at version 1.x+1 and 1.x. This means the control plane must be upgraded before Istio CNI, as long as their version difference is within one minor version.

> **Warning:**
>
> Istio does not currently support canary upgrades of istio-cni, **even with the use of revisions**.
>
> Upgrading the Istio CNI node agent to a compatible version in-place will not disrupt networking for running pods already successfully added to an ambient mesh, but no new pods should be scheduled on the node until the upgrade is complete and the upgraded Istio CNI agent on the node passes readiness checks. If this is a significant disruption concern, or stricter blast radius controls are desired for CNI upgrades, node taints and/or node cordons are recommended.

```bash
$ helm upgrade istio-cni istio/cni -n istio-system
```

## Upgrade the data plane

### ztunnel DaemonSet

The ztunnel DaemonSet is the node proxy component. The ztunnel at version 1.x is compatible with the control plane at version 1.x+1 and 1.x. This means the control plane must be upgraded before ztunnel, as long as their version difference is within one minor version. If you have previously customized your ztunnel installation, you can reuse the `values.yaml` file from previous upgrades or installs to keep your data plane consistent.

> **Warning:**
>
> Upgrading ztunnel in-place will briefly disrupt all ambient mesh traffic on the node,  **even with the use of revisions**. In practice the disruption period is a very small window, primarily affecting long-running connections.
>
> Node cordoning and blue/green node pools are recommended to mitigate blast radius risk during production upgrades. See your Kubernetes provider documentation for details.

**Tabset (upgrade-ztunnel):**

**Tab: In-place upgrade**

```bash
$ helm upgrade ztunnel istio/ztunnel -n istio-system --wait
```

**Tab: Revisioned upgrade**

```bash
$ helm upgrade ztunnel istio/ztunnel -n istio-system --set revision="$REVISION" --wait
```

**Tabset (change-gateway-revision):**

**Tab: In-place upgrade**

### Upgrade manually deployed gateway chart (optional)

`Gateway`s that were [deployed manually](../../../tasks/traffic-management/ingress/gateway-api/index.md#manual-deployment) must be upgraded individually using Helm:

```bash
$ helm upgrade istio-ingress istio/gateway -n istio-ingress
```

**Tab: Revisioned upgrade**

### Upgrade waypoints and gateways using tags

If you have followed best practices, all of your gateways, workloads, and namespaces use either the default revision (effectively, a tag named `default`), or the `istio.io/rev` label with the value set to a tag name. You can now upgrade all of these to the new version of the Istio data plane by moving their tags to point to the new version, one at a time. To list all tags in your cluster, run:

```bash
$ kubectl get mutatingwebhookconfigurations -l 'istio.io/tag' -L istio\.io/tag,istio\.io/rev
```

For each tag, you can upgrade the tag by running the following command, replacing `$MYTAG` with your tag name, and `$REVISION` with your revision name:

```bash
$ helm template istiod istio/istiod -s templates/revision-tags.yaml --set revisionTags="{$MYTAG}" --set revision="$REVISION" -n istio-system | kubectl apply -f -
```

This will upgrade all objects referencing that tag, except for those using [manual gateway deployment mode](../../../tasks/traffic-management/ingress/gateway-api/index.md#manual-deployment), which are dealt with below, and sidecars, which are not used in ambient mode.

It is recommended that you closely monitor the health of applications using the upgraded data plane before upgrading the next tag. If you detect a problem, you can rollback a tag, resetting it to point to the name of your old revision:

```bash
$ helm template istiod istio/istiod -s templates/revision-tags.yaml --set revisionTags="{$MYTAG}" --set revision="$OLD_REVISION" -n istio-system | kubectl apply -f -
```

### Upgrade manually deployed gateways (optional)

`Gateway`s that were [deployed manually](../../../tasks/traffic-management/ingress/gateway-api/index.md#manual-deployment) must be upgraded individually using Helm:

```bash
$ helm upgrade istio-ingress istio/gateway -n istio-ingress
```

## Uninstall the previous control plane

If you have upgraded all data plane components to use the new revision of the Istio control plane, and are satisfied that you do not need to roll back, you can remove the previous revision of the control plane by running:

```bash
$ helm delete istiod-"$OLD_REVISION" -n istio-system
```
