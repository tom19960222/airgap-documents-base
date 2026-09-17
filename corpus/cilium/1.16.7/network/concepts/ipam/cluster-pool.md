---
collection: cilium
version: "1.16.7"
title: "Cluster Scope (Default)"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/concepts/ipam/cluster-pool.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   http://docs.cilium.io

<a id="ipam_crd_cluster_pool"></a>

# Cluster Scope (Default)

The cluster-scope IPAM mode assigns per-node PodCIDRs to each node and
allocates IPs using a host-scope allocator on each node. It is thus similar to
the [k8s_hostscope](kubernetes.md#k8s_hostscope) mode. The difference is that instead of Kubernetes
assigning the per-node PodCIDRs via the Kubernetes ``v1.Node`` resource, the
Cilium operator will manage the per-node PodCIDRs via the ``v2.CiliumNode``
resource. The advantage of this mode is that it does not depend on Kubernetes
being configured to hand out per-node PodCIDRs.

## Architecture

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/concepts/ipam/cluster_pool.png)

This is useful if Kubernetes cannot be configured to hand out PodCIDRs or if
more control is needed.

In this mode, the Cilium agent will wait on startup until the ``podCIDRs`` range
are made available via the Cilium Node ``v2.CiliumNode`` object for all enabled
address families via the resource field set in the ``v2.CiliumNode``:

| Field | Description |
| --- | --- |
| ``spec.ipam.podCIDRs`` | IPv4 and/or IPv6 PodCIDR range |

## Configuration

For a practical tutorial on how to enable this mode in Cilium, see
[gsg_ipam_crd_cluster_pool](../../kubernetes/ipam-cluster-pool.md#gsg_ipam_crd_cluster_pool).

### Expanding the cluster pool

Don't change any existing elements of the ``clusterPoolIPv4PodCIDRList`` list, as
changes cause unexpected behavior. If the pool is exhausted,
add a new element to the list instead. The minimum mask length is ``/30``, with a recommended minimum mask
length of at least ``/29``. The reason to add new elements rather than change existing elements is that
the allocator reserves 2 IPs per CIDR block for the network and broadcast addresses.
Changing ``clusterPoolIPv4MaskSize`` is also not possible.

## Troubleshooting

### Look for allocation errors

Check the ``Error`` field in the ``status.ipam.operator-status`` field:

```shell-session
kubectl get ciliumnodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.ipam.operator-status}{"\n"}{end}'
```

### Check for conflicting node CIDRs

``10.0.0.0/8`` is the default pod CIDR. If your node network is in the same range
you will lose connectivity to other nodes. All egress traffic will be assumed
to target pods on a given node rather than other nodes.

You can solve it in two ways:

  - Explicitly set ``clusterPoolIPv4PodCIDRList`` to a non-conflicting CIDR
  - Use a different CIDR for your nodes
