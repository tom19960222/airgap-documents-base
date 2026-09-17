---
collection: cilium
version: "1.16.7"
title: "IP Address Management (IPAM)"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/concepts/ipam/index.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="address_management"></a>

# IP Address Management (IPAM)

IP Address Management (IPAM) is responsible for the allocation and management
of IP addresses used by network endpoints (container and others) managed by
Cilium. Various IPAM modes are supported to meet the needs of different users:

| Feature | Kubernetes Host Scope | Cluster Scope (default) | Multi-Pool | CRD-backed | AWS ENI | Azure IPAM | GKE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tunnel routing | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |  |
| Direct routing | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  |
| CIDR Configuration | Kubernetes | Cilium | Cilium | External | External (AWS) | External (Azure) | External (GCP) |
| Multiple CIDRs per cluster | ❌ | ✅ | N/ | N/ | N/ | N/ |  |
| Multiple CIDRs per node | ❌ | ✅ | N/ | N/ | N/ | N/ |  |
| Dynamic CIDR/IP allocation | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |  |

Don't change the IPAM mode of an existing cluster. Changing the IPAM mode in
a live environment may cause persistent disruption of connectivity for existing workloads.
The safest path to change IPAM mode is to install a fresh Kubernetes cluster with the new IPAM configuration.
If you are interested in extending Cilium to support migration between IPAM modes, see 27164.

.. toctree::
   :maxdepth: 1
   :glob:

   cluster-pool
   kubernetes
   multi-pool
   azure
   azure-delegated-ipam
   eni
   gke
   crd
   deep_dive
