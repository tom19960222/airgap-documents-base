---
collection: istio
version: "1.24"
title: "Multi-cluster Traffic Management"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/configuration/traffic-management/multicluster/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "How to configure how traffic is distributed among clusters in the mesh."
---
Within a multicluster mesh, traffic rules specific to the cluster topology may be desirable. This document describes
a few ways to manage traffic in a multicluster mesh. Before reading this guide:

1. Read [Deployment Models](../../../deployment/deployment-models/index.md#multiple-clusters)
1. Make sure your deployed services follow the concept of namespace sameness.

## Keeping traffic in-cluster

In some cases the default cross-cluster load balancing behavior is not desirable. To keep traffic "cluster-local" (i.e.
traffic sent from `cluster-a` will only reach destinations in `cluster-a`), mark hostnames or wildcards as `clusterLocal`
using [`MeshConfig.serviceSettings`](https://istio.io/v1.24/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ServiceSettings-Settings) <!-- unresolved-site-link: route=/docs/reference/config/istio.mesh.v1alpha1 -->.

For example, you can enforce cluster-local traffic for an individual service, all services in a particular namespace, or globally for all services in the mesh, as follows:

**Tabset (meshconfig):**

**Tab: per-service**

```yaml
serviceSettings:
- settings:
    clusterLocal: true
  hosts:
  - "mysvc.myns.svc.cluster.local"
```

**Tab: per-namespace**

```yaml
serviceSettings:
- settings:
    clusterLocal: true
  hosts:
  - "*.myns.svc.cluster.local"
```

**Tab: global**

```yaml
serviceSettings:
- settings:
    clusterLocal: true
  hosts:
  - "*"
```

## Partitioning Services {#partitioning-services}

[`DestinationRule.subsets`](https://istio.io/v1.24/docs/reference/config/networking/destination-rule/#Subset) <!-- unresolved-site-link: route=/docs/reference/config/networking/destination-rule --> allows partitioning a service
by selecting labels. These labels can be the labels from Kubernetes metadata, or from [built-in labels](https://istio.io/v1.24/docs/reference/config/labels/) <!-- unresolved-site-link: route=/docs/reference/config/labels -->.
One of these built-in labels, `topology.istio.io/cluster`, in the subset selector for a `DestinationRule` allows
creating per-cluster subsets.

```yaml
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: mysvc-per-cluster-dr
spec:
  host: mysvc.myns.svc.cluster.local
  subsets:
  - name: cluster-1
    labels:
      topology.istio.io/cluster: cluster-1
  - name: cluster-2
    labels:
      topology.istio.io/cluster: cluster-2
```

Using these subsets you can create various routing rules based on the cluster such as [mirroring](../../../../tasks/traffic-management/mirroring/index.md)
or [shifting](../../../../tasks/traffic-management/traffic-shifting/index.md).

This provides another option to create cluster-local traffic rules by restricting the destination subset in a `VirtualService`:

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: mysvc-cluster-local-vs
spec:
  hosts:
  - mysvc.myns.svc.cluster.local
  http:
  - name: "cluster-1-local"
    match:
    - sourceLabels:
        topology.istio.io/cluster: "cluster-1"
    route:
    - destination:
        host: mysvc.myns.svc.cluster.local
        subset: cluster-1
  - name: "cluster-2-local"
    match:
    - sourceLabels:
        topology.istio.io/cluster: "cluster-2"
    route:
    - destination:
        host: mysvc.myns.svc.cluster.local
        subset: cluster-2
```

Using subset-based routing this way to control cluster-local traffic, as opposed to
[`MeshConfig.serviceSettings`](https://istio.io/v1.24/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ServiceSettings-Settings) <!-- unresolved-site-link: route=/docs/reference/config/istio.mesh.v1alpha1 -->,
has the downside of mixing service-level policy with topology-level policy.
For example, a rule that sends 10% of traffic to `v2` of a service will need twice the
number of subsets (e.g., `cluster-1-v2`, `cluster-2-v2`).
This approach is best limited to situations where more granular control of cluster-based routing is needed.
