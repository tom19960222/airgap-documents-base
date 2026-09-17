---
collection: cilium
version: "1.16.7"
title: "eBPF Program Types"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/internals/hooks.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# eBPF Program Types

Cilium uses the following eBPF program types to attach programs to the kernel:

- ``BPF_PROG_TYPE_XDP``
- ``BPF_PROG_TYPE_SCHED_ACT``
- ``BPF_PROG_TYPE_CGROUP_SOCK_ADDR``
