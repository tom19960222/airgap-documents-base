---
collection: cilium
version: "1.16.7"
title: "requirements-aks"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/requirements-aks.rst
fetched_at: 2025-02-13T12:04:31Z
---
**Configuration:**

| Datapath | IPAM | Datastore |
| --- | --- | --- |
| Encapsulation | Cluster Pool | Kubernetes CRD |

**Requirements:**

> **Note:**
> On AKS, Cilium can be installed either manually by administrators via Bring your own CNI or
> automatically by AKS via Azure CNI Powered by Cilium. Bring your own CNI offers more flexibility
> and customization as administrators have full control over the installation, but it does not
> integrate natively with the Azure network stack and administrators need to handle Cilium upgrades.
> Azure CNI Powered by Cilium integrates natively with the Azure network stack and upgrades are
> handled by AKS, but it does not offer as much flexibility and customization as it is controlled by AKS.
> The following instructions assume Bring your own CNI. For Azure CNI Powered by
> Cilium, see the external installer guide [aks_install](k8s-install-aks.md#aks_install) for dedicated instructions.

* The AKS cluster must be created with ``--network-plugin none``. See the
  [Bring your own CNI](https://docs.microsoft.com/en-us/azure/aks/use-byo-cni?tabs=azure-cli)
  documentation for more details about BYOCNI prerequisites / implications.

* Make sure that you set a cluster pool IPAM pod CIDR that does not overlap with the default service
  CIDR of AKS. For example, you can use ``--helm-set ipam.operator.clusterPoolIPv4PodCIDRList=192.168.0.0/16``.
