---
collection: cilium
version: "1.16.7"
title: "Installation using Azure CNI Powered by Cilium in AKS"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/k8s-install-aks.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="aks_install"></a>

# Installation using Azure CNI Powered by Cilium in AKS

This guide walks you through the installation of Cilium on AKS (Azure Kubernetes Service) via
the [Azure Container Network Interface (CNI) Powered by Cilium](https://learn.microsoft.com/en-us/azure/aks/azure-cni-powered-by-cilium) option.

## Create the cluster

Create an Azure CNI Powered by Cilium AKS cluster with ``network-plugin azure`` and
``--network-dataplane cilium``. You can create the cluster either in ``podsubnet`` or ``overlay`` mode.
In both modes, traffic is routed through the Azure Virtual Network Stack. The choice between these
modes depends on the specific use case and requirements of the cluster. Refer to [the related documentation](https://learn.microsoft.com/en-us/azure/aks/azure-cni-overlay#choosing-a-network-model-to-use)  to know more about these two modes.

.. tabs::

   .. group-tab:: Overlay

     .. code-block:: shell-session

         az aks create -n <clusterName> -g <resourceGroupName> -l <location> \
         --network-plugin azure \
         --network-dataplane cilium \
         --network-plugin-mode overlay \
         --pod-cidr 192.168.0.0/16

     See also [the detailed instructions from scratch](https://learn.microsoft.com/en-us/azure/aks/azure-cni-powered-by-cilium#option-1-assign-ip-addresses-from-an-overlay-network).

   .. group-tab:: Podsubnet

     .. code-block:: shell-session

         az aks create -n <clusterName> -g <resourceGroupName> -l <location> \
         --network-plugin azure \
         --network-dataplane cilium \
         --vnet-subnet-id /subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/Microsoft.Network/virtualNetworks/<vnetName>/subnets/nodesubnet \
         --pod-subnet-id /subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/Microsoft.Network/virtualNetworks/<vnetName>/subnets/podsubnet

     See also [the detailed instructions from scratch](https://learn.microsoft.com/en-us/azure/aks/azure-cni-powered-by-cilium#option-2-assign-ip-addresses-from-a-virtual-network).

Included file `Documentation/installation/k8s-install-validate.rst`:

## Validate the Installation

.. tabs::

   .. tab:: Cilium CLI

     .. include:: /installation/cli-download.rst
     .. include:: /installation/cli-status.rst
     .. include:: /installation/cli-connectivity-test.rst

   .. tab:: Manually

     .. include:: /installation/kubectl-status.rst
     .. include:: /installation/kubectl-connectivity-test.rst

## Delegated Azure IPAM

Delegated Azure IPAM (IP Address Manager) manages the IP allocation for pods created in Azure CNI Powered by Cilium clusters.
It assigns IPs that are routable in Azure Virtual Network stack. To know more about the Delegated Azure IPAM,
see [azure_delegated_ipam](../network/concepts/ipam/azure-delegated-ipam.md#azure_delegated_ipam).
