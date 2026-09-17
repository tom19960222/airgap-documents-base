---
collection: istio
version: "1.24"
title: "CNI"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/cni.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
The [Container Network Interface (CNI)](https://www.cni.dev/) is the standard used by Kubernetes for configuring cluster networking. It is implemented using *plugins*, of which there are two types:

* *interface* plugins, which create a network interface, and are provided by the cluster operator
* *chained* plugins, which can configure the created interface, and can be provided by software installed on the cluster

Istio works with all CNI implementations that follow the CNI standard, in both sidecar and ambient mode.

In order to configure mesh traffic redirection, Istio includes a [CNI node agent](../../setup/additional-setup/cni/index.md). This agent installs a chained CNI plugin, which runs after all configured CNI interface plugins.

The CNI node agent is optional for sidecar mode and required for ambient mode.
