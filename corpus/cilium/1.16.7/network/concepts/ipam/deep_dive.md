---
collection: cilium
version: "1.16.7"
title: "Technical Deep Dive"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/concepts/ipam/deep_dive.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Technical Deep Dive

## Cilium Container Networking Control Flow

The control flow diagram below gives an overview on how endpoints obtain their
IP address from the IPAM for each different mode of Address Management that
Cilium Supports.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/concepts/ipam/cilium_container_networking_control_flow.png)
