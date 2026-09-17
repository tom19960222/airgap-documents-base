---
collection: cilium
version: "1.16.7"
title: "Network Policy"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/clustermesh/policy.rst
fetched_at: 2025-02-13T12:04:31Z
---
<a id="gs_clustermesh_network_policy"></a>

# Network Policy

This tutorial will guide you how to define NetworkPolicies affecting multiple
clusters.

## Prerequisites

You need to have a functioning Cluster Mesh setup, please follow the guide
[gs_clustermesh](clustermesh.md#gs_clustermesh) to set it up.

## Security Policies

As addressing and network security are decoupled, network security enforcement
automatically spans across clusters. Note that Kubernetes security policies are
not automatically distributed across clusters, it is your responsibility to
apply ``CiliumNetworkPolicy`` or ``NetworkPolicy`` in all clusters.

### Allowing Specific Communication Between Clusters

The following policy illustrates how to allow particular pods to communicate
between two clusters. The cluster name refers to the name given via the
``--cluster-name`` agent option or ``cluster-name`` ConfigMap option.

```yaml
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "allow-cross-cluster"
spec:
  description: "Allow x-wing in cluster1 to contact rebel-base in cluster2"
  endpointSelector:
    matchLabels:
      name: x-wing
      io.cilium.k8s.policy.cluster: cluster1
  egress:
  - toEndpoints:
    - matchLabels:
        name: rebel-base
        io.cilium.k8s.policy.cluster: cluster2
```
