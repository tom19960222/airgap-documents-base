---
collection: istio
version: "1.24"
title: "Ambient and the Istio control plane"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/architecture/control-plane/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Understand how ambient interacts with the Istio control plane."
---
Like all Istio data plane modes, Ambient uses the Istio control plane. In ambient, the control plane communicates with the ztunnel proxy on each Kubernetes node.

The figure shows an overview of the control plane related components and flows between ztunnel proxy and the `istiod` control plane.

![Ztunnel architecture](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/architecture/control-plane/ztunnel-architecture.svg)

The ztunnel proxy uses xDS APIs to communicate with the Istio control plane (`istiod`). This enables the fast, dynamic configuration updates required in modern distributed systems. The ztunnel proxy also obtains mTLS certificates for the Service Accounts of all pods that are scheduled on its Kubernetes node using xDS. A single ztunnel proxy may implement L4 data plane functionality on behalf of any pod sharing it's node which requires efficiently obtaining relevant configuration and certificates. This multi-tenant architecture contrasts sharply with the sidecar model where each application pod has its own proxy.

It is also worth noting that in ambient mode, a simplified set of resources are used in the xDS APIs for ztunnel proxy configuration. This results in improved performance (having to transmit and process a much smaller set of information that is sent from istiod to the ztunnel proxies) and improved troubleshooting.
