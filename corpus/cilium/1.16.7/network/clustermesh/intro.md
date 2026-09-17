---
collection: cilium
version: "1.16.7"
title: "Multi-Cluster (Cluster Mesh)"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/clustermesh/intro.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="cluster-mesh"></a>

# Multi-Cluster (Cluster Mesh)

Cluster mesh extends the networking datapath across multiple clusters. It
allows endpoints in all connected clusters to communicate while providing full
policy enforcement. Load-balancing is available via Kubernetes annotations.

See [gs_clustermesh](clustermesh.md#gs_clustermesh) for instructions on how to set up cluster mesh.

<a id="kvstoremesh"></a>

## KVStoreMesh

KVStoreMesh is an extension of Cluster Mesh. It caches the information obtained
from the remote clusters in a local kvstore (such as etcd), to which all local
Cilium agents connect. This is different from vanilla Cluster Mesh, where each
agent directly pulls the information from the remote clusters. KVStoreMesh enables
improved scalability and isolation.

> **Note:**
> Starting from v1.16 KVStoreMesh is enabled by default.
> If you wish to disable it, please refer to [enable_clustermesh](clustermesh.md#enable_clustermesh)
> for instructions on how to disable KVStoreMesh.
