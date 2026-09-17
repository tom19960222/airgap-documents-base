---
collection: istio
version: "1.24"
title: "Verify the installation"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/install/multicluster/verify/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Verify that Istio has been installed properly on multiple clusters."
---
Follow this guide to verify that your multicluster Istio installation is working
properly.

Before proceeding, be sure to complete the steps under
[before you begin](../before-you-begin/index.md) as well as
choosing and following one of the multicluster installation guides.

In this guide, we will deploy the `HelloWorld` application `V1` to `cluster1`
and `V2` to `cluster2`. Upon receiving a request, `HelloWorld` will include
its version in its response.

We will also deploy the `curl` container to both clusters. We will use these
pods as the source of requests to the `HelloWorld` service,
simulating in-mesh traffic. Finally, after generating traffic, we will observe
which cluster received the requests.

## Deploy the `HelloWorld` Service

In order to make the `HelloWorld` service callable from any cluster, the DNS
lookup must succeed in each cluster (see
[deployment models](../../../../ops/deployment/deployment-models/index.md#dns-with-multiple-clusters)
for details). We will address this by deploying the `HelloWorld` Service to
each cluster in the mesh.

To begin, create the `sample` namespace in each cluster:

```bash
$ kubectl create --context="${CTX_CLUSTER1}" namespace sample
$ kubectl create --context="${CTX_CLUSTER2}" namespace sample
```

Enable automatic sidecar injection for the `sample` namespace:

```bash
$ kubectl label --context="${CTX_CLUSTER1}" namespace sample \
    istio-injection=enabled
$ kubectl label --context="${CTX_CLUSTER2}" namespace sample \
    istio-injection=enabled
```

Create the `HelloWorld` service in both clusters:

```bash
$ kubectl apply --context="${CTX_CLUSTER1}" \
    -f @samples/helloworld/helloworld.yaml@ \
    -l service=helloworld -n sample
$ kubectl apply --context="${CTX_CLUSTER2}" \
    -f @samples/helloworld/helloworld.yaml@ \
    -l service=helloworld -n sample
```

## Deploy `HelloWorld` `V1`

Deploy the `helloworld-v1` application to `cluster1`:

```bash
$ kubectl apply --context="${CTX_CLUSTER1}" \
    -f @samples/helloworld/helloworld.yaml@ \
    -l version=v1 -n sample
```

Confirm the `helloworld-v1` pod status:

```bash
$ kubectl get pod --context="${CTX_CLUSTER1}" -n sample -l app=helloworld
NAME                            READY     STATUS    RESTARTS   AGE
helloworld-v1-86f77cd7bd-cpxhv  2/2       Running   0          40s
```

Wait until the status of `helloworld-v1` is `Running`.

## Deploy `HelloWorld` `V2`

Deploy the `helloworld-v2` application to `cluster2`:

```bash
$ kubectl apply --context="${CTX_CLUSTER2}" \
    -f @samples/helloworld/helloworld.yaml@ \
    -l version=v2 -n sample
```

Confirm the status the `helloworld-v2` pod status:

```bash
$ kubectl get pod --context="${CTX_CLUSTER2}" -n sample -l app=helloworld
NAME                            READY     STATUS    RESTARTS   AGE
helloworld-v2-758dd55874-6x4t8  2/2       Running   0          40s
```

Wait until the status of `helloworld-v2` is `Running`.

## Deploy `curl`

Deploy the `curl` application to both clusters:

```bash
$ kubectl apply --context="${CTX_CLUSTER1}" \
    -f @samples/curl/curl.yaml@ -n sample
$ kubectl apply --context="${CTX_CLUSTER2}" \
    -f @samples/curl/curl.yaml@ -n sample
```

Confirm the status `curl` pod on `cluster1`:

```bash
$ kubectl get pod --context="${CTX_CLUSTER1}" -n sample -l app=curl
NAME                             READY   STATUS    RESTARTS   AGE
curl-754684654f-n6bzf            2/2     Running   0          5s
```

Wait until the status of the `curl` pod is `Running`.

Confirm the status of the `curl` pod on `cluster2`:

```bash
$ kubectl get pod --context="${CTX_CLUSTER2}" -n sample -l app=curl
NAME                             READY   STATUS    RESTARTS   AGE
curl-754684654f-dzl9j            2/2     Running   0          5s
```

Wait until the status of the `curl` pod is `Running`.

## Verifying Cross-Cluster Traffic

To verify that cross-cluster load balancing works as expected, call the
`HelloWorld` service several times using the `curl` pod. To ensure load
balancing is working properly, call the `HelloWorld` service from all
clusters in your deployment.

Send one request from the `curl` pod on `cluster1` to the `HelloWorld` service:

```bash
$ kubectl exec --context="${CTX_CLUSTER1}" -n sample -c curl \
    "$(kubectl get pod --context="${CTX_CLUSTER1}" -n sample -l \
    app=curl -o jsonpath='{.items[0].metadata.name}')" \
    -- curl -sS helloworld.sample:5000/hello
```

Repeat this request several times and verify that the `HelloWorld` version
should toggle between `v1` and `v2`:

```plain
Hello version: v2, instance: helloworld-v2-758dd55874-6x4t8
Hello version: v1, instance: helloworld-v1-86f77cd7bd-cpxhv
...
```

Now repeat this process from the `curl` pod on `cluster2`:

```bash
$ kubectl exec --context="${CTX_CLUSTER2}" -n sample -c curl \
    "$(kubectl get pod --context="${CTX_CLUSTER2}" -n sample -l \
    app=curl -o jsonpath='{.items[0].metadata.name}')" \
    -- curl -sS helloworld.sample:5000/hello
```

Repeat this request several times and verify that the `HelloWorld` version
should toggle between `v1` and `v2`:

```plain
Hello version: v2, instance: helloworld-v2-758dd55874-6x4t8
Hello version: v1, instance: helloworld-v1-86f77cd7bd-cpxhv
...
```

**Congratulations!** You successfully installed and verified Istio on multiple
clusters!

## Next Steps

Check out the [locality load balancing tasks](../../../../tasks/traffic-management/locality-load-balancing/_index.md)
to learn how to control the traffic across a multicluster mesh.
