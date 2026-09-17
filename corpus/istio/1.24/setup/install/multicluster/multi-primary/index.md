---
collection: istio
version: "1.24"
title: "Install Multi-Primary"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/multicluster/multi-primary/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Install an Istio mesh across multiple primary clusters."
---
Follow this guide to install the Istio control plane on both `cluster1` and
`cluster2`, making each a primary cluster. Both
clusters reside on the `network1` network, meaning there is direct
connectivity between the pods in both clusters.

Before proceeding, be sure to complete the steps under
[before you begin](../before-you-begin/index.md).

In this configuration, each control plane observes the API Servers in both
clusters for endpoints.

Service workloads communicate directly (pod-to-pod) across cluster boundaries.

![Multiple primary clusters on the same network](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/multicluster/multi-primary/arch.svg)

## Configure `cluster1` as a primary

Create the `istioctl` configuration for `cluster1`:

**Tabset (multicluster-install-type-cluster-1):**

**Tab: IstioOperator**

Install Istio as primary in `cluster1` using istioctl and the `IstioOperator` API.

```bash
$ cat <<EOF > cluster1.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  values:
    global:
      meshID: mesh1
      multiCluster:
        clusterName: cluster1
      network: network1
EOF
```

Apply the configuration to `cluster1`:

```bash
$ istioctl install --context="${CTX_CLUSTER1}" -f cluster1.yaml
```

**Tab: Helm**

Install Istio as primary in `cluster1` using the following Helm commands:

Install the `base` chart in `cluster1`:

```bash
$ helm install istio-base istio/base -n istio-system --kube-context "${CTX_CLUSTER1}"
```

Then, install the `istiod` chart in `cluster1` with the following multi-cluster settings:

```bash
$ helm install istiod istio/istiod -n istio-system --kube-context "${CTX_CLUSTER1}" --set global.meshID=mesh1 --set global.multiCluster.clusterName=cluster1 --set global.network=network1
```

## Configure `cluster2` as a primary

Create the `istioctl` configuration for `cluster2`:

**Tabset (multicluster-install-type-cluster-2):**

**Tab: IstioOperator**

Install Istio as primary in `cluster2` using istioctl and the `IstioOperator` API.

```bash
$ cat <<EOF > cluster2.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  values:
    global:
      meshID: mesh1
      multiCluster:
        clusterName: cluster2
      network: network1
EOF
```

Apply the configuration to `cluster2`:

```bash
$ istioctl install --context="${CTX_CLUSTER2}" -f cluster2.yaml
```

**Tab: Helm**

Install Istio as primary in `cluster2` using the following Helm commands:

Install the `base` chart in `cluster2`:

```bash
$ helm install istio-base istio/base -n istio-system --kube-context "${CTX_CLUSTER2}"
```

Then, install the `istiod` chart in `cluster2` with the following multi-cluster settings:

```bash
$ helm install istiod istio/istiod -n istio-system --kube-context "${CTX_CLUSTER2}" --set global.meshID=mesh1 --set global.multiCluster.clusterName=cluster2 --set global.network=network1
```

## Enable Endpoint Discovery

Install a remote secret in `cluster2` that provides access to `cluster1`’s API server.

```bash
$ istioctl create-remote-secret \
    --context="${CTX_CLUSTER1}" \
    --name=cluster1 | \
    kubectl apply -f - --context="${CTX_CLUSTER2}"
```

Install a remote secret in `cluster1` that provides access to `cluster2`’s API server.

```bash
$ istioctl create-remote-secret \
    --context="${CTX_CLUSTER2}" \
    --name=cluster2 | \
    kubectl apply -f - --context="${CTX_CLUSTER1}"
```

**Congratulations!** You successfully installed an Istio mesh across multiple
primary clusters!

## Next Steps

You can now [verify the installation](../verify/index.md).

## Cleanup

Uninstall Istio from both `cluster1` and `cluster2` using the same mechanism you installed Istio with (istioctl or Helm).

**Tabset (multicluster-uninstall-type-cluster-1):**

**Tab: IstioOperator**

Uninstall Istio in `cluster1`:

```bash
$ istioctl uninstall --context="${CTX_CLUSTER1}" -y --purge
$ kubectl delete ns istio-system --context="${CTX_CLUSTER1}"
```

Uninstall Istio in `cluster2`:

```bash
$ istioctl uninstall --context="${CTX_CLUSTER2}" -y --purge
$ kubectl delete ns istio-system --context="${CTX_CLUSTER2}"
```

**Tab: Helm**

Delete Istio Helm installation from `cluster1`:

```bash
$ helm delete istiod -n istio-system --kube-context "${CTX_CLUSTER1}"
$ helm delete istio-base -n istio-system --kube-context "${CTX_CLUSTER1}"
```

Delete the `istio-system` namespace from `cluster1`:

```bash
$ kubectl delete ns istio-system --context="${CTX_CLUSTER1}"
```

Delete Istio Helm installation from `cluster2`:

```bash
$ helm delete istiod -n istio-system --kube-context "${CTX_CLUSTER2}"
$ helm delete istio-base -n istio-system --kube-context "${CTX_CLUSTER2}"
```

Delete the `istio-system` namespace from `cluster2`:

```bash
$ kubectl delete ns istio-system --context="${CTX_CLUSTER2}"
```

(Optional) Delete CRDs installed by Istio:

Deleting CRDs permanently removes any Istio resources you have created in your clusters.
Delete Istio CRDs installed in your clusters by running:

```bash
$ kubectl get crd -oname --context "${CTX_CLUSTER1}" | grep --color=never 'istio.io' | xargs kubectl delete --context "${CTX_CLUSTER1}"
$ kubectl get crd -oname --context "${CTX_CLUSTER2}" | grep --color=never 'istio.io' | xargs kubectl delete --context "${CTX_CLUSTER2}"
```
