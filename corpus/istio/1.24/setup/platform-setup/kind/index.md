---
collection: istio
version: "1.24"
title: "kind"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/kind/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up kind for Istio."
---
[kind](https://kind.sigs.k8s.io/) is a tool for running local Kubernetes clusters using Docker container `nodes`.
kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.
Follow these instructions to prepare a kind cluster for Istio installation.

## Prerequisites

- Please use the latest Go version.
- To use kind, you will also need to [install docker](https://docs.docker.com/install/).
- Install the latest version of [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
- Increase Docker's [memory limit](../docker/index.md).

## Installation steps

1.  Create a cluster with the following command:

```bash
$ kind create cluster --name istio-testing
```

    `--name` is used to assign a specific name to the cluster. By default, the cluster will be given the name "kind".

1.  To see the list of kind clusters, use the following command:

```bash
$ kind get clusters
istio-testing
```

1.  To list the local Kubernetes contexts, use the following command.

```bash
$ kubectl config get-contexts
CURRENT   NAME                 CLUSTER              AUTHINFO             NAMESPACE
*         kind-istio-testing   kind-istio-testing   kind-istio-testing
          minikube             minikube             minikube
```

> **Tip:**
>
> `kind` is prefixed to the context and cluster names, for example: `kind-istio-testing`

1.  If you run multiple clusters, you need to choose which cluster `kubectl` talks to. You can set a default cluster
    for `kubectl` by setting the current context in the [Kubernetes kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) file. Additionally you can run following command
    to set the current context for `kubectl`.

```bash
$ kubectl config use-context kind-istio-testing
Switched to context "kind-istio-testing".
```

    Once you are done setting up a kind cluster, you can proceed to [install Istio](../../additional-setup/download-istio-release/index.md)
    on it.

1.  When you are done experimenting and you want to delete the existing cluster, use the following command:

```bash
$ kind delete cluster --name istio-testing
Deleting cluster "istio-testing" ...
```

## Setup LoadBalancer for kind

kind does not have any built-in way to provide IP addresses to your `Loadbalancer` service types, to ensure IP address assignments to `Gateway` Services please consult [this guide](https://kind.sigs.k8s.io/docs/user/loadbalancer/) for more information.

## Setup Dashboard UI for kind

kind does not have a built-in Dashboard UI like minikube. But you can still setup Dashboard, a web-based Kubernetes UI, to view your cluster.
Follow these instructions to set up Dashboard for kind.

1.  To deploy Dashboard, run the following command:

```bash
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```

1.  Verify that Dashboard is deployed and running.

```bash
$ kubectl get pod -n kubernetes-dashboard
NAME                                         READY   STATUS    RESTARTS   AGE
dashboard-metrics-scraper-76585494d8-zdb66   1/1     Running   0          39s
kubernetes-dashboard-b7ffbc8cb-zl8zg         1/1     Running   0          39s
```

1.  Create a `ServiceAccount` and `ClusterRoleBinding` to provide admin access to the newly created cluster.

```bash
$ kubectl create serviceaccount -n kubernetes-dashboard admin-user
$ kubectl create clusterrolebinding -n kubernetes-dashboard admin-user --clusterrole cluster-admin --serviceaccount=kubernetes-dashboard:admin-user
```

1.  To log in to your Dashboard, you need a Bearer Token. Use the following command to store the token in a variable.

```bash
$ token=$(kubectl -n kubernetes-dashboard create token admin-user)
```

    Display the token using the `echo` command and copy it to use for logging in to your Dashboard.

```bash
$ echo $token
```

1.  You can access your Dashboard using the kubectl command-line tool by running the following command:

```bash
$ kubectl proxy
Starting to serve on 127.0.0.1:8001
```

    Click [Kubernetes Dashboard](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/) to
    view your deployments and services.

> **Warning:**
>
> You have to save your token somewhere, otherwise you have to run step number 4 everytime you need a token to log in to your Dashboard.
