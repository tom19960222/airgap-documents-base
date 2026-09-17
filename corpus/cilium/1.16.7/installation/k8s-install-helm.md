---
collection: cilium
version: "1.16.7"
title: "Installation using Helm"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/k8s-install-helm.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="k8s_install_helm"></a>

# Installation using Helm

This guide will show you how to install Cilium using [Helm](https://helm.sh/). This involves a couple of additional steps compared to
the [k8s_quick_install](../gettingstarted/k8s-install-default.md#k8s_quick_install) and requires you to manually select the best
datapath and IPAM mode for your particular environment.

## Install Cilium

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

.. tabs::

   .. group-tab:: Generic

      These are the generic instructions on how to install Cilium into any
      Kubernetes cluster using the default configuration options below. Please
      see the other tabs for distribution/platform specific instructions which
      also list the ideal default configuration for particular platforms.

      **Default Configuration:**

      =============== =============== ==============
      Datapath        IPAM            Datastore
      =============== =============== ==============
      Encapsulation   Cluster Pool    Kubernetes CRD
      =============== =============== ==============

      .. include:: requirements-generic.rst

      **Install Cilium:**

      Deploy Cilium release via Helm:

      .. parsed-literal::

         helm install cilium |CHART_RELEASE| \\
           --namespace kube-system

   .. group-tab:: GKE

      .. include:: requirements-gke.rst

      **Install Cilium:**

      Extract the Cluster CIDR to enable native-routing:

      .. code-block:: shell-session

         NATIVE_CIDR="$(gcloud container clusters describe "${NAME}" --zone "${ZONE}" --format 'value(clusterIpv4Cidr)')"
         echo $NATIVE_CIDR

      Deploy Cilium release via Helm:

      .. parsed-literal::

         helm install cilium |CHART_RELEASE| \\
           --namespace kube-system \\
           --set nodeinit.enabled=true \\
           --set nodeinit.reconfigureKubelet=true \\
           --set nodeinit.removeCbrBridge=true \\
           --set cni.binPath=/home/kubernetes/bin \\
           --set gke.enabled=true \\
           --set ipam.mode=kubernetes \\
           --set ipv4NativeRoutingCIDR=$NATIVE_CIDR

      The NodeInit DaemonSet is required to prepare the GKE nodes as nodes are added
      to the cluster. The NodeInit DaemonSet will perform the following actions:

      * Reconfigure kubelet to run in CNI mode
      * Mount the eBPF filesystem

   .. group-tab:: AKS

      .. include:: ../installation/requirements-aks.rst

      **Install Cilium:**

      Deploy Cilium release via Helm:

      .. parsed-literal::

         helm install cilium |CHART_RELEASE| \\
           --namespace kube-system \\
           --set aksbyocni.enabled=true

      .. note::

         Installing Cilium via helm is supported only for AKS BYOCNI cluster and
         not for Azure CNI Powered by Cilium clusters.

   .. group-tab:: EKS

      .. include:: requirements-eks.rst

      **Patch VPC CNI (aws-node DaemonSet)**

      Cilium will manage ENIs instead of VPC CNI, so the ``aws-node``
      DaemonSet has to be patched to prevent conflict behavior.

      .. code-block:: shell-session

         kubectl -n kube-system patch daemonset aws-node --type='strategic' -p='{"spec":{"template":{"spec":{"nodeSelector":{"io.cilium/aws-node-enabled":"true"}}}}}'

      **Install Cilium:**

      Deploy Cilium release via Helm:

      .. parsed-literal::

         helm install cilium |CHART_RELEASE| \\
           --namespace kube-system \\
           --set eni.enabled=true \\
           --set ipam.mode=eni \\
           --set egressMasqueradeInterfaces=eth+ \\
           --set routingMode=native

      .. note::

         This helm command sets ``eni.enabled=true`` and ``routingMode=native``,
         meaning that Cilium will allocate a fully-routable AWS ENI IP address
         for each pod, similar to the behavior of the [Amazon VPC CNI plugin](https://docs.aws.amazon.com/eks/latest/userguide/pod-networking.html).

         This mode depends on a set of [ec2privileges](../network/concepts/ipam/eni.md#ec2privileges) from the EC2 API.

         Cilium can alternatively run in EKS using an overlay mode that gives
         pods non-VPC-routable IPs.  This allows running more pods per
         Kubernetes worker node than the ENI limit but includes the following caveats:

           1. Pod connectivity to resources outside the cluster (e.g., VMs in the VPC
              or AWS managed services) is masqueraded (i.e., SNAT) by Cilium to use the
              VPC IP address of the Kubernetes worker node.
           2. The EKS API Server is unable to route packets to the overlay network. This
              implies that any [webhook](https://kubernetes.io/docs/reference/access-authn-authz/webhook/)
              which needs to be accessed must be host networked or exposed through a service
              or ingress.

         To set up Cilium overlay mode, follow the steps below:

           1. Excluding the lines for ``eni.enabled=true``, ``ipam.mode=eni`` and
              ``routingMode=native`` from the helm command will configure Cilium to use
              overlay routing mode (which is the helm default).
           2. Flush iptables rules added by VPC CNI

              .. code-block:: shell-session

                 iptables -t nat -F AWS-SNAT-CHAIN-0 \\
                    && iptables -t nat -F AWS-SNAT-CHAIN-1 \\
                    && iptables -t nat -F AWS-CONNMARK-CHAIN-0 \\
                    && iptables -t nat -F AWS-CONNMARK-CHAIN-1

        Some Linux distributions use a different interface naming convention.
        If you use masquerading with the option ``egressMasqueradeInterfaces=eth+``,
        remember to replace ``eth+`` with the proper interface name. For
        reference, Amazon Linux 2 uses ``eth+``, whereas Amazon Linux 2023 uses
        ``ens+``.

   .. group-tab:: OpenShift

      .. include:: requirements-openshift.rst

      **Install Cilium:**

      Cilium is a [Certified OpenShift CNI Plugin](https://access.redhat.com/articles/5436171)
      and is best installed when an OpenShift cluster is created using the OpenShift
      installer. Please refer to [k8s_install_openshift_okd](k8s-install-openshift-okd.md#k8s_install_openshift_okd) for more information.

   .. group-tab:: RKE

      .. include:: requirements-rke.rst

   .. group-tab:: k3s

      .. include:: requirements-k3s.rst

      **Install Cilium:**

      .. parsed-literal::

         helm install cilium |CHART_RELEASE| \\
            --namespace $CILIUM_NAMESPACE \\
            --set operator.replicas=1

   .. group-tab:: Rancher Desktop

      **Configure Rancher Desktop:**

      To install Cilium on [Rancher Desktop](https://rancherdesktop.io),
      perform the following steps:

      .. include:: rancher-desktop-configure.rst

      **Install Cilium:**

      .. parsed-literal::

         helm install cilium |CHART_RELEASE| \\
            --namespace $CILIUM_NAMESPACE \\
            --set operator.replicas=1 \\
            --set cni.binPath=/usr/libexec/cni

   .. group-tab:: Talos Linux

      To install Cilium on [Talos Linux](https://www.talos.dev/),
      perform the following steps.

      .. include:: k8s-install-talos-linux.rst

   .. group-tab:: Alibaba ACK

       .. include:: ../installation/alibabacloud-eni.rst

.. admonition:: Video
   :class: attention

   If you'd like to learn more about Cilium Helm values, check out [eCHO episode 117: A Tour of the Cilium Helm Values](https://www.youtube.com/watch?v=ni0Uw4WLHYo).

Included file `Documentation/installation/k8s-install-restart-pods.rst`:

## Restart unmanaged Pods

If you did not create a cluster with the nodes tainted with the taint
``node.cilium.io/agent-not-ready``, then unmanaged pods need to be restarted
manually. Restart all already running pods which are not running in
host-networking mode to ensure that Cilium starts managing them. This is
required to ensure that all pods which have been running before Cilium was
deployed have network connectivity provided by Cilium and NetworkPolicy applies
to them:

```shell-session
$ kubectl get pods --all-namespaces -o custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name,HOSTNETWORK:.spec.hostNetwork --no-headers=true | grep '<none>' | awk '{print "-n "$1" "$2}' | xargs -L 1 -r kubectl delete pod
pod "event-exporter-v0.2.3-f9c896d75-cbvcz" deleted
pod "fluentd-gcp-scaler-69d79984cb-nfwwk" deleted
pod "heapster-v1.6.0-beta.1-56d5d5d87f-qw8pv" deleted
pod "kube-dns-5f8689dbc9-2nzft" deleted
pod "kube-dns-5f8689dbc9-j7x5f" deleted
pod "kube-dns-autoscaler-76fcd5f658-22r72" deleted
pod "kube-state-metrics-7d9774bbd5-n6m5k" deleted
pod "l7-default-backend-6f8697844f-d2rq2" deleted
pod "metrics-server-v0.3.1-54699c9cc8-7l5w2" deleted
```

> **Note:**
> This may error out on macOS due to ``-r`` being unsupported by
> ``xargs``. In this case you can safely run this command without ``-r``
> with the symptom that this will hang if there are no pods to
> restart. You can stop this with ``ctrl-c``.

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
