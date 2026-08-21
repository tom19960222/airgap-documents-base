---
collection: k8s
version: "1.31.6"
title: "Attach Handlers to Container Lifecycle Events"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/configure-pod-container/attach-handler-lifecycle-event.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

This page shows how to attach handlers to Container lifecycle events. Kubernetes supports
the postStart and preStop events. Kubernetes sends the postStart event immediately
after a Container is started, and it sends the preStop event immediately before the
Container is terminated. A Container may specify one handler per event.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)
 

<!-- steps -->

## Define postStart and preStop handlers

In this exercise, you create a Pod that has one Container. The Container has handlers
for the postStart and preStop events.

Here is the configuration file for the Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: lifecycle-demo
spec:
  containers:
  - name: lifecycle-demo-container
    image: nginx
    lifecycle:
      postStart:
        exec:
          command: ["/bin/sh", "-c", "echo Hello from the postStart handler > /usr/share/message"]
      preStop:
        exec:
          command: ["/bin/sh","-c","nginx -s quit; while killall -0 nginx; do sleep 1; done"]
```

In the configuration file, you can see that the postStart command writes a `message`
file to the Container's `/usr/share` directory. The preStop command shuts down
nginx gracefully. This is helpful if the Container is being terminated because of a failure.

Create the Pod:

    kubectl apply -f https://k8s.io/examples/pods/lifecycle-events.yaml

Verify that the Container in the Pod is running:

    kubectl get pod lifecycle-demo

Get a shell into the Container running in your Pod:

    kubectl exec -it lifecycle-demo -- /bin/bash

In your shell, verify that the `postStart` handler created the `message` file:

    root@lifecycle-demo:/# cat /usr/share/message

The output shows the text written by the postStart handler:

    Hello from the postStart handler

<!-- discussion -->

## Discussion

Kubernetes sends the postStart event immediately after the Container is created.
There is no guarantee, however, that the postStart handler is called before
the Container's entrypoint is called. The postStart handler runs asynchronously
relative to the Container's code, but Kubernetes' management of the container
blocks until the postStart handler completes. The Container's status is not
set to RUNNING until the postStart handler completes.

Kubernetes sends the preStop event immediately before the Container is terminated.
Kubernetes' management of the Container blocks until the preStop handler completes,
unless the Pod's grace period expires. For more details, see
[Pod Lifecycle](/docs/concepts/workloads/pods/pod-lifecycle/).

> **Note:**
>
> Kubernetes only sends the preStop event when a Pod or a container in the Pod is *terminated*.
> This means that the preStop hook is not invoked when the Pod is *completed*.
> About this limitation, please see [Container hooks](/docs/concepts/containers/container-lifecycle-hooks/#container-hooks) for the detail.

## What's next

* Learn more about [Container lifecycle hooks](/docs/concepts/containers/container-lifecycle-hooks/).
* Learn more about the [lifecycle of a Pod](/docs/concepts/workloads/pods/pod-lifecycle/).

### Reference

* [Lifecycle](/docs/reference/generated/kubernetes-api/version/#lifecycle-v1-core)
* [Container](/docs/reference/generated/kubernetes-api/version/#container-v1-core)
* See `terminationGracePeriodSeconds` in [PodSpec](/docs/reference/generated/kubernetes-api/version/#podspec-v1-core)
