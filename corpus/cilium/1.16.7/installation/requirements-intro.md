---
collection: cilium
version: "1.16.7"
title: "Requirements"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/requirements-intro.rst
fetched_at: 2025-02-13T12:04:31Z
---
# Requirements

Make sure your Kubernetes environment is meeting the requirements:

* Kubernetes >= 1.16
* Linux kernel >= 5.4 or equivalent
* Kubernetes in CNI mode
* Mounted eBPF filesystem mounted on all worker nodes
* Recommended: Enable PodCIDR allocation (``--allocate-node-cidrs``) in the ``kube-controller-manager`` (recommended)

Refer to the section [k8s_requirements](../network/kubernetes/requirements.md#k8s_requirements) for detailed instruction on how to
prepare your Kubernetes environment.
