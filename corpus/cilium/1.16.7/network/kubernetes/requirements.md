---
collection: cilium
version: "1.16.7"
title: "Requirements"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/kubernetes/requirements.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="k8s_requirements"></a>

# Requirements

## Kubernetes Version

All Kubernetes versions listed are e2e tested and guaranteed to be compatible
with this Cilium version. Older Kubernetes versions not listed here do not have
Cilium support. Newer Kubernetes versions, while not listed, will depend on the
backward compatibility offered by Kubernetes.

* 1.27
* 1.28
* 1.29
* 1.30

Additionally, Cilium runs e2e tests against various cloud providers' managed
Kubernetes offerings using multiple Kubernetes versions. See the following links
for the current test matrix for each cloud provider:

- AKS
- EKS
- GKE

## System Requirements

See [admin_system_reqs](../../operations/system_requirements.md#admin_system_reqs) for all of the Cilium system requirements.

## Enable CNI in Kubernetes

CNI - Container Network Interface is the plugin layer used by Kubernetes to
delegate networking configuration and is enabled by default in Kubernetes 1.24 and
later. Previously, CNI plugins were managed by the kubelet using the ``--network-plugin=cni``
command-line parameter. For more information, see the
[Kubernetes CNI network-plugins documentation](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/).

## Enable automatic node CIDR allocation (Recommended)

Kubernetes has the capability to automatically allocate and assign a per node IP
allocation CIDR. Cilium automatically uses this feature if enabled. This is the
easiest method to handle IP allocation in a Kubernetes cluster. To enable this
feature, simply add the following flag when starting
``kube-controller-manager``:

```shell-session
--allocate-node-cidrs
```

This option is not required but highly recommended.
