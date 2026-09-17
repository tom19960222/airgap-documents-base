---
collection: istio
version: "1.24"
title: "Before you begin"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/locality-load-balancing/before-you-begin/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Initial steps before configuring locality load balancing."
---
Before you begin the locality load balancing tasks, you must first
[install Istio on multiple clusters](../../../../setup/install/multicluster/_index.md). The
clusters must span three regions, containing four availability zones. The
number of clusters required may vary based on the capabilities offered by
your cloud provider.

> **Tip:**
>
> For simplicity, we will assume that there is only a single
> primary cluster in the mesh. This simplifies
> the process of configuring the control plane, since changes only need to be
> applied to one cluster.

We will deploy several instances of the `HelloWorld` application as follows:

![Setup for locality load balancing tasks](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/locality-load-balancing/before-you-begin/setup.svg)

> **Tip:**
>
> In a single multi-zone cluster environment, locality load balancing can also be configured for failover to a different zone within the same cluster.
> To test it, you will need to create a cluster with multiple worker zones and deploy an istiod instance and the app to each zone.
>
> 1: If you don’t have a multi-zone Kubernetes cluster, you can deploy one locally using `kind` with the following command:
>
>
>
> ```bash
> $ kind create cluster --config=- <<EOF
> kind: Cluster
> apiVersion: kind.x-k8s.io/v1alpha4
> nodes:
> - role: control-plane
> - role: worker
> - role: worker
> - role: worker
> EOF
> ```
>
>
>
> 2: Use `topology.kubernetes.io/zone` to label each worker with a zone name:
>
>
>
> ```bash
> $ kubectl label node kind-worker topology.kubernetes.io/zone=us-south10
> $ kubectl label node kind-worker2 topology.kubernetes.io/zone=us-south12
> $ kubectl label node kind-worker3 topology.kubernetes.io/zone=us-south13
> ```
>
>
>
> 3: Deploy istiod to the control-plane node and the helloworld app to each of the worker nodes.

## Environment Variables

This guide assumes that all clusters will be accessed through contexts in the
default [Kubernetes configuration file](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/).
The following environment variables will be used for the various contexts:

Variable | Description
-------- | -----------
`CTX_PRIMARY` | The context used for applying configuration to the primary cluster.
`CTX_R1_Z1` | The context used to interact with pods in `region1.zone1`.
`CTX_R1_Z2` | The context used to interact with pods in `region1.zone2`.
`CTX_R2_Z3` | The context used to interact with pods in `region2.zone3`.
`CTX_R3_Z4` | The context used to interact with pods in `region3.zone4`.

## Create the `sample` namespace

To begin, generate yaml for the `sample` namespace with automatic sidecar
injection enabled:

```bash
$ cat <<EOF > sample.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: sample
  labels:
    istio-injection: enabled
EOF
```

Add the `sample` namespace to each cluster:

```bash
$ for CTX in "$CTX_PRIMARY" "$CTX_R1_Z1" "$CTX_R1_Z2" "$CTX_R2_Z3" "$CTX_R3_Z4"; \
  do \
    kubectl --context="$CTX" apply -f sample.yaml; \
  done
```

## Deploy `HelloWorld`

Generate the `HelloWorld` YAML for each locality, using the
locality as the version string:

```bash
$ for LOC in "region1.zone1" "region1.zone2" "region2.zone3" "region3.zone4"; \
  do \
    ./@samples/helloworld/gen-helloworld.sh@ \
      --version "$LOC" > "helloworld-${LOC}.yaml"; \
  done
```

Apply the `HelloWorld` YAML to the appropriate cluster for each locality:

```bash
$ kubectl apply --context="${CTX_R1_Z1}" -n sample \
  -f helloworld-region1.zone1.yaml
```

```bash
$ kubectl apply --context="${CTX_R1_Z2}" -n sample \
  -f helloworld-region1.zone2.yaml
```

```bash
$ kubectl apply --context="${CTX_R2_Z3}" -n sample \
  -f helloworld-region2.zone3.yaml
```

```bash
$ kubectl apply --context="${CTX_R3_Z4}" -n sample \
  -f helloworld-region3.zone4.yaml
```

## Deploy `curl`

Deploy the `curl` application to `region1` `zone1`:

```bash
$ kubectl apply --context="${CTX_R1_Z1}" \
  -f @samples/curl/curl.yaml@ -n sample
```

## Wait for `HelloWorld` pods

Wait until the `HelloWorld` pods in each zone are `Running`:

```bash
$ kubectl get pod --context="${CTX_R1_Z1}" -n sample -l app="helloworld" \
  -l version="region1.zone1"
NAME                                       READY   STATUS    RESTARTS   AGE
helloworld-region1.zone1-86f77cd7b-cpxhv   2/2     Running   0          30s
```

```bash
$ kubectl get pod --context="${CTX_R1_Z2}" -n sample -l app="helloworld" \
  -l version="region1.zone2"
NAME                                       READY   STATUS    RESTARTS   AGE
helloworld-region1.zone2-86f77cd7b-cpxhv   2/2     Running   0          30s
```

```bash
$ kubectl get pod --context="${CTX_R2_Z3}" -n sample -l app="helloworld" \
  -l version="region2.zone3"
NAME                                       READY   STATUS    RESTARTS   AGE
helloworld-region2.zone3-86f77cd7b-cpxhv   2/2     Running   0          30s
```

```bash
$ kubectl get pod --context="${CTX_R3_Z4}" -n sample -l app="helloworld" \
  -l version="region3.zone4"
NAME                                       READY   STATUS    RESTARTS   AGE
helloworld-region3.zone4-86f77cd7b-cpxhv   2/2     Running   0          30s
```

**Congratulations!** You successfully configured the system and are now ready
to begin the locality load balancing tasks!

## Next steps

You can now configure one of the following load balancing options:

- [Locality failover](../failover/index.md)

- [Locality weighted distribution](../distribute/index.md)

> **Warning:**
>
> Only one of the load balancing options should be configured, as they are
> mutually exclusive. Attempting to configure both may lead to unexpected
> behavior.
