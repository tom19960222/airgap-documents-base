---
collection: istio
version: "1.24"
title: "Download the Istio release"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/download-istio-release/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Get the files required to install and explore Istio."
---
Each Istio release includes a _release archive_ which contains:

- the [`istioctl`](../../../ops/diagnostic-tools/istioctl/index.md) binary
- [installation profiles](../config-profiles/index.md) and [Helm charts](../../install/helm/index.md)
- samples, including the [Bookinfo](../../../examples/bookinfo/index.md) application

A release archive is built for each supported processor architecture and operating system.

## Download Istio {#download}

1.  Go to the [Istio release](https://github.com/istio/istio/releases/tag/1.24.0) page to
    download the installation file for your OS, or download and
    extract the latest release automatically (Linux or macOS):

```bash
$ curl -L https://istio.io/downloadIstio | sh -
```

> **Tip:**
>
> The command above downloads the latest release (numerically) of Istio.
>     You can pass variables on the command line to download a specific version
>     or to override the processor architecture.
>     For example, to download Istio [istio_full_version] for the x86_64 architecture,
>     run:
>
>
>
> ```bash
> $ curl -L https://istio.io/downloadIstio | ISTIO_VERSION=[istio_full_version] TARGET_ARCH=x86_64 sh -
> ```

1.  Move to the Istio package directory. For example, if the package is
    `istio-{{< istio_full_version >}}`:

```bash
$ cd istio-[istio_full_version]
```

    The installation directory contains:

    - Sample applications in `samples/`
    - The [`istioctl`](https://istio.io/v1.24/docs/reference/commands/istioctl) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> client binary in the
      `bin/` directory.

1.  Add the `istioctl` client to your path (Linux or macOS):

```bash
$ export PATH=$PWD/bin:$PATH
```
