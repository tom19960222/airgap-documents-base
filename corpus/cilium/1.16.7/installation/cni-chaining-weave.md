---
collection: cilium
version: "1.16.7"
title: "Weave Net"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/cni-chaining-weave.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Weave Net

This guide instructs how to install Cilium in chaining configuration on top of
[Weave Net](https://github.com/weaveworks/weave).

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

## Create a CNI configuration

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
        "cniVersion": "0.3.1",
        "name": "weave",
        "plugins": [
            {
                "name": "weave",
                "type": "weave-net",
                "hairpinMode": true
            },
            {
                "type": "portmap",
                "capabilities": {"portMappings": true},
                "snat": true
            },
            {
                "type": "cilium-cni"
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

> **Note:**
> The new CNI chaining configuration will *not* apply to any pod that is
> already running the cluster. Existing pods will be reachable and Cilium will
> load-balance to them but policy enforcement will not apply to them and
> load-balancing is not performed for traffic originating from existing pods.
>
> You must restart these pods in order to invoke the chaining configuration on
> them.

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
