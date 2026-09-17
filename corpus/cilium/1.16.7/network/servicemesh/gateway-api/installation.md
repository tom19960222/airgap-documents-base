---
collection: cilium
version: "1.16.7"
title: "Prerequisites"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/gateway-api/installation.rst
fetched_at: 2025-02-13T12:04:31Z
---
# Prerequisites

* Cilium must be configured with NodePort enabled, using
  ``nodePort.enabled=true`` or by enabling the kube-proxy replacement with
  ``kubeProxyReplacement=true``. For more information, see [kube-proxy replacement](../../kubernetes/kubeproxy-free.md#kubeproxy-free).
* Cilium must be configured with the L7 proxy enabled using ``l7Proxy=true``
  (enabled by default).
* The below CRDs from Gateway API v1.1.0 ``must`` be pre-installed.
  Please refer to this [docs](https://gateway-api.sigs.k8s.io/guides/?h=crds#getting-started-with-gateway-api)
  for installation steps. Alternatively, the below snippet could be used.

    - [GatewayClass](https://gateway-api.sigs.k8s.io/api-types/gatewayclass/)
    - [Gateway](https://gateway-api.sigs.k8s.io/api-types/gateway/)
    - [HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/)
    - [GRPCRoute](https://gateway-api.sigs.k8s.io/api-types/grpcroute/)
    - [ReferenceGrant](https://gateway-api.sigs.k8s.io/api-types/referencegrant/)
    - [TLSRoute (experimental)](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io%2fv1alpha2.TLSRoute/)

.. admonition:: warning
   :class: attention

   An issue in Gateway API requires Cilium having the experimental CRDs to
   be installed in order to use Gateway API. The issue is being tracked
   [here](https://github.com/kubernetes-sigs/gateway-api/issues/3080).

   To install the experimental CRDs, please refer to
   the [Gateway API documentation](https://gateway-api.sigs.k8s.io/guides/#install-experimental-channel).

```shell-session
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_gatewayclasses.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_gateways.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_httproutes.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_referencegrants.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_grpcroutes.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/experimental/gateway.networking.k8s.io_tlsroutes.yaml
```

* By default, the Gateway API controller creates a service of LoadBalancer type,
  so your environment will need to support this. Alternatively, since Cilium 1.16+,
  you can directly expose the Cilium L7 proxy on the [host network](gateway-api.md#gs_gateway_host_network_mode).

# Installation

Included file `Documentation/installation/cli-download.rst`:

> **Warning:**
> Make sure you install [cilium-cli v0.15.0](https://github.com/cilium/cilium-cli/releases/tag/v0.15.0)
> or later. The rest of instructions do not work with older versions of
> cilium-cli. To confirm the cilium-cli version that's installed in your system,
> run:
>
> ```shell-session
> cilium version --client
> ```
>
> See [Cilium CLI upgrade notes](../../../operations/upgrade.md#upgrade_cilium_cli_helm_mode) for more details.

Install the latest version of the Cilium CLI. The Cilium CLI can be used to
install Cilium, inspect the state of a Cilium installation, and enable/disable
various features (e.g. clustermesh, Hubble).

.. tabs::
   .. group-tab:: Linux

     .. code-block:: shell-session

       CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
       CLI_ARCH=amd64
       if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
       curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
       sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
       sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
       rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}

   .. group-tab:: macOS

     .. code-block:: shell-session

       CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
       CLI_ARCH=amd64
       if [ "$(uname -m)" = "arm64" ]; then CLI_ARCH=arm64; fi
       curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}
       shasum -a 256 -c cilium-darwin-${CLI_ARCH}.tar.gz.sha256sum
       sudo tar xzvfC cilium-darwin-${CLI_ARCH}.tar.gz /usr/local/bin
       rm cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}

   .. group-tab:: Other

     See the full page of [releases](https://github.com/cilium/cilium-cli/releases/latest).

.. only:: not stable

   Clone the Cilium GitHub repository so that the Cilium CLI can access the
   latest unreleased Helm chart from the main branch:

   .. parsed-literal::

      git clone git@github.com:cilium/cilium.git
      cd cilium

.. tabs::

   .. group-tab:: Helm

       Cilium Gateway API Controller can be enabled with helm flag ``gatewayAPI.enabled``
       set as true. Please refer to [k8s_install_helm](../../../installation/k8s-install-helm.md#k8s_install_helm) for a fresh installation.

       .. parsed-literal::

           $ helm upgrade cilium |CHART_RELEASE| \\
               --namespace kube-system \\
               --reuse-values \\
               --set kubeProxyReplacement=true \\
               --set gatewayAPI.enabled=true

           $ kubectl -n kube-system rollout restart deployment/cilium-operator
           $ kubectl -n kube-system rollout restart ds/cilium

       Next you can check the status of the Cilium agent and operator:

       .. code-block:: shell-session

           $ cilium status

   .. group-tab:: Cilium CLI

       Cilium Gateway API Controller can be enabled with the below command

       .. parsed-literal::

           $ cilium install |CHART_VERSION| \\
               --set kubeProxyReplacement=true \\
               --set gatewayAPI.enabled=true

       Next you can check the status of the Cilium agent and operator:

       .. code-block:: shell-session

           $ cilium status
