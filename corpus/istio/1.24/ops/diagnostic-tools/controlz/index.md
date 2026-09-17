---
collection: istio
version: "1.24"
title: "Istiod Introspection"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/diagnostic-tools/controlz/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes how to use ControlZ to get insight into a running istiod component."
---
Istiod is built with a flexible introspection framework, called ControlZ, which makes it easy to inspect and manipulate the internal state
of an istiod instance. Istiod opens a port which can be used from a web browser to get an interactive view into its state,
or via REST for access and control from external tools.

When Istiod starts, a message is logged indicating the IP address and port to connect to in order to interact with ControlZ.

```plain
2020-08-04T23:28:48.889370Z     info    ControlZ available at 100.76.122.230:9876
```

Here's sample of the ControlZ interface:

![ControlZ User Interface](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/diagnostic-tools/controlz/ctrlz.png)

To access the ControlZ page of istiod, you can port-forward its ControlZ endpoint
locally and connect through your local browser:

```bash
$ istioctl dashboard controlz deployment/istiod.istio-system
```

This will redirect the component's ControlZ page to `http://localhost:9876` for remote access.
