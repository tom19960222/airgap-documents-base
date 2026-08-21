---
collection: rook
version: "1.17.2"
title: "Import Ceph configuration to the Rook consumer cluster"
source_url: https://rook.io/docs/rook/v1.17/CRDs/Cluster/external-cluster/consumer-import/
fetched_at: 2026-08-21T02:34:26+00:00
---
# Import Ceph configuration to the Rook consumer cluster

## Installation types

Install Rook in the the consumer cluster, either with [Helm](index.md#helm-installation) or the [manifests](index.md#manifest-installation).

### Helm Installation

To install with Helm, the rook cluster helm chart will configure the necessary resources for the external cluster with the example `values-external.yaml`.

```
clusterNamespace=rook-ceph
operatorNamespace=rook-ceph
cd deploy/examples/charts/rook-ceph-cluster
helm repo add rook-release https://charts.rook.io/release
helm install --create-namespace --namespace $clusterNamespace rook-ceph rook-release/rook-ceph -f values.yaml
helm install --create-namespace --namespace $clusterNamespace rook-ceph-cluster \
--set operatorNamespace=$operatorNamespace rook-release/rook-ceph-cluster -f values-external.yaml
```

### Manifest Installation

If not installing with Helm, here are the steps to install with manifests.

1. Deploy Rook, create [common.yaml](https://github.com/rook/rook/blob/master/deploy/examples/common.yaml), [crds.yaml](https://github.com/rook/rook/blob/master/deploy/examples/crds.yaml) and [operator.yaml](https://github.com/rook/rook/blob/release-1.17/deploy/examples/operator.yaml) manifests.
2. Create [common-external.yaml](https://github.com/rook/rook/blob/master/deploy/examples/external/common-external.yaml) and [cluster-external.yaml](https://github.com/rook/rook/blob/release-1.17/deploy/examples/external/cluster-external.yaml)

## Import the Provider Data

1. Paste the above output from `create-external-cluster-resources.py` into your current shell to allow importing the provider data.
2. The import script in the next step uses the current kubeconfig context by default. If you want to specify the kubernetes cluster to use without changing the current context, you can specify the cluster name by setting the KUBECONTEXT environment variable.

   ```
   export KUBECONTEXT=<cluster-name>
   ```
3. Here is the link for [import](https://github.com/rook/rook/blob/release-1.17/deploy/examples/external/import-external-cluster.sh) script. The script has used the `rook-ceph` namespace and few parameters that also have referenced from namespace variable. If user's external cluster has a different namespace, change the namespace parameter in the script according to their external cluster. For example with `new-namespace` namespace, this change is needed on the namespace parameter in the script.

   ```
   NAMESPACE=${NAMESPACE:="new-namespace"}
   ```
4. Run the import script.

   > **Note:**
   >
   > If your Rook cluster nodes are running a kernel earlier than or equivalent to 5.4, remove `fast-diff, object-map, deep-flatten,exclusive-lock` from the `imageFeatures` line.

   ```
   . import-external-cluster.sh
   ```

## Cluster Verification

1. Verify the consumer cluster is connected to the provider ceph cluster:

   ```
   $ kubectl -n rook-ceph  get CephCluster
   NAME                 DATADIRHOSTPATH   MONCOUNT   AGE    STATE       HEALTH
   rook-ceph-external   /var/lib/rook                162m   Connected   HEALTH_OK
   ```
2. Verify the creation of the storage class depending on the rbd pools and filesystem provided. `ceph-rbd` and `cephfs` would be the respective names for the RBD and CephFS storage classes.

   ```
   kubectl -n rook-ceph get sc
   ```
3. Create a [persistent volume](https://github.com/rook/rook/tree/release-1.17/deploy/examples/csi) based on these StorageClass.
