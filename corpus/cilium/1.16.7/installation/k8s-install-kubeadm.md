---
collection: cilium
version: "1.16.7"
title: "Installation using kubeadm"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/k8s-install-kubeadm.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Installation using kubeadm

This guide describes deploying Cilium on a Kubernetes cluster created with
``kubeadm``.

For installing ``kubeadm`` on your system, please refer to [the official
kubeadm documentation](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
The official documentation also describes additional options of kubeadm which
are not mentioned here.

If you are interested in using Cilium's kube-proxy replacement, please
follow the [kubeproxy-free](../network/kubernetes/kubeproxy-free.md#kubeproxy-free) guide and skip this one.

## Create the cluster

Initialize the control plane via executing on it:

```shell-session
kubeadm init
```

> **Note:**
> If you want to use Cilium's kube-proxy replacement, kubeadm needs to skip
> the kube-proxy deployment phase, so it has to be executed with the
> ``--skip-phases=addon/kube-proxy`` option:
>
> ```shell-session
> kubeadm init --skip-phases=addon/kube-proxy
> ```
>
> For more information please refer to the [kubeproxy-free](../network/kubernetes/kubeproxy-free.md#kubeproxy-free) guide.

Afterwards, join worker nodes by specifying the control-plane node IP address
and the token returned by ``kubeadm init``:

```shell-session
kubeadm join <..>
```

## Deploy Cilium

Included file `Documentation/installation/k8s-install-download-release.rst`:

.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

.. only:: stable

   Setup Helm repository:

   .. code-block:: shell-session

      helm repo add cilium https://helm.cilium.io/

.. only:: not stable

   Download the Cilium release tarball and change to the kubernetes install directory:

   .. parsed-literal::

      curl -LO |SCM_ARCHIVE_LINK|
      tar xzf |SCM_ARCHIVE_FILENAME|
      cd |SCM_ARCHIVE_NAME|/install/kubernetes

Deploy Cilium release via Helm:

.. parsed-literal::

   helm install cilium |CHART_RELEASE| --namespace kube-system

Included file `Documentation/installation/k8s-install-validate.rst`:

## Validate the Installation

.. tabs::

   .. tab:: Cilium CLI

     .. include:: /installation/cli-download.rst
     .. include:: /installation/cli-status.rst
     .. include:: /installation/cli-connectivity-test.rst

   .. tab:: Manually

     .. include:: /installation/kubectl-status.rst
     .. include:: /installation/kubectl-connectivity-test.rst

Included file `Documentation/installation/next-steps.rst`:

## Next Steps

 * [hubble_setup](../observability/hubble/setup.md#hubble_setup)
 * [hubble_cli](../observability/hubble/hubble-cli.md#hubble_cli)
 * [hubble_ui](../observability/hubble/hubble-ui.md#hubble_ui)
 * [gs_http](../security/http.md#gs_http)
 * [clustermesh](../internals/security-identities.md#clustermesh)
