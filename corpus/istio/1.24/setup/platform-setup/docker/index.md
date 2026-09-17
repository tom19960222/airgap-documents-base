---
collection: istio
version: "1.24"
title: "Docker Desktop"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/docker/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up Docker Desktop for Istio."
---
1. To run Istio with Docker Desktop, install a version which contains a [supported Kubernetes version](../../../releases/supported-releases/index.md#support-status-of-istio-releases)
    ([supported_kubernetes_versions]).

1. If you want to run Istio under Docker Desktop's built-in Kubernetes, you need to increase Docker's memory limit
    under the *Resources->Advanced* pane of Docker Desktop's *Settings...*. Set the resources to at least 8.0 `GB` of memory and 4 `CPUs`.

![Docker Preferences](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/docker/dockerprefs.png)

> **Warning:**
>
> Minimum memory requirements vary.  8 `GB` is sufficient to run
>     Istio and Bookinfo.  If you don't have enough memory allocated in Docker Desktop,
>     the following errors could occur:
>
>     - image pull failures
>     - healthcheck timeout failures
>     - kubectl failures on the host
>     - general network instability of the hypervisor
>
>     Additional Docker Desktop resources may be freed up using:
>
>
>
> ```bash
> $ docker system prune
> ```
