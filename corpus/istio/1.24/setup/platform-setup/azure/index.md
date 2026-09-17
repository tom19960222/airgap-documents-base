---
collection: istio
version: "1.24"
title: "Azure"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/azure/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up an Azure cluster for Istio."
---
Follow these instructions to prepare an Azure cluster for Istio.

> **Tip:**
>
> Azure offers a managed control plane add-on for the Azure Kubernetes Service (AKS),
> which you can use instead of installing Istio manually.
> Please refer to [Deploy Istio-based service mesh add-on for Azure Kubernetes Service](https://learn.microsoft.com/azure/aks/istio-deploy-addon)
> for details and instructions.

You can deploy a Kubernetes cluster to Azure via [AKS](https://azure.microsoft.com/en-us/services/kubernetes-service/) or [Cluster API provider for Azure (CAPZ) for self-managed Kubernetes or AKS](https://capz.sigs.k8s.io/) which fully supports Istio.

## AKS

You can create an AKS cluster via numerous means such as [the az cli](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough), [the Azure portal](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-portal), [az cli with Bicep](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-bicep?tabs=azure-cli), or [Terraform](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-terraform?tabs=bash)

For the `az` cli option, complete `az login` authentication OR use cloud shell, then run the following commands below.

1. Determine the desired region name which supports AKS

```bash
$ az provider list --query "[?namespace=='Microsoft.ContainerService'].resourceTypes[] | [?resourceType=='managedClusters'].locations[]" -o tsv
```

1. Verify the supported Kubernetes versions for the desired region

    Replace `my location` using the desired region value from the above step, and then execute:

```bash
$ az aks get-versions --location "my location" --query "orchestrators[].orchestratorVersion"
```

1. Create the resource group and deploy the AKS cluster

    Replace `myResourceGroup` and `myAKSCluster` with desired names, `my location` using the value from step 1, `1.28.3` if not supported in the region, and then execute:

```bash
$ az group create --name myResourceGroup --location "my location"
$ az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 3 --kubernetes-version 1.28.3 --generate-ssh-keys
```

1. Get the AKS `kubeconfig` credentials

   Replace `myResourceGroup` and `myAKSCluster` with the names from the previous step and execute:

```bash
$ az aks get-credentials --resource-group myResourceGroup --name myAKSCluster
```
