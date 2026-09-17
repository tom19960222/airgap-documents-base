---
collection: cilium
version: "1.16.7"
title: "requirements-gke"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/requirements-gke.rst
fetched_at: 2025-02-13T12:04:31Z
---
To install Cilium on [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine),
perform the following steps:

**Default Configuration:**

| Datapath | IPAM | Datastore |
| --- | --- | --- |
| Direct Routing | Kubernetes PodCIDR | Kubernetes CRD |

**Requirements:**

* The cluster should be created with the taint ``node.cilium.io/agent-not-ready=true:NoExecute``
  using ``--node-taints`` option. However, there are other options. Please make
  sure to read and understand the documentation page on [taint effects and unmanaged pods](taints.md#taint_effects).
