---
collection: istio
version: "1.24"
title: "Set up a Local Computer"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/setup-local-computer/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
---
---

> **Warning:**
>
> This is work in progress. We will add its sections in pieces. Your feedback is welcome at [discuss.istio.io](https://discuss.istio.io).

In this module you prepare your local computer for the tutorial.

1.  Install [`curl`](https://curl.haxx.se/download.html).

1.  Install [Node.js](https://nodejs.org/en/download/).

1.  Install [Docker](https://docs.docker.com/install/).

1.  Install [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

1.  Set the `KUBECONFIG` environment variable for the configuration file you received from the tutorial instructors, or
    created yourself in the previous module.

```bash
$ export KUBECONFIG=<the file you received or created in the previous module>
```

1.  Verify that the configuration took effect by printing the current namespace:

```bash
$ kubectl config view -o jsonpath="{.contexts[?(@.name==\"$(kubectl config current-context)\")].context.namespace}"
tutorial
```

    You should see in the output the name of the namespace, allocated for you by the instructors or allocated by
    yourself in the previous module.

1.  Download one of the [Istio release archives](https://github.com/istio/istio/releases) and extract
    the `istioctl` command line tool from the `bin` directory, and verify that you
    can run `istioctl` with the following command:

```bash
$ istioctl version
client version: 1.22.0
control plane version: 1.22.0
data plane version: 1.22.0 (4 proxies)
```

Congratulations, you configured your local computer!

You are ready to [run a single service locally](../single/index.md).
