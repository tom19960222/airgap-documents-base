---
collection: cilium
version: "1.16.7"
title: "Installation with external etcd"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/k8s-install-external-etcd.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="admin_install_daemonset"></a>
<a id="k8s_install_etcd"></a>

# Installation with external etcd

This guide walks you through the steps required to set up Cilium on Kubernetes
using an external etcd. Use of an external etcd provides better performance and
is suitable for larger environments.

Should you encounter any issues during the installation, please refer to the
[troubleshooting_k8s](../network/kubernetes/troubleshooting.md#troubleshooting_k8s) section and/or seek help on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack -->.

## When do I need to use a kvstore?

Unlike the section [k8s_quick_install](../gettingstarted/k8s-install-default.md#k8s_quick_install), this guide explains how to
configure Cilium to use an external kvstore such as etcd. If you are unsure
whether you need to use a kvstore at all, the following is a list of reasons
when to use a kvstore:

 * If you are running in an environment where you observe a high overhead in
   state propagation caused by Kubernetes events.
 * If you do not want Cilium to store state in Kubernetes custom resources
   (CRDs).
 * If you run a cluster with more pods and more nodes than the ones tested
   in the [scalability_guide](../operations/performance/scalability/report.md#scalability_guide).

<a id="ds_deploy"></a>

Included file `Documentation/installation/requirements-intro.rst`:

## Requirements

Make sure your Kubernetes environment is meeting the requirements:

* Kubernetes >= 1.16
* Linux kernel >= 5.4 or equivalent
* Kubernetes in CNI mode
* Mounted eBPF filesystem mounted on all worker nodes
* Recommended: Enable PodCIDR allocation (``--allocate-node-cidrs``) in the ``kube-controller-manager`` (recommended)

Refer to the section [k8s_requirements](../network/kubernetes/requirements.md#k8s_requirements) for detailed instruction on how to
prepare your Kubernetes environment.

You will also need an external etcd version 3.4.0 or higher.

## Kvstore and Cilium dependency
When using an external kvstore, it's important to break the circular dependency between Cilium and kvstore.
If kvstore pods are running within the same cluster and are using a pod network then kvstore relies on Cilium.
However, Cilium also relies on the kvstore, which creates a circular dependency.
There are two recommended ways of breaking this dependency:

 * Deploy kvstore outside of cluster or on separately managed cluster.
 * Deploy kvstore pods with a host network, by specifying ``hostNetwork: true`` in the pod spec.

## Configure Cilium

When using an external kvstore, the address of the external kvstore needs to be
configured in the ConfigMap. Download the base YAML and configure it with
Helm:

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

   helm install cilium |CHART_RELEASE| \\
     --namespace kube-system \\
     --set etcd.enabled=true \\
     --set "etcd.endpoints[0]=http://etcd-endpoint1:2379" \\
     --set "etcd.endpoints[1]=http://etcd-endpoint2:2379" \\
     --set "etcd.endpoints[2]=http://etcd-endpoint3:2379"

If you do not want Cilium to store state in Kubernetes custom resources (CRDs),
consider setting ``identityAllocationMode``:

```
--set identityAllocationMode=kvstore
```

### Optional: Configure the SSL certificates

Create a Kubernetes secret with the root certificate authority, and client-side
key and certificate of etcd:

```shell-session
kubectl create secret generic -n kube-system cilium-etcd-secrets \
    --from-file=etcd-client-ca.crt=ca.crt \
    --from-file=etcd-client.key=client.key \
    --from-file=etcd-client.crt=client.crt
```

Adjust the helm template generation to enable SSL for etcd and use https instead
of http for the etcd endpoint URLs:

.. parsed-literal::

   helm install cilium |CHART_RELEASE| \\
     --namespace kube-system \\
     --set etcd.enabled=true \\
     --set etcd.ssl=true \\
     --set "etcd.endpoints[0]=https://etcd-endpoint1:2379" \\
     --set "etcd.endpoints[1]=https://etcd-endpoint2:2379" \\
     --set "etcd.endpoints[2]=https://etcd-endpoint3:2379"

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
