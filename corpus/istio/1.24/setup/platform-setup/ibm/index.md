---
collection: istio
version: "1.24"
title: "IBM Cloud"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/ibm/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up an IBM Cloud cluster for Istio."
---
Follow these instructions to prepare a cluster for Istio using the
[IBM Cloud Kubernetes Service](https://cloud.ibm.com/docs/containers?topic=containers-getting-started).

> **Tip:**
>
> IBM offers a managed control plane add-on for the IBM Cloud Kubernetes Service,
> which you can use instead of installing Istio manually.
> Refer to [Istio on IBM Cloud Kubernetes Service](https://cloud.ibm.com/docs/containers?topic=containers-istio)
> for details and instructions.

To prepare a cluster before manually installing Istio, proceed as follows:

1.  [Install the IBM Cloud CLI, the IBM Cloud Kubernetes Service plug-in, and the Kubernetes CLI](https://cloud.ibm.com/docs/containers?topic=containers-cs_cli_install).

1.  Create a standard Kubernetes cluster using the following command.
    Replace `<cluster-name>` with the name you want to use for your cluster and `<zone-name>` with the name of an
    available zone.

> **Tip:**
>
> You can display your available zones by running `ibmcloud ks zones --provider classic`.
>     The IBM Cloud Kubernetes Service [Locations Reference Guide](https://cloud.ibm.com/docs/containers?topic=containers-regions-and-zones)
>     describes the available zones and how to specify them.

```bash
$ ibmcloud ks cluster create classic --zone <zone-name> --machine-type b3c.4x16 \
  --workers 3 --name <cluster-name>
```

> **Tip:**
>
> If you already have a private or a public VLAN, you must specify them in the above command
>     using the `--private-vlan` and `--public-vlan` options. Otherwise, they will be automatically created for you.
>     You can view your available VLANs by running `ibmcloud ks vlans --zone <zone-name>`.

1.  Run the following command to download your cluster configuration.

```bash
$ ibmcloud ks cluster config --cluster <cluster-name>
```

> **Warning:**
>
> Make sure to use the `kubectl` CLI version that matches the Kubernetes version of your cluster.
