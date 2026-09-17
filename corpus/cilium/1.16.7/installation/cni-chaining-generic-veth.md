---
collection: cilium
version: "1.16.7"
title: "Generic Veth Chaining"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/cni-chaining-generic-veth.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="generic_veth_cni_chaining"></a>

# Generic Veth Chaining

The generic veth chaining plugin enables CNI chaining on top of any CNI plugin
that is using a veth device model. The majority of CNI plugins use such a
model.

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

## Validate that the current CNI plugin is using veth

1. Log into one of the worker nodes using SSH
2. Run ``ip -d link`` to list all network devices on the node. You should be
   able spot network devices representing the pods running on that node.
3. A network device might look something like this:

```shell-session
103: lxcb3901b7f9c02@if102: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
    link/ether 3a:39:92:17:75:6f brd ff:ff:ff:ff:ff:ff link-netnsid 18 promiscuity 0
    veth addrgenmode eui64 numtxqueues 1 numrxqueues 1 gso_max_size 65536 gso_max_segs 65535
```

4. The ``veth`` keyword on line 3 indicates that the network device type is virtual ethernet.

If the CNI plugin you are chaining with is currently not using veth then the
``generic-veth`` plugin is not suitable. In that case, a full CNI chaining
plugin is required which understands the device model of the underlying plugin.
Writing such a plugin is trivial, contact us on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack --> for more
details.

## Create a CNI configuration to define your chaining configuration

Create a ``chaining.yaml`` file based on the following template to specify the
desired CNI chaining configuration:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cni-configuration
  namespace: kube-system
data:
  cni-config: |-
    {
      "name": "generic-veth",
      "cniVersion": "0.3.1",
      "plugins": [
        {
          "type": "XXX",
          [...]
        },
        {
          "type": "cilium-cni",
          "chaining-mode": "generic-veth"
        }
      ]
    }
```

Deploy the ConfigMap:

```shell-session
kubectl apply -f chaining.yaml
```

## Deploy Cilium with the portmap plugin enabled

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
     --namespace=kube-system \\
     --set cni.chainingMode=generic-veth \\
     --set cni.customConf=true \\
     --set cni.configMap=cni-configuration \\
     --set routingMode=native \\
     --set enableIPv4Masquerade=false
