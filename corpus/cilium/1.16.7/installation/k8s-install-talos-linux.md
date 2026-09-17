---
collection: cilium
version: "1.16.7"
title: "k8s-install-talos-linux"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/k8s-install-talos-linux.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="talos_linux_install"></a>

**Prerequisites / Limitations**

  - Cilium's Talos Linux support is only tested with Talos versions ``>=1.5.0``.
  - As Talos [does not allow loading Kernel modules](https://www.talos.dev/latest/learn-more/process-capabilities/) by Kubernetes workloads, ``SYS_MODULE`` needs to be dropped from the Cilium default capability list.
  - Talos Linux's [Forwarding kube-dns to Host DNS](https://www.talos.dev/latest/talos-guides/network/host-dns/#forwarding-kube-dns-to-host-dns) (enabled by default since Talos 1.8+) doesn't work together with Cilium's [eBPF_Host_Routing](../operations/performance/tuning.md#ebpf_host_routing). To make it work, you must set ``bpf.hostLegacyRouting`` to ``true`` as DNS won't work otherwise.

> **Note:**
> The official Talos Linux documentation already covers many different Cilium deployment
> options inside their [Deploying Cilium CNI guide](https://www.talos.dev/latest/kubernetes-guides/network/deploying-cilium/). Thus, this guide will only focus on
> the most recommended deployment option, from a Cilium perspective:
>
> - Deployment via official [Cilium Helm chart](https://github.com/cilium/charts)
> - Cilium `Kube-Proxy replacement<kubeproxy-free>` enabled
> - Reuse the ``cgroupv2`` mount that Talos already provides
> - `Kubernetes Host Scope<k8s_hostscope>` IPAM mode as Talos, by default, assigns ``PodCIDRs`` to ``v1.Node`` resources

**Configure Talos Linux**

Before installing Cilium, there are two [Talos Linux Kubernetes configurations](https://www.talos.dev/latest/reference/configuration/v1alpha1/config/#Config.cluster) that
need to be adjusted:

1. Ensuring no other CNI is deployed via ``cluster.network.cni.name: none``
1. Disabling Kube-Proxy deployment via ``cluster.proxy.disabled: true``

Prepare a ``patch.yaml`` file:

```yaml
cluster:
  network:
    cni:
      name: none
  proxy:
    disabled: true
```

Next, generate the configuration files for the Talos cluster by using the
``talosctl gen config`` command:

```shell-session
talosctl gen config \
  my-cluster https://mycluster.local:6443 \
  --config-patch @patch.yaml
```

**Install Cilium**

To run Cilium with `Kube-Proxy replacement<kubeproxy-free>` enabled, it's required
to configure ``k8sServiceHost`` and ``k8sServicePort``, and point them to the
Kubernetes API. Luckily, Talos Linux provides [KubePrism](https://www.talos.dev/v1.6/kubernetes-guides/configuration/kubeprism/) which allows it to access
the Kubernetes API in a convenient way, which solely relies on host networking without
using an external loadbalancer. This [KubePrism](https://www.talos.dev/v1.6/kubernetes-guides/configuration/kubeprism/) endpoint can be accessed from every
Talos Linux node on ``localhost:7445``.

.. parsed-literal::

   helm install cilium |CHART_RELEASE| \\
     --namespace $CILIUM_NAMESPACE \\
     --set=ipam.mode=kubernetes \\
     --set=kubeProxyReplacement=true \\
     --set=securityContext.capabilities.ciliumAgent="{CHOWN,KILL,NET_ADMIN,NET_RAW,IPC_LOCK,SYS_ADMIN,SYS_RESOURCE,DAC_OVERRIDE,FOWNER,SETGID,SETUID}" \\
     --set=securityContext.capabilities.cleanCiliumState="{NET_ADMIN,SYS_ADMIN,SYS_RESOURCE}" \\
     --set=cgroup.autoMount.enabled=false \\
     --set=cgroup.hostRoot=/sys/fs/cgroup \\
     --set=k8sServiceHost=localhost \\
     --set=k8sServicePort=7445
