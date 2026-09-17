---
collection: istio
version: "1.24"
title: "Dynamic Admission Webhooks Overview"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/configuration/mesh/webhook/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Provides a general overview of Istio's use of Kubernetes webhooks and the related issues that can arise."
---
From [Kubernetes mutating and validating webhook mechanisms](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/):

> **Tip:**
>
> Admission webhooks are HTTP callbacks that receive admission requests
> and do something with them. You can define two types of admission
> webhooks, validating admission webhook and mutating admission
> webhook. With validating admission webhooks, you may reject requests
> to enforce custom admission policies. With mutating admission
> webhooks, you may change requests to enforce custom defaults.

Istio uses `ValidatingAdmissionWebhooks` for validating Istio
configuration and `MutatingAdmissionWebhooks` for automatically
injecting the sidecar proxy into user pods.

The webhook setup guides assuming general familiarity with Kubernetes
Dynamic Admission Webhooks. Consult the Kubernetes API references for
detailed documentation of the [Mutating Webhook Configuration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.29/#mutatingwebhookconfiguration-v1-admissionregistration-k8s-io) and [Validating Webhook Configuration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.29/#validatingwebhookconfiguration-v1-admissionregistration-k8s-io).

## Verify dynamic admission webhook prerequisites

See the [platform setup instructions](../../../../setup/platform-setup/_index.md)
for Kubernetes provider specific setup instructions. Webhooks will not
function properly if the cluster is misconfigured. You can follow
these steps once the cluster has been configured and dynamic
webhooks and dependent features are not functioning properly.

1. Verify you’re using a [supported version](../../../../releases/supported-releases/index.md#support-status-of-istio-releases) ([supported_kubernetes_versions]) of
   [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/) and of the Kubernetes server:

```bash
$ kubectl version --short
Client Version: v1.29.0
Server Version: v1.29.1
```

1. `admissionregistration.k8s.io/v1` should be enabled

```bash
$ kubectl api-versions | grep admissionregistration.k8s.io/v1
admissionregistration.k8s.io/v1
```

1. Verify `MutatingAdmissionWebhook` and `ValidatingAdmissionWebhook` plugins are
   listed in the `kube-apiserver --enable-admission-plugins`. Access
   to this flag is [provider specific](../../../../setup/platform-setup/_index.md).

1. Verify the Kubernetes api-server has network connectivity to the
   webhook pod. e.g. incorrect `http_proxy` settings can interfere
   api-server operation (see related issues
   [here](https://github.com/kubernetes/kubernetes/pull/58698#discussion_r163879443)
   and [here](https://github.com/kubernetes/kubeadm/issues/666) for more information).
