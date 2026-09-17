---
collection: cert-manager
version: "1.14"
title: "Installation"
source_url: https://github.com/cert-manager/website/blob/d2e1bdfbbe23fcf24dcb68ab54353a65a4131c20/content/v1.14-docs/installation/README.md
fetched_at: 2026-09-15T21:21:15Z
app_version: "1.14.7"
---
Learn about the various ways you can install cert-manager and how to choose between them.

## Default static install

> You don't require any tweaking of the cert-manager install parameters.

The default static configuration can be installed as follows:

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/[[VAR::cert_manager_latest_version]]/cert-manager.yaml
```

📖 Read more about [installing cert-manager using kubectl apply and static manifests](kubectl.md).

## Getting started

> You quickly want to learn how to use cert-manager and what it can be used for.

📖 **kubectl apply**: For new users we recommend [installing cert-manager using kubectl apply and static manifests](kubectl.md).

📖 **helm**: You can [use helm to install cert-manager](helm.md) and this also allows you to customize the installation if necessary.

📖 **OperatorHub**: If you have an OpenShift cluster, consider [installing cert-manager via OperatorHub](operator-lifecycle-manager.md),
which you can do from the OpenShift web console.

🚧 **cmctl**: Try the [experimental `cmctl x install` command](../reference/cmctl.md#install) to quickly install cert-manager.

## Continuous deployment

> If you know how to configure your cert-manager setup and want to automate this,
> you can use the cert-manager Helm chart directly with tools like Flux, ArgoCD and Anthos.
> Or you can output YAML using `helm template` to generate customized cert-manager installation manifests,
> which can be piped into your preferred deployment tool.

📖 **Continuous Deployment**: Learn [how to automate the installation of cert-manager using tools like Flux and Argo CD](continuous-deployment-and-gitops.md).
