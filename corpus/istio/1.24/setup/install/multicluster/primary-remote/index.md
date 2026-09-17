---
collection: istio
version: "1.24"
title: "Install Primary-Remote"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/multicluster/primary-remote/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Install an Istio mesh across primary and remote clusters."
---
Follow this guide to install the Istio control plane on `cluster1` (the
primary cluster) and configure `cluster2` (the
remote cluster) to use the control plane in `cluster1`.
Both clusters reside on the `network1` network, meaning there is direct
connectivity between the pods in both clusters.

Before proceeding, be sure to complete the steps under
[before you begin](../before-you-begin/index.md).

---
---

> **Tip:**
>
> If you are testing multicluster setup on `kind` you can use [MetalLB](https://metallb.universe.tf/installation/) to make use of `EXTERNAL-IP` for `LoadBalancer` services.

> **Warning:**
>
> These instructions are not suitable for AWS EKS primary cluster deployment.
> The reason behind this incompatibility is that AWS Load Balancers (LB) are
> presented as Fully Qualified Domain Names (FQDN), while the remote cluster
> utilizes the Kubernetes service type `ExternalName`. However, the `ExternalName`
> type exclusively supports IP addresses and does not accommodate FQDNs.

In this configuration, cluster `cluster1` will observe the API Servers in
both clusters for endpoints. In this way, the control plane will be able to
provide service discovery for workloads in both clusters.

Service workloads communicate directly (pod-to-pod) across cluster boundaries.

Services in `cluster2` will reach the control plane in `cluster1` via a
dedicated gateway for [east-west](https://en.wikipedia.org/wiki/East-west_traffic)
traffic.

![Primary and remote clusters on the same network](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/multicluster/primary-remote/arch.svg)

## Configure `cluster1` as a primary

Create the `istioctl` configuration for `cluster1`:

**Tabset (multicluster-primary-remote-install-type-primary-cluster):**

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
      externalIstiod: true
EOF
```

Apply the configuration to `cluster1`:

```bash
$ istioctl install --context="${CTX_CLUSTER1}" -f cluster1.yaml
```

Notice that `values.global.externalIstiod` is set to `true`. This enables the control plane
installed on `cluster1` to also serve as an external control plane for other remote clusters.
When this feature is enabled, `istiod` will attempt to acquire the leadership lock, and consequently manage,
[appropriately annotated](#set-the-control-plane-cluster-for-cluster2) remote clusters that are
attached to it (`cluster2` in this case).

**Tab: Helm**

Install Istio as primary in `cluster1` using the following Helm commands:

Install the `base` chart in `cluster1`:

```bash
$ helm install istio-base istio/base -n istio-system --kube-context "${CTX_CLUSTER1}"
```

Then, install the `istiod` chart in `cluster1` with the following multi-cluster settings:

```bash
$ helm install istiod istio/istiod -n istio-system --kube-context "${CTX_CLUSTER1}" --set global.meshID=mesh1 --set global.externalIstiod=true --set global.multiCluster.clusterName=cluster1 --set global.network=network1
```

Notice that `values.global.externalIstiod` is set to `true`. This enables the control plane
installed on `cluster1` to also serve as an external control plane for other remote clusters.
When this feature is enabled, `istiod` will attempt to acquire the leadership lock, and consequently manage,
[appropriately annotated](#set-the-control-plane-cluster-for-cluster2) remote clusters that are
attached to it (`cluster2` in this case).

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

## Expose the control plane in `cluster1`

Before we can install on `cluster2`, we need to first expose the control plane in
`cluster1` so that services in `cluster2` will be able to access service discovery:

```bash
$ kubectl apply --context="${CTX_CLUSTER1}" -n istio-system -f \
    @samples/multicluster/expose-istiod.yaml@
```

> **Warning:**
>
> If the control-plane was installed with a revision `rev`, use the following command instead:
>
>
>
> ```bash
> $ sed 's/{{.Revision}}/rev/g' @samples/multicluster/expose-istiod-rev.yaml.tmpl@ | kubectl apply --context="${CTX_CLUSTER1}" -n istio-system -f -
> ```

## Set the control plane cluster for `cluster2`

We need identify the external control plane cluster that should manage `cluster2` by annotating the
istio-system namespace:

```bash
$ kubectl --context="${CTX_CLUSTER2}" create namespace istio-system
$ kubectl --context="${CTX_CLUSTER2}" annotate namespace istio-system topology.istio.io/controlPlaneClusters=cluster1
```

Setting the `topology.istio.io/controlPlaneClusters` namespace annotation to `cluster1` instructs the `istiod`
running in the same namespace (istio-system in this case) on `cluster1` to manage `cluster2` when it
is [attached as a remote cluster](#attach-cluster2-as-a-remote-cluster-of-cluster1).

## Configure `cluster2` as a remote

Save the address of `cluster1`’s east-west gateway.

```bash
$ export DISCOVERY_ADDRESS=$(kubectl \
    --context="${CTX_CLUSTER1}" \
    -n istio-system get svc istio-eastwestgateway \
    -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
```

Now create a remote configuration for `cluster2`.

**Tabset (multicluster-primary-remote-install-type-remote-cluster):**

**Tab: IstioOperator**

```bash
$ cat <<EOF > cluster2.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  profile: remote
  values:
    istiodRemote:
      injectionPath: /inject/cluster/cluster2/net/network1
    global:
      remotePilotAddress: ${DISCOVERY_ADDRESS}
EOF
```

Apply the configuration to `cluster2`:

```bash
$ istioctl install --context="${CTX_CLUSTER2}" -f cluster2.yaml
```

**Tab: Helm**

Install Istio as remote in `cluster2` using the following Helm commands:

Install the `base` chart in `cluster2`:

```bash
$ helm install istio-base istio/base -n istio-system --set profile=remote --kube-context "${CTX_CLUSTER2}"
```

Then, install the `istiod` chart in `cluster2` with the following multi-cluster settings:

```bash
$ helm install istiod istio/istiod -n istio-system --set profile=remote --set global.multiCluster.clusterName=cluster2 --set istiodRemote.injectionPath=/inject/cluster/cluster2/net/network1 --set global.configCluster=true --set global.remotePilotAddress="${DISCOVERY_ADDRESS}" --kube-context "${CTX_CLUSTER2}"
```

> **Tip:**
>
> The `remote` profile for the `base` and `istiod` Helm charts is only available from Istio release 1.24 onwards.

> **Tip:**
>
> Here we're configuring the location of the control plane using the `injectionPath` and
> `remotePilotAddress` parameters. Although convenient for demonstration, in a production
> environment it is recommended to instead configure the `injectionURL` parameter using
> properly signed DNS certs similar to the configuration shown in the
> [external control plane instructions](../../external-controlplane/index.md#register-the-new-cluster).

## Attach `cluster2` as a remote cluster of `cluster1`

To attach the remote cluster to its control plane, we give the control
plane in `cluster1` access to the API Server in `cluster2`. This will do the
following:

- Enables the control plane to authenticate connection requests from
  workloads running in `cluster2`. Without API Server access, the control
  plane will reject the requests.

- Enables discovery of service endpoints running in `cluster2`.

Because it has been included in the `topology.istio.io/controlPlaneClusters` namespace
annotation, the control plane on `cluster1` will also:

- Patch certs in the webhooks in `cluster2`.

- Start the namespace controller which writes configmaps in namespaces in `cluster2`.

To provide API Server access to `cluster2`, we generate a remote secret and
apply it to `cluster1`:

```bash
$ istioctl create-remote-secret \
    --context="${CTX_CLUSTER2}" \
    --name=cluster2 | \
    kubectl apply -f - --context="${CTX_CLUSTER1}"
```

**Congratulations!** You successfully installed an Istio mesh across primary
and remote clusters!

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
