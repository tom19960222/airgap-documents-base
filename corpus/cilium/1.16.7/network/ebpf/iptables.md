---
collection: cilium
version: "1.16.7"
title: "Iptables Usage"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/ebpf/iptables.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Iptables Usage

Depending on the Linux kernel version being used, the eBPF datapath can
implement a varying feature set fully in eBPF. If certain required capabilities
are not available, the functionality is provided using a legacy iptables
implementation. See [features_kernel_matrix](../../operations/system_requirements.md#features_kernel_matrix) for more details.

## kube-proxy Interoperability

The following diagram shows the integration of iptables rules as installed by
kube-proxy and the iptables rules as installed by Cilium.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/ebpf/_static/kubernetes_iptables.svg)
