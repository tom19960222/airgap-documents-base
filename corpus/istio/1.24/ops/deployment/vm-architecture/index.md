---
collection: istio
version: "1.24"
title: "Virtual Machine Architecture"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/deployment/vm-architecture/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes Istio's high-level architecture for virtual machines."
---
Before reading this document, be sure to review [Istio's architecture](../architecture/index.md) and [deployment models](../deployment-models/index.md).
This page builds on those documents to explain how Istio can be extended to support joining virtual machines into the mesh.

Istio's virtual machine support allows connecting workloads outside of a Kubernetes cluster to the mesh.
This enables legacy applications, or applications not suitable to run in a containerized environment, to get all the benefits that Istio provides to applications running inside Kubernetes.

For workloads running on Kubernetes, the Kubernetes platform itself provides various features like service discovery, DNS resolution, and health checks which are often missing in virtual machine environments.
Istio enables these features for workloads running on virtual machines, and in addition allows these workloads to utilize Istio functionality such as mutual TLS (mTLS), rich telemetry, and advanced traffic management capabilities.

The following diagram shows the architecture of a mesh with virtual machines:

**Tabset (network-mode):**

**Tab: Single-Network**

In this mesh, there is a single [network](../deployment-models/index.md#network-models), where pods and virtual machines can communicate directly with each other.

Control plane traffic, including XDS configuration and certificate signing, are sent through a Gateway in the cluster.
This ensures that the virtual machines have a stable address to connect to when they are bootstrapping. Pods and virtual machines can communicate directly with each other without requiring any intermediate Gateway.

![A service mesh with a single network and virtual machines](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/deployment/vm-architecture/single-network.svg)

**Tab: Multi-Network**

In this mesh, there are multiple [networks](../deployment-models/index.md#network-models), where pods and virtual machines are not able to communicate directly with each other.

Control plane traffic, including XDS configuration and certificate signing, are sent through a Gateway in the cluster.
Similarly, all communication between pods and virtual machines goes through the gateway, which acts as a bridge between the two networks.

![A service mesh with multiple networks and virtual machines](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/deployment/vm-architecture/multi-network.svg)

## Service association

Istio provides two mechanisms to represent virtual machine workloads:

* [`WorkloadGroup`](https://istio.io/v1.24/docs/reference/config/networking/workload-group/) <!-- unresolved-site-link: route=/docs/reference/config/networking/workload-group --> represents a logical group of virtual machine workloads that share common properties. This is similar to a `Deployment` in Kubernetes.
* [`WorkloadEntry`](https://istio.io/v1.24/docs/reference/config/networking/workload-entry/) <!-- unresolved-site-link: route=/docs/reference/config/networking/workload-entry --> represents a single instance of a virtual machine workload. This is similar to a `Pod` in Kubernetes.

Creating these resources (`WorkloadGroup` and `WorkloadEntry`) does not result in provisioning of any resources or running any virtual machine workloads.
Rather, these resources just reference these workloads and inform Istio how to configure the mesh appropriately.

When adding a virtual machine workload to the mesh, you will need to create a `WorkloadGroup` that acts as template for each `WorkloadEntry` instance:

```yaml
apiVersion: networking.istio.io/v1
kind: WorkloadGroup
metadata:
  name: product-vm
spec:
  metadata:
    labels:
      app: product
  template:
    serviceAccount: default
  probe:
    httpGet:
      port: 8080
```

Once a virtual machine has been [configured and added to the mesh](../../../setup/install/virtual-machine/index.md#configure-the-virtual-machine), a corresponding `WorkloadEntry` will be automatically created by the Istio control plane.
For example:

```yaml
apiVersion: networking.istio.io/v1
kind: WorkloadEntry
metadata:
  annotations:
    istio.io/autoRegistrationGroup: product-vm
  labels:
    app: product
  name: product-vm-1.2.3.4
spec:
  address: 1.2.3.4
  labels:
    app: product
  serviceAccount: default
```

This `WorkloadEntry` resource describes a single instance of a workload, similar to a pod in Kubernetes. When the workload is removed from the mesh, the `WorkloadEntry` resource will
be automatically removed.  Additionally, if any probes are configured in the `WorkloadGroup` resource, the Istio control plane automatically updates the health status of associated `WorkloadEntry` instances.

In order for consumers to reliably call your workload, it's recommended to declare a `Service` association. This allows clients to reach a stable hostname, like `product.default.svc.cluster.local`, rather than an ephemeral IP addresses. This also enables you to use advanced routing capabilities in Istio via the `DestinationRule` and `VirtualService` APIs.

Any Kubernetes service can transparently select workloads across both pods and virtual machines via the selector fields which are matched with pod and `WorkloadEntry` labels respectively.

For example, a `Service` named `product` is composed of a `Pod` and a `WorkloadEntry`:

![Service Selection](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/deployment/vm-architecture/service-selector.svg)

With this configuration, requests to `product` would be load-balanced across both the pod and virtual machine workload instances.

## DNS

Kubernetes provides DNS resolution in pods for `Service` names allowing pods to easily communicate with one another by stable hostnames.

For virtual machine expansion, Istio provides similar functionality via a [DNS Proxy](../../configuration/traffic-management/dns-proxy/index.md).
This feature redirects all DNS queries from the virtual machine workload to the Istio proxy, which maintains a mapping of hostnames to IP addresses.

As a result, workloads running on virtual machines can transparently call `Service`s (similar to pods) without requiring any additional configuration.
