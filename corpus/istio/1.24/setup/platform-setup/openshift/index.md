---
collection: istio
version: "1.24"
title: "OpenShift"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/openshift/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up an OpenShift cluster for Istio."
---
Follow these instructions to prepare an OpenShift cluster for Istio.

Install Istio using the OpenShift profile:

```bash
$ istioctl install --set global.platform=openshift
```

After installation is complete, expose an OpenShift route for the ingress gateway.

```bash
$ oc -n istio-system expose svc/istio-ingressgateway --port=http2
```
