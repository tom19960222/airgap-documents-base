---
collection: istio
version: "1.24"
title: "MicroK8s"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/MicroK8s/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up MicroK8s for use with Istio."
---
This page was last updated August 28, 2019.

---
---

> **Warning:**
>
> This vendor-provided document has not been tested on the Istio 1.9 release and may contain bugs.

Follow these instructions to prepare MicroK8s for using Istio.

> **Warning:**
>
> Administrative privileges are required to run MicroK8s.

1.  Install the latest version of [MicroK8s](https://microk8s.io) using the command

```bash
$ sudo snap install microk8s --classic
```

1.  Enable Istio with the following command:

```bash
$ microk8s.enable istio
```

1.  When prompted, choose whether to enforce mutual TLS authentication among sidecars.
    If you have a mixed deployment with non-Istio and Istio enabled services or you're unsure, choose No.

Please run the following command to check deployment progress:

```bash
$ watch microk8s.kubectl get all --all-namespaces
```
