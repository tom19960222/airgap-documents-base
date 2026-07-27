---
collection: ceph
version: "19.2.2"
title: "NVME-oF Gateway Requirements"
source_url: https://docs.ceph.com/en/squid/rbd/nvmeof-requirements/
fetched_at: 2026-07-27T16:42:36+00:00
---
# NVME-oF Gateway Requirements

We recommend that you provision at least two NVMe/TCP gateways on different
nodes to implement a highly-available Ceph NVMe/TCP solution.

We recommend at a minimum a single 10Gb Ethernet link in the Ceph public
network for the gateway. For hardware recommendations, see
[hardware recommendations](../../start/hardware-recommendations/index.md#hardware-recommendations) .

> **Note:**
>
> On the NVMe-oF gateway, the memory footprint is a function of the
> number of mapped RBD images and can grow to be large. Plan memory
> requirements accordingly based on the number of RBD images to be mapped.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
