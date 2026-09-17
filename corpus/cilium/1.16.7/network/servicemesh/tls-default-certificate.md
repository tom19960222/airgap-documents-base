---
collection: cilium
version: "1.16.7"
title: "Defaults certificate for Ingresses"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/tls-default-certificate.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Defaults certificate for Ingresses

Cilium can use a default certificate for ingresses without ``.spec.tls[].secretName`` set.
It's still necessary to have ``.spec.tls[].hosts`` defined.

## Prerequisites

* Cilium must be configured with Kubernetes Ingress Support.
  Please refer to [Kubernetes Ingress Support](ingress.md#gs_ingress) for more details.

## Installation

.. tabs::

   .. group-tab:: Helm

       Defaults certificate for Ingresses can be enabled with helm flags
       ``ingressController.defaultSecretNamespace`` and
       ``ingressController.defaultSecretName```
       set as true. Please refer to [k8s_install_helm](../../installation/k8s-install-helm.md#k8s_install_helm) for a fresh installation.

       .. parsed-literal::

           $ helm upgrade cilium |CHART_RELEASE| \\
               --namespace kube-system \\
               --reuse-values \\
               --set ingressController.defaultSecretNamespace=kube-system \\
               --set ingressController.defaultSecretName=default-cert \\

           $ kubectl -n kube-system rollout restart deployment/cilium-operator
           $ kubectl -n kube-system rollout restart ds/cilium

   .. group-tab:: Cilium CLI

       .. include:: ../../installation/cli-download.rst

       Cilium Ingress Controller can be enabled with the following command:

       .. parsed-literal::

           $ cilium install |CHART_VERSION| \
               --set kubeProxyReplacement=true \
               --set ingressController.enabled=true \
               --set ingressController.defaultSecretNamespace=kube-system \
               --set ingressController.defaultSecretName=default-cert
