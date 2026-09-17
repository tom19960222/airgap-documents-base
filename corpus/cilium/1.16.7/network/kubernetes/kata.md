---
collection: cilium
version: "1.16.7"
title: "Kata Containers with Cilium"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/kubernetes/kata.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="kata"></a>

# Kata Containers with Cilium

[Kata Containers](https://katacontainers.io/) is an open source project that
provides a secure container runtime with lightweight virtual machines that feel
and perform like containers, but provide stronger workload isolation using
hardware virtualization technology as a second layer of defense.  Kata
Containers implements OCI runtime spec, just like ``runc`` that is used by
Docker. Cilium can be used along with Kata Containers, using both enables
higher degree of security. Kata Containers enhances security in the compute
layer, while Cilium provides policy and observability in the networking layer.

This guide shows how to install Cilium along with Kata Containers. It assumes
that you have already followed the official
[Kata Containers installation user guide](https://github.com/kata-containers/documentation/tree/master/install)
to get the Kata Containers runtime up and running on your platform of choice
but that you haven't yet setup Kubernetes.

> **Note:**
> This guide has been validated by following the Kata Containers guide for
> Google Compute Engine (GCE) and using Ubuntu 18.04 LTS with the packaged
> version of Kata Containers, CRI-containerd and Kubernetes 1.18.3.

## Setup Kubernetes with CRI

Kata Containers runtime is an OCI compatible runtime and cannot directly
interact with the CRI API level. For this reason, it relies on a CRI
implementation to translate CRI into OCI. At the time of writing this guide,
there are two supported ways called CRI-O and CRI-containerd. It is up to you
to choose the one that you want, but you have to pick one.

Refer to the section [k8s_requirements](requirements.md#k8s_requirements) for detailed instruction on how to
prepare your Kubernetes environment and make sure to use Kubernetes >= 1.12.
Then, follow the
[official guide to run Kata Containers with Kubernetes](https://github.com/kata-containers/documentation/blob/master/how-to/run-kata-with-k8s.md).

> **Note:**
> Minimum version of kubernetes 1.12 is required to use the RuntimeClass Feature
> for Kata Container runtime described below.

With your Kubernetes cluster ready, you can now proceed to deploy Cilium.

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

.. tabs::

   .. group-tab:: Using CRI-O

      .. parsed-literal::

         helm install cilium |CHART_RELEASE| \\
           --namespace kube-system \\
           --set bpf.autoMount.enabled=false

   .. group-tab:: Using CRI-containerd

      .. parsed-literal::

         helm install cilium |CHART_RELEASE| \\
           --namespace kube-system

> **Warning:**
> When using [kube-proxy-replacement](kubeproxy-free.md#kubeproxy-free) or its socket-level
> loadbalancer with Kata containers, the socket-level loadbalancer should be
> disabled for pods by setting ``socketLB.hostNamespaceOnly=true``. See
> [socketlb-host-netns-only](kubeproxy-free.md#socketlb-host-netns-only) for more details.

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

## Run Kata Containers with Cilium CNI

Now that your Kubernetes cluster is configured with the Kata Containers runtime
and Cilium as the CNI, you can run a sample workload by following
[these instructions](https://github.com/kata-containers/packaging/tree/master/kata-deploy#run-a-sample-workload).
