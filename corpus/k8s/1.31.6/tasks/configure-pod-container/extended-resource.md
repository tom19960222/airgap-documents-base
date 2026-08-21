---
collection: k8s
version: "1.31.6"
title: "Assign Extended Resources to a Container"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/configure-pod-container/extended-resource.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

(Feature state: stable)

This page shows how to assign extended resources to a Container.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)
 

Before you do this exercise, do the exercise in
[Advertise Extended Resources for a Node](/docs/tasks/administer-cluster/extended-resource-node/).
That will configure one of your Nodes to advertise a dongle resource.

<!-- steps -->

## Assign an extended resource to a Pod

To request an extended resource, include the `resources:requests` field in your
Container manifest. Extended resources are fully qualified with any domain outside of
`*.kubernetes.io/`. Valid extended resource names have the form `example.com/foo` where
`example.com` is replaced with your organization's domain and `foo` is a
descriptive resource name.

Here is the configuration file for a Pod that has one Container:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: extended-resource-demo
spec:
  containers:
  - name: extended-resource-demo-ctr
    image: nginx
    resources:
      requests:
        example.com/dongle: 3
      limits:
        example.com/dongle: 3
```

In the configuration file, you can see that the Container requests 3 dongles.

Create a Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/extended-resource-pod.yaml
```

Verify that the Pod is running:

```shell
kubectl get pod extended-resource-demo
```

Describe the Pod:

```shell
kubectl describe pod extended-resource-demo
```

The output shows dongle requests:

```yaml
Limits:
  example.com/dongle: 3
Requests:
  example.com/dongle: 3
```

## Attempt to create a second Pod

Here is the configuration file for a Pod that has one Container. The Container requests
two dongles.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: extended-resource-demo-2
spec:
  containers:
  - name: extended-resource-demo-2-ctr
    image: nginx
    resources:
      requests:
        example.com/dongle: 2
      limits:
        example.com/dongle: 2
```

Kubernetes will not be able to satisfy the request for two dongles, because the first Pod
used three of the four available dongles.

Attempt to create a Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/extended-resource-pod-2.yaml
```

Describe the Pod

```shell
kubectl describe pod extended-resource-demo-2
```

The output shows that the Pod cannot be scheduled, because there is no Node that has
2 dongles available:

```
Conditions:
  Type    Status
  PodScheduled  False
...
Events:
  ...
  ... Warning   FailedScheduling  pod (extended-resource-demo-2) failed to fit in any node
fit failure summary on nodes : Insufficient example.com/dongle (1)
```

View the Pod status:

```shell
kubectl get pod extended-resource-demo-2
```

The output shows that the Pod was created, but not scheduled to run on a Node.
It has a status of Pending:

```yaml
NAME                       READY     STATUS    RESTARTS   AGE
extended-resource-demo-2   0/1       Pending   0          6m
```

## Clean up

Delete the Pods that you created for this exercise:

```shell
kubectl delete pod extended-resource-demo
kubectl delete pod extended-resource-demo-2
```

## What's next

### For application developers

* [Assign Memory Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-memory-resource/)
* [Assign CPU Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-cpu-resource/)

### For cluster administrators

* [Advertise Extended Resources for a Node](/docs/tasks/administer-cluster/extended-resource-node/)
