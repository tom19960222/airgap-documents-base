---
collection: istio
version: "1.24"
title: "Install Multi-Primary on different networks"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/multicluster/multi-primary_multi-network/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Install an Istio mesh across multiple primary clusters on different networks."
---
Follow this guide to install the Istio control plane on both `cluster1` and
`cluster2`, making each a primary cluster. Cluster
`cluster1` is on the `network1` network, while `cluster2` is on the
`network2` network. This means there is no direct connectivity between pods
across cluster boundaries.

Before proceeding, be sure to complete the steps under
[before you begin](../before-you-begin/index.md).

---
---

> **Tip:**
>
> If you are testing multicluster setup on `kind` you can use [MetalLB](https://metallb.universe.tf/installation/) to make use of `EXTERNAL-IP` for `LoadBalancer` services.

In this configuration, both `cluster1` and `cluster2` observe the API Servers
in each cluster for endpoints.

Service workloads across cluster boundaries communicate indirectly, via
dedicated gateways for [east-west](https://en.wikipedia.org/wiki/East-west_traffic)
traffic. The gateway in each cluster must be reachable from the other cluster.

![Multiple primary clusters on separate networks](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/multicluster/multi-primary_multi-network/arch.svg)

## Set the default network for `cluster1`

If the istio-system namespace is already created, we need to set the cluster's network there:

```bash
$ kubectl --context="${CTX_CLUSTER1}" get namespace istio-system && \
  kubectl --context="${CTX_CLUSTER1}" label namespace istio-system topology.istio.io/network=network1
```

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

## Install the east-west gateway in `cluster1`

Install a gateway in `cluster1` that is dedicated to
[east-west](https://en.wikipedia.org/wiki/East-west_traffic) traffic. By
default, this gateway will be public on the Internet. Production systems may
require additional access restrictions (e.g. via firewall rules) to prevent
external attacks. Check with your cloud vendor to see what options are
available.

**Tabset (east-west-gateway-install-type-cluster-1):**

**Tab: IstioOperator**

```bash
$ @samples/multicluster/gen-eastwest-gateway.sh@ \
    --network network1 | \
    istioctl --context="${CTX_CLUSTER1}" install -y -f -
```

> **Warning:**
>
> If the control-plane was installed with a revision, add the `--revision rev` flag to the `gen-eastwest-gateway.sh` command.

**Tab: Helm**

Install the east-west gateway in `cluster1` using the following Helm command:

```bash
$ helm install istio-eastwestgateway istio/gateway -n istio-system --kube-context "${CTX_CLUSTER1}" --set name=istio-eastwestgateway --set networkGateway=network1
```

> **Warning:**
>
> If the control-plane was installed with a revision, you must add a `--set revision=<my-revision>` flag to the Helm install command.

Wait for the east-west gateway to be assigned an external IP address:

```bash
$ kubectl --context="${CTX_CLUSTER1}" get svc istio-eastwestgateway -n istio-system
NAME                    TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)   AGE
istio-eastwestgateway   LoadBalancer   10.80.6.124   34.75.71.237   ...       51s
```

## Expose services in `cluster1`

Since the clusters are on separate networks, we need to expose all services
(*.local) on the east-west gateway in both clusters. While this gateway is
public on the Internet, services behind it can only be accessed by services
with a trusted mTLS certificate and workload ID, just as if they were on the
same network.

```bash
$ kubectl --context="${CTX_CLUSTER1}" apply -n istio-system -f \
    @samples/multicluster/expose-services.yaml@
```

## Set the default network for `cluster2`

If the istio-system namespace is already created, we need to set the cluster's network there:

```bash
$ kubectl --context="${CTX_CLUSTER2}" get namespace istio-system && \
  kubectl --context="${CTX_CLUSTER2}" label namespace istio-system topology.istio.io/network=network2
```

## Configure cluster2 as a primary

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
      network: network2
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
$ helm install istiod istio/istiod -n istio-system --kube-context "${CTX_CLUSTER2}" --set global.meshID=mesh1 --set global.multiCluster.clusterName=cluster2 --set global.network=network2
```

## Install the east-west gateway in `cluster2`

As we did with `cluster1` above, install a gateway in `cluster2` that is dedicated
to east-west traffic.

**Tabset (east-west-gateway-install-type-cluster-2):**

**Tab: IstioOperator**

```bash
$ @samples/multicluster/gen-eastwest-gateway.sh@ \
    --network network2 | \
    istioctl --context="${CTX_CLUSTER2}" install -y -f -
```

**Tab: Helm**

Install the east-west gateway in `cluster2` using the following Helm command:

```bash
$ helm install istio-eastwestgateway istio/gateway -n istio-system --kube-context "${CTX_CLUSTER2}" --set name=istio-eastwestgateway --set networkGateway=network2
```

> **Warning:**
>
> If the control-plane was installed with a revision, you must add a `--set revision=<my-revision>` flag to the Helm install command.

Wait for the east-west gateway to be assigned an external IP address:

```bash
$ kubectl --context="${CTX_CLUSTER2}" get svc istio-eastwestgateway -n istio-system
NAME                    TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)   AGE
istio-eastwestgateway   LoadBalancer   10.0.12.121   34.122.91.98   ...       51s
```

## Expose services in `cluster2`

As we did with `cluster1` above, expose services via the east-west gateway.

```bash
$ kubectl --context="${CTX_CLUSTER2}" apply -n istio-system -f \
    @samples/multicluster/expose-services.yaml@
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
primary clusters on different networks!

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
$ helm delete istio-eastwestgateway -n istio-system --kube-context "${CTX_CLUSTER1}"
$ helm delete istio-base -n istio-system --kube-context "${CTX_CLUSTER1}"
```

Delete the `istio-system` namespace from `cluster1`:

```bash
$ kubectl delete ns istio-system --context="${CTX_CLUSTER1}"
```

Delete Istio Helm installation from `cluster2`:

```bash
$ helm delete istiod -n istio-system --kube-context "${CTX_CLUSTER2}"
$ helm delete istio-eastwestgateway -n istio-system --kube-context "${CTX_CLUSTER2}"
$ helm delete istio-base -n istio-system --kube-context "${CTX_CLUSTER2}"
```

Delete the `istio-system` namespace from `cluster2`:

```bash
$ kubectl delete ns istio-system --context="${CTX_CLUSTER2}"
```

(Optional) Delete CRDs installed by Istio:

Deleting CRDs permanently removes any Istio resources you have created in your clusters.
To delete Istio CRDs installed in your clusters:

```bash
$ kubectl get crd -oname --context "${CTX_CLUSTER1}" | grep --color=never 'istio.io' | xargs kubectl delete --context "${CTX_CLUSTER1}"
$ kubectl get crd -oname --context "${CTX_CLUSTER2}" | grep --color=never 'istio.io' | xargs kubectl delete --context "${CTX_CLUSTER2}"
```
