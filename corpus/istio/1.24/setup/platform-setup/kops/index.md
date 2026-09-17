---
collection: istio
version: "1.24"
title: "Kops"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/kops/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up Kops for use with Istio."
---
> **Tip:**
>
> No special configuration is required to run Istio on Kubernetes clusters version 1.22 or newer. For prior Kubernetes versions, you will need to continue to perform these steps.

If you wish to run Istio [Secret Discovery Service](https://www.envoyproxy.io/docs/envoy/latest/configuration/security/secret#sds-configuration) (SDS) for your mesh on Kops managed clusters, you must add [extra configurations](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection) to enable service account token projection volumes in the api-server.

1. Open the configuration file:

```bash
$ kops edit cluster $YOURCLUSTER
```

1. Add the following in the configuration file:

```yaml
kubeAPIServer:
    apiAudiences:
    - api
    - istio-ca
    serviceAccountIssuer: kubernetes.default.svc
```

1. Perform the update:

```bash
$ kops update cluster
$ kops update cluster --yes
```

1. Launch the rolling update:

```bash
$ kops rolling-update cluster
$ kops rolling-update cluster --yes
```
