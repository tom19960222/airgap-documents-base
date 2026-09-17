---
collection: istio
version: "1.24"
title: "Canary Upgrades"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/upgrade/canary/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Upgrade Istio by first running a canary deployment of a new control plane."
---
Upgrading Istio can be done by first running a canary deployment of the new control plane, allowing you
to monitor the effect of the upgrade with a small percentage of the workloads before migrating all of the
traffic to the new version. This is much safer than doing an
[in-place upgrade](../in-place/index.md) and is the recommended upgrade method.

When installing Istio, the `revision` installation setting can be used to deploy multiple independent control planes
at the same time. A canary version of an upgrade can be started by installing the new Istio version's control plane
next to the old one, using a different `revision` setting. Each revision is a full Istio control plane implementation
with its own `Deployment`, `Service`, etc.

## Before you upgrade

Before upgrading Istio, it is recommended to run the `istioctl x precheck` command to make sure the upgrade is compatible with your environment.

```bash
$ istioctl x precheck
✔ No issues found when checking the cluster. Istio is safe to install or upgrade!
  To get started, check out https://istio.io/latest/docs/setup/getting-started/
```

> **Idea:**
>
> When using revision-based upgrades jumping across two minor versions is supported (e.g. upgrading directly from
> version `1.15` to `1.17`). This is in contrast to in-place upgrades where it is required to upgrade to each intermediate minor
> release.

## Control plane

To install a new revision called `canary`, you would set the `revision` field as follows:

> **Tip:**
>
> In a production environment, a better revision name would correspond to the Istio version.
> However, you must replace `.` characters in the revision name, for example, `revision={{< istio_full_version_revision >}}` for Istio `{{< istio_full_version >}}`,
> because `.` is not a valid revision name character.

```bash
$ istioctl install --set revision=canary
```

After running the command, you will have two control plane deployments and services running side-by-side:

```bash
$ kubectl get pods -n istio-system -l app=istiod
NAME                             READY   STATUS    RESTARTS   AGE
istiod-[istio_previous_version_revision]-1-bdf5948d5-htddg    1/1     Running   0          47s
istiod-canary-84c8d4dcfb-skcfv   1/1     Running   0          25s
```

```bash
$ kubectl get svc -n istio-system -l app=istiod
NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                 AGE
istiod-[istio_previous_version_revision]-1   ClusterIP   10.96.93.151     <none>        15010/TCP,15012/TCP,443/TCP,15014/TCP   109s
istiod-canary   ClusterIP   10.104.186.250   <none>        15010/TCP,15012/TCP,443/TCP,15014/TCP   87s
```

You will also see that there are two sidecar injector configurations including the new revision.

```bash
$ kubectl get mutatingwebhookconfigurations
NAME                            WEBHOOKS   AGE
istio-sidecar-injector-[istio_previous_version_revision]-1   2          2m16s
istio-sidecar-injector-canary   2          114s
```

## Data plane

Refer to [Gateway Canary Upgrade](../../additional-setup/gateway/index.md#canary-upgrade-advanced) to understand how to run revision specific instances of Istio gateway.
In this example, since we use the `default` Istio profile, Istio gateways do not run revision-specific instances, but are instead in-place upgraded to use the new control plane revision. You can verify that the `istio-ingress` gateway is using the `canary` revision by running the following command:

```bash
$ istioctl proxy-status | grep "$(kubectl -n istio-system get pod -l app=istio-ingressgateway -o jsonpath='{.items..metadata.name}')" | awk -F '[[:space:]][[:space:]]+' '{print $8}'
istiod-canary-6956db645c-vwhsk
```

However, simply installing the new revision has no impact on the existing sidecar proxies. To upgrade these,
you must configure them to point to the new `istiod-canary` control plane. This is controlled during sidecar injection
based on the namespace label `istio.io/rev`.

Create a namespace `test-ns` with `istio-injection` enabled. In the `test-ns` namespace, deploy a sample curl pod:

1. Create a namespace `test-ns`.

```bash
$ kubectl create ns test-ns
```

1. Label the namespace using `istio-injection` label.

```bash
$ kubectl label namespace test-ns istio-injection=enabled
```

1. Bring up a sample curl pod in `test-ns` namespace.

```bash
$ kubectl apply -n test-ns -f samples/curl/curl.yaml
```

To upgrade the namespace `test-ns`, remove the `istio-injection` label, and add the `istio.io/rev` label to point to the `canary` revision. The `istio-injection` label must be removed because it takes precedence over the `istio.io/rev` label for backward compatibility.

```bash
$ kubectl label namespace test-ns istio-injection- istio.io/rev=canary
```

After the namespace updates, you need to restart the pods to trigger re-injection.
One way to restart all pods in namespace `test-ns` is using:

```bash
$ kubectl rollout restart deployment -n test-ns
```

When the pods are re-injected, they will be configured to point to the `istiod-canary` control plane. You can verify this by using `istioctl proxy-status`.

```bash
$ istioctl proxy-status | grep "\.test-ns "
```

The output will show all pods under the namespace that are using the canary revision.

## Stable revision labels

> **Tip:**
>
> If you're using Helm, refer to the [Helm upgrade documentation](../helm/index.md).

---
---
Manually relabeling namespaces when moving them to a new revision can be tedious and error-prone.
[Revision tags](https://istio.io/v1.24/docs/reference/commands/istioctl/#istioctl-tag) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> solve this problem.
[Revision tags](https://istio.io/v1.24/docs/reference/commands/istioctl/#istioctl-tag) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> are stable identifiers that point to revisions and can be used to avoid relabeling namespaces. Rather than relabeling the namespace, a mesh operator can simply change the tag to point to a new revision. All namespaces labeled with that tag will be updated at the same time.

### Usage

---
---
Consider a cluster with two revisions installed, `{{< istio_previous_version_revision >}}-1` and `{{< istio_full_version_revision >}}`. The cluster operator creates a revision tag `prod-stable`,
pointed at the older, stable `{{< istio_previous_version_revision >}}-1` version, and a revision tag `prod-canary` pointed at the newer `{{< istio_full_version_revision >}}` revision. That
state could be reached via the following commands:

1. Install two revisions of control plane:

```bash
$ istioctl install --revision=[istio_previous_version_revision]-1 --set profile=minimal --skip-confirmation
$ istioctl install --revision=[istio_full_version_revision] --set profile=minimal --skip-confirmation
```

1. Create `stable` and `canary` revision tags and associate them to the respective revisions:

```bash
$ istioctl tag set prod-stable --revision [istio_previous_version_revision]-1
$ istioctl tag set prod-canary --revision [istio_full_version_revision]
```

1. Label application namespaces to map to the respective revision tags:

```bash
$ kubectl create ns app-ns-1
$ kubectl label ns app-ns-1 istio.io/rev=prod-stable
$ kubectl create ns app-ns-2
$ kubectl label ns app-ns-2 istio.io/rev=prod-stable
$ kubectl create ns app-ns-3
$ kubectl label ns app-ns-3 istio.io/rev=prod-canary
```

1. Bring up a sample curl pod in each namespace:

```bash
$ kubectl apply -n app-ns-1 -f samples/curl/curl.yaml
$ kubectl apply -n app-ns-2 -f samples/curl/curl.yaml
$ kubectl apply -n app-ns-3 -f samples/curl/curl.yaml
```

1. Verify application to control plane mapping using `istioctl proxy-status` command:

```bash
$ istioctl ps
NAME                                CLUSTER        CDS        LDS        EDS        RDS        ECDS         ISTIOD                             VERSION
curl-78ff5975c6-62pzf.app-ns-3      Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED     NOT SENT     istiod-[istio_full_version_revision]-7f6fc6cfd6-s8zfg     [istio_full_version]
curl-78ff5975c6-8kxpl.app-ns-1      Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED     NOT SENT     istiod-[istio_previous_version_revision]-1-bdf5948d5-n72r2      [istio_previous_version].1
curl-78ff5975c6-8q7m6.app-ns-2      Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED     NOT SENT     istiod-[istio_previous_version_revision]-1-bdf5948d5-n72r2      [istio_previous_version_revision].1
```

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
$ istioctl tag set prod-stable --revision [istio_full_version_revision] --overwrite
```

---
---
Now, the updated mapping between revisions, tags, and namespaces is as shown below:

![Namespace labels unchanged but now all namespaces pointed to [istio_full_version_revision]](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/upgrade/canary/revision-tags-after.svg)

Restarting injected workloads in the namespaces marked `prod-stable` will now result in those workloads using the `{{< istio_full_version_revision >}}`
control plane. Notice that no namespace relabeling was required to migrate workloads to the new revision.

```bash
$ kubectl rollout restart deployment -n app-ns-1
$ kubectl rollout restart deployment -n app-ns-2
```

Verify the application to control plane mapping using `istioctl proxy-status` command:

```bash
$ istioctl ps
NAME                                                   CLUSTER        CDS        LDS        EDS        RDS          ECDS         ISTIOD                             VERSION
curl-5984f48bc7-kmj6x.app-ns-1                         Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED       NOT SENT     istiod-[istio_full_version_revision]-7f6fc6cfd6-jsktb     [istio_full_version]
curl-78ff5975c6-jldk4.app-ns-3                         Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED       NOT SENT     istiod-[istio_full_version_revision]-7f6fc6cfd6-jsktb     [istio_full_version]
curl-7cdd8dccb9-5bq5n.app-ns-2                         Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED       NOT SENT     istiod-[istio_full_version_revision]-7f6fc6cfd6-jsktb     [istio_full_version]
```

### Default tag

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
$ istioctl tag set default --revision [istio_full_version_revision]
```

---
---
When using the `default` tag alongside an existing non-revisioned Istio installation it is recommended to remove the old
`MutatingWebhookConfiguration` (typically called `istio-sidecar-injector`) to avoid having both the older and newer control
planes attempt injection.

## Uninstall old control plane

After upgrading both the control plane and data plane, you can uninstall the old control plane. For example, the following command uninstalls a control plane of revision `{{< istio_previous_version_revision >}}-1`:

```bash
$ istioctl uninstall --revision [istio_previous_version_revision]-1 -y
```

If the old control plane does not have a revision label, uninstall it using its original installation options, for example:

```bash
$ istioctl uninstall -f manifests/profiles/default.yaml -y
```

Confirm that the old control plane has been removed and only the new one still exists in the cluster:

```bash
$ kubectl get pods -n istio-system -l app=istiod
NAME                             READY   STATUS    RESTARTS   AGE
istiod-canary-55887f699c-t8bh8   1/1     Running   0          27m
```

Note that the above instructions only removed the resources for the specified control plane revision, but not cluster-scoped resources shared with other control planes. To uninstall Istio completely, refer to the [uninstall guide](../../install/istioctl/index.md#uninstall-istio).

## Uninstall canary control plane

If you decide to rollback to the old control plane, instead of completing the canary upgrade,
you can uninstall the canary revision using:

```bash
$ istioctl uninstall --revision=canary -y
```

However, in this case you must first reinstall the gateway(s) for the previous revision manually,
because the uninstall command will not automatically revert the previously in-place upgraded ones.

> **Tip:**
>
> Make sure to use the `istioctl` version corresponding to the old control plane to reinstall the
> old gateways and, to avoid downtime, make sure the old gateways are up and running before proceeding
> with the canary uninstall.

## Cleanup

1. Clean up created revisioned tags:

```bash
$ istioctl tag remove prod-stable
$ istioctl tag remove prod-canary
```

1. Clean up the namespaces used for canary upgrade with revision labels example:

```bash
$ kubectl delete ns istio-system test-ns
```

1. Clean up the namespaces used for canary upgrade with revision tags example:

```bash
$ kubectl delete ns istio-system app-ns-1 app-ns-2 app-ns-3
```
