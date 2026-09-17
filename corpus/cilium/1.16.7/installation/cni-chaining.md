---
collection: cilium
version: "1.16.7"
title: "CNI Chaining"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/cni-chaining.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="cni_chaining"></a>

# CNI Chaining

CNI chaining allows to use Cilium in combination with other CNI plugins.

With Cilium CNI chaining, the base network connectivity and IP address management
is managed by the non-Cilium CNI plugin, but Cilium attaches eBPF programs to the
network devices created by the non-Cilium plugin to provide L3/L4 network
visibility, policy enforcement and other advanced features.

.. toctree::
   :maxdepth: 1
   :glob:

   cni-chaining-aws-cni
   cni-chaining-azure-cni
   cni-chaining-calico
   cni-chaining-generic-veth
   cni-chaining-portmap
   cni-chaining-weave
