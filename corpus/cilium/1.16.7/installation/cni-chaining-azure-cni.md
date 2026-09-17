---
collection: cilium
version: "1.16.7"
title: "Azure CNI (Legacy)"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/cni-chaining-azure-cni.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="chaining_azure"></a>

# Azure CNI (Legacy)

> **Note:**
> For most users, the best way to run Cilium on AKS is either
> AKS BYO CNI as described in [k8s_install_quick](../gettingstarted/k8s-install-default.md#k8s_install_quick)
> or [Azure CNI Powered by Cilium](https://aka.ms/aks/cilium-dataplane).
> This guide provides alternative instructions to run Cilium with Azure CNI
> in a chaining configuration. This is the legacy way of running Azure CNI with
> cilium as Azure IPAM is legacy, for more information see [ipam_azure](../network/concepts/ipam/azure.md#ipam_azure).

Included file `Documentation/installation/cni-chaining-limitations.rst`:

.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

> **Note:**
> Some advanced Cilium features may be limited when chaining with other
> CNI plugins, such as:
>
> * [Layer 7 Policy](../security/policy/language.md#l7_policy) (see 12454)
> * [encryption_ipsec](../security/network/encryption-ipsec.md#encryption_ipsec) (see 15596)

.. admonition:: Video
   :class: attention

    If you'd like a video explanation of the Azure CNI Powered by Cilium, check out [eCHO episode 70: Azure CNI Powered by Cilium](https://www.youtube.com/watch?v=8it8Hm2F_GM).

This guide explains how to set up Cilium in combination with Azure CNI in a
chaining configuration. In this hybrid mode, the Azure CNI plugin is
responsible for setting up the virtual network devices as well as address
allocation (IPAM). After the initial networking is setup, the Cilium CNI plugin
is called to attach eBPF programs to the network devices set up by Azure CNI to
enforce network policies, perform load-balancing, and encryption.

## Create an AKS + Cilium CNI configuration

Create a ``chaining.yaml`` file based on the following template to specify the
desired CNI chaining configuration. This ConfigMap will be installed as the CNI
configuration file on all nodes and defines the chaining configuration. In the
example below, the Azure CNI, portmap, and Cilium are chained together.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cni-configuration
  namespace: kube-system
data:
  cni-config: |-
    {
      "cniVersion": "0.3.0",
      "name": "azure",
      "plugins": [
        {
          "type": "azure-vnet",
          "mode": "transparent",
          "ipam": {
             "type": "azure-vnet-ipam"
           }
        },
        {
          "type": "portmap",
          "capabilities": {"portMappings": true},
          "snat": true
        },
        {
           "name": "cilium",
           "type": "cilium-cni"
        }
      ]
    }
```

Deploy the ConfigMap:

```shell-session
kubectl apply -f chaining.yaml
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

   helm install cilium |CHART_RELEASE| \\
     --namespace kube-system \\
     --set cni.chainingMode=generic-veth \\
     --set cni.customConf=true \\
     --set cni.exclusive=false \\
     --set nodeinit.enabled=true \\
     --set cni.configMap=cni-configuration \\
     --set routingMode=native \\
     --set enableIPv4Masquerade=false \\
     --set endpointRoutes.enabled=true

This will create both the main cilium daemonset, as well as the cilium-node-init daemonset, which handles tasks like mounting the eBPF filesystem and updating the
existing Azure CNI plugin to run in 'transparent' mode.

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
