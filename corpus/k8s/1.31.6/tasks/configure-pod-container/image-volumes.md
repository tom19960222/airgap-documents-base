---
collection: k8s
version: "1.31.6"
title: "Use an Image Volume With a Pod"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/configure-pod-container/image-volumes.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

(Feature gate: ImageVolume)

This page shows how to configure a pod using image volumes. This allows you to
mount content from OCI registries inside containers.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)
 

- The container runtime needs to support the image volumes feature
- You need to exec commands in the host
- You need to be able to exec into pods
- You need to enable the `ImageVolume` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)

<!-- steps -->

## Run a Pod that uses an image volume {#create-pod}

An image volume for a pod is enabled by setting the `volumes.[*].image` field of `.spec`
to a valid reference and consuming it in the `volumeMounts` of the container. For example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: image-volume
spec:
  containers:
  - name: shell
    command: ["sleep", "infinity"]
    image: debian
    volumeMounts:
    - name: volume
      mountPath: /volume
  volumes:
  - name: volume
    image:
      reference: quay.io/crio/artifact:v1
      pullPolicy: IfNotPresent
```

1. Create the pod on your cluster:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/image-volumes.yaml
   ```

1. Attach to the container:

   ```shell
   kubectl attach -it image-volume bash
   ```

1. Check the content of a file in the volume:

   ```shell
   cat /volume/dir/file
   ```

   The output is similar to:

   ```none
   1
   ```

   You can also check another file in a different path:

   ```shell
   cat /volume/file
   ```

   The output is similar to:

   ```none
   2
   ```

## Further reading

- [`image` volumes](/docs/concepts/storage/volumes/#image)
