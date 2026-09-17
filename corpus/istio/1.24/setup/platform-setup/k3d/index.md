---
collection: istio
version: "1.24"
title: "k3d"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/k3d/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up k3d for Istio."
---
k3d is a lightweight wrapper to run [k3s](https://github.com/rancher/k3s) (Rancher Lab’s minimal Kubernetes distribution) in docker.
k3d makes it very easy to create single- and multi-node k3s clusters in docker, e.g. for local development on Kubernetes.

## Prerequisites

- To use k3d, you will also need to [install docker](https://docs.docker.com/install/).
- Install the latest version of [k3d](https://k3d.io/v5.4.7/#installation).
- To interact with the Kubernetes cluster [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- (Optional) [Helm](https://helm.sh/docs/intro/install/) is the package manager for Kubernetes

## Installation

1.  Create a cluster and disable `Traefik` with the following command:

```bash
$ k3d cluster create --api-port 6550 -p '9080:80@loadbalancer' -p '9443:443@loadbalancer' --agents 2 --k3s-arg '--disable=traefik@server:*'
```

1.  To see the list of k3d clusters, use the following command:

```bash
$ k3d cluster list
k3s-default
```

1.  To list the local Kubernetes contexts, use the following command.

```bash
$ kubectl config get-contexts
CURRENT   NAME                 CLUSTER              AUTHINFO             NAMESPACE
*         k3d-k3s-default      k3d-k3s-default      k3d-k3s-default
```

> **Tip:**
>
> `k3d-` is prefixed to the context and cluster names, for example: `k3d-k3s-default`

1.  If you run multiple clusters, you need to choose which cluster `kubectl` talks to. You can set a default cluster
    for `kubectl` by setting the current context in the [Kubernetes kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) file. Additionally you can run following command
    to set the current context for `kubectl`.

```bash
$ kubectl config use-context k3d-k3s-default
Switched to context "k3d-k3s-default".
```

## Set up Istio for k3d

1.  Once you are done setting up a k3d cluster, you can proceed to [install Istio with Helm 3](../../install/helm/index.md) on it.

```bash
$ kubectl create namespace istio-system
$ helm install istio-base istio/base -n istio-system --wait
$ helm install istiod istio/istiod -n istio-system --wait
```

1.  (Optional) Install an ingress gateway:

```bash
$ helm install istio-ingressgateway istio/gateway -n istio-system --wait
```

## Set up Dashboard UI for k3d

k3d does not have a built-in Dashboard UI like minikube. But you can still set up Dashboard, a web based Kubernetes UI, to view your cluster.
Follow these instructions to set up Dashboard for k3d.

1.  To deploy Dashboard, run the following command:

```bash
$ helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
$ helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
```

1.  Verify that Dashboard is deployed and running.

```bash
$ kubectl get pod -n kubernetes-dashboard
NAME                                         READY   STATUS    RESTARTS   AGE
dashboard-metrics-scraper-8c47d4b5d-dd2ks    1/1     Running   0          25s
kubernetes-dashboard-67bd8fc546-4xfmm        1/1     Running   0          25s
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

    Click [Kubernetes Dashboard](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard-web:web/proxy/) to
    view your deployments and services.

> **Warning:**
>
> You have to save your token somewhere, otherwise you have to run step number 4 everytime you need a token to log in to your Dashboard.

## Uninstall

1.  When you are done experimenting and you want to delete the existing cluster, use the following command:

```bash
$ k3d cluster delete k3s-default
Deleting cluster "k3s-default" ...
```
